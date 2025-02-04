multiline= '''i am intern in ust,
i want to be the best,
nice to meet u.'''
print(multiline)

another= '''this is for the concatenation of the string'''
print(multiline+' '+another)
print(len(multiline+ ' '+another))
str= 'khalee is the new intern, \n she is new to kerala \t and she is from andhra'
print(str)


#\n is used for new line
#\t is used for tab space

pi=22/7
r=3
area=pi*r**2
print(area)

# num=int(input('enter the number'))
# for i in range (1,10):
#     print(num,'*',i,'=',num*i)



# atr ="khaleeda"
# for i in atr:
#     print(i)


# length= len(atr)
# for i in range(0,length):
#     print(atr[i])


# k="kahlee"
# print(k[::-1]) 

prac= "heyhellofrommyside"
#print(prac[0:7:2])
#print(prac[-1:10:-1])

print(prac.count('hey'))
print(prac.endswith('side'))
print(prac.endswith('sides'))


prac1 = "hey\thello\tfrom\tmy\tside"
print(prac1.expandtabs(10))