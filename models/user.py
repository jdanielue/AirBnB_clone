#!/usr/bin/python3
""" Class User"""

import uuid
import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """Class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
