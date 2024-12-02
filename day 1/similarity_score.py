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
    list1 = list(map(int, list1))
    list2 = list(map(int, list2))
    x = 0
    similarity_array = []
    while x < len(list1):
        similarity_array.append(list1[x] * list2.count(list1[x]))
        x = x + 1
    print(sum(similarity_array))