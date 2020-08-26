# -*- coding: utf-8 -*-
from flask import Blueprint

'''
Code for creating Blueprint
'''

# Tham số đầu: 'errors': tên của Blueprint
# Tham số 2: Tên module cơ sở, thường đc đặt là: '__name__'
bp = Blueprint('errors', __name__)

from app.errors import handlers
