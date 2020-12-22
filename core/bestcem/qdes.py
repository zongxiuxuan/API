# -*- coding: utf-8 -*-
from core.utils import request
from core.utils.read_yaml import get_api
import sys


class Folders:
    def post_creat_project(self, title, folder_id, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "title": title, "folder_id": folder_id
        }
        return request.post(api, payload=payload, token=token)

    def delete_project(self, pid=None, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "pid": pid
        }
        return request.delete(api, payload=payload, token=token)

    def put_project(self, status: int, pid: str, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "pid": pid, "status": status
        }
        return request.put(api, payload=payload, token=token)

    def post_lib_creat_project(self, folder_id='', title='', token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "title": title, "folder_id": folder_id
        }
        return request.post(api, payload=payload, token=token)

    # todo: where is need to do
    def post_copy_project(self, foldersList=None, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "foldersList": foldersList
        }
        return request.put(api, payload=payload, token=token)

    def post_import_project(self, projectID=None, folder_id=None, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "folder_id": folder_id
        }
        return request.get(api, ID=projectID, token=token)

    def put_project_title(self, title='', token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "title": title
        }
        return request.put(api, payload=payload, token=token)

    def get_project_list(self, foldersList=None, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "foldersList": foldersList
        }
        return request.put(api, payload=payload, token=token)

    def post_project_release(self, projectID=None, folder_id=None, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "folder_id": folder_id
        }
        return request.get(api, ID=projectID, token=token)



