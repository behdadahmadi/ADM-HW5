import numpy as np
# I am using numpy for faster calculation
#At first, I used a Python List, but the problem was it's too slow

class Graph:
    def __init__(self,edge_size):
        #Whenever we want to create a new graph, we adjust the edge_size
        #Otherwise, we adjust it with 0 size and then load it with our files
        self.g = np.zeros((edge_size,2),dtype=int) #Our graph matrix
        self.weights = np.zeros(edge_size) #Our weights vector
        self.node = set() #Our nodes, we want them be unique
        self.index_g = 0 #Our indexer
    def AddEdge(self,node1,node2,weight):
        #We know we don't have any duplicate that's why we don't check for any existence
        self.g[self.index_g] = node1,node2 #Adding edge
        self.weights[self.index_g] = self.weights[self.index_g] + weight #Adding weight
        self.index_g = self.index_g + 1
        self.node.add(node1) #Adding node1 name to our nodes set
        self.node.add(node2) #Adding node2 name to our nodes set

    def LoadGraph(self,graphStructureFile,graphWeightsFile):
        #To load a graph
        with open(graphStructureFile,"r") as f:
            self.g = np.load(f)
        with open(graphWeightsFile,"r") as f:
            self.weights = np.load(f)
        print("Graph is loaded")
    def GetGraph(self):
        return self.g #Returning graph itself
    def _getSize(self):
        return len(self.g)
    def GetNodeSize(self):
        return len(self.node) #Returning graphNodeSize
    def GetEdgeByName(self,edgeName):
        indexes = np.where(self.g == edgeName)[0] #Finding edge index by it's name
        return self.g[indexes] #Then returning it
    def _writeGraph(self,filePath):
        #Graph Structure
        with open(filePath+".gs", 'wb') as f:
            np.save(f,self.g)
    def _writeWeights(self,filePath):
        #Graph Weights
        with open(filePath+".gw","wb") as f:
            np.save(f,self.weights)

    def WriteGraphToFile(self,filePath):
        self._writeWeights(filePath)
        self._writeGraph(filePath)
        print("Graph is saved")

