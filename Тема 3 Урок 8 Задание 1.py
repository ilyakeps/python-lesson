# a = [1, 2, 3, 4, 5]
# a[2] = 10
# a.append(150)
# a.insert(1, 199)
# a.pop(4)
# a.reverse()
# print(a.count(1))

# n = int(input())
# res = []
# for i in range(n):
#     a = int(input())
#     res.append(a)
# print(res)

# res = list((map(int, input().split())))
# print(res)

# a = [3 for i in range(100)]
# print(a)


n = int(input())
a = [int(input()) for i in range(n)]
a.reverse()
print(a)
