import math
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if (x1<=xCenter and x2>=xCenter and y1<=yCenter and y2>=yCenter):
            return True
        for i in range(x1, x2+1):
            if math.sqrt((i - xCenter)**2 + (y2 - yCenter)**2) <= radius:
                return True
            if math.sqrt((i - xCenter)**2 + (y1 - yCenter)**2) <= radius:
                return True
        for i in range(y1, y2+1):
            if math.sqrt((x1 - xCenter)**2 + (i - yCenter)**2) <= radius:
                return True
            if math.sqrt((x2 - xCenter)**2 + (i - yCenter)**2) <= radius:
                return True
        return False