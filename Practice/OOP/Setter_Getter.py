class person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self,name):
        if isinstance(name , str
