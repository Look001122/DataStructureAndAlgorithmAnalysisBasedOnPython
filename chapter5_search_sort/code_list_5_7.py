# @Time:2025/7/27 15:31
# @Author:卢科
# @Description:代码清单5-7 put函数
from code_list_5_6 import HashTable

def put(self,key,data):
    hashvalue=self.hashfunction(key,len(self.slots))

    if self.slots[hashvalue]==None:
        self.slots[hashvalue]=key
        self.data[hashvalue]=data
    else:
        if self.slots[hashvalue]==key:
            self.data[hashvalue]=data  #替换
        else:
            nextslot=self.rehash(hashvalue,len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot=self.rehash(nextslot,len(self.slots))

            if self.slots[nextslot] == None:
                self.slots[nextslot]=key
                self.data[hashvalue] = data
            else:
                self.data[nextslot] = data  # 替换

def hashfunction(self,key,size):
    return key%size

def rehash(self,oldhash,size):
    return (oldhash+1)%size


