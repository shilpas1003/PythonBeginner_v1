def main():
    # s = "Alexa, Switch off the lights."
    # print(s)
    # print(s[7:17])
    # print(s[:5])
    # print(s[-2])
    #
    # a = 1
    # print(id(a))
    # a = 2
    # print(id(a))
    #
    # web = "https://www.scaler.com"
    # web = input()
    # if web.startswith("https") or web.startswith("HTTPS") or web.startswith("http") or web.startswith("HTTP") or web.startswith("HTtp")\
    #         or web.startswith("HTtps") or web.startswith("hTTPs") or web.startswith("hTTP"):
    #     print("True")
    # else:
    #     print("False")
    #
    # sentence = "be the change you wish to see in the world"
    # print(sentence.split())
    #
    # marks = [90,100,30,85,60]
    #
    # for idx in range(0,len(marks)):
    #     print(idx,marks[idx])
    #
    # for element in enumerate(marks):
    #     print(element)
    # a = tuple(['a', 'b', 'c', ['ad'], tuple('a')])
    # print(a)
    #
    # sampleDict = {
    #     "class":
    #         {"student":
    #              {"name": "Mike",
    #               "marks":
    #                   {"physics": 70,
    #                    "history": 80
    #                    }
    #               }
    #          }
    # }
    # print(sampleDict['class']['student']['marks']['history'])
    # Roadmap_set = set()
#     # Roadmap_set.add('Data Analytics')
#     # Roadmap_set.add('FrontEnd')
#     # Roadmap_set.add('Machine Learning')
#     # Roadmap_set.remove('FrontEnd')
#     # Roadmap_set.add('Machine Learning')
#     # print(Roadmap_set)
#     List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]
#     print(List)
#     sortList = lambda x: (sorted(i) for i in x)
#     # print(sortList)
#     secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
#     res = secondLargest(List, sortList)
#     print(res)

    # dict1 = {"name": "MB", "salary": 126000}
    # temp = dict1.get("age", 0)
    # temp2 = dict1.get("name2","ABAC")
    # print(temp)
    # print(temp2)

    # Q8: While Loop
    # #1.
    # d = {'me' : 1,'you':2,'we':3}
    # while len(d) > 3:
    #     print(d.popitem(),end=" ")
    # print('Boom!')
    #2.
    # d = {'me': 1, 'you': 2, 'we': 3}
    #
    # while d > 3:
    #     print(d.popitem(), end=" ")
    #
    # print('Boom!')
    # #3.
    # d = {'me': 1, 'you': 2, 'we': 3}
    #
    # while True:
    #     print(d.popitem(), end=" ")
    #
    # print('Boom!')
    # #4.
    # d = {'me': 1, 'you': 2, 'we': 3}
    #
    # while sum([d[e] for e in d]) < len(d):
    #     print(d.popitem(), end=" ")
    #
    # print('Boom!')

    # set1 = {1,2,4}
    # set2 = set1.copy()
    # print(set1)
    # print(set2)
    # set3 = {2,3,4}
    # set4 = set(set3)
    # print(set4)
    #
    # set5 = {6,7,8}
    # set6 = set5
    # print(set6)
    l = ['Red', 'Blue', 'Black', 'White', 'Pink']
    # Q1
    # ans = []
    # for test in l:
    #     ans.append(list(test))
    # print(ans)

    # Q2:
    # for test in l:
    #     print(list(test))
    # # Q3:
    # test = list(map(list, l))
    # print(test)
    # ans = []
    # for test in l:
    #     ans += (list(test))
    # print(ans)

    # def iseven(seq):
    #     result = filter(lambda x: x%2 == 0,seq)
    #     return result
    #
    # seq = [0, 13, 2, 38, 52, 8, 15, 78, 9]
    # filtered = iseven(seq)
    # for s in filtered:
    #     print(s)

    # def iseven(number):
    #
    #     if (number%2 == 0):
    #         return True
    #     else:
    #         return False
    # seq = [0, 13, 2, 38, 52, 8, 15, 78, 9]
    # filtered = filter(iseven, seq)
    # for s in filtered:
    #     print(s)
    # def iseven(seq):
    #     result = [num for num in seq if num % 2 == 0]
    #     return result
    #
    # seq = [0, 13, 2, 38, 52, 8, 15, 78, 9]
    # filtered = iseven(seq)
    # # print(type(filtered))
    # for s in filtered:
    #     print(s)

    # def iseven(seq):
    #
    #     num = 0
    #     result = []
    #     while (num < len(seq)):
    #         if seq[num] % 2 == 0:
    #             result.append(seq[num])
    #         num += 1
    #     return result
    #
    # seq = [0, 13, 2, 38, 52, 8, 15, 78, 9]
    # filtered = iseven(seq)
    # for s in filtered:
    #     print(s)

    

if __name__ == '__main__':
    main()