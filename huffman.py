from node import Node
import time
import math

start_time = time.perf_counter();

idcounter = 0
def getNewID():
    global idcounter
    idcounter = idcounter + 1
    return idcounter

input = ""
with open("thelastwish.txt", encoding="utf8") as file:
    input = file.read()


# count probabilities

prob = {}
items = []

for i in input:
    if i in prob:
        prob[i] = prob[i] + 1
    else:
        prob[i] = 1

nodes = []

for key, value in prob.items():
    nodes.append(Node(getNewID(), key, value))
    items.append(key)

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

# indexing

path_t = []

def find_recursive(key, node):
    if key is not node.key:
        found = None
        if node.right is not None:
            t = find_recursive(key, node.right)
            if t is not None:
                found = t
                path_t.append(0)
        if node.left is not None:
            t = find_recursive(key, node.left)
            if t is not None:
                found = t
                path_t.append(1)
        return found
    return node


def find_in_tree(key):
    global path_t
    path_t = []
    result = find_recursive(key, nodes[0])
    path_t.reverse()
    path_s = ""
    for i in path_t:
        path_s = path_s + str(i)

    return result, path_s


code_table = {}

for i in items:
    node, path = find_in_tree(i)
    code_table[node.key] = path

# encoding

output = []

for i in input:
    output.append(code_table[i])

output = "".join(output)

# invert code_table
decode_table = {v: k for k, v in code_table.items()}

decoded_string = ""

curr_word = ""
for i in output:
    curr_word = curr_word + i
    if curr_word in decode_table:
        decoded_string = decoded_string + decode_table[curr_word]
        curr_word = ""

end_time = time.perf_counter();
print("Time: ", end_time - start_time)
# print("Coded String: ", output)
print("Bytes: ", math.ceil(len(output) / 8.0))
# print("Decoded String: ", decoded_string)