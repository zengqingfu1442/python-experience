class Person():
    hobby = "make money"

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def change_class_var(self):
        Person.hobby = 'make love'

    @property
    def get_weight(self):
        return self.__weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    def say_hello(self) -> str:
        return 'Hello, I am {0}, nice to meet you!'.format(self.name)

    def self_introduction(self):
        print('My name is {0}, I am {1} years old! My weight is {2} kg'.format(self.name, self._age,  self.__weight))


class Student(Person):
    def __init__(self, name: str, age: int, weight: int, grade: int, major: int) -> None:
        super(Student, self).__init__(name, age, weight)
        self.grade = grade
        self.major = major

    @property
    def self_major(self):
        return self.major


if __name__ == '__main__':
    # p = Person('david', 25, 62)
    # print(dir(p))
    # print(p.get_hobby())
    # print(p.get_weight)
    # p.self_introduction()
    # print(isinstance(p, Person))
    # print(issubclass(Student, Person))
    # s = Student('david', 25, 62, 2013, 'math')
    # print(s.__dict__)
    # print(s.name)
    # print(isinstance(s, (Student, Person)))
    p1 = Person('aaa', 25, 62)
    p2 = Person('bbb', 26, 63)
    p3 = Person('ccc', 22, 56)
    print(p1.get_hobby())
    print(p2.get_hobby())
    print(p3.get_hobby(), '\n')

    p2.hobby = 'make love'
    print(p1.get_hobby())
    print(p1.hobby)
    print(p2.get_hobby())
    print(p2.hobby)
    print(p3.hobby)
    print(p3.get_hobby(), '\n')

    p1.change_class_var()
    print(p1.get_hobby())
    print(p2.get_hobby())
    print(p3.get_hobby())
    print(p1.name, p1.hobby)
    print(p2.name, p2.hobby)
    print(p3.name, p3.hobby)
    print(p1.__dict__)

