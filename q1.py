def remove_duplicates(string):
    unique_chars = ""
    for char in string:
        if char not in unique_chars:
            unique_chars += char
    return unique_chars

user_input = input("Enter a string: ")
result = remove_duplicates(user_input)
print("Result:", result)
