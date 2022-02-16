def linear(some_list):
    if some_list == []:
        return []
    if isinstance(some_list, list):
        return linear(some_list[0]) + linear(some_list[1:])
    else:
        return [some_list]
