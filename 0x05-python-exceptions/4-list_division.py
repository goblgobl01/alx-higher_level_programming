#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    my_list = []
    for a in range(list_length):
        try:
            result = my_list_1[a] / my_list_2[a]
            my_list.append(result)
        except TypeError:
            print("wrong type")
            result = 0
            my_list.append(result)
        except ZeroDivisionError:
            print("devision by 0")
            result = 0
            my_list.append(result)
        except IndexError:
            print("out of range")
            result = 0
            my_list.append(result)
    return my_list
