
# 素数判断 day3

if __name__ == '__main__':
    while True:
        input_content = input("Enter a number: ")
        if input_content == "exit":
            break
        num = int(input_content)
        if num <= 2:
            print(num, "is less than 2.")
        else:
            center_num = num // 2
            start = 2
            flag = True
            while start <= center_num:
                if num % start == 0:
                    print("no")
                    flag = False
                    break
                start = start + 1
            if flag:
                print("yes")