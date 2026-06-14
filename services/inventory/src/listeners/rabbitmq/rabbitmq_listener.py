
import aio
import pika
from listener import RequestListener

import config

class RabbitMQListener(RequestListener):

    def __init__(self):
        self.connection = None
        self.channel = None
        self.host = config.get("RABBITMQ_HOST")

    def create_listener(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )

    def start_listener(self):
        pass

    def stop_listener(self):
        pass
    
    def start_listening(self):
        pass

