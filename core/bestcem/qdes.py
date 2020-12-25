# -*- coding: utf-8 -*-
from core.utils import request
from core.utils.read_yaml import get_api
import sys


class Qdes:
    def post_creat_project(self, title, folder_id, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "title": title, "folder_id": folder_id
        }
        return request.post(api, payload=payload, token=token)

    def delete_project(self, project_id=None, token=None):
        """
        :param pid: project_id
        :param token:
        :return:
        """
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "pid": project_id
        }
        return request.delete(api, payload=payload, token=token)

    def put_project(self, status: int, project_id: str, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "pid": project_id, "status": status
        }
        return request.put(api, payload=payload, token=token)

    # 通过模板创建项目
    def post_lib_creat_project(self, lib_id, folder_id='', title='', token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "title": title, "folder_id": folder_id
        }
        return request.post(api, payload=payload, ID=lib_id, token=token)

    # 复制项目
    def post_copy_project(self, project_id, title=None, folder_id=None, token=None):
        """
        :param project_id: 复制项目的项目ID
        :param title: 创建项目的标题
        :param folder_id: 创建项目所属的问价夹ID
        :param token:
        :return:
        """
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "title": title,
            "folder_id": folder_id
        }
        return request.post(api, payload=payload, ID=project_id, token=token)

    # 移动项目
    def put_move_project(self, projectID=None, folder_id=None, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "folder_id": folder_id
        }
        return request.put(api, ID=projectID, payload=payload, token=token)

    # 上传excel项目
    def post_import_project(self, filepath=None, type='excel', token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        params = {
            "type": type
        }
        return request.post(api, params=params, file=filepath, token=token)

    # excel上传项目确定保存生成项目
    def post_import_project_qstruct(self, sid, folder_id=None, title=None, token=None):
        """
        :param sid: excel生成文件的sid
        :param folder_id:
        :param title:
        :param token:
        :return:
        """
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "folder_id": folder_id,
            "title": title
        }
        return request.post(api, payload=payload, ID=sid, token=token)

    def put_project_title(self, project_id, title='', token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "title": title
        }
        return request.put(api, ID=project_id, payload=payload, token=token)

    def get_project_list(self, title=None, status=None, folder_id=None, page=1, rowsPerPage=10, token=None):
        """
        :param title: 项目标题，模糊搜索
        :param status: 项目状态：0，1，2
        :param folder_id: 所属文件夹
        :param page: 第几页
        :param rowsPerPage: 每页条数
        :param token:
        :return:
        """
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        params = {
            "title": title,
            "status": status,
            "folder_id": folder_id,
            "page": page,
            "rowsPerPage": rowsPerPage
        }
        return request.get(api, params=params, token=token)

    def post_project_release(self, project_id, force=False, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "force": force
        }
        return request.post(api, ID=project_id, payload=payload, token=token)
