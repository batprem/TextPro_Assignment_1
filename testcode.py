 
Dict_test = {
    "a":{ 1:2,
        2:3,
        4:10
        },
    "b":{ 1:5,
        4:5,
        10:11
        },
    "c":{ 7:10,
        15:2,
        13:14
        }
}

#### function for preprocessing (Make vector model) #####
vector = {} #return the vector values as a dictionary object 
for key,value in Dict_test.items(): # Getting keys and values in the first layer; key is term and value is dictionary inside
    print(key, " : ", value)  
    for key_in,value_in in value.items(): # Getting keys and values in the second layer
        print(key_in, " : ", value_in) #key_in is document and value_in is number of the term in the document
        if key_in in vector: #Checking whether "vector" contains key_in
            vector[key_in][key] = value_in #adding value
        else:
            vector[key_in] = {}
            vector[key_in][key] = value_in #adding value
##    if 2 in value:
##        print(key, " : ", value[2])
##    else:
##        print("There is no key 2 in ", key)
