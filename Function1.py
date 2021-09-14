# Function1.py 
#리턴을 하지 않는 경우
def setValue(newValue):
    #함수 내부에서 초기화(지역변수)
    x = newValue
    print("함수 내부:", x)

#함수 호출
result = setValue(5)
print(result)

#리턴을 하는 경우(Tuple형식)
def swap(x,y):
    return y,x 

#호출
result = swap(5,6)
print(result[0], result[1])

