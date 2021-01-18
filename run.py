# -*- coding: utf-8 -*-
import pytest
import os
import time

"""
# 执行用例
pytest -q -s tests/test_user/ --clean-alluredir --alluredir=report/report_json/
# 生成报告
allure serve report/report_json/
"""
if __name__ == '__main__':
	pytest.main()
	os.system("allure generate report/api_report_json/ -o report/report_result --clean")
	time.sleep(5)
	os.system("allure open -h 127.0.0.1 -p 8883 report/report_result/")

