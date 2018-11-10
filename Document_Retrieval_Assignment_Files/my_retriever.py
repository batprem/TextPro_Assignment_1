import numpy as np

class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        #print(self.index)
        self.termWeighting = termWeighting
        

    # Method performing retrieval for specified query
    def forQuery(self, query):
        print(self.termWeighting)
        #print("The index is ",self.index)
        #print("The query is ", query)
        #print(self.index['a'])
        index_set = set(self.index.keys())# Make the set of words
        print(query)
        q_set = set(query.keys())# Make the set of query
        new_set = q_set.intersection(index_set)
        new_set = sorted(list(new_set))
        print("new_set : ",new_set)
        print("self :",len(self.index[new_set[0]]))
        print("query :", query)
        #print(len(new_set))
        return list([1,2])
    def Make_Vector_Model(Document):
        vector= {}
        if "a" in vector:
            print("no key")
        else:
            print("Has key")
        #for i in xrange(100):
        #    key = i % 10
        #     if key in d:
        #    d[key] += 1
        #else:
        #d[key] = 1
        return vector

