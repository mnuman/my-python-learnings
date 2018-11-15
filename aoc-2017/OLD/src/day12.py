r"""
--- Day 12: Digital Plumber ---
Walking along the memory banks of the stream, you find a small
village that is experiencing a little confusion: some programs can't
communicate with each other.

Programs in this village communicate using a fixed system of pipes
 Messages are passed between programs using these pipes, but most 
 programs aren't connected to each other directly. Instead, programs 
 pass messages between each other until the message reaches the 
 intended recipient.

For some reason, though, some of these messages aren't ever 
reaching their intended recipient, and the programs suspect 
that some pipes are missing. They would like you to investigate.

You walk through the village and record the ID of each program and 
the IDs with which it can communicate directly (your puzzle input). 
Each program has one or more programs with which it can communicate, 
and these pipes are bidirectional; if 8 says it can communicate 
with 11, then 11 will say it can communicate with 8.

You need to figure out how many programs are in the group that 
contains program ID 0.

For example, suppose you go door-to-door like a travelling 
salesman and record the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
In this example, the following programs are in the 
group that contains program ID 0:

Program 0 by definition.
Program 2, directly connected to program 0.
Program 3 via program 2.
Program 4 via program 2.
Program 5 via programs 6, then 4, then 2.
Program 6 via programs 4, then 2.
Therefore, a total of 6 programs are in this group; all but 
program 1, which has a pipe that connects it to itself.

How many programs are in the group that contains program ID 0?
"""
import os

def readfile(fname):
    """Given a filename, parse its contents into a dictionary
       listing the connections for a the given key/node
       as a list
    """
    nodes = {}
    with open(fname, "r") as f:
        res = f.readlines()
    for line in [regel.split('<->') for regel in res]:
        nodes[line[0].strip()] = [n.strip() for n in line[1].split(',')]
        
    return nodes
    
def reachable(graph, node):
    """Givea graph dictionary listing the connected vertices 
       for a given vertex, return the unique list of nodes
       that can be reached from this vertex
       """
    return reachability(graph, node, seen=None)

def reachability(graph, node, seen=None):
    """Walk the graph"""
    seen = seen or []
    seen.append(node)
    reached = set(node)
    adjacent = graph.get(node)
    
    if adjacent:
        reached.update(adjacent)
        for subnode in adjacent:
            if subnode in adjacent:
                if subnode not in seen:
                    reached.update(reachability(graph, subnode, seen))
    final_result = list(reached)
    return final_result

def R(G,s,A):
    """ Code golf solution! https://codegolf.stackexchange.com/questions/26031/find-all-reachable-nodes-in-a-graph"""
    A|={s}
    for n in set(G[s])-A:R(G,n,A)

if __name__ == '__main__':
    NODES = readfile(os.path.join(os.path.dirname(__file__), 'day12.txt'))
    
    groupSet = set()
    # brute force: just iterate over all nodes to collect the 
    # sorted list of reachable nodes for every node without
    # considering whether the current node of interest already
    # occurs as one of the reachable nodes for another node.
    # In that case the group is already known ...
    for node in NODES:
        A=set()
        R(NODES, node, A)
        groupSet.add(tuple(sorted(A)))
    print(len(groupSet))
    # 12: 145
    # 12b: 207
