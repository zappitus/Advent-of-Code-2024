#lowkey i feel really bad about this solution i think theres gotta be a better way but i dont know what im doing so its okay
#like. i have 4 different arrays and 2 while loops in this 23 line piece of code
with open('input1.txt', 'r') as f:
    content = f.read()
    content_array = content.split()
    list1 = []
    list2 = []
    i = 0
    while i < len(content_array):
        if (i % 2):
            list1.append(content_array[i])
        else:
            list2.append(content_array[i])
        i = i + 1
    list1.sort()
    list2.sort()
    list1 = list(map(int, list1))
    list2 = list(map(int, list2))
    difference_array = []
    x = 0
    while x < len(list1):
        difference_array.append(list1[x] - list2[x])
        x = x + 1
    difference_array = list(map(abs, difference_array))
    print(sum(difference_array))