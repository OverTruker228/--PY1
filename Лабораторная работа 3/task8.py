money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

def Econom(money_capital, salary, spend, increase, month):
    while money_capital >= spend:
        money_capital -= spend
        money_capital += salary
        spend = (1 + increase) * spend
        month = month + 1
    return month



a = Econom(money_capital, salary, spend, increase, month)
print(a)
