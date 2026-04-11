from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], source: int, destination: int) -> int:
        a,b = 0,0
        if source>destination:
            source,destination = destination,source
        for i in range(len(distance)):
            if source<=i<destination:
                a += distance[i]
            else:
                b += distance[i]
        return min(a,b)
            