# -*- coding: utf-8 -*-
"""
Created on Thu Aug 09 16:30:16 2018

@author: Alain Raymond
"""

import numpy as np
#
def calculateUnknownSimilarity(i,j):
    #Init
    
    iRow=similarity_copy[i,:].copy()
    jColumn=similarity_copy[:,j].copy()

    #Dot Product between both vectors normalized by the sum is the calculated 
    #Similarity
    sumElements=(np.sum(iRow)-1)
    if sumElements==0:
        return UNKNOWN
    calculatedSimilarity=np.dot(iRow,jColumn)/sumElements #WEIGHTED AVERAGE
    
    #Using this method it is possible to get similarities that are less than -1 
    #and greater than 1 when handling both positive and negative weights.
    #To solve this, we can either:
    # * Do nothing
    # * Force the similarities into the [-1,1] domain
    # * Ignore the calculated similarity --This is what we'll do.
    #In practice, we would probably use the K closest neighbours or those whose 
    #similarities are greater than 0. Therefore, this should not be a problem.

    #print(calculatedSimilarity)
    if calculatedSimilarity < -1 or calculatedSimilarity > 1:
        return UNKNOWN
    else:
        return calculatedSimilarity

    
#Code Start

#INITIALIZATION
float_formatter = lambda x: "%.3f" % x #Output formatting
np.set_printoptions(formatter={'float_kind':float_formatter})                          
similarity=np.matrix([[1,0.5,0,0,0,0.3],#Previously calculated Similarity Matrix
                      [0.5,1,0.4,0.6,-0.3,-0.1],
                      [0,0.4,1,-0.3,0,0.4],
                      [0,0.6,0,1,0.2,0],
                      [0,0,0,0.2,1,0],
                      [0.3,-0.1,0.4,0,0,1]])
similarity_copy=similarity.copy()   #Setup Working Matrix
UNKNOWN=0                           #How we define an unknown similarity 
                                    #between user x and y
anyChanges = True                   #Stop Condition
counter=1                           #Iteration Counter


print("Starting Conditions:")
print(similarity)

while (anyChanges):
    print("Results after Iteration N°" + str(counter) + ":")
    anyChanges = False                                      #No changes so far
 
    for j in range(len(similarity)):
        for i in range(len(similarity)):
            if i>j:
                oldSimilarity=similarity[i,j]
                if oldSimilarity == UNKNOWN: #We need to calculate a similarity!
                    newSimilarity=calculateUnknownSimilarity(i,j)
                     #Keeping things symmetrical
                    similarity[i,j]=similarity[j,i]=newSimilarity      
                    #If we find an actual calculated similarity value, 
                    #then we keep it
                    if(oldSimilarity<>newSimilarity):                   
                        anyChanges=True
        
    print(similarity)
    similarity_copy=similarity.copy()
    counter+=1
    
print("Processing Finished!")
#Imprimimos resultado

