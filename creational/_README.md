### Factory
We want a burger but we don't want to worry about getting all the ingredients and putting them together.
So instead we just order a burger at a drive-in.

So it takes a list of ingredients to create a burger, we can instead use a factory which will instantiate
the burger for us and return it to us whether it's a cheeseburger, a big-mac or a vegan burger.

We need to tell the factory what kind of burger we want, just like in a restaurant.

### Builder
Here we don't immediately have to pass in all the parameters. We can use a burger builder instead. 
We will have an individual method for adding each ingredient, each one will return a reference to the Builder.

And finally we will have a build method which will return the final product.

Then we can instantiate a burger builder add the buns, the patty and the cheese that we want.
We can chain these methods because each one will return a reference to the builder.

Finally, we can build it, and we have the exact burger that we want, giving us more control over the making of the burger.

### Singleton
A singleton is a class that can only have a single instance of it that is instantiated.
We would start by having a static instance variable. Let's say in our app we want to know if a user is logged in or not.

We won't use the constructor to instantiate the application state, we will use a static method (getAppState()) which will
first check if there is already an existing instance of out application. If not, we will instantiate one. If there already is though
we will return the existing instance. We will never create more than one.

So, if we get our app State for the first time the logged in value will initially be false, but if we get the app State again
this will actually still be the first instance. So if we modify the first instance and then print the logged in value for both of
them, they will both now be true.

This pattern can be useful so that multiple components in our application will have a shared source of truth.