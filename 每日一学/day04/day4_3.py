def getlist(num):
    n = 0
    a = 0
    b = 1
    while n < num:
        yield b
        a, b = b, a+b
        n += 1

if __name__ == '__main__':
    li = getlist(10)   # 返回的是一个生成器对象 方便，不额外需要存储
    print(li)
    for i in li:
        print(i,end=' ')