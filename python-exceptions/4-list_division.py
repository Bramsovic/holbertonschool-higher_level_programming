#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        try:
            value1 = my_list_1[index]
            value2 = my_list_2[index]
            result = value1 / value2
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            new_list.append(result)
    return new_list
