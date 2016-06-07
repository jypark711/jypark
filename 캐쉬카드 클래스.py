# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
class SimpleCashCard
    def __init__(self):
        print "simpleCashCard __init__()"
        self.balance_won = 0

    def deposit(self, amount_won):
        """
        입금
        :param amount_won:
        :return:
        """
        print("SimpleCashCard deposit()")
        self.balance_won += amount_won

    def withdra(self, amount_won):
        """
        출금
        :param amount_won:
        :return:
        """
        print ("SimpleCashCard withdraw()")
        self.balance_won += (-amount_won)

    def check_balance(self):
        """
        잔고조회
        :return:
        """
        print ("SimpleCashCard check_balance()")
        return self.balance_won

    if "__main__"==__nama__:
        from CashCard_user import  chk_bal

        myCard = SimpleCashCard()

        myCard.deposit(10,000)
        chk_bal("입금 후 잔고 확인", myCard)
        myCard.withdraw(1000)
        chk_bal("출금 후 잔고 확인" myCard)

        mySisterCard = SimpleCashCard()
        chk_bal("잔액")