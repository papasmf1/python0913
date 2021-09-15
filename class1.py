# class1.py 
#클래스를 정의
class Person:
    #생성자 메서드(초기화 담당)
    def __init__(self):
        self.name = "default name"
    #인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스(복사본 생성)
p1 = Person()
p1.print()

