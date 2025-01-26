class DetectSquares:

    def __init__(self):
        self.arr = []
        self.d = {}

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.d:
            self.d[tuple(point)] += 1
            
        else:
            self.d[tuple(point)] = 1 
            self.arr.append(point)

    def count(self, point: List[int]) -> int:
        y = point[1]
        x = point[0]
        total = 0
        for i in range(len(self.arr)):
            if (self.arr[i][1] == y):
                x2 = self.arr[i][0]
                dist = abs(x - x2)
                if dist != 0:
                    if [x,y-dist] in self.arr:
                        if [x2, y - dist] in self.arr:
                            count1 = self.d[(x2,y)]
                            count2 = self.d[(x, y - dist)]
                            count3 = self.d[(x2,y - dist)]
                            total += count1*count2*count3
                    if [x,y+dist] in self.arr:
                        if [x2, y + dist] in self.arr:
                            count1 = self.d[(x2,y)]
                            count2 = self.d[(x, y + dist)]
                            count3 = self.d[(x2,y + dist)]
                            total += count1*count2*count3
        return total



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)