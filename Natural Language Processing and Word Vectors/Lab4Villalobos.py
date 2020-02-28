'''
Ismael Villalobos
10-23-19
Lab Assignment 4
Professor Fuentes
TA-Dita Nath
Purpose:
'''
import numpy as np

import time
class BST(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
          
def NumberOfNodes(T):
    if T is None:
        return 0
    leftNum = NumberOfNodes(T.left)
    rightNum = NumberOfNodes(T.right) 
    
    return 1 + sum([leftNum,rightNum])

def Height(T):
    if T == None:
        return -1
    lh = Height(T.left)
    rh = Height(T.right)
    return 1+ max([lh,rh])


def PrintInOrder(T):
    if T is not None:
        PrintInOrder(T.left)
        print(T.data.word, T.data.emb)
        PrintInOrder(T.right)
        
        
def InsertBST(T,newWord):
    if T == None:
        T = BST(newWord)
    elif T.data.word > newWord.word:
        T.left = InsertBST(T.left,newWord)
    else:
        T.right = InsertBST(T.right,newWord)
    return T

def SearchBST(T, k):
    if T is None or T.data.word ==k:
        return T  
    elif k<T.data.word:
        return SearchBST(T.left,k)

    else:
        return SearchBST(T.right, k)
class BTree(object):
    # Constructor
    def __init__(self,data,child=[],isLeaf=True,max_data=5):    
        self.data = data
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data


def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    for i in range(len(T.data)):
        
        if k.word < T.data[i].word:
            return i
    return len(T.data)
 

def InsertInternal(T,wordObj):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,wordObj)
    else:
        k = FindChild(T,wordObj)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.data.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,wordObj)  
        InsertInternal(T.child[k],wordObj)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_data//2
    if T.isLeaf:
        leftChild = BTree(T.data[:mid],max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],max_data=T.max_data) 
    else:
        leftChild = BTree(T.data[:mid],T.child[:mid+1],T.isLeaf,max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],T.child[mid+1:],T.isLeaf,max_data=T.max_data) 
    return T.data[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    #appends data to node 
    T.data.append(i) 
    
    #sorting in alphabetical order 
    T.data.sort(key = lambda x: x.word) 

def IsFull(T):
    return len(T.data) >= T.max_data

def Leaves(T):
    # Returns the leaves in a b-tree
    if T.isLeaf:
        return [T.data]
    s = []
    for c in T.child:
        s = s + Leaves(c)
    return s

        
def InsertBTree(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.data =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
     
def HeightBTree(T):
    if T.isLeaf:
        return 0
    return 1 + HeightBTree(T.child[0])    
    
def Print(T):
    # Prints data in tree in ascending order
    if T.isLeaf:
        for t in T.data:
            print(t,end=' ')
    else:
        for i in range(len(T.data)):
            Print(T.child[i])
            print(T.data[i],end=' ')
        Print(T.child[len(T.data)])    

#returns number of nodes.
def NumberOfItems(T):
    sum = len(T.data)
    #iterating through each node of each child 
    for i in T.child:
        sum+=NumberOfItems(i)
        
    return sum 
         
def PrintD(T,space):
    # Prints data and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i])
    else:
        PrintD(T.child[len(T.data)],space+'   ')  
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i])
            PrintD(T.child[i],space+'   ')
 

def SearchBTree(T,k):
  
    for i in range(len( T.data)):
        if k.word == T.data[i].word:
            return T.data[i]
        if T.isLeaf:
            return None
        return SearchBTree(T.child[FindChild(T,k)],k)
    
    
class WordEmbedding(object):
	def __init__(self,word,embedding=[]):
		# word must be a string, embedding can be a list or and array of ints or floats
		self.word = word
		self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)
    


if __name__ =="__main__":
    
    while True:
        print('\n1. BST Implementation \n2. B-Tree Implementaion \n3. Exit ')
        
        choice  = int(input('Choose an implementation: '))
        
        
        if choice==1:
            BinaryST=None
            
            print('Creating Binary Search Tree!')
            print('Please be patient its alot of words!')
            print()
            with open("glove.6B.50d.txt",'r',encoding='utf-8') as f:
                start = time.time()
                for line in f:
                    bin_list=line.split(" ")
                    word_object=WordEmbedding(bin_list[0],bin_list[1:])
                    
                    BinaryST= InsertBST(BinaryST,word_object)
            end = time.time()
            print('Running time for constructing BST', "{:.3f}".format(end-start),' seconds')
            print('Height: ', Height(BinaryST))
            print('Number of items: ',NumberOfNodes(BinaryST))
            
            with open("pairs.txt","r") as f2:
                start2= time.time()
                for line2 in f2:
                    listBST= line2.split(" ")
                    
                    listBST[1] = listBST[1].strip()
                    
                    word1 = SearchBST(BinaryST,listBST[0])
                    word2 = SearchBST(BinaryST,listBST[1])
                    
                    distance = np.dot(word1.data.emb,word2.data.emb)/(abs(np.linalg.norm(word1.data.emb))*abs(np.linalg.norm(word2.data.emb))) 
                    
                    print("Similarity [", word1.data.word, word2.data.word, "] =","{:.3f}".format(distance))
         
                    
            end2 = time.time()
            print("\nTime taken to compute similarities", "{:.3f}".format(end2-start2),' seconds',"\n") 

                
        if choice==2:
            input_max_data = int(input('Enter max data: '))
            
            T = BTree([],max_data =input_max_data )
            print('Creating B-Tree!')
            print('Please be patient its alot of words!')
            
            with open("glove.6B.50d.txt",'r',encoding='utf-8') as file:
                start = time.time()
                for line in file:
                    eachline=line.split(" ")
                    
                    word_object = WordEmbedding(eachline[0],eachline[1:])
                    
                    InsertBTree(T,word_object)
            end = time.time()
            print('Running time for constructing BTree',"{:.3f}".format(end-start),' seconds')
            print('Height: ', HeightBTree(T))
            print('Number of items: ',NumberOfItems(T))
            
            with open("pairs.txt",'r') as file2:
                start1 = time.time()
        
                for line in file2:
                    line = line.strip().split(" ")
                    
                    #searching for each word in B-tree 
                    obj1 = WordEmbedding(line[0]) #creating an object with the current word
                    obj2 = WordEmbedding(line[1])  
                    
                    word1 = SearchBTree(T,obj1) #searching for the first word 
                    word2 = SearchBTree(T,obj2) #searching for second word
                    
                    distance = np.dot(word1.emb,word2.emb)/(abs(np.linalg.norm(word1.emb))*abs(np.linalg.norm(word2.emb))) 
                    
                    print("Similarity [", word1.word, word2.word, "] =","{:.3f}".format(distance))
    
            end2 = time.time()
            print("\nTime taken to compute similarities","{:.3f}".format(end2-start2),' seconds',"\n")
            
        elif choice ==3:
            print('Ending program, BYE!')
            break
      
