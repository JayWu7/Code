from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__order_dict = OrderedDict()
        self.__capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.__order_dict:
            return -1
        self.__order_dict.move_to_end(key)  # 使用该key，将该item移到dict最后
        return self.__order_dict.get(key)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.__order_dict:  # 元素在字典中
            self.__order_dict[key] = value
            self.__order_dict.move_to_end(key)  # 使用了该key
        else:
            if len(self.__order_dict) == self.__capacity:
                self.__order_dict.popitem(last=False)  # 先进先出删除字典元素
            self.__order_dict[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
