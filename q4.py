try:
    # Get user input
    user_input = input("Enter a statement: ")

    # Write user input to file
    with open("mymotivation.txt", "w") as file:
        file.write(user_input)

    # Read content from file
    with open("mymotivation.txt", "r") as file:
        content = file.read()

    # Display content
    print("Content from mymotivation.txt:")
    print(content)

except IOError as e:
    print("An error occurred while reading or writing the file:", e)
