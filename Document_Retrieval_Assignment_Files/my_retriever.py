class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting): #Initial an object
        self.index = index #
        self.termWeighting = termWeighting #Collect termWeighting
        self.vectormodel = self.Make_Vector_Model(index) #Model vector space for index
        #print(list(self.vectormodel.items())[1])
    # Method performing retrieval for specified query
    def forQuery(self, query): #Query function
        index_set = set(self.index.keys())# Make the set of words
        q_set = set(query.keys())# Make the set of query
        #print("query :", query)
        #print(len(new_set))
        ###Check Mode
        similarity = {}
        if self.termWeighting == "binary":
            size_q = len(query)**(0.5)
            print("Mode : binary")
            for d,terms in self.vectormodel.items():
                size_d = len(terms)**(0.5) # Getting the size of d
                #print("|d| = ",size_d)
                #print("|q| = ",size_q)
                qd = {k: terms[k]*query[k] for k in query if k in terms}
                #print("terms : ",terms)
                #print("Query : ",query)
                #print("qd : ",qd)
                size_qd = len(qd)**(0.5) #Getting the size of qd
                similarity[d] = size_qd/(size_q*size_d) #Calculate for similarity using similar equation
            #print("sim : ",similarity)
            sorted_similarity = sorted(similarity.items(), key=lambda values: values[1], reverse=True) #Sorting values and get only first 10 values
            print(sorted_similarity[0:10])
            return sorted_similarity
        if self.termWeighting ==  "tf":
            print("Mode : tf")
        if self.termWeighting == "tfidf":
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
