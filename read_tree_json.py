import json

class TreeNode:
    """
    This module contains a class TreeNode and two functions dict_to_tree and read_tree_from_json.

    TreeNode represents a node in a tree data structure, where each node has a data field and
    a list of children.
    It has an add_child method to add a child to the list of children, and a display
    method to print the node and its children in a readable format.

    dict_to_tree is a recursive function that takes in a dictionary representing a tree,
    creates a TreeNode object with the data from the dictionary, and adds its children
    by recursively calling dict_to_tree on each child dictionary.

    read_tree_from_json is a function that takes in the name of a JSON file, reads the
    contents of the file, and converts it to a dictionary using the json.load function.
    It then calls dict_to_tree to create a tree structure from the dictionary, and returns
    the root node of the tree.

    To use this module, import it and call read_tree_from_json with the name of a JSON
    file containing the tree data. The function will return the root node of the tree,
    which can be used to navigate the tree structure using the methods of the TreeNode class.

    Input the name of a json file to examine the tree.
    """

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
