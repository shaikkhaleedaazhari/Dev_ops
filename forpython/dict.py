# person= {"first_name":"John",
#           "uid":1001,
#             "friends":["Jane", "Jack"],
#             "skills" :{"backend":["python", "java"]}}
# print(len(person))
# person["adress"]="ny"
# print(len(person))
# print(person.get("skills").get("backend"))
# print(person.get("adress"))
# print(len(person))
# del person["adress"]
# print(len(person))
# person["skills"]["backend"].append("c")
#print(person)
# print(person.items())
# print(person.keys())
# for k in person.keys():
#     print(person.get(k))
# num=int(input("Enter your age"))
# if num < 18:
#     #print("YOU CANT VOTE")
#     pass
#     print("passed")
# elif num >=18 and num <21:
#     print("first time voter")
# else:
#     print("you can vote again")
#imple bubble include hashing

# num=int(input("Enter the number"))
# i=1
# while(i<=10):
#     print(i)
#     i=i+1
# else:
#     print("loop is over")



# def hello_world(a,b):
#     print("Hello World")
#     print(a+b)
# hello_world(10,20)


# def sum_w(nums):
#     sum=0
#     for i in nums:
#         sum=sum+i
#     print(sum)
# sum_w([1,2,3,4,5,6,7,8,9,10])



def primt(num):
    if num >1:
        for i in range(2,num):
            if num %i==0:
                print("not prime")
                break
            else:
                print("prime")
                break

primt(5)

