from .listener import Listener

class accountability_listener[T](Listener):
    
    def notify(self, event : T):
        print(f"Notificando el evento {event}")