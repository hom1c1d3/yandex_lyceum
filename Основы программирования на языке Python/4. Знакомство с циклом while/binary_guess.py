low = 1
high = 100
mid = (low + high) // 2
print(mid)
user_input = input()

while user_input != "=" and low <= high:
    if user_input == "<":
        high = mid - 1
    elif user_input == ">":
        low = mid + 1
    mid = (low + high) // 2
    print(mid)
    user_input = input()
