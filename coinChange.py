class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 



# insuffiecent 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins.sort(reverse= True)
        count = b = tot = 0
             
        while tot < amount:

             # end of coins reached
            if b >= len(coins):
                return -1
            
            # get smaller coin
            if tot + coins[b] > amount:
                b += 1
            else:
                count += 1
                tot += coins[b]
                
            if tot == amount:
                return count
                           
            print("tot: ", tot, " count: ", count, " coin: ", coins[b])
        return count
