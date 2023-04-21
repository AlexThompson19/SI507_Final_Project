import json

def tree_to_dict(tree_node):
    """
    This module contains a single function tree_to_dict.

    tree_to_dict is a recursive function that takes in a TreeNode object representing the root node of a tree data structure, and returns a dictionary representing the tree in a nested format.

    The returned dictionary has a "data" field, which contains the data of the root node, and a "children" field, which is a list of dictionaries representing the children of the root node. Each child dictionary is created by recursively calling tree_to_dict on each child of the root node.

    To use this module, import it and call tree_to_dict with a TreeNode object representing the root node of a tree. The function will return a nested dictionary representing the tree structure, which can be saved to a file or used for other purposes.
    """

    tree_dict = {"data": tree_node.data, "children": []}
    for child in tree_node.children:
        tree_dict["children"].append(tree_to_dict(child))
    return tree_dict