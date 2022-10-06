"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        queue = collections.deque()
        # dicitonary to map each value from the old map to the node in the new map
        newVisitedDict = {}
        
        newNode = Node(node.val, [])
        queue.append(node)
        
        newVisitedDict[node.val] = newNode
        
        # perform BFS
        while len(queue) > 0:
            curr = queue.popleft()
            
            # at each step, we iterate through the curr node's neighbors
            for n in curr.neighbors:
                # if we run into a neighbor that is not a node we have visited before, we create a new node 
                # to represent that neighbor, and append our current node as one of its neighbors,
                # then we add the original node that we copied into the queue to continue the traversal
                if not n.val in newVisitedDict:
                    newNeighbor = Node(n.val, [])
                    newVisitedDict[n.val] = newNeighbor
                    newVisitedDict[curr.val].neighbors.append(newNeighbor)
                    
                    queue.append(n)
                # if we run into a node we have seen before, we simply add the reference we saved in the dictionary
                # as a neighbor to our current node
                else:
                    newVisitedDict[curr.val].neighbors.append(newVisitedDict[n.val])
            
        
        return newNode