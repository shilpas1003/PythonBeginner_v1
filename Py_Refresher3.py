def string_function():
    str = "Ce La Vi"
    print(str.split())

    str2 = "Ce?La?Vi"
    split_str = str2.split('?')
    print(split_str)

    #Joining seperate list
    str3 = ['Hello','I','am','Shilpa']
    full = " ".join(str3)
    print(full)

    #Advance Function in Python
    #One liner for if
    signal = "red"
    print("Stop" if signal == "red" else "Go")

    #One liner for Loop
    print([x ** 2 for x in range(5)])

    #Lambda
    double = lambda x : 2 * x
    print("Lambda Function return value :",double(5))

    f1 = lambda x,y : x + y
    print('Multiple arugument using lambda',f1(3,4))

    



string_function()