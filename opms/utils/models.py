# coding:utf-8
from django.db import models

class ModelToDict(models.Model):

    def convert_to_dict(self):
        """
        模型转字典
        :return: 
        """
        obj_dict = {}
        obj_dict.update(self.__dict__)
        obj_dict.pop("_state", None)
        return obj_dict

    class Meta:
        """声明抽象类"""
        abstract = True


class QuerySetUtil():
    def __init__(self, description):
        """
        :param description: cursor.description
        """
        self.fields = list()
        for item in description:
            self.fields.append(item[0])


    def parse_obj(self, query_one):
        """
        传入一条查询结果，返回k-v字典
        :param query_one: 
        :return: 
        """
        obj = dict()
        for i, field in enumerate(self.fields):
            obj[field] = query_one[i]
        return obj

    def parse_objs(self, query_all):
        """
        传入查询集，返回字典对象列表
        :param query_all: 
        :return: 
        """
        objs = list()
        for item in query_all:
            obj = self.parse_obj(item)
            objs.append(obj)

        return objs

