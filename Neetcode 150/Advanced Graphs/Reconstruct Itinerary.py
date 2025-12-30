from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Adjacency List
        tickets.sort()
        adj = defaultdict(lambda: [])
        for dep, arr in tickets:
            adj[dep].append(arr)

        # DFS
        n = len(tickets)

        res = ["JFK"]

        def dfs(src: str):
            if len(res) == n + 1:
                return True
            if adj[src] == []:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)

                if dfs(v):
                    return True

                adj[src].insert(i, v)
                res.pop()

        dfs("JFK")
        return res

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        res = []

        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]

# Intuition:
# Our goal is to fully explore the directed graph, by visiting every edge once

# Build the adjacency list by iterating through tickets - ensure we order the neighbors in lexical order
# We perform DFS on the starting node, JFK, to build the result

# Time Complexity: O(E^2) Due to backtracking, the DFS could visit every edge for each edge in the list
# Space Complexity: O(E) recursive stack depth, also adjacency list


print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
      )
