from node import Node


idcounter = 0
def getNewID():
    global idcounter
    idcounter = idcounter + 1
    return idcounter

input = ""
with open("moserunser.txt") as file:
    input = file.read()


# count probabilities

prob = {}

for i in input:
    if i in prob:
        prob[i] = prob[i] + 1
    else:
        prob[i] = 1

nodes = []

for key, value in prob.items():
    nodes.append(Node(getNewID(), key, value))

# generate huffman tree

while True:
    nodes = sorted(nodes, key=lambda node: node.value, reverse=True)
    if len(nodes) > 1:
        n1 = nodes[-1]
        n2 = nodes[-2]

        n3 = Node(getNewID(), n1.key + "+" + n2.key, n1.value + n2.value)
        if n1.value < n2.value:
            n3.right = n1
            n3.left = n2
        else:
            n3.right = n2
            n3.left = n1
        n3.right.parent = n3
        n3.left.parent = n3
        
        nodes = nodes[:-2]
        nodes.append(n3)
    else:
        break

# encoding


def find_recursive(key, node, right=True):
    if key is not node.key:
        found = None
        if node.right is not None:
            t = find_recursive(key, node.right)
            if t is not None:
                found = t
        if node.left is not None:
            t = find_recursive(key, node.left)
            if t is not None:
                found = t
        return found
    return node


        
werner = find_recursive("e", nodes[0]);

print(werner)

















