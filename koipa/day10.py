
#a = int(input("a :"))
#b = int(input("b :"))
#try:
#	a/b
#except:
#	print("unknown Error")
#
#print(a/b)
from urllib	import request as req 
import datetime as d 
import bs4

r =	req.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108") 

soup = bs4.BeautifulSoup(r, "html.parser") 
now	= d.datetime.now()


print("=" *	30)
print("* {}년 {}월 {}일 날씨 정보 * ".format(now.year, now.month, now.day))
print("=" * 30) 
print("  도시     날 씨    온  도  ") 
print("=" * 30) 

for	i in soup.select("location"):				
    name = i.select_one("city").string				
    wf   = i.select_one("wf").string				
    tmn  = i.select_one("tmn").string				
    tmx	 = i.select_one("tmx").string								

    print("{:>4s} {:>7s} {}도 ~ {}도".format(name, wf, tmn, tmx))

print("=" * 30)

