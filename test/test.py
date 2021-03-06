"""
本文件用于执行测试功能。
形如“RegisterTest”的每一个类表示一组针对接口的测试数据。
填写时只要实现__init__()皆可。

其中需要实现expected_io和reshape（可选）

self.expected_io包含各种情况下每一组输入对应的相对输出,应当为zip。
对于输入对应的输出中输出不确定的内容返回值设置为空字符串，并且需要实现下面的函数。
self.reshape是一个函数，在包含不确定返回值的情况下将不确定的内容转换为空字符串。
"""

from sys import argv

from testClasses import *

TestUnit.domain = "http://localhost:8080"
TestUnit.repeat = 5

# TestUnit.domain = "http://202.119.245.31:80"
TestUnit.domain = argv[1]
TestUnit.repeat = int(argv[2])

if __name__ == "__main__":
    print(f"开始测试,重复测试次数：{TestUnit.repeat}")
    # InfoTest().test()
    passedTest = all(testcls().test() for testcls in TestUnit.__subclasses__())
    print("测试结束")
    if passedTest:
        print("所有测试都成功通过！")
    else:
        print("未通过测试")
