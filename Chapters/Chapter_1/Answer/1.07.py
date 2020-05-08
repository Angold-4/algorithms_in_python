# Angold4 20200507 C1.1.07
n = int(input())
Total = sum(k*k for k in range(1, n+1) if k % 2 != 0)
print(Total)
