import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

url = 'https://music.bugs.co.kr/chart'
response = request.get(url)
soup=bs(response.text, 'html.parser')
rank = 1

results=soup.findAll('p','title')

file = open('practice1.txt','a')

print(datetime.today(),'의 벅스 실시간 차트 순위입니다.\n')

for result in results:
    file.write(str(rank)+'위:'+result.get_text()+'\n')
    print(rank,'위: ',result.get_text(), '\n')
    rank+=1

#제 vscode가 이상한건지 모든 모듈이 import되지 않습니다 ㅠ0ㅠ