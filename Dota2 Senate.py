class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Var definition
        RQueue = []
        DQueue = []
        senateLength = len(senate)

        # Iterate through senate to build 2 queues
        for i in range(senateLength):
            if senate[i] == 'R': RQueue.append(i)
            else: DQueue.append(i)
        
        # Iterate through queues for voting comparison
        while (len(RQueue) > 0) and (len(DQueue) > 0):
            if RQueue[0] < DQueue[0]: 
                DQueue.pop(0)
                winner = RQueue.pop(0)
                RQueue.append(winner + senateLength)
            else:
                RQueue.pop(0)
                winner = DQueue.pop(0)
                DQueue.append(winner + senateLength)
        
        return "Radiant" if len(RQueue) > 0 else "Dire"