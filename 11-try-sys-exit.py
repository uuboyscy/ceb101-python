import sys

try:
    print(sys.exit("123123"))
except Exception:
    print('error')
except SystemExit:
    print("System")