
class HashTable : 
    def __init__(self , size ) : 
        self.MAX = size
        self.arr = [[] for i in range (self.MAX)]
    # hashing function by ASCI
    def hashing (self , keys) : 
        h= 0 
        for key in keys : 
            asc = ord(key)
            h += asc 
        return h % self.MAX
    # add to the hash tabel 
    def __setitem__(self , key , value) : 
        hasehdKey = self.hashing(key)
        found  = False
        for index , element in enumerate(self.arr[hasehdKey]) : 
            if (len(element) == 2 and element[0] == key) : 
                self.arr[hasehdKey][index] = (key, value)
                found = True
                break
        if not found : 
            self.arr[hasehdKey].append((key, value))
    # get a vallue by key 
    def __getitem__ (self , key ) : 
        hashed_key = self.hashing(key)
        if self.arr[hashed_key]:
            for element in self.arr[hashed_key]:
                if element[0] == key:
                    return element[1]
        else : 
            return "key :{0} is not found in hashed tabel".format(key)
        
    # delet item by key
    def __delitem__ (self , key) : 
        hashed_key = self.hashing(key)
        if self.arr[hashed_key]:
            for index,  element in enumerate(self.arr[hashed_key]):
                if element[0] == key:
                    del self.arr[hashed_key][index]
        else:
            return "key :{0} is not found in hashed tabel".format(key)
        






