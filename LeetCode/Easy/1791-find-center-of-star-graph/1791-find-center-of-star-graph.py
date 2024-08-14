from collections import Counter

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = []
        
        for edge in edges:
            for node in edge:
                nodes.append(node)
                
        count = Counter(nodes)
        
        for node, freq in count.items():
            if freq == len(edges):
                return node