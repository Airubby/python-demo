#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Airubby
@file: xxoo.py
@time: 2018/05/05
"""

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def houyafan(a1,a2):
    return a1 + a2