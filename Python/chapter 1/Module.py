import pyjokes  
#  We installed pyjokes using pip install pyjokes so we can use it in our code. first we need to import it.then we can use it.
#  pyjokes.get_joke() is a function that returns a random joke.
#  We can store the joke in a variable and print it.
#  We can also use the print statement directly without storing the joke in a variable.

joke = pyjokes.get_joke()
print(joke) 