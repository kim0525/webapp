#여기에 숫자를 넣으면 어떻게 되는지 알려주는 함수
def ifpung(inp):
    if inp == '1':
        print("펑하고 터졌다")

def idpw_ck(userid, pwd):
    if userid == 'aaa' and pwd =='1234':
        return "로그인 성공. <br>{}<br>님 반갑습니다.".format(userid) 
    else:
        return"틀림"
