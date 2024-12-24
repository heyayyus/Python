# 1. len() - Returns the length of the string
s = "Hello"
print("Length of string:", len(s))  # Output: 5

# 2. upper() - Converts all characters to uppercase
s = "hello"
print("Uppercase:", s.upper())  # Output: "HELLO"

# 3. lower() - Converts all characters to lowercase
s = "HELLO"
print("Lowercase:", s.lower())  # Output: "hello"

# 4. strip() - Removes leading and trailing whitespace
s = "  Hello World  "
print("Stripped:", s.strip())  # Output: "Hello World"

# 5. replace() - Replaces substring with another substring
s = "Hello World"
print("Replaced 'World' with 'Python':", s.replace("World", "Python"))  # Output: "Hello Python"

# 6. split() - Splits the string into a list based on a delimiter (default is space)
s = "Hello World Python"
print("Split into list:", s.split())  # Output: ['Hello', 'World', 'Python']

# 7. join() - Joins elements of a list into a string with a specified separator
words = ["Hello", "World", "Python"]
print("Joined words:", " ".join(words))  # Output: "Hello World Python"

# 8. find() - Finds the index of the first occurrence of a substring (returns -1 if not found)
s = "Hello World"
print("Index of 'World':", s.find("World"))  # Output: 6
print("Index of 'Python':", s.find("Python"))  # Output: -1 (not found)

# 9. count() - Returns the number of occurrences of a substring in the string
s = "Hello World"
print("Count of 'o':", s.count("o"))  # Output: 2

# 10. startswith() - Checks if the string starts with a given prefix
s = "Hello World"
print("Starts with 'Hello':", s.startswith("Hello"))  # Output: True
print("Starts with 'World':", s.startswith("World"))  # Output: False

# 11. endswith() - Checks if the string ends with a given suffix
s = "Hello World"
print("Ends with 'World':", s.endswith("World"))  # Output: True
print("Ends with 'Python':", s.endswith("Python"))  # Output: False

# 12. isalpha() - Checks if all characters in the string are alphabetic
s = "Hello"
print("Is alphabetic:", s.isalpha())  # Output: True
s = "Hello123"
print("Is alphabetic:", s.isalpha())  # Output: False

# 13. isdigit() - Checks if all characters in the string are digits
s = "12345"
print("Is digit:", s.isdigit())  # Output: True
s = "123a45"
print("Is digit:", s.isdigit())  # Output: False

# 14. capitalize() - Capitalizes the first character of the string
s = "hello"
print("Capitalized:", s.capitalize())  # Output: "Hello"

# 15. title() - Capitalizes the first letter of each word in the string
s = "hello world"
print("Title case:", s.title())  # Output: "Hello World"

# 16. format() - Formats the string by substituting placeholders with values
name = "Alice"
age = 25
formatted_string = "Name: {}, Age: {}".format(name, age)
print("Formatted string:", formatted_string)  # Output: "Name: Alice, Age: 25"
