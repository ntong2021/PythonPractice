import os

if __name__ == '__main__':
    name = os.name
    print(name)

    #绝对路径
    abs_path = os.path.abspath('.')
    print(abs_path)

    #当前目录下所有文件
    ls = os.listdir('.')
    print(ls)

    print(os.getlogin())