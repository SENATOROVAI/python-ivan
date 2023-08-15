# https://codeforces.com/problemset/problem/4/A
w = int(input())
print("YES" if (w % 2 == 0 and w > 2) else "NO")

# https://codeforces.com/problemset/problem/50/A
x, y = [int(x) for x in input().split()]
print(int(x * y / 2))

# https://codeforces.com/problemset/problem/546/A
k, n, w = [float(x) for x in input().split()]
cost = w * (k / 2 + (w * k) / 2)
print(0 if (cost <= n) else int(cost - n))

# https://codeforces.com/problemset/problem/617/A
import math
distance = int(input())
print(math.ceil(distance / 5))


