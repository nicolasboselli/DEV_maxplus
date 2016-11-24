'''
    Creates a simple text representation of the scene graph
'''
import MaxPlus
import sys

def outputNode(n, indent = ''):
    print indent, n.Name
    for c in n.Children:
        outputNode(c, indent + '--')
        
if __name__ == '__main__':
    outputNode(MaxPlus.Core.GetRootNode())