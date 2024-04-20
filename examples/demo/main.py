#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from typing import TypeVar, Generic
from fastapi import FastAPI, Depends
from demo.db import create_tables, get_db, db_factory
from demo.core.models import Student
from sqlalchemy.orm import Session

import demo.rest as rest
import demo.core.models as models

from fastapitool import CreateModelResponse, SimpleRestAPI, ListModelResponse, RestCreateModelResponse, RestListModelResponse, \
    RestGetModelResponse, RestDeleteModelResponse, RestUpdateModelResponse, RestPatchModelResponse

from demo.rest.student_rest_api import StudentRestAPI

create_tables()
app = FastAPI() # 定义一个fast API application

student_rest_api = StudentRestAPI(base_url = "/api", db_factory = db_factory)
student_rest_api.register(app)