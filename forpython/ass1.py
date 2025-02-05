#create a list of fruits and sort it
#to do in reverse order

#sorted wil not change the original list
#sort will change the original list
# l=["mango","kiwi","orange","apple","banana"]
# l.sort(reverse=True)
# print(l)


# def st(ft):
#     print(ft)
#     r=sorted(ft, reverse=True)
#     return r

# ft= ["mango","kiwi","orange","apple","banana"]
# print(st(ft))

#u have list of numbers u have to find the largest and smallest number
# l=[50,79,26,81,10]
# r=sorted(l)
# print(max(r))
# print(min(r))


#without sorting find 2nd largets and nth smallest number or nth latgest also

# l=[50,79,26,81,10]
# l1=l.copy()

#no removing and all
#using algorithum

def finsmal(arr,n):      #10, 5, 20, 8, 15, 18
    for _ in range(n):
        small = None
        for i in arr:
            if small is None or i <small:
                small =i
        new_arr=[] #10, 5, 20,8,15,18
        for x in arr:
            if x!= small:
                new_arr.append(x)#10, 20, 8, 15, 18
        arr=new_arr
    return small

def finlar(arr,n):
    for _ in range(n):
        large=None
        for num in arr:
            if large is None or num > large:
                large=num
        new_arr=[]
        for i in arr:
            if i!=large:
                new_arr.append(i)
        arr=new_arr
    return large


arr =[10, 5, 20, 8, 15, 2, 18]
print("2nd Smallest:", finsmal(arr, 2))  # Output: 5
print("3rd Largest:", finlar(arr, 3))    # Output: 15



