# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# dictionary with some key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Basic operation on the list

# Print the original list
print("Original list:", numbers)

# Append a new element to the list
numbers.append(6)
print("On appending 6:", numbers)

# Remove an element from the list
numbers.remove(3)
print("On removing 3:", numbers)

# Access an element by index
third_element = numbers[2]
print("Third element is:", third_element)

# Basic operations on the dictionary

# Print the original dictionary
print("Original dictionary:", person)

# Add a new key-value pair to the dictionary
person["email"] = "alice@example.com"
print("On adding email:", person)

# Remove a key-value pair from the dictionary
del person["age"]
print("On removing age:", person)

# Access a value by key
name = person["name"]
print("Name in the dictionary:", name)

# Check if a key exists in the dictionary
is_city_present = "city" in person
print("Is 'city' key present in the dictionary?", is_city_present)
