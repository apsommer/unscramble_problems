"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
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

# initialize a blank dictionary
duration = dict()

# loop through all the call data
for call in calls:

    # get method initializes the new key with a value of zero if doesn't exist, otherwise it returns the existing value
    duration[call[0]] = duration.get(call[0], 0) + int(call[3])
    duration[call[1]] = duration.get(call[1], 0) + int(call[3])

# extract the key with the maximum value in the dictionary
max_phone_number = max(duration, key = duration.get)

print(max_phone_number + " spent the longest time, " + str(duration[max_phone_number]) + " seconds, on the phone during September 2016.")
    
