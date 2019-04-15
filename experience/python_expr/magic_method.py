class Programmer():
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be an integer')

    def __eq__(self, other):
        if isinstance(other, Programmer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The compared object must be Programmer')

    def __add__(self, other):
        if isinstance(other, Programmer):
            return self.age + other.age
        else:
            raise Exception('The added object must be Programmer')

    def __getattribute__(self, name):
        # return getattr(self, name)   wrong
        # return self.__dict__[name]   wrong
        return super(Programmer, self).__getattribute__(name)

    def __getattr__(self, name):
        # return getattr(self, name)
        return self.__dict__[name]

    def __setattr__(self, name, value):
        # setattr(self, name, value)   wrong
        self.__dict__[name] = value


if __name__ == '__main__':
    p1 = Programmer('david', 25)
    p2 = Programmer('Andy', 45)
    print(p1 == p2)
    print(p1 + p2)
