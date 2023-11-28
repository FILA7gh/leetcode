class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        counter = numBottles

        while numBottles >= numExchange:
            changed_bottles = numBottles // numExchange
            counter += changed_bottles
            numBottles = changed_bottles + (numBottles % numExchange)
        return counter
