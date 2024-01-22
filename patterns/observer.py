import uuid
from typing import Dict


class Broadcaster:
    def __init__(self):
        self._subscribers: Dict[str, Subscriber] = {}

    def subscribe(self, subscriber):
        self._subscribers[subscriber.id] = subscriber

    def unsubscribe(self, subscriber):
        del self._subscribers[subscriber.id]

    def notify(self, event: dict):
        for subscriber in self._subscribers.values():
            subscriber.notify(self, event)


class Subscriber:
    def __init__(self, instance, _id=uuid.uuid4, notify_method='notify'):
        self.instance = instance
        self.notify_method = getattr(instance, notify_method)
        self.id = _id() if callable(_id) else _id

    def __str__(self):
        return str(self.id)

    def notify(self, broadcaster: Broadcaster, event: dict):
        self.notify_method(broadcaster=broadcaster, event=event)


class A:
    def __init__(self, a):
        self.a = a

    def __str__(self, **kwargs):
        print(kwargs)
        return f'{self.a} {kwargs}'


a1 = A(1)
a2 = A(2)

ob1 = Subscriber(instance=a1, notify_method='__str__')
ob2 = Subscriber(instance=a2, notify_method='__str__')

b1 = Broadcaster()
b1.subscribe(ob1)
b1.subscribe(ob2)

b1.notify({'type': 'event1'})
b1.notify({'type': 'event2'})

# Subject(model) triggers  a event, which inform the connected receiver functions
# named each signal - responsible for communication between subject and receiver
# - subject is not aware of its subscribers
# - subject will trigger (through the django orm) the event through signal
# Event -> Signal
# Subject -> Model
# Observer -> Receiver function
