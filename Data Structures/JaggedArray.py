from typing import List
import random

class JaggedArray:
    @staticmethod
    def createJaggedArray() -> List[List[int]]:
        jaggedArray = []
        randomHeight = int((random.random() * 5 + 1) // 1)
        
        for i in range(randomHeight):
            randomLength = int((random.random() * 5 + 1) // 1)
            row = []
            for j in range(randomLength):
                row.append(int((random.random() * 5 + 1) // 1))
            jaggedArray.append(row)
        
        return jaggedArray
    
# Example usage
for i in range(5):
    print(JaggedArray.createJaggedArray())
