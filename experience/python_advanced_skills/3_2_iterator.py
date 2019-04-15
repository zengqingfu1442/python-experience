from collections import Iterator, Iterable
import requests


# 通过实现迭代器的__next__抽象方法来构造一个迭代器, 进而实现一个可迭代对象
# 迭代器一定是可迭代对象，但是可迭代对象不一定是迭代器。
# 可迭代对象调用__iter__方法之后变成了迭代器对象
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    @staticmethod
    def get_weather(city):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '{0}: {1}, {2}'.format(city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

    # def __iter__(self):
    #     return WeatherIterator(self.cities)


# class WeatherIterable(Iterable):
#     def __init__(self, cities):
#         self.cities = cities
#
#     def __iter__(self):
#         return WeatherIterator(self.cities)


if __name__ == '__main__':
    cities = ['北京', '上海', '广州', '深圳', '武汉', '长沙', '长春', '哈尔滨', '乌鲁木齐', '拉萨', '成都']
    for x in WeatherIterator(cities):
        print(x)
    print(WeatherIterator.__dict__)
    w_iterator = WeatherIterator(cities)
    w_iterator.__iter__()
