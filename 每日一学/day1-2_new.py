import re


#正则表达式 r"(-?\d+\.?\d*)\s*([+\-*/])\s*(-?\d+\.?\d*)" 的解释：
#(-?\d+\.?\d*)：匹配一个可能带负号的浮点数或整数。
#\s*：匹配任意数量的空白字符。
#([+\-*/])：匹配一个运算符（加、减、乘、除）。
#(-?\d+\.?\d*)：再次匹配一个可能带负号的浮点数或整数

def caulculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return '输入有误'


if __name__ == '__main__':
    company, date, *other = ['sinow', '20241122', 'cool', 'sun']
    print(company, date, other)

while True:  # 无限循环
    operator = input('请输入想要计算的等式：')
    #进阶版 使用正则表达式
    match = re.match(r"(-?\d+\.?\d*)\s*([+\-*/])\s*(-?\d+\.?\d*)", operator)

    if match:
        front = float(match.group(1))
        operator_str = match.group(2)
        back = float(match.group(3))
        # print(eval(f'{front}{operator_str}{back}'))
        print('计算的结果为' + str(caulculate(front, back, operator_str)))
