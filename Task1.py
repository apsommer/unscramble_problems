"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

# declare a set to allow only unique entries to the collection
unique_numbers = set()

# parse texts
for text in texts:
    unique_numbers.add(text[0])
    unique_numbers.add(text[1])

# parse calls
for call in calls:
    unique_numbers.add(call[0])
    unique_numbers.add(call[1])

# count of unique numbers
count = len(unique_numbers)

print("There are " + str(count) + " different telephone numbers in the records.")
