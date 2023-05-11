## Design Patterns Practice in Python

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