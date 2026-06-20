from abc import ABC, abstractmethod


class Producer(ABC):

    @abstractmethod
    def create_producer(self, *args, **kwargs):
        pass

    @abstractmethod
    def start_producer(self, *args, **kwargs):
        pass

    @abstractmethod
    def stop_producer(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def send(self, *args, **kwargs):
        pass