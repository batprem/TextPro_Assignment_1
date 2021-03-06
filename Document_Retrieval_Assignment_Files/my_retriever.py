     
class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting): #Initial an object
        self.index = index #Save index
        self.termWeighting = termWeighting #Collect termWeighting
        self.vectormodel = self.Make_Vector_Model(index) #Model vector space for index
        if self.termWeighting == "tfidf": #in case of ifidf is selected
            from numpy import log10 #import log10 fucntion
            self.Log = log10 #Save log10 function
            D = len(self.vectormodel) # |D|
            idf = {} #initial idf
            tfidf = {} #initial tfidf
            for d,terms in index.items(): #Calculate for idf
                df = len(terms) #All document containing term 'w'
                idf[d] = self.Log(D/df) #obtaining idf(w)
            for tf,terms in self.vectormodel.items(): #Calculate for tfidf tf is a document, terms are words with frequency
                tfidf[tf] = {} #initial tfidf vector
                for word,TF in self.vectormodel[tf].items(): #Obtain term frequency of a vector  #TF in the number of times word occur in a Document.
                    tfidf[tf][word] = TF*idf[word] #Adding tfidf of each term in a document using tf(w,d)*idf(w)
            self.idf = idf #save idf of each term
            self.tfidf = tfidf #save tfidf of each document
        
    # Method performing retrieval for specified query
    def forQuery(self, query): #Query function
        ###Check Mode
        similarity = {} #initial similarity for returning
        if self.termWeighting == "binary": #Mode binary
            size_q = len(query)**(0.5) # Getting the size of q
            #print("Mode : binary")
            for d,terms in self.vectormodel.items(): # d is document, terms are words and frequency in d
                size_d = len(terms)**(0.5) # Getting the size of d
                qd = {k: terms[k]*query[k] for k in query if k in terms} #Calculate qd
                if qd == {}: #If there is no query's term is the document, continue the loop
                    continue
                size_qd = len(qd)**(0.5) #Getting the size of qd
                similarity[d] = size_qd/(size_q*size_d) #Calculate for similarity using similar equation
            sorted_similarity = sorted(similarity.keys(), key=lambda k: similarity[k], reverse=True) #Sorting values and get only first 10 values
            return sorted_similarity #return first 10 highest similarity
        elif self.termWeighting ==  "tf": #Mode tf
            size_q = sum([q**2 for q in list(query.values())])**(0.5) #Getting the size of query
            for d,terms in self.vectormodel.items(): #d is document, terms is a word in d
                qd = {} #initial qd
                for k in query: #k is a term in query
                    if k in terms: #check if k is in a document
                        qd[k] = terms[k]*query[k] #Calculate qd
                    else:
                        continue #If there is no query's term is the document, continue the loop
                #size_d = sum([t**2 for t in list(terms.values())])**(0.5) # Getting the size of d
                size_d = sum(x*x for x in terms.values())**(0.5) # Getting the size of d
                #size_qd = sum([QD**2 for QD in list(qd.values())])**(0.5) # Getting the size of qd
                size_qd = sum(x*x for x in qd.values())**(0.5) #Calculate size_qd
                similarity[d] = size_qd/(size_q*size_d) #Calculate for similarity using similar equation
            sorted_similarity = sorted(similarity.keys(), key=lambda k: similarity[k], reverse=True) #Sorting values and get only first 10 values
            return sorted_similarity[0:10] #return first 10 highest similarity
        elif self.termWeighting == "tfidf": #Mode tfidf
            ###calculate tfidf of query##
            tfidf_query = {} #initial tfidf of query
            for tf,terms in query.items(): #Calculate for tfidf of query, tf is a word and terms are frequencies of the word
                
                if tf in self.idf: #Check if word presents in idf

                    tfidf_query[tf] = terms*self.idf[tf] #save tfidf of word "tf"
                else:
                    tfidf_query[tf] = 0
            #\print(tfidf_query)
            #############################
            size_q = sum(q**2 for q in tfidf_query.values())**(0.5) #Getting the size of tfidf of query
            for d,terms_tfidf in self.tfidf.items():
                qd={} #initail qd
                for k in tfidf_query: #k is a word in query
                    if k in terms_tfidf: #check if k is in d
                        qd[k] = terms_tfidf[k]*tfidf_query[k] #calculate each qd
                    else:
                        continue
                if qd == {}: #if there is no word which qd and k have common, continue the loop
                    continue #ignore null case
                size_d = sum(x*x for x in terms_tfidf.values())**(0.5) # Getting the size of d
                size_qd = sum(x*x for x in qd.values())**(0.5) # Getting the size of qd
                similarity[d] = size_qd/(size_q*size_d) #Calculate for similarity using similar equation
            sorted_similarity = sorted(similarity.keys(), key=lambda k: similarity[k], reverse=True) #Sorting values and get only first 10 values
            #print(sorted_similarity[0], " : ", similarity[1410])
            return sorted_similarity[0:20] #return first 10 highest similarity
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
        return vector #return calculate vector
