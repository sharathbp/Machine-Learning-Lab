import pandas as pd
import math

class Node:
    def __init__(self, l):
        self.label = l
        self.branches = {}
        
def entropy(data):
    total_ex = len(data)
    positive_ex = len(data.loc[data["Play Tennis"]=="Y"])
    negative_ex = len(data.loc[data["Play Tennis"]=="N"])
    entropy = 0
    if positive_ex>0:
        entropy += -positive_ex/total_ex*math.log2(positive_ex/total_ex)
    if negative_ex>0:
        entropy += -negative_ex/total_ex*math.log2(negative_ex/total_ex)
    return entropy

def gain(data, attrib):
    values = set(data[attrib])
    print(values)
    gain = entropy(data)
    for val in values:
        gain -= len(data.loc[data[attrib]==val])/float(len(data))*entropy(data.loc[data[attrib]==val])
    return gain

def get_attrib(data):
    attribute = ""
    max_gain = 0
    for attr in data.columns[:-1]:
        g = gain(data, attr)
        if g>max_gain:
            max_gain = g
            attribute = attr         
    return attribute

def decision_tree(data):
    root = Node("NULL")
    if entropy(data)==0:
        root.label=data.iloc[0, -1]
        return root
    elif len(data.columns)==1:
        return root
    else:
        attrib = get_attrib(data)
        root.label = attrib
        for val in set(data[attrib]):
            root.branches[val] = decision_tree(data.loc[data[attrib]==val].drop(attrib, axis=1)) 
        return root
    
def get_rules(root, rule, rules):
    if not root.branches:
        rules.append(rule[:-2]+"=> "+root.label)
        return rules
    
    for branch_name, child_node in root.branches.items():
        get_rules(child_node, rule+root.label + "=" + branch_name + " ^ ", rules)
    return rules

def test(tree, test_str):
    if not tree.branches:
        return tree.label
    
    return test(tree.branches[test_str[tree.label]], test_str)

data = pd.read_csv("nb_data.csv")
tree = decision_tree(data[:-2])

rules = get_rules(tree, "", [])
print(rules)

test_str = {}
print("Enter test case input", end="")
for i in data.columns[:-1]:
    test_str[i] = input(i+": ")
    
print(test_str)
print(test(tree, test_str))