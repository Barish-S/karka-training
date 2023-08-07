in1=input("Enter The Word: ")
word=""
for i in in1:
    word=i+word
    if word==in1:
        print("This Is Palindrome")
    else:
        print("Not a Palindrome")