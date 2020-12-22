# -*- coding: utf-8 -*-
from core.utils import request
from core.utils.read_yaml import get_api
import sys


class Folders:
    def get_folders(self, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        return request.get(api, token=token)

    def put_folders(self, foldersList=None, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "foldersList": foldersList
        }
        return request.put(api, payload=payload, token=token)

    def put_move_project(self, projectID=None, folder_id=None, token=None):
        api = get_api(f'$..{sys._getframe().f_code.co_name}')
        payload = {
            "folder_id": folder_id
        }
        return request.get(api, ID=projectID, token=token)


if __name__ == '__main__':
    # s = Authorize()
    # s.post_company_token(1,2,1)
    User().get_self()
