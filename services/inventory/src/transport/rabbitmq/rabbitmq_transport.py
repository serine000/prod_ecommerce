
from typing import List, Optional

import aio
import pika
from shared.messaging.listener import Listener
from shared.messaging.producer import Producer

from config.settings import settings

class RabbitMQTransport(Listener, Producer):

    def __init__(self):
        self.listener_connection = None
        self.listener_channel = None
        self.producer_connection = None
        self.producer_channel = None
        self.host = settings.rabbitmq_host
        self.port = settings.rabbitmq_port
        self.exchange = settings.rabbitmq_exchange
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port)
        )

    def create_listener(self):
        """Create RabbitMQ listener connection and channel."""
        self.listener_connection = self.connection
        self.listener_channel = self.listener_connection.channel()

    def initialize_listener(self, queue_name: Optional[str] = None):
        """Initialize RabbitMQ listener by declaring the queue and binding it to the exchange."""
        self.listener_channel.queue_declare(queue=queue_name, durable=True)
        self.listener_channel.queue_bind(exchange=self.exchange, queue=queue_name)
        
    def start_listener(self, queue_names: Optional[List[str]] = None):
        """Start RabbitMQ listener to consume messages from the specified queue."""
        self.listener_channel.basic_qos(prefetch_count=1)  # Limit the number of unacknowledged messages to 1
        for queue_name in queue_names:
            self.initialize_listener(queue_name)
            self.listener_channel.basic_consume(queue=queue_name, 
                                            on_message_callback=self.listener_callback, 
                                            auto_ack=True) # Turned on manually but otherwise it's off by default
        
        self.listener_channel.start_consuming()

    def stop_listener(self):
        """Stop RabbitMQ listener and close the connection."""
        self.listener_connection.close()

    def create_producer(self):
        """Create RabbitMQ producer connection and channel."""
        self.producer_connection = self.connection
        self.producer_channel = self.producer_connection.channel()

    def start_producer(self):
        """Start RabbitMQ producer to send messages to the specified queue."""
        pass

    def stop_producer(self):
        """Stop RabbitMQ producer and close the connection."""
        self.producer_connection.close()

    def send(self, routing_key, message):
        """Send a message to the specified routing key."""
        self.producer_channel.basic_publish(self.exchange,  
                                   routing_key=routing_key, 
                                   body=message)
    
    def listener_callback(self, ch, method, properties, body):
        """Callback function to handle incoming messages from the queue."""
        print(f" [x] Received {body}")
    
    def producer_callback(self, ch, method, properties, body):
        """Callback function to handle outgoing messages to the queue."""
        print(f" [x] Sending {body}")
        

    
