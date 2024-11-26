

if __name__ == '__main__':
    path = 'test.txt'
    f = open(path)

    content = f.read()
    print(content)
    f.close()

    # with 可自动关闭文件
    with open(path) as f:
        content = f.read()
        print(content)

    with open(path) as f:
        for line in f:
            print(line, end='')

    #写入文件
    with open('p.md',"w") as f:
        f.write('hello ')
        f.write('world')