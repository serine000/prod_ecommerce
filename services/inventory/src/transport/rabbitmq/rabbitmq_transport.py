
from typing import Optional

import aio
import pika
from shared.messaging.listener import Listener
from shared.messaging.producer import Producer

from config.settings import settings

class RabbitMQTransport(Listener, Producer):

    def __init__(self, declare_exchange: bool = False, exchange_info: dict = None):
        self.listener_connection = None
        self.listener_channel = None
        self.producer_connection = None
        self.producer_channel = None
        self.host = settings.rabbitmq_host
        self.port = settings.rabbitmq_port
        self.exchange = settings.rabbitmq_exchange
        self.declare_exchange: bool = declare_exchange
        self.exchange_info: dict = exchange_info

    def create_listener(self):
        """Create RabbitMQ listener connection and channel."""
        self.listener_connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
        self.listener_channel = self.listener_connection.channel()

    def start_listener(self, queue_name: Optional[str] = None):
        """Start RabbitMQ listener to consume messages from the specified queue."""
        if self.declare_exchange:
            self.listener_channel.exchange_declare(exchange=self.exchange_info.get('name'), exchange_type=self.exchange_info.get('type'))
            queue_name = self.listener_channel.queue_declare(queue = '', exclusive=True).method.queue
            self.listener_channel.queue_bind(exchange = self.exchange_info.get('name'), queue = queue_name)
            self.listener_channel.basic_qos(prefetch_count=1)  # Limit the number of unacknowledged messages to 1
            self.listener_channel.basic_consume(queue=queue_name, 
                                           on_message_callback=self.callback, 
                                           auto_ack=True) # Turned on manually but otherwise it's off by default

        else:
            self.listener_channel.queue_declare(queue=queue_name)
            self.listener_channel.queue_bind(exchange = self.exchange, queue = queue_name)    
            self.listener_channel.basic_qos(prefetch_count=1)  # Limit the number of unacknowledged messages to 1
            self.listener_channel.basic_consume(queue=queue_name, 
                                            on_message_callback=self.callback, 
                                            auto_ack=True) # Turned on manually but otherwise it's off by default
        
        self.listener_channel.start_consuming()

    def stop_listener(self):
        """Stop RabbitMQ listener and close the connection."""
        self.listener_connection.close()

    def create_producer(self):
        """Create RabbitMQ producer connection and channel."""
        self.producer_connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
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
    
    def callback(self, ch, method, properties, body):
        """Callback function to handle incoming messages from the queue."""
        print(f" [x] Received {body}")
        

    
