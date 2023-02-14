n = int(input())
a = []
b = []
for _ in range(n):
  a.append(int(input()))
  b.append(int(input()))

  
def dp(a,b):
  dp = [[0 for col in range(a+b+3)] for row in range(a+b+2)]
  for i in range(b+1):
    dp[0][i] = i
  for i in range(a+1):
    dp[i][1] = 1
  dp[0][1],dp[0][2] = 1,2
  for i in range(1,a+1):
    for j in range(1,b+1):
      dp[i][j] = dp[i][j-1]+dp[i-1][j]
  print(dp[a][b])

  
for i in range(n):
  dp(a[i],b[i])
  