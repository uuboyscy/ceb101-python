def createFile(name):
    try:
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except FileNotFoundError as e:
        with open(name.replace('/', '-'), 'w', encoding='utf-8') as f:
            f.write('123')
        print(e)
    except OSError:
        pass
    except:
        pass

createFile('test123123/test1')
createFile('test?test')
