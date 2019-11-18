from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):

    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


class SocketStream(IStream):

    def read(self, maxbytes=-1):
        print(maxbytes)

    def write(self, data):
        print(data)

    @classmethod
    def method1(cls):
        return cls()

    @staticmethod
    def method2():
        print("nothinf")


if __name__ == "__main__":
    a = SocketStream()
