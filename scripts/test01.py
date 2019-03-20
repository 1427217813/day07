import os
import allure
import sys

import pytest

sys.path.append(os.getcwd())
class Test01:

    @allure.step("新增")
    def test001(self):
        allure.attach("描述", "点击新增按钮")
        allure.attach("描述", "点击新增输入手机号")
        allure.attach("描述", "点击新增输入收件人")
        allure.attach("描述", "点击新增输入具体地址")
        print("1")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step("更新")
    def test002(self):
        print("2")


    def test003(self):
        print("3")
        with open("./image/faile.png", "rb")as f:
            allure.attach("失败原因：", f.read(), allure.attach_type.PNG)






























