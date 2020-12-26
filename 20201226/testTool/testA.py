class TestA:
    def __init__(self, x):
        self.x = x

    def input1(self, x):
        return "-" + x + "-"

    def input2(self, x):
        return "+" + x + "+"

    def __input3(self, x):
        return "PRIVATE_" + x + "_PRIVATE"

    def run(self):
        output1 = self.input1(self.x)
        output2 = self.input2(output1)
        print(output2)
        output3 = self.__input3(output2)
        print(output3)


if __name__ == "__main__":
    tmpStr = "123"
    a = TestA(tmpStr)
    # print(a.x)
    a.run()