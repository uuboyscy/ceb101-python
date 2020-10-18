def add(x, y):
    try:
        s = x + y
    except TypeError as e:
        print(e)
        try:
            s = int(x) + int(y)
        except ValueError:
            return 0
        except:
            pass
    except Exception as e:
        print(e)
        pass
    else:
        print('Successed!')
    finally:
        print('Finally')
    return s

print(add(1, '2'))
print('=============')
print(add(1, 'a'))
print('=============')
print(add(2,4))