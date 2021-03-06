# pylint: disable=W0621,W0612,C0103,W1401
"""
--- Day 7: Recursive Circus ---
Wandering further through the circuits of the computer, you come upon,
a tower of programs that have gotten themselves into a bit of trouble.,
A recursive algorithm has gotten out of hand, and now they're balanced,
precariously in a large tower.

One program at the bottom supports the entire tower. It's holding a,
large disc, and on the disc are balanced several more sub-towers.,
At the bottom of these sub-towers, standing on the bottom disc, are,
other programs, each holding their own disc, and so on. At the very,
tops of these sub-sub-sub-...-towers, many programs stand simply keeping,
the disc below them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of,
these towers. You ask each program to yell out their name, their weight,,
and (if they're holding a disc) the names of the programs immediately,
above them balancing on that disc. You write this information down,
(your puzzle input). Unfortunately, in their panic, they don't do,
this in an orderly fashion; by the time you're done, you're not,
sure which program gave which information.

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
...then you would be able to recreate the structure of the t
owers that looks like this:

                gyxo
              /    ,
         ugml - ebii
       /      \    ,
      |         jptl
      |       ,
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |            ,
      |         ktlj
       \      /    ,
         fwft - cntj
              \    ,
                xhth
In this example, tknk is at the bottom of the tower (the bottom program),,
and is holding up ugml, padx, and fwft. Those programs are, in turn,,
holding up other programs; in this example, none of those programs are,
holding up any other programs, and are all the tops of their own towers.,
(The actual tower balancing in front of you is much larger.)

Before you're ready to help them, you need to make sure your information,
is correct. What is the name of the bottom program?"""
import os
import re

class Node():
    """Class to hold the Node object for building a tree"""
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = [c for c in children if len(c) > 0]
        self.parent = None
        self.subtreeweight = None

def parse_data_7b(lines):
    """Process the array of lines into dictionary where every node points to its parent"""
    lineregex = re.compile(r'^(\w*) \((\d*)\) ?(?:\->)? ?(.*)')
    all_nodes = {}
    # matches: 0 - node, 1 - weight, 2: list of children
    for line in lines:
        match = lineregex.match(line)
        nodes = match.groups()
        n = Node(nodes[0], int(nodes[1]), [c.strip() for c in nodes[2].split(',') if c != ','])
        all_nodes[n.name] = n
    return all_nodes

def build_tree(nodeDict):
    """Add parent to each child node"""
    for node in nodeDict:
        current_node = nodeDict[node]
        if current_node.children is not None:
            for child in current_node.children:
                nodeDict[child].parent = current_node
    return nodeDict

def find_tree_root(nodeDict):
    """Find the tree root by starting with the first key
       and inspecting its parent until we find a node
       without a parent - by definition that is the root
    """
    node = nodeDict[list(nodeDict.keys())[0]]
    while (node is not None and node.parent is not None):
        node = node.parent
    return node


def weigh_subtree(nodeDict, node):
    """Calculate the weight of the subtree by summing the node's
       weight plus the weights of its children.
       """
    node.subtreeweight = node.weight + sum(
        weigh_subtree(nodeDict, nodeDict[c]) for c in node.children)
    return node.subtreeweight

def weighted_tree(nodeDict):
    """This is the man that performs the top-down recursive weight calculation on the tree"""
    root = find_tree_root(nodeDict)
    weigh_subtree(nodeDict, root)
    return nodeDict

def find_unbalanced_node(nodeDict):
    """Return the unbalanced node, i.e. the one where the children
    have different subtree weights.
    Returns a tuple of: name of unbalanced node, my weight, their weights
    and the correct weight for the node
    """
    nodeDict = build_tree(nodeDict)
    nodeDict = weighted_tree(nodeDict)

    for nodeKey in nodeDict:
        subtreeweights = {}
        for c in nodeDict[nodeKey].children:
            if nodeDict[c].subtreeweight in subtreeweights:
                subtreeweights[nodeDict[c].subtreeweight].append(c)
            else:
                subtreeweights[nodeDict[c].subtreeweight] = [c]
            for k in subtreeweights:
                if len(subtreeweights) > 1 and len(subtreeweights[k]) == 1:
                    offendingChild = nodeDict[subtreeweights[k][0]]
                    childWeight = offendingChild.subtreeweight
                    parentNode = offendingChild.parent
                    for childkey in parentNode.children:
                        if nodeDict[childkey].subtreeweight != childWeight:
                            print(subtreeweights)
                            return offendingChild.name, childWeight, \
                                    nodeDict[childkey].subtreeweight, \
                                    offendingChild.weight - \
                                    childWeight + \
                                    nodeDict[childkey].subtreeweight


def readfile(filename):
    """Read file and return as a list of lines"""
    with open(filename, "r") as the_file:
        lines = the_file.readlines()
    return [l for l in lines]

def parse_data_7(lines):
    """Process the array of lines into dictionary where every node points to its parent"""
    lineregex = re.compile(r'^([a-z]*) \(([0-9]*)\) \-> (.*)')
    parent = {}
    # matches: 0 - node, 1 - weight, 2: list of children
    for line in lines:
        match = lineregex.match(line)
        if match is not None:
            nodes = match.groups()
            if len(nodes) == 3:
                # for now, just consider the parent
                for child in [c.strip() for c in nodes[2].split(',') if c != ',']:
                    parent[child] = nodes[0]
    return parent

def find_root(parents):
    """ Given a dictionary where each child is a key and its value is its parent,
        we determine the single element which does not have a parent.
        By definition, this is the tree's root.
    """
    roots = set([parents[n] for n in parents if parents[n] not in parents])
    assert len(roots) == 1
    return roots.pop()

# lines = readfile(os.path.join(os.path.dirname(__file__), 'day7.txt'))
# parents = parse_data_7(lines)
# print(find_root(parents))
# # 7a: eugwuhl
if __name__ =='__main__':
    lines = readfile(os.path.join(os.path.dirname(__file__), 'day7.txt'))
    all_nodes = parse_data_7b(lines)
    r = find_unbalanced_node(all_nodes)
    print(f'Unbalanced node: {r[0]}, current-weight: {r[1]}, ideal weight: {r[2]}, node-weight: {r[3]}')
