# [1,2,4][599]
# 1/0
def zero_division(a , b):
    if b == 0:
        return 'ZeroDivisionError'

    [1, 2, 4][599]
    return a / b


def zero_division2(a , b):
    print('--' * 50)
    try:
        # raise ArithmeticError

        result = a / b
        # [1, 2, 4][599]

    #


    except ZeroDivisionError as e:
        print('ZeroDivisionError')
        print(e)
        return  a

    except IndexError as e:
        print('IndexError')
        print(e)

    except TypeError as e:
        print('TypeError')
        return int(a) / int(b)

    except Exception as e:
        print('Smth was wrong' )
        print(e)

    else:
        print('success result ')
        return result

    finally:
        print('block finally')
        print(f'first item: {a} second item: {b}')


# print(zero_division(1, 0))
# print(zero_division(1, 2))
print(zero_division2(1, 0))
print(zero_division2(1, 2))

print(zero_division2('1', 2))

# print('1' / 2)




def db_connect():
    print('db connect')
    return True

def db_disconnect():
    print('db disconnect')

def sql_query():
    print('sql query')
    raise  TypeError

def db_work():
    # try:
    #     db_connect()
    #     sql_query()
    #     db_disconnect()
    #
    # except TypeError as e:
    #     print('TypeError')
    #     db_disconnect()
    #
    # except Exception as e:
    #     print('Smth was wrong')
    #     db_disconnect()

    try:
        db_connect_ = None
        db_connect_ = db_connect()
        sql_query()

    except TypeError as e:
        print('TypeError')

    except Exception as e:
        print('Smth was wrong')

    finally:
        if db_connect_:
            db_disconnect()



