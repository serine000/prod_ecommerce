
import aio
import pika
from shared.messaging.listener import RequestListener

from config.settings import settings

class RabbitMQListener(RequestListener):

    def __init__(self):
        self.connection = None
        self.channel = None
        self.host = settings.rabbitmq_host
        self.port = settings.rabbitmq_port
        self.exchange = settings.rabbitmq_exchange

    def create_listener(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
        self.channel = self.connection.channel()

    def start_listener(self, queue_name):
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_consume(queue=queue_name, 
                                   on_message_callback=self.callback, 
                                   auto_ack=True)

    def stop_listener(self):
        self.connection.close()
    
    def reply(self, routing_key, message):
        self.channel.basic_publish(self.exchange,  
                                   routing_key=routing_key, 
                                   body=message)
    
    def callback(self, ch, method, properties, body):
        print(f" [x] Received {body}")
        

    
