#  *args - doesnot care about how many arguments are provided
# **kwargs

# def advanced(*args):
#     lis = list(args)
#     return sum(lis)

# print(advanced(1,2,3,4,5,6,7,8,9,10))

def advanced(**kwargs):
    kwargs["Fruits"] = "Mangoes"
    return kwargs

print(advanced(Fruits = "Oranges", movies = "Marvel/DC"))