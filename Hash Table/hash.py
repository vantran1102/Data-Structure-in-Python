class HashTable:
    def __init__(self,size = 7): #create a hashmap with index from 0-6
        self.data_map = [None] * size
    def hash(self, key):
        hash_map = 0
        for letter in key:
            #ord - take single character convert to Unicode code point as an integer
            hash_map = (hash_map + ord(letter)*23) % len(self.data_map)
        return hash_map
    
    def print_hash(self):
        for i, value in enumerate(self.data_map):
            print(i, ": ", value)
    
    def set(self, key, value):
        index = self.hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get(self, key):
        index = self.hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def key(self):
        all_key = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_key.append(self.data_map[i][j][0])
        return all_key
    
def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    
    for j in list2:
        if j in my_dict:
            return True
    return False

list1 = [1,2,3]
list2 = [3,2,5]
print(item_in_common(list1,list2))

