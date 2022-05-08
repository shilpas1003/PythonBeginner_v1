# def invert_dict(data):
#     inv_dict = dict(zip(data.values(), data.keys()))
#     return inv_dict
#
# print(invert_dict({'a': 1, 'b':2}))
#
#
def most_frequent(List):
    dict = {}
    count, itm = 0, ''
    for key1 in reversed(List):
        dict[key1] = dict.get(key1, 0) + 1  #dict keys and values created
        if dict[key1] >= count :
            count, itm = dict[key1], key1
            print('Value:',count,'Key:',itm)
    # print(dict)
    print(itm)

most_frequent([22,33,44,55,66,77,44,66,4,44,66])
# #count Method -
# def most_frequent_List():
#     list = [22,33,44,55,66,77,44,66,4,44,66]
#
#     count = 0
#     temp = 0
#     index = 0
#
#     for x in range(0,len(list)):
#         temp = list.count(list[x])
#         # print(list[x] ,':',temp)
#         if temp > count:
#             count = temp
#             index = x
#     most_frequentNumber = list[index]
#     print(most_frequentNumber)
# most_frequent_List()
#
# #Counter Variable
# from collections import Counter
# list = [22,33,44,55,66,77,44,66,4,44,66]
# counter = Counter(list)
# x = counter.most_common(1)[0]
# print(f"most frequent value is {x[0]}")

# #Dictionary
# num1 = [22,33,44,55,66,77,44,66,4,44,66]
# dict1 = {}
# for num in num1:
#     if num in dict1:
#         dict1[num] = dict1[num] + 1
#     else:
#         dict1[num] = 1
#
# dict1_keys = dict1.keys()
# dict1_values = dict1.values()
# for i in range(len(dict1)):
#     if max(dict1_values):
#         print(dict1_keys[dict1_values])