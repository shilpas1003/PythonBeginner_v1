def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # str = input()
    # def custom_reverse(str):
    #     if len(str) == 0:
    #         return
    #
    #     temp = str[0]
    #     custom_reverse(str[1:])
    #     print(temp,end='')
    # custom_reverse(str)

    # a =[10,20,30]
    # b = a
    # c = [10,20,30]
    # d = list(a)
    # e =a[:]
    # print(a == a)
    # print(a == b)
    # print(a == c)
    # print(a == d)
    # print(a == e)
    # a[0] = 100
    # print(a)
    # print(a == a)
    # print(a == b)
    # print(a == c)
    # print(a == d)
    # print(a == e)
    # mean = 89
    # median = 88
    # print(f"Mean of the given observation is {mean} and Median is {median} .")
    # print("Mean of the given observation is {} and Median is {} .".format(mean, median))
    # print("Mean of the given observation is", mean, "and Median is", median, ".")
    # print("Mean of the given observation is " + str(mean), "and Median is " + str(median), ".")
    #
    # #Question 2
    # String = 'pythonprogramming'
    # string_without_duplicate = "".join(set(String))
    # print('A :',string_without_duplicate)
    #
    # string_without_duplicate = "".join(dict.fromkeys(String))
    # print('B :',string_without_duplicate)
    # string_without_duplicate = "".join(list(String))
    # print('C :',string_without_duplicate)
    # string_without_duplicate = String.replace('amiofp', '')
    # print('D :',string_without_duplicate)

    # #Question 4:
    # columns = [' Age ', 'body_type', 'DiEt', 'drinks', 'drugs', 'education', 'essay0', 'essay1', 'e ssay2 ', ' essay3 ',
    #            'es say4', 'eSsay5',
    #            'essay6', 'essay7', 'essay8', 'essay9', 'EthniCity ', 'h eig ht', 'Income ', 'j Ob', 'last_online',
    #            'location', 'offspring',
    #            ' OrientatioN ', 'petS', ' Religion', ' sEx ', ' Sign ', ' sMo kes ', 'speaks', ' sTatus ']
    #
    # # cleaned_columns = [i.strip().lower() for i in columns]
    # cleaned_columns = [i.replace(' ', '').lower() for i in columns]
    # # cleaned_columns = [''.join(i.lower()) for i in columns]
    # print(cleaned_columns)

    #Question 5:
    # def reverse1(s):
    #     str = ""
    #     for i in s:
    #         # print(i)
    #         str = i + str
    #         # str = str + i
    #     return str
    #
    # string1 = reverse1('Shilpa')
    # print(string1)
    #
    # def reverse2(s):
    #     if len(s) == 0:
    #         return s
    #     else:
    #         return reverse2(s[1:]) + s[0]
    #
    # string1 = reverse2('Shilpa')
    # print(string1)

    #Question 6:
    # A = [1,2,3,4,5]
    # # A.append([6,7])
    # # A.extend([6, 7])
    # # A = A + [6, 7]
    # A.insert(-1, [6, 7])
    # print(A)

    # #Question 7:
    # my_string = 'pythonprogramming'
    # k = [i for i in my_string if i not in "aeiou"]
    # print(k)

    #Question 8:
    # l1 = [10, 20, 30]
    # l2 = l1
    # print(id(l1) == id(l2))
    #
    # l2 = l1.copy()
    # print(id(l1) == id(l2))

    #Question 9:
    # addition = []
    #
    # def func(x, y):
    #     addition = []
    #     addition.append(x + y)
    #     return addition
    #
    # print(func(7,8))
    # print(addition)

    #Question 10:
    # def outerFun(a,b):
    #     def innerFun(c,d):
    #         return c + d
    #     return innerFun(a,b)
    #     return a
    # result = outerFun(5,10)
    # print(result)

    #Question 11:
    x = 50

    def func(x):
        print('x is', x)
        x = 2
        print('Changed x to ', x)

    func(x)
    print('x is now', x)

if __name__ == '__main__':
    main()