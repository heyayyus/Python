a = 'ayyus is a good boy\nbut not a bad \'boy\''


print(a)




# Demonstrating various escape sequences in Python

# 1. \\ - Backslash
print("Backslash example: This is a backslash: \\")

# 2. \n - Newline (Moves to the next line)
print("Newline example:\nHello World")

# 3. \t - Tab (Inserts a tab space)
print("Tab example: Hello\tWorld")

# 4. \r - Carriage Return (Moves the cursor to the beginning of the line)
print("Carriage Return example: Hello\rWorld")  # 'Hello' will be overwritten by 'World'

# 5. \b - Backspace (Removes the last character)
print("Backspace example: Hello\bWorld")  # Removes 'o' from 'Hello'

# 6. \f - Form Feed (Next page, not commonly visible in most environments)
print("Form Feed example: Hello\fWorld")  # May cause a page break (depending on the environment)

# 7. \v - Vertical Tab (Moves down vertically, not commonly visible in most environments)
print("Vertical Tab example: Hello\vWorld")

# 8. \a - Bell (Alert or beep sound, may work depending on the system)
print("Bell example: Hello\aWorld")  # May cause a beep sound

# 9. \xhh - Hexadecimal (Character with hexadecimal value)
print("Hexadecimal example: \x48\x65\x6c\x6c\x6f")  # Outputs 'Hello' (hex for 'H', 'e', 'l', 'l', 'o')

# 10. \ooo - Octal Value (Character with octal value)
print("Octal example: \101")  # Outputs 'A' (octal value for 'A')

# 11. \u - Unicode (Character with 4 hexadecimal digits)
print("Unicode example: \u0048")  # Outputs 'H' (Unicode for 'H')

# 12. \U - Unicode (Character with 8 hexadecimal digits)
print("Unicode example: \U0001F600")  # Outputs 😀 (Unicode for grinning face emoji)

# 13. \N{name} - Named Unicode Character (Unicode by name)
print("Named Unicode example: \N{GRINNING FACE}")  # Outputs 😀 (Unicode for grinning face emoji)

# 14. \d - Regular Expression Digit (Used in regex, not a string escape sequence)
import re
match = re.match(r"\d", "5")
if match:
    print("Regex example: Matched digit -", match.group())  # Outputs '5'


