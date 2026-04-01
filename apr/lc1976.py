import heapq

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for i, j, k in roads:
            adj[i].append((j, k))
            adj[j].append((i, k))
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0], ways[0] = 0, 1
        que,MOD = [(0, 0)],10**9 + 7
        while que:
            d, u = heapq.heappop(que)
            if d > dist[u]:
                continue 
            for v, weight in adj[u]:
                if d + weight < dist[v]:
                    dist[v] = d + weight
                    ways[v] = ways[u]
                    heapq.heappush(que, (dist[v], v))
                elif d + weight == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        return ways[n-1]