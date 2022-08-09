import sys 
input = sys.stdin.readline

def coin_dp():
    global dp
    dp = [0]*100
    coin = [1,10,25]
    for i in range(1,len(dp)):
        dp[i] = sys.maxsize
        for j in range(len(coin)):
            if i-coin[j] >=0:
                dp[i] = min(dp[i],dp[i-coin[j]]+1) #동전 개수 최솟값

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        coin_dp()
        cnt = 0
        while n>0:
            tmp = n%100
            cnt += dp[tmp]
            n //=100
        print(cnt)
