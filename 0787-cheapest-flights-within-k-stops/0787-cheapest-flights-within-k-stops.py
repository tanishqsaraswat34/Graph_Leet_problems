class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF=float("inf")
        dist=[INF]*n
        dist[src]=0

        for _ in range(k+1):
            newDist=dist.copy()
            for u,v,price in flights:
                if dist[u]!=INF:
                    newDist[v]=min(
                        newDist[v],dist[u]+price
                    )
            dist = newDist
        if dist[dst]==INF:
            return -1
        return dist[dst]

        