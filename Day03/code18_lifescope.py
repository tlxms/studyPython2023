# 라이프 스코프 - 함수의 생명주기
# 로컬변수, 전역변수
# 함수 외에서는 로컬 글로벌 이 같다.
# 함수에서만 로컬 글로벌의 구분이 생긴다.
a = 1 # a 라는 글로벌변수

def vartest(): # 여기 a는 함수용 매개변수 - Local 변수
    global a # 전역 변수 a를 함수(지역변수 = 매개변수)에 가져다 쓰겠다.
    a = a + 1
    return a

a = vartest() # 전역 변수 Global 변수
print(a)