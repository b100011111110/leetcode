from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        que = [0]
        while que:
            node = que.pop(0)
            if node in visited:
                continue
            visited.add(node)
            que.extend(rooms[node])
        return len(visited) == len(rooms)