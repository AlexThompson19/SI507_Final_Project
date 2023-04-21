import json

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print("  " * level + str(self.data))
        for child in self.children:
            child.display(level + 1)

def dict_to_tree(tree_dict):
    tree_node = TreeNode(tree_dict["data"])
    for child_dict in tree_dict["children"]:
        child_node = dict_to_tree(child_dict)
        tree_node.add_child(child_node)
    return tree_node

def read_tree_from_json(json_file):
    with open(json_file, "r") as f:
        tree_dict = json.load(f)
    return dict_to_tree(tree_dict)

if __name__ == "__main__":
    json_file = input("Please enter the name of the JSON file: ")
    michigan_tree = read_tree_from_json(json_file)
    michigan_tree.display()
