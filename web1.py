# web1.py 
from bs4 import BeautifulSoup

#웹페이지를 로딩(유니코드) 
#메소드를 연속으로 호출(메서드 체인)
#페이지는 문자열 변수
page = open("c:\\work\\test01.html", "rt",
    encoding="utf-8").read() 
#검색을 잘 하는 스프객체 생성(html태그 파싱)
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )
#<p>태그 몽땅 가져와~~ ==> 리스트에 담아서 
#print( soup.find_all("p") )
#<a>태그 몽땅
print( soup.find_all("a") )


