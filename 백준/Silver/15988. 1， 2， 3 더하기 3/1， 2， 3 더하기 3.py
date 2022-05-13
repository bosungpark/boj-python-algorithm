import sys

dp=[0 for _ in range(1000001)]
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(4,1000001):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])
    if dp[i]>1000000009:
        dp[i]%=1000000009
T=int(sys.stdin.readline())
for _ in range(T):
    n=int(sys.stdin.readline())
    print(dp[n])