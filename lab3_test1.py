# -*- coding: utf-8 -*-
"""
CS 2302 Data Structures
Professor: Fuentes
TAs: Anindita Nath, Maliheh Zargaran
Assignment: Lab3
03/12/2019
@author: Joey Roe
"""
import numpy as np
import matplotlib.pyplot as plt
import math

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right) 
    
    
    
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

        
#Number 1       
def draw_circles(ax,center,radius, tree, Distance):
    if tree != None:
        x,y = circle(center,radius)
        ax.fill(x,y, c = 'w')
        ax.plot(x,y,color='k')
        ax.text(center[0]-5, center[1]-1, tree.item, fontsize = 8)
        newCenterL = np.array([center[0] - (Distance // 2), center[1] - 40])
        newCenterR = np.array([center[0] + Distance, center[1] - 40])
        draw_circles(ax, newCenterL, radius, tree.left, Distance * 0.4)
        draw_circles(ax, newCenterR, radius, tree.right, Distance * 0.4)
        
    


#Number 2        
def Find(T, k):
    while T != None:
        if T.item == k:
            return T
        if k > T.item:
            T = T.right
        elif k < T.item:
            T = T.left
    else:
        return None
            
            
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
        

#Number 3
def TreeBuilder(theList):
    if len(theList) == 0:
        return None
    else:
        middleindex = len(theList) // 2
        tree = BST(theList[middleindex])

        tree.left = TreeBuilder(theList[: middleindex])
        tree.right = TreeBuilder(theList[middleindex + 1 :])
        return tree
  
    
#Number 4        
def turnTreeToList(tree):
    if tree == None:
        return []
    else:
        return turnTreeToList(tree.left) + [tree.item] + turnTreeToList(tree.right)   
    

#part of number 5
def findHeight(tree):
    if tree == None:
        return -1
    else:
        a = 1 + findHeight(tree.left)
        b = 1 + findHeight(tree.right)
    if a >= b:
        return a
    if b >= a:
        return b


#part of number 5
def printElementsAtDepth(T,n):
    if T is None: 
        return 
    if n == 0: 
        print (T.item, end = ' ')
    else: 
        printElementsAtDepth(T.left, n-1) 
        printElementsAtDepth(T.right, n-1)
        
  
#number 5      
def printDepthOrder(tree, height):
    for i in range(height + 1):
        print('Keys at depth ', i, ': ', end = ' ')
        printElementsAtDepth(tree, i)
        print()
    
        
        
   
        
"""
Main Method
""" 
       
t = None   
a = [10, 4, 15, 2, 8, 12, 18, 1, 3, 5, 9, 7]
for i in a:
    t = Insert(t, i)
treeBuilt = TreeBuilder(a)

plt.close("all")
fig, ax = plt.subplots()
ax.set_aspect(1.0)
center = np.array([100, 100])
draw_circles(ax, center, 10, t, 152)
plt.show()
treeBuilt = TreeBuilder(a)
print('tree built: ')
InOrderD(treeBuilt, ' ')
print()
print('--------------------------------')
print()
FindAndPrint(t, 15)
FindAndPrint(t, 33)
print()
sortedList = turnTreeToList(t)
print('sorted list from a tree: ', sortedList)
print()
printDepthOrder(t, findHeight(t))
