# class person:
#     name = "akash"
#     last = "chandran"

#     def skill(self,language):
#         self.l=[]
#         self.l.append(language)
#         return self.l


# p1 = person()
# print(p1.name)
# skills=p1.skill('c')
# print(skills)


# class parent:

#     def ouput(self,Name,age):
#         self.Name=Name
#         self.age=age
#         print(self.Name,self.age)
# # ob=parent()
# parent().ouput("kahle",21)



class parc:
    def __init__(self,ph,address):
        self.ph=ph
        self.address=address
        
    def fun(self):
        print(self.ph,self.address)
class b:
    def f2(self):
        print(self.ph,self.address)
ob=parc(567,"fghj")
ob=b(234,"sdf")
ob.fun()
ob.f2()