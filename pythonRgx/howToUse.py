import re

# Match global false
str = "Hello, World!"
pattern = "Hello"
str = re.match(pattern, str).group()
print("Match global false:", str)

# Match global true
str = "Hello, World!"
pattern = "World!"
str = re.search(pattern, str).group()
print("Match global True:", str)

# Replace global true
str = "Hello, World!"
pattern = "l"
str = re.sub(pattern, "", str)
print("Replace:", str)

# Matches
str = "Hello, World!"
pattern = "."
matches = re.findall(pattern, str)
print("Matches:", matches)