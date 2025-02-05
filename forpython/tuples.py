day=("monday","tuesday","wednesday","thursday","friday","saturday","h","r","h","q")
day_add=("sunday",)
#print(day[1:2])
#print(day[::-1])
#print(day+day_add)
# day_list=list(day)
# print(day_list)
# #print(day*2)

data_set =set()
print(type(data_set))
for i in range(1,8):
    data_set.add(i)
print(data_set)

for i in data_set:
    data_set.pop()
print(data_set)