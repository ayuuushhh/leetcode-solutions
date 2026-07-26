# Last updated: 27/07/2026, 00:20:35
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth  = 0

        for customer in accounts:
            wealth = sum(customer)
            if wealth > max_wealth:
                max_wealth = wealth
        
        return max_wealth