def divisible_by_2(my_list=None):
    bool_list = my_list[:] if my_list else []
    for count, num in enumerate(my_list):
        bool_list[count] = True if num % 2 == 0 else False
    return bool_list

def delete_at(my_list=None, idx=0):
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
