# Take input from user
text = input("Enter a string: ")

# Convert to lowercase and remove spaces
cleaned_text = ""
for ch in text.lower():
    if ch != " ":
        cleaned_text += ch

# Check palindrome by comparing with reverse using slicing
if cleaned_text == cleaned_text[::-1]:
    print("✅ The string is a palindrome.")
else:
    print("❌ The string is not a palindrome.")
