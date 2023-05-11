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
An iterator is a pretty simple pattern that defines how the values in an object can be iterated through.
In Python, just defining an array and then iterating through it with the 'in' keyword uses the build-in list iterator, this way
we don't even have to index the array. 

For more complex objects like binary search trees or linked lists we can define our own. We can take a list node which just has a value
and a next pointer. And then a linked list which has a head pointer and current pointer, we can first define the iterator with the inner
function which will just set the current pointer to the head and then return a reference to the linked list.

To get the next value in the sequence, we defined the 'next' function. If our current pointer is non-null we get the value and then return it 
and also shift the current pointer. But if we reach the end of the linked list, we can send a signal that we are going to stop iterating.
To test it out, we can initialize the linked list and iterate through it with the 'in' keyword.

### Strategy
If we want to modify or extend the behavior of a class without directly changing it, we can go with the strategy pattern.
For example, we can filter an array by removing positive values or we could filter it by removing all odd values.

These are two strategies but maybe in the future we want to add more...
We want to follow the open/closed principle (Open -> for extension | Closed -> for modifications)

We can define a filter strategy, create an implementation which will remove all negative values and an implementation which will remove
all odd values. And then at run time, we can pass this strategy into our values object. To test it out, we pass in the strategy into our filter
method and we will get our desired result. This way we can add additional strategies without modifying our values class.
