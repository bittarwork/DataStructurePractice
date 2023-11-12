
class HashTable : 
    def __init__(self , size ) : 
        self.MAX = size
        self.arr = [None for i in range (self.MAX)]
    # hashing function by ASCI
    def hasing (self , keys) : 
        h= 0 
        for key in keys : 
            asc = ord(key)
            h += asc 
        return h % self.MAX
    # add to the hash tabel 
    def __setitem__(self , key , value) : 
        hasehdKey = self.hasing(key)
        self.arr[hasehdKey] = value
    # get a vallue by key 
    def __getitem__ (self , key ) : 
        hashedKey = self.hasing(key)
        if (self.arr[hashedKey]) : 
            return self.arr[hashedKey]
        else : 
            return "key is wrong"
    # delet item by key
    def __delitem__ (self , key) : 
        hashedKey = self.hasing(key)
        self.arr[hashedKey] = None

t = HashTable(100)
t["osama bittar"] = 140
t["osama bitta"] = 150
t["osama bitr"] = 160
t["osamatar"] = 170
t["o bittar"] = 180

