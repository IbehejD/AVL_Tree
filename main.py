
class Vertex:

    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None
        self.__height = 1

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height


if __name__ == "__main__":
    pass
