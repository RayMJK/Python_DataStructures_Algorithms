def find_second(string):
    a_dict = {}
    a_list=[]
    num_list=[]

    a=list(string)
    print(a)
    a = list(set(a))
    print(a)

    for i in a:
        a_dict[i] = string.count(i)
    a_list = sorted(a_dict.items(), key=lambda x:x[0])
    print(a_list)
    num_list = sorted(a_dict.items(), key=lambda x:x[1])
    print(num_list)
    num_list.reverse()
    print(num_list)

    return num_list[1][0], num_list[1][1]



string = 'abcdeeeooauiea'

print(find_second(string))
