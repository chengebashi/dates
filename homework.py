# def move(n, a, b, c):  # n为圆盘数，a代表初始位圆柱，b代表过渡位圆柱，c代表目标位圆柱
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n - 1, a, c, b)# 将初始位的n-1个圆盘移动到过渡位，此时初始位为a，上一级函数的过渡位b即为本级的目标位，上级的目标位c为本级的过渡位
#         print(a, '-->', c)
#
#         move(n - 1, b, a, c)# 将过渡位的n-1个圆盘移动到目标位，此时初始位为b，上一级函数的目标位c即为本级的目标位，上级的初始位a为本级的过渡位
# move(3, 'A', 'B', 'C')
#
# import qrcode
#
# img = qrcode.make(input('请输入二维码的内容：')).show()
# img.save("qr.jpg")
#
# def outer(x):
#     y = 3
#     def inner():
#         nonlocal x, y
#         y += 1
#         x += 2
#         print(x, y)
#     return inner
#
# f = outer(4)
# f()
# f()
# class Person:
#     def set_name(self):
#         self.name = '123'
#
#     def get_name(self):
#         return self.name
#
#     def greet(self):
#         print("Hello,word! I'm{}.".format(self.name))
#
# p = Person()
# p.set_name()
# p.greet()

# class Class:
#     def method(self):
#         print('I have a self')
#
# def function():
#     print('I dont ...')
# instance = Class
# instance.method('123')
# instance.method = function
# instance.method()
# class Bird:
#     song = 'Squaawk'
#     def sing(self):
#         print(self.song)
#
# p = Bird()
# p.sing()



class Person:
    cnt = 0
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age
        Person.cnt += 1

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def show(self):
        print('{}, {}, {}'.format(self.__name, self.__sex, self.__age))

class Chinese(Person):
    def __init__(self, name, sex, age, gongfu):
        super().__init__(name, sex, age)
        self.__gongfu = gongfu

    def set_gongfu(self, gongfu):
        self.__gongfu = gongfu

    def show(self):
        super().show()
        print(self.__gongfu)

if __name__ == '__main__':
    p1 = Person("tom", "mal", "23")
    p1.show()
    p1.set_name("jim")
    p1.show()
    print(Person.cnt)

    c1 = Chinese("张三", "男", "25", "太极剑")
    c1.show()
    c1.set_name("张三丰")
    c1.set_gongfu("乾坤大挪移")
    c1.show()
    print(Chinese.cnt)






