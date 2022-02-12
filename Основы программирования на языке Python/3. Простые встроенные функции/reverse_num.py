num = float(input())

if -0.000001 < num < 0.000001:
    print(1000000)
else:
    print(num**-1)
