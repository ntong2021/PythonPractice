
def jiecheng (n):
    if n == 1:
        return 1
    else:
        return n * jiecheng(n-1)

# 自建迭代器
class myclss:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        return self.index


if __name__ == '__main__':
    # print(jiecheng(10))
    list_num = [1,2,3]
    it = iter(list_num) # 迭代器
    while True:
        try:
            print(next(it))
        except StopIteration:  ###
            break

    css = myclss()
    myitem = iter(css)
    i = 0
    while i < 10:
        try:
            print(next(myitem))
            i += 1
        except StopIteration:  ###
            break


