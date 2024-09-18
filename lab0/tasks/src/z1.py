#1
a, b = map(int, input().split())

while abs(a) > 10**9 or abs(b) > 10**9:
    print('Error data, write again')
    a, b = map(int, input().split())

print(a + b)
