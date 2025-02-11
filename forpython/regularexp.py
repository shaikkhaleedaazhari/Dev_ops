import re
# string="hello every one hello"
# match = re.match("hello",string,re.I)  #only begining of the string
# # match=re.search('Hello',string,re.I)   # search will be entire string and return the first match i(index it will give)
# # match=re.findall('hello',string,re.I)  #findall means in all the string 
# # print(match)


# match1 = re.findall("(?!)one", string)

# print(match1)
# # match2=re.findall("good.morning",string,re.I)
# # print(match2)

# match3= re.search ("hello",string,re.I | re.DOTALL)
# print(match3)
# # If you use re.DOTALL, the . will match across multiple lines.

# l=[]
# for i in re.finditer(re.escape("Hello"),string,re.I):   #I is used to for cehking case insecsitive it will check all
#     l.append(i.span())
#     print(i)
# print(l)



# The span() method in Python's re module is used with match objects to return the start and end positions (indices) of the matched substring within the original string.
# The function re.escape() is used to escape special characters in a string so that they are treated as literal characters in a regex pattern.






str1='''Hi 
Hello
Welcome'''
match5 = re.split("\n",str1)

print(match5)

string="ello world kerala is good kerala "
pattern = r'[k].*'
match6=re.findall(pattern,string)
print(match6)



