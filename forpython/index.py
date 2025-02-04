# s="hello"
# x=s.index('e',2)
# print(x)

# s="hello123$"
# print(s.isalnum())
# #The isalnum() method checks if all the characters in the string are alphanumeric (i.e., either letters or digits) and returns True if they are, and False otherwise.

# print(s.isdecimal())

# s3="\u00b2"
# s4="ha123"
# print(s3.isdecimal())
# print(s4.isdigit())
# print(s4.isnumeric())



# s1 = "123"
# s2 = "²"
# s3 = "⅓"

# print(s1.isdigit())  # True
# print(s1.isnumeric())  # True

# print(s2.isdigit())  # True
# print(s2.isnumeric())  # True

# print(s3.isdigit())  # False
# print(s3.isnumeric())  # True



# k1= "12356"
# print(k1.isdecimal())

# l="hello"
# print(l.isupper())
# print(l.islower())

a=["hi","how","are","you"]
print("?".join(a))
y=(" ".join(a))
print(y.strip("hyu"))



