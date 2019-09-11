"""
Slice and dice

Take the block of text provided and strip off the whitespace at both ends. Split the text by newline (\n).
Loop through the lines, for each line:

strip off any leading spaces,
check if the first character is lowercase,
if so, split the line into words and get the last word,
strip the trailing dot (.) and exclamation mark (!) from this last word,
and finally add it to the results list.

Return the results list.
"""

from string import ascii_lowercase

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""


def slice_and_dice(text: str = text) -> list:
    """Get a list of words from the passed in text.
    See the Bite description for step by step instructions"""
    results = []
    text = text.strip().split("\n")
    for line in text:
        if line.strip()[0].islower():
            results.append(line.split()[-1].strip(".").strip("!"))
    print(results)
    return results


slice_and_dice()

