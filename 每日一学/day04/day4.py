
#捕捉异常
if __name__ == '__main__':
    try:
        result = 8/0
        print(result)
    except Exception as e:
        print(e)

    try:
        result = 8/0
        print(result)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    finally:
        print('good')
