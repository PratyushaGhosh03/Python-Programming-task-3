# Get input from the user
main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to check: ")

# Check if sub_string is present in main_string
if sub_string in main_string:
    print("Yes, it is a substring.")
else:
    print("No, it is not a substring.")
