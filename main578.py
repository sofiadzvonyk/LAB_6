a = set(input().split())
b = set(input().split())
c = a & b
for x in c:
    print(x, end=" ")