import sys
sys.path.append("/Users/uuboy.scy/PycharmProjects/ceb101-OO/testTool")
# from testTool import testA
import testA

class TestB(testA.TestA):
    def input1(self, x):
        return "||" + x + "||"

    def __input3(self, x):
        return "PUBLIC_" + x + "_PUBLIC"

if __name__ == "__main__":
    tmpStr = "123"
    a = TestB(tmpStr)
    a.run()
    for i in sys.path:
        print(i)