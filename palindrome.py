String = input("Enter the String: ").lower()
Reverse = reversed(String)    
if list(String) == list(Reverse):       # reversed() fn return only the object...thats why we are type casting
    print("Palindrome")
else:
    print("Not a Palindrome")