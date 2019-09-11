"""
Split and join

Split up the message on newline (\n) using the split builtin, 
then use the join builtin to stitch it together using a '|' (pipe).
So Hello world:\nI am coding in Python :)\nHow awesome! would turn 
into: Hello world:|I am coding in Python :)|How awesome!
Your code should work for other message strings as well.
"""

message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


def split_in_columns(message=message):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output"""
    split_message = message.split("\n")
    joined_message = "|".join(split_message)
    print(joined_message)
    return joined_message


split_in_columns()
