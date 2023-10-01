# Access by index number
list_item = ["Apple", "Mango", "Orange"]
print(list_item[1])
# Negative indexing
print(list_item[-1])
# Range based indexing
new_list_from_old_one = list_item[0:2]
print(new_list_from_old_one)
# Check if item exists
if "Apple" in new_list_from_old_one:
    print("Found")
else:
    print("Not found")
