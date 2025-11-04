import numpy as np
arr1 = ["cat", "bear", "dog", "snake", "tiger", "lion", "lion", "panda", "elephant",
         "giraffe", "bear", "eagle", "monkey", "horse", "goat", "snake", "lion", "panda", "bear"]

arr2 = ["zebra", "elephant", "panda", "wolf", "fox", "owl", "dog", "tiger",
         "rabbit", "lion", "lion", "panda", "elephant", "tiger", "owl", "bear", "panda"]
print("array 1 is ", arr1)
print("array 2 is ",arr2)

def findMostFrequentWord(inputList1: list[str], inputList2: list[str]) -> str:
    def find():
        plural=[] #empty array
        needed=[] #empty array
        not_needed=[] #empty array
        counts={} #empty dictionary
        for word in inputList1:
            if word not in inputList2: #if the word in arr1 is not in arr2
                needed.append(word) #add to needed list
            else:
                None
        for word in needed:
            if needed.count(word)>1: #if the word is there more than once
                plural.append(word) #add to plural list
                counts[word] = counts.get(word,0) +1 #Look up the current count for this word, add one and save it back
            else:
                not_needed.append(word) #add to not needed if only appears once
        most_common=max(counts, key=counts.get) #to get most common word
                
        return needed, plural, most_common, counts #return all

    needed,counts,plural,most_common=find()
    print("most common word not in array 1 is ", most_common)
    
findMostFrequentWord(arr1,arr2)
            
                      
