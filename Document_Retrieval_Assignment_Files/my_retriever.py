     
class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    import sys, getopt, re, time
    def __init__(self,index, termWeighting): #Initial an object
        self.index = index #
        self.termWeighting = termWeighting #Collect termWeighting
        self.vectormodel = self.Make_Vector_Model(index) #Model vector space for index
        if self.termWeighting == "tfidf": #in case of ifidf is selected
            from numpy import log10
            self.Log = log10 #Save log10 function
            D = len(self.vectormodel) # |D|
            idf = {} #initial idf
            tfidf = {}
            for d,terms in index.items(): #Calculate for idf
                df = len(terms)
                idf[d] = self.Log(D/df)
            for tf,terms in self.vectormodel.items(): #Calculate for tfidf
                tfidf[tf] = {}
                print(tf)
                for word,IDF in idf.items():
                    if word in self.vectormodel[tf]:
                        tfidf[tf][word] =self.vectormodel[tf][word]*idf[word]
                    else:
                        continue
                    #print(idf[word])
                    #tfidf[tf][word] =self.vectormodel[tf][word]*idf[word]
            print("tfidf : ",tfidf)
        
    # Method performing retrieval for specified query
    def forQuery(self, query): #Query function
        ###Check Mode
        similarity = {}
        if self.termWeighting == "binary": #Mode binary
            size_q = len(query)**(0.5) # Getting the size of q
            #print("Mode : binary")
            for d,terms in self.vectormodel.items():
                size_d = len(terms)**(0.5) # Getting the size of d
                qd = {k: terms[k]*query[k] for k in query if k in terms} #Calculate qd
                if qd == {}: #If there is no query's term is the document, continue the loop
                    continue
                size_qd = len(qd)**(0.5) #Getting the size of qd
                similarity[d] = size_qd/(size_q*size_d) #Calculate for similarity using similar equation
            sorted_similarity = sorted(similarity.keys(), key=lambda k: similarity[k], reverse=True) #Sorting values and get only first 10 values
            return sorted_similarity
        elif self.termWeighting ==  "tf": #Mode tf
            #print("Mode : tf")
            size_q = sum([q**2 for q in list(query.values())])**(0.5) #Getting the size of query
            for d,terms in self.vectormodel.items():
                qd = {k: terms[k]*query[k] for k in query if k in terms} 
                if qd == {}: #If there is no query's term is the document, continue the loop
                    continue
                size_d = sum([t**2 for t in list(terms.values())])**(0.5) # Getting the size of d
                size_qd = sum([QD**2 for QD in list(qd.values())])**(0.5) 
                #print(size_qd)
                #print(d," : ",qd)
                #size_qd = len(qd)**(0.5) #Getting the size of qd
                similarity[d] = size_qd/(size_q*size_d) #Calculate for similarity using similar equation
            sorted_similarity = sorted(similarity.keys(), key=lambda k: similarity[k], reverse=True) #Sorting values and get only first 10 values
            #print(similarity[sorted_similarity[0]])
            #print(similarity[sorted_similarity[1]])
            return sorted_similarity
        elif self.termWeighting == "tfidf":
            print("Mode : tfidf")
        return list([1,2])
        ###
    def Make_Vector_Model(self, Document):
        vector = {} #return the vector values as a dictionary object 
        for key,value in Document.items(): # Getting keys and values in the first layer; key is term and value is dictionary inside
        #   print(key, " : ", value)  
            for key_in,value_in in value.items(): # Getting keys and values in the second layer
                #print(key_in, " : ", value_in) #key_in is document and value_in is number of the term in the document
                if key_in in vector: #Checking whether "vector" contains key_in
                    vector[key_in][key] = value_in #adding value
                else:
                    vector[key_in] = {} #initial basis
                    vector[key_in][key] = value_in #adding value
        return vector
