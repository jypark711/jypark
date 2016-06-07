# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-

#현금 카드 모듈을 불러들임
import  CashCard as CashCard_module

def chk_bal(message, account):
    """

    :param message:
    :param account:
    :return:
    """
    print(("%s : %d")% (message, accont,check_balance()))

# 아래의 내용은 이 .py 파일이 import 될 땨는 실행되지 않음
if '__main__' ==__name__:
    #현금 카드 모듈의 잔액 확인
    chk_bal("CashCard_module 잔액확인", CashCard_module)
    #현금 카드에 10,000원 입금
    print("10,000원 입금")

    #CashCard py. 모듈 안의 check_balcne() 함수를 호출
    # CashCard.py 모듈 안의 balance_won 값을 반환
    chk_bal("입금 후 잔고 확인", CashCard_module)

    #여러 장의 카드를 만들 수 있는지 알아보자
    # 두번째 카드를 만든다
    mySisterCard =  SimpleCashCard()
    chk_bal("잔액확인 myCard", myCard)
    chk_bal("잔액확인 mySisterCard", mySisterCard)

    print('my card : %s' % myCard)
    print('mySisterCard : %s' % mySisterCard)

