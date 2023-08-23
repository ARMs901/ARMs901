# coding: utf-8
# 写一个理财计算器，实现将每日/月/年的利息进行复投进行计算

money = float(input('请输入您打算用来投资的本金:PV= '))
year = int(input('请输入投资期限(单位：年):N= '))
rate = float(input('请输入投资年化收益率:I= '))
mm = int(input('''0.每日 1.每月 3.每3月 6.每6月 12.每年 请选择利息复投方式: '''))


def day_return(money, year, rate=0.06):
    '''方案：每日利息加入本金复投'''
    for y in range(year):
        for day in range(365):
            money = money * rate / 365 + money
        print('第%d年结束时，本利合计：%.2f' % (y + 1, money))


def month_return(money, year, mm, rate=0.06):
    '''方案：每月利息加入本金复投'''
    for y in range(year):
        cs = 12 // mm
        for month in range(cs):
            money = money * rate / cs + money
        print('第%d年结束时，本利合计：%.2f' % (y + 1, money))


def year_return(money, year, rate=0.06):
    '''方案：每年利息加入本金复投'''
    for y in range(year):
        money = money * rate + money
        print('第%d年结束时，本利合计：%.2f' % (y + 1, money))


if mm == 0:
    day_return(money, year, rate)
elif mm in (1, 2, 3, 4, 6):
    month_return(money, year, mm, rate)
elif mm == 12:
    year_return(money, year, rate)
else:
    print('mm 输入有误！')

