# find out the character which is reaping the most in the string
s = "abcdebasaacfgskrkaaaa"
# a=6
# b=2
char_count = {}
for i in s:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

most = None
max_count = 0

for i, count in char_count.items():
    if count > max_count:
        max_count = count
        most = i

print(most)
print(max_count)