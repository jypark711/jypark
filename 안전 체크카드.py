# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
from CashCardClass import SimpleCashCard as CashCard





class SafeCasjCard(CashCard):
    def withdraw(self, amount_won):
        print("SafeCashCard withdraw()")
        if self.check_balance() >= amount_won:
            CashCard.withdraw(self, amount_won)
        else
            print("**오류 발생**")
            print("잔고가 부족합니다")
            print("인출되지 않았습니다")
