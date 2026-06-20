"""Listener module for plugging in the current listener being used to send requests to the inventory service"""


from abc import ABC, abstractmethod

class Listener(ABC):

    @abstractmethod
    def create_listener(self, *args, **kwargs):
        pass

    @abstractmethod
    def start_listener(self, *args, **kwargs):
        pass

    @abstractmethod
    def stop_listener(self, *args, **kwargs):
        pass