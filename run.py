# -*- coding: utf-8 -*-
import pytest
"""
# 执行用例
pytest -q -s tests/test_user/ --clean-alluredir --alluredir=report/report_001/
# 生成报告
allure serve report/report_001/
"""
if __name__ == '__main__':
    pytest.main()