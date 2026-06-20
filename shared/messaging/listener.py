"""Listener module for plugging in the current listener being used to send requests to the inventory service"""


from abc import ABC, abstractmethod

class RequestListener(ABC):

    @abstractmethod
    def create_listener(self):
        pass

    @abstractmethod
    def start_listener(self):
        pass

    @abstractmethod
    def stop_listener(self):
        pass
    
    @abstractmethod
    def reply(self):
        pass