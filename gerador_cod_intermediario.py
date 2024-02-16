class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

def generate_intermediate_code(expression):
    tokens = expression.split()
    root = Node(tokens[0])

    current_node = root
    for token in tokens[1:]:
        if token in ['+', '-', '*', '/']:
            current_node.add_child(Node(token))
            current_node = current_node.children[-1]
        else:
            current_node.add_child(Node(token))

    return root

def print_intermediate_code(node, depth=0):
    print("  " * depth + node.value)
    for child in node.children:
        print_intermediate_code(child, depth + 1)

expression = "a + b * c"
intermediate_code = generate_intermediate_code(expression)
print("Intermediate Code:")
print_intermediate_code(intermediate_code)
