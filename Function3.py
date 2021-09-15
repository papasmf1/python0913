# Function3.py 
#정의되지 않은 인자 딕셔너리로 받기
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

#호출
print( userURIBuilder("creud.com", "80", id="kim",     
    passwd="1234") )
print( userURIBuilder("creud.com", "80", id="kim", 
    passwd="1234", name="mike", age="30") )

#람다함수(간결하게 함수 정의)
g = lambda x,y:x*y
print( g(3,4) )
print( (lambda x:x*x)(3) )
print( globals() )
print("---dir()---")
print( dir() )

#함수 내부에서 함수를 바로 호출
lst = [10, 25, 30]
#함수의 인자로 함수를 바로 정의(람다 함수 사용)
itemL = filter(lambda x:x>20, lst)
for i in itemL:
    print(i)




