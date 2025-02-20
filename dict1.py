# Input: Two lines of space-separated values for keys and values
keys_list = input().split()
values_list = input().split()

# Create dictionary by zipping keys_list and values_list
dictionary = dict(zip(keys_list, values_list))

# Sort dictionary by keys and print in required format
for key in sorted(dictionary):
    print(f"{key}:{dictionary[key]}")
