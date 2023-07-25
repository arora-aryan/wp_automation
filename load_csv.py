# Import necessary libraries
import re

# Initialize an empty array to store the numbers
unformatted = []

# Open the file and read its content
with open('practice.txt', 'r') as f:
    content = f.read()
    content = content.replace('\n', '')

    # Split the content by the "|" delimiter
    items = re.split('\|', content)

    # Iterate over each item
    for item in items:
        # Try to convert the item to a number
        try:
            unformatted.append(item)
        except ValueError:
            # If not successful, skip the item
            pass

print(unformatted)
