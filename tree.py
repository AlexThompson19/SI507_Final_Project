import json

def tree_to_dict(tree_node):
    tree_dict = {"data": tree_node.data, "children": []}
    for child in tree_node.children:
        tree_dict["children"].append(tree_to_dict(child))
    return tree_dict