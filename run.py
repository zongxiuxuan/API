# -*- coding: utf-8 -*-
import pytest
"""
# 执行用例
pytest -q -s tests/test_user/ --clean-alluredir --alluredir=report/api_report/
# 生成报告
allure serve report/api_report/
"""
if __name__ == '__main__':
    pytest.main()
