
if __name__ == '__main__':
    # 定义一个空字典
    dict_none = {}
    print(dict_none)


    # 定义一个非空字典
    dict_new = {'santo': 100, 'ntong': 98}
    print(dict_new)


    # 使用使用dict()创建字典
    santo = ('santo', '100')
    ntong = ('ntong', '98')
    dict_new2 = dict([santo, ntong])
    print(dict_new2)


    # 使用zip()合并两个列表分别作为字典的key和value
    list_key = ['santo', 'ntong']
    list_value = [100, 98]
    dict_new3 = dict(zip(list_key, list_value))

    # 读取字典的value
    print(dict_new3['santo'])


    # 修改字典的value
    dict_new3['ntong'] = 100
    print(dict_new3)

    # keys()获取字典所有的key
    dict_keys = dict_new3.keys()
    print(dict_keys)

    # values()获取字典所有的value
    dict_values = dict_new3.values()
    print(dict_values)

    # 使用get()获取key值对应的value
    key = dict_new3.get('santo')
    print(key)


    # in 和 not in 判断key在字典中是否存在
    print('santo' in dict_new3)
    print('ntong111' not in dict_new3)


    # 使用items()把字典的对应的key和value组成一个元组返回一个列表
    list_new =dict_new3.items()
    print(list_new)


    # 使用copy()复制一个字典
    dict_new4 = dict_new3.copy()
    print(dict_new4)
    print(dict_new3 is not dict_new4)


    # 使用clear()清空字典所有元素
    dict_new4.clear()
    print(dict_new4)

    # pop()删除一个key对应的元素，key存在，返回对应的value，可以指定不存在时的默认返回值
    pop = dict_new3.pop('ntong')
    print(pop)
    pop1 = dict_new3.pop('santo0','none')
    print(pop1)


    # 使用update()更新字典，也就是追加元素的意思
    dict_new3 = dict_new3.update({'xie':'1000'})#里面嵌套一个字典
    print(dict_new3)

