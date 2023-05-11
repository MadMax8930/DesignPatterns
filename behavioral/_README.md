### Observer
Also known as the pub sub pattern, it's widely used beyond just OOP including in distributed systems.
For example Youtube, when a content creator uploads a video all of his subscribers get a notification. In this context
the YT channel is the Subject / Publisher which will be the source of events, and the subscribers are Observers.
Observers will be notified when these events happen in real time.

We will have a YT channel class which maintains a list of its subscribers. When a new user subscribes, we add them to the
list of subscribers. When an event occurs, we go through that list of subscribers and send the event data to each of them
with a notification. We also need to define the subscriber interface which we can do with an abstract class or interface

For a youtube user, let's say we just want to print the notification that was received. So then we can create a Youtube channel,
add a few subscribers and we only have to call notify once. And all of the subscribers will receive the notification.

### Iterator
