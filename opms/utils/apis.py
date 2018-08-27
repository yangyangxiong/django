# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project:     mota
   IDE Name:    PyCharm
   File Name:   apis
   Email:       hupe_jt@163.com
   Author :     玖天
   Date:        2018/4/27
   Description :
-------------------------------------------------
   Change Activity: 2018/4/27:
-------------------------------------------------
"""
import json

from django.http import JsonResponse
from django.views.generic import View


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        #
        return context


class APIView(View, JSONResponseMixin):
    """
    除模型增删改查外，API视图的基类
    :param status: 处理的状态
    :param msg: 返回的处理信息
    :param context: json
    """
    status = False
    msg = ''

    def json_response(self, context=''):
        response = {
            'status': self.status,
            'msg': self.msg,
            'result': context
        }
        return self.render_to_json_response(response)
