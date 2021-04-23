my_list = []

no = int(input("Input the element of the list:"))
for i in range(no):
    ele = input()
    my_list.append(ele)
print("Original list:", my_list)
n = 2
list = []
for i in range(0, len(my_list), n):
    list.append(my_list[i+1])
    list.append(my_list[i])
print("Updated list:", list)