# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 11:44:48 2014

@author: preetikataly
"""

def load_dataset():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
    
def construct_candidates(dataSet):
    candidates = {}
    for group in dataSet:
        for elem in group:
                candidates.setdefault(elem, 0)
                candidates[elem] += 1
    return candidates

def filter_candidates(dataset, candidate_set, support):
    filteredSet = candidate_set
    item_num = len(dataset)
    del_keys = []
    for item, freq in candidate_set.iteritems():
        if float(freq)/float(item_num) < support:
           # print "Deleting", item
           # print item_num, freq, float(freq)/float(item_num) 
            del_keys.append(item)
    for val in del_keys:
        if val in candidate_set.keys():
            del candidate_set[val]
        
    return candidate_set

def second_pass(dataset, candidates):
    resultSet = {}
    for first_elem in candidates:
        for sec_elem in candidates:
            for group in dataset:
                if(first_elem in group and sec_elem in group):
                    resultSet.setdefault((first_elem, sec_elem,),0)
                    resultSet[(first_elem, sec_elem)] += 1
    return resultSet

dataset = load_dataset()
print dataset
candidate_set = construct_candidates(dataset)
print candidate_set
filtered_set = filter_candidates(dataset, candidate_set, 0.6)
print filtered_set
result = second_pass(dataset, filtered_set)
print result


            
                
                


                    
            
    
            
    