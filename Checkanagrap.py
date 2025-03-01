def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for uniform comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted versions of both strings are identical
    return sorted(str1) == sorted(str2)

# Get user input
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Verify if the two strings are anagrams
if are_anagrams(string1, string2):
    print("The given strings are anagrams.")
else:
    print("The given strings are not anagrams.")
