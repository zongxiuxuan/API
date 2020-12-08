#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import allure
from core.bestcem import user


@allure.feature('authorize')
@allure.severity(allure.severity_level.BLOCKER)
class TestAuthorize:
	apis = user.Authorize()
	users = user.User()
	@allure.title('company login and get user info')
	@pytest.mark.parametrize(('org_code', 'username', 'password'), [
		('bvt', 'superadmin', 'zxx12345'),
		('bvt', 'zongxiuxuan001@163.com', '1234567890'),
		('bvt', '17839236545', '1234567890')
	])
	def test_company_login(self, org_code, username, password):
		with allure.step('通过公司域名登陆'):
			result1 = self.apis.post_company_token(org_code, username, password).json()
			assert result1['code'] == 0
			token = f"Bearer {result1['data']['token']}"
		with allure.step('获取公司信息'):
			result2 = self.users.get_company(token).json()
			assert result2['code'] == 0
			assert result2['data']['code'] == org_code
		with allure.step('获取个人信息'):
			result3 = self.users.get_self(token).json()
			assert result3['code'] == 0
			assert result3['data']['userName'] == 'superadmin'



if __name__ == '__main__':
	pass
	# 执行用例
	#pytest -q -s tests/test_user/ --clean-alluredir --alluredir=report/report_001/
	# 生成报告
	#  allure serve report/report_001/