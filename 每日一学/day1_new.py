import random

# day1 输出10个随机数
if __name__ == '__main__':
    print('Hello World!')
    print('====================================================')
    i = 0
    rand_list = []
    while i < 10:
        rand_num = random.randint(0, 499)
        if rand_num not in rand_list:
            rand_list.append(rand_num)
            i += 1
    print("random digital:")
    print(rand_list)