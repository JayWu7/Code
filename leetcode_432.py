
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__datas = [[]]  # 使用桶排序，处理max和min
        self.__dict = {}  # 储存每个key值，以及key值对应的出现次数

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        self.__datas.append([])  # 添加桶
        if key in self.__dict:
            self.__datas[self.__dict[key]].remove(key)  # 在当前key在的桶子删除key
            self.__dict[key] = self.__dict[key] + 1
            self.__datas[self.__dict[key]].append(key)
        else:  #key不在dict里
            self.__dict[key] = 1
            self.__datas[1].append(key)  #序号为1的桶里添加key


    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.__dict:
            if self.__dict[key] == 1:
                self.__datas[1].remove(key)   #序号为1的桶里删除key
                self.__dict.pop(key)
            else:
                self.__datas[self.__dict[key]].remove(key)  # 在当前key在的桶子删除key
                self.__dict[key] = self.__dict[key] - 1
                self.__datas[self.__dict[key]].append(key)

            self.__datas.pop()  #删除最后的桶子（因为dict里面数不够，用不到）


    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        index = len(self.__datas) - 1
        while index:
            if self.__datas[index]:
                return self.__datas[index][0]  #返回当前桶里第一个元素
            index = index - 1
        return ''

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        for data in self.__datas[1:]:
            if data:
                return data[0]
        return ''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
