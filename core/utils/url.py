#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Config import config
"""
url地址集
"""

class xm_api:
    create_booking = config.xm + '/api/company/create_booking/'
    list = config.xm + '/api/homepage/template/industry/list/'
    list_search = config.xm + '/api/homepage/template/list/?search=&topws=&industry=&page=0'
    libtopic = config.xm + '/api/homepage/template/libtopic/'
    list_sort = config.xm + '/api/homepage/template/list/?sort=-1'
    stat = config.xm + '/api/gw/stat/'
    login = config.xm + '/api/authorize/token/'
    user_bookingstracks = config.xm + '/api/user/bookingtracks/'
    user_industry = config.xm + '/api/user/industrys/'
    user_bookings = config.xm + '/api/user/bookings/'
    user_organizations = config.xm + '/api/user/organizations/'
    user_packs = config.xm + '/api/user/packs/'
    user_modules = config.xm + '/api/user/modules/'


class cem_api:
    login = config.env + "/api/authorize/token/"
    projects = config.env + "/api/qdes/projects/"

