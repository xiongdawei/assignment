#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 23:53:55 2018

@author: davidxiong
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class KNN():
    def _init_(self,test,trained_data,labels,k):
        self.test = None
        self.trained_data = None
        self.labels = None
        self.k = None
        
    def set_test(self,test):
        self.test = test
        
    def set_trained_data(self,trained_data):
        self.trained_data = trained_data
    
    def set_labels(self,labels):
        self.labels = labels
        
    def set_k(self,k):
        self.k = k
      
    # four function to set the value of the four important parameters
        
    def classify(self):
        """
        test: a list that will be classied
        trained_data: array
        labels: types of data
        k: the parameter of the algorithms
        """
        size = self.trained_data.shape[0] # get the number of lines 
        matrix = np.tile(self.test,(size,1)) - self.trained_data 
        # np.tile() creates a matrix
        # test is the array that will be duplicated, size for row and 1 column
        # '-trained_data' minus 'test'
        
        square_matrix = matrix**2
        # sqaure every elements in the matrix
        
        distance = (square_matrix.sum(axis=1))**0.5
        # add up horizontally
        
        sorted_indices = distance.argsort()
        # return the index after bring sorted from the smallest to the biggest
        
        classCount = {} # create a new dictionary
        
        for i in range(k):
            label = self.labels[sorted_indices[i]] # get the according indice
            classCount[label] = classCount.get(label,0) +1
            sortedClassCount = sorted(classCount,reverse = True)# sorted reversely
            return sortedClassCount[0]
        
    def vslz(self):
        """
        trained_data: array that is the data we trained 
        test: a list that will be classcified
        This function intends to visualize the data
        """
        x = self.trained_data[:,0]
        y = self.trained_data[:,1]
        plt.xlabel('x-value')
        plt.ylabel('y-value')
        plt.scatter(x,y,s=20,c='b',marker='o')
        plt.scatter(self.test[0],self.test[1],c='r',marker='o')
        plt.show() # visualization of the data
        
    def count(self):
        """
        get the number of trained data and the number labels
        """
        print("Group:" + str(len(self.trained_data)))
        print('Labels:' + str(len(self.labels)))
        
    def openfile(self,filename):
        testlist = []
        df = pd.read_excel(filename)
        testlist.append(df)
        testlist1 = []
        testlist2 = []
        a = -1 
        b = 0
        c = 1
        while b<len(testlist)-3:
            testlist1.append([testlist[a+3],testlist[b+3]])
            testlist2.append([testlist[a+3],testlist[c+3]])
        test_array1 = np.array(testlist1)
        test_array2 = np.array(testlist2)
        return test_array1, test_array2

    def autoNorm(self,dataSet):
        minVals = dataSet.min(0) # get the minimum value of the data
        maxVals = dataSet.max(0) # get the maximum value of the data
        ranges = maxVals - minVals # the range of the maximum value and the minimum value
        normDataSet = np.zeros(np.shape(dataSet))# shape(dataSet) return the number of lines of the matrix
        m = dataSet.shape[0]
        normDataSet = dataSet - np.tile(minVals,(m,1))
        normDataSet = normDataSet / np.tile(ranges,(m,1)) # 
        return normDataSet, ranges, minVals
      
    def open_file(self,filename):
        df = pd.read_excel(filename)
        testlist = []
        testlist.append(df)
        return testlist
    
"""   
    def acc(self,test_matrix,trained_data,test_labels):
        error = 0
        k = KNN()
        number = len(test_matrix)
        for i in test_matrix:
           if k.classify_new(test_matrix[i],trained_data,test_labels,) != test_labels[i]:
               error +=1
        return error       
"""    

    

    
                
            
            

    
    #def accuracy(self,filename):
    #def algorithm_test(self,test_array):
"""    
df = pd.read_excel('data_for_hw.xlsx')
print(df)
print(df.shape[0])
print(df.shape[1])
#print(df.shape[2])
"""        
test = np.array([200,1])
labels = ['Romantics','Romantics','Romantics','Romantics','Action','Action','Action','Action','Action','Action']
k = 10
group = np.array([[1,101],[5,89],[10,88],[11,92],[108,5],[115,8],[120,7],[110,6],[112,8],[105,13]])

#group_new = np.array([[0,22],[0,7677],[1,36],[2,39],[3,32],[4,29],[5,35],[6,34],[7,12]])
#labels_new = ['A','B','A','A','A','A','A','A','A']
obj = KNN()
obj.set_test(test)
obj.set_trained_data(group)
obj.set_labels(labels)
obj.set_k(k)

print(obj.classify())
obj.vslz()
#obj.count()
#print(obj.openfile('data_for_hw.xlsx'))
#print(obj.open_file('data_for_hw.xlsx'))


test_matrix = np.array([[15,88],[20,67],[30,50],[88,12],[67,30],[50,50]])
test_labels = ['Romantics','Romantics','Romantics','Action','Action','Action']
obj.set_test(test_matrix)
obj.set_labels(test_labels)
#obj.classify_new(test,test_matrix,test_labels,len(test_matrix))
obj.vslz()


#print(obj.acc(test_matrix,group,test_labels))





            
            
            
            
            
        
    
            
        
        
    
        
    
        
        