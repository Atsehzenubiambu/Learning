text = input("Enter a word or a phrase:")
text = text.lower()
text = text = text.replace(" ","")
if text == text[::-1]:
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")