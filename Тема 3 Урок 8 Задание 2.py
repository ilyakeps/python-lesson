a = int(input())
b = list(map(int, input().split()))

new_a = [b[-1]] + b[:-1]
print(' '.join(map(str, new_a)))


