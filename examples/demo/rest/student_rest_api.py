from typing import Callable
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapitool import SimpleRestAPI, \
    RestCreateModelRequest, RestCreateModelResponse, \
    RestListModelResponse, \
    RestGetModelResponse, \
    RestDeleteModelResponse, \
    RestUpdateModelRequest, RestUpdateModelResponse, \
    RestPatchModelRequest, RestPatchModelResponse
import demo.core.apis as apis
from demo.db import create_tables, get_db, db_factory
import demo.core.models as models

class RestStudent(BaseModel):
    id: int
    name: str
    age: int

class RestCreateStudentRequest(RestCreateModelRequest[RestStudent]):
    name:str
    age:int

class RestUpdateStudentRequest(RestUpdateModelRequest[RestStudent]):
    name:str
    age:int

class RestPatchStudentRequest(RestPatchModelRequest[RestStudent]):
    # field has default value so user can skip setting value for it in case not needed
    name: str = ""
    age: int = 0

class StudentRestAPI(SimpleRestAPI[models.Student, RestStudent, int]):
    def __init__(self, db_factory:Callable[[], Session], base_url:str):
        super().__init__(
            label = "student",
            db_factory = db_factory,
            model_api = apis.StudentAPI(),
            t_create = [
                RestCreateStudentRequest, 
                RestCreateModelResponse[RestStudent]
            ],
            t_list = RestListModelResponse[RestStudent], 
            t_get = RestGetModelResponse[RestStudent],
            t_delete = RestDeleteModelResponse[RestStudent],
            t_update = [RestUpdateStudentRequest, RestUpdateModelResponse[RestStudent]],
            t_patch = [RestPatchStudentRequest, RestPatchModelResponse[RestStudent]], 
            base_url = base_url
        )
    


