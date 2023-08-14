def age(n):
    if n > 60:
        return "Old"
    elif 30 <= n <= 60:
        return "Mid Aged"
    elif 19 < n < 30:
        return "Young"
    elif 13 <= n <= 19:
        return "Teen Age"
    else:
        return "kid"


print(age(int(input("Enter the Age: "))))