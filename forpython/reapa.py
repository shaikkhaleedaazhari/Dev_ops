#find out the first repeating element in the list
def first_repeating_element(lst):
    seen = set()
    for element in lst:
        if element in seen:
            return element
        seen.add(element)

lst = [1, 2, 3, 4, 5, 3, 2, 1]
print(first_repeating_element(lst))     