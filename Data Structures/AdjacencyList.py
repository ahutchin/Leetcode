class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

class adjacencyList:
    def __init__(self):
        self.adj_list = {} # we are using a dictionary so querying for a ListNode is O(1) time

    def addEdge(self, src: int, dest: int):
        newNode = ListNode(dest)

        if src not in self.adj_list:
            self.adj_list[src] = newNode
        else:
            currentNode = self.adj_list[src]
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
    
    def display(self):
        for src in self.adj_list:
            currentNode = self.adj_list[src]
            connections = []
            while currentNode:
                connections.append(currentNode.val)
                currentNode = currentNode.next
            print(f"{src}: {' -> '.join(map(str, connections))}")

# example 
graph = adjacencyList()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 5)

graph.display()