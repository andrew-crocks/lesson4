input_list = input("Введіть список чисел розділених комою: ")

list = [int(x.strip()) for x in input_list.split(',')]

if len(list) == 0:

    list1 = []
    list2 = []
else:
    half = len(list) // 2
    list1 = list[:half]
    list2 = list[half:]
    if len(list) % 2 != 0:
        list2 = list[half+1:]

split_lists = [list1, list2]
print(split_lists)