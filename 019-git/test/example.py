"""
Text manipulation utilities
"""

def capitalize(text):
    if type(text) is not str:
        text = ''.join(text)
    return text.capitalize()

def reverse(text):
    return text[::-1]

if __name__ == "__main__":
    print(capitalize("testing"))
    print(capitalize(['a', 'b', ' ', 'c']))
    print(reverse("Testing"))