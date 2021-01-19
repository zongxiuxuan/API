#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import read_yaml
import os
from utils import getDir

path = '/demo/organization.yaml'


def gen_api(file=path):
	data = read_yaml.read_yaml(file)
	class_name = [i for i in data.keys()][0]
	module_name = class_name.lower()
	file_path = f'{getDir.proDir}/core/bestcem/{module_name}.py'
	print(file_path)
	if os.path.exists(file_path):
		os.remove(file_path)
	print(os.path.exists(file_path))
	with open(f'{getDir.proDir}/core/bestcem/{module_name}.py', 'a') as f:
		begin = \
f"""# -*- coding: utf-8 -*-
from core.utils import request

class {class_name}:
"""
		f.write(begin)
		for i in data[class_name]:
			name = i.get('name')
			path = i.get('path')
			method = i.get('method')
			payload = i.get('payload')
			params = i.get('params')
			file = i.get('file')
			ID = i.get('ID')
			token = i.get('token')
			if method == 'post':
				module = f"""
	def {name}(self, url='{path}', payload={payload}, token={token}, params={params}, file={file}, ID={ID}):
		return request.post(url=url, payload=payload, token=token, params=params, file=file, ID=ID)

"""
				f.write(module)
			elif method == 'get':
				module = f"""
	def {name}(self, url='{path}',token={token}, params={params}, ID={ID}):
		return request.get(url=url, token=token, params=params, ID=ID)

"""
				f.write(module)
			elif method == 'put':
				module = f"""
	def {name}(self, url='{path}',payload={payload}, params={params}, ID={ID}):
		return request.put(url=url, token=token, payload=payload, ID=ID)

"""
				f.write(module)
			elif method == 'delete':
				module = f"""
	def {name}(self, url='{path}',token={token}, payload={payload}, ID={ID}):
		return request.delete(url=url, token=token, payload=payload, ID=ID)

"""
				f.write(module)

if __name__ == '__main__':
	gen_api()
