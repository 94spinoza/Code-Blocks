##############################################################################################################
# 작성 날짜 : 2021년 5월 8일
# 작성자 : 94spinoza
##############################################################################################################
# 목차 :
#   1. URL 페이지 소스 가져오기
#   2. HTML 파일 읽어오기
#   3. 페이지 소스를 Tag로 접근하기
#       3-1. 최초 Tag 1개 접근하기
#           - soup.Tag
#           - soup.find('Tag')
#           - soup.find(attrs = {'Tag' : 'attribute'})
#           - soup.find('Tag1', attrs = {'Tag2' : 'attribute'})
#       3-2. 관련 Tag 모두 접근하기
#           - soup.find_all('Tag')
#           - soup.find_all(attrs = {'Tag' : 'attribute'})
#           - soup.find_all('Tag1', attrs = {'Tag2' : 'attribute'})
#       3-3. 반복문 활용하기
#   4. 데이터 저장하기
##############################################################################################################

# 1. URL 페이지 소스 가져오기

import requests

url = "https://www.naver.com"   # 쓰고자 하는 사이트 주소로 변경
r = requests.get(url)   # 페이지 소스를 가져옴
r.text  # 페이지 소스 중 text 정보가 있는 것만 추출

############################################################

# 2. HTML 파일 읽어오기

file = open('불러올 파일.html', 'r', encoding='utf-8')   # HTML 파일을 'r'(읽기) 모드로 불러옴(encoding으로 한글도 읽음)
html = file.read()  # html 변수에다가 파일 내용을 읽어옴

############################################################

# 3. 페이지 소스를 Tag로 접근하기

from bs4 import BeautifulSoup   # Tag를 통해 접근가능하게 자료를 바꿔주는 패키지

soup = BeautifulSoup(r.text, 'lxml')    # 'lxml'은 Parser의 종류

##############################

# 3-1. 최초 Tag 1개 접근하기

info = soup.Tag
info = soup.find('Tag')
info = soup.find(attrs = {'Tag' : 'attribute'}) # 같은 이름의 Tag가 여러개 있을 때, attribute를 통해 특정
info = soup.find('Tag1', attrs = {'Tag2' : 'attribute'}) # 위의 방식보다 더 세밀하게 특정

##############################

# 3-2. 관련 Tag 모두 접근하기

info = soup.find_all('Tag') # Tag가 같은 정보를 모두 찾음
info = soup.find_all(attrs = {'Tag' : 'attribute'}) # attribute를 통해 보다 정확하게 특정
info = soup.find_all('Tag1', attrs = {'Tag2' : 'attribute'}) # 위의 방식보다 더 세밀하게 특정

info_specific = info[number]    # 불러온 Tag 집합 중 number로 순서를 특정해서 1개만 고름
info_specific.text  # 찾아서 특정한 Tag안의 text 정보 추출

##############################

# 3-3. 반복문 활용하기

info = soup.find_all('Tag')

for i in info:  # info에 담긴 Tag 리스트들을 하나하나 접근함
    data = i.get('a')   # 하나씩 접근한 항목 중 Tag 'a'를 가져옴

############################################################

# 4. 데이터 저장하기

with open('파일명.txt', 'w', encoding='utf-8') as f:   # 파일 확장자는 .txt말고 .csv 등이 가능하고 'w'는 쓰기 모드를 뜻함
    f.write("아무거나 쓰고 싶은 내용")    # 위에서 '파일명.txt'를 f라는 변수명으로 열었으니 f.write를 통해 쓰기 가능

    info = soup.find_all('Tag') # 앞의 내용을 활용하여 쓰기도 가능함
    for i in info:
        data = i.get('a')
        f.write(data)   # Tag의 내용 중 특정한 정보를 파일에 씀

f.close()   # 쓰기를 끝마치고 파일을 꼭 닫아줘야함

##############################################################################################################