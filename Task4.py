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
TASK 4:
The telephone company wants to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# initialize a blank set
telemarketers = set()

# loop through all the incoming calls to build a unique numbers set
for call in calls:
    telemarketers.add(call[0])

# filter out answering numbers, these can not be telemarketers
for call in calls:
    telemarketers.discard(call[1])

# filter out numbers with texts sent or text recieved, these can not be telemarketers
for text in texts:
    telemarketers.discard(text[0])
    telemarketers.discard(text[1])

# sort in lexicographic order (ascending)
sorted_telemarketers = sorted(telemarketers)

print("These numbers could be telemarketers:\n")
print(*sorted_telemarketers, sep = "\n")
