from typing import List

# Implement pagination
# pagination(db, startVal, pageNumber, pageLength)
# You can assume the following
#   index may or may not exist
#   page Number can be infinite
#   pageLength can be infinite
# Return the indexes for that page
# Do no use any O(n) space operations
# no repeating elements in returned array

class Solution:
    @staticmethod
    def pagination(db: List[int], startVal: int, pageNumber: int, pageLength: int) -> List[int]:    
        # Catch for db empty
        if not db:
            return []
        
        # Find startVal index
        valIndex = -1
        for index, num in enumerate(db):
            if num == startVal:
                valIndex = index
                break
        
        # Catch: startVal does not exist
        if valIndex == -1:
            return []

        # Calculate the start index for this page
        startIndex = valIndex + (pageNumber * pageLength)
        
        # Maximum elements we can return without wrapping back to startVal
        maxElements = len(db)  # Exclude startVal from being repeated
        
        # Catch: We've gone through all available elements
        if (pageNumber * pageLength) >= maxElements:
            return []
        
        # Calculate how many elements we can still return
        elementsPassed = pageNumber * pageLength
        remainingElements = maxElements - elementsPassed
        elementsToReturn = min(pageLength, remainingElements)
        
        # Build result with wrap-around
        result = []
        for i in range(elementsToReturn):
            # Use modulo to wrap around
            currentIndex = (startIndex + i) % len(db)
            result.append(db[currentIndex])
        
        return result

solution = Solution()

# Time & Space complexity: O(n) and O(1)