def print_sorted_dictionary(a_dictionary):
    key = sorted(a_dictionary.keys())
    for index in key:
        print(f"{index}: {a_dictionary[index]}")
