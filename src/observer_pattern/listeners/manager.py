from dataclasses import dataclass, field
from .listener import Listener


@dataclass
class ListenersManager:
    listeners : list[Listener] = field(default_factory=list)

    def add(self, listener : Listener):
        self.listeners.append(listener)

    
    def remove(self, listener : Listener):
        self.listeners.remove(listener)

    def notify_all(self, event: T):
        for listener in self.listeners:
            listener.notify(event) 