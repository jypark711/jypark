# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
balance_won = 0

def deposit(amount_won):
    #deposit 함수 안의 balance_won 이
    #전역변수임을 표시
    global blance_won

    #입금 하면 잔고가 증가한다
    balance_won += amount_won

def withdraw(amount_won):
    #deposit 함수 안의 balance_won 이
    #전역변수임을 표시
    global blance_won
    #출금 하면 잔고가 증가한다
    balance_won += (-amount_won)

def check_balance():
    #통장 잔고를 반환한다
    # reader funchtion
    return balance_won

