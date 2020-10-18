import os

print(os.getcwd())
print(os.listdir('./'))
if not os.path.exists('test'):
    os.mkdir('test')
if not os.path.exists('./test1/test2'):
    os.makedirs('./test1/test2')
os.rmdir('test')
