from typing import Optional
from dataclasses import dataclass
from fastapitool import CreateModelRequest, UpdateModelRequest, PatchModelRequest, SimpleModelAPI
from demo.core.models import Student


class StudentAPI(SimpleModelAPI[Student, int]):
    @dataclass
    class CreateModelRequest(CreateModelRequest[Student]):
        name: str
        age: int

    @dataclass
    class UpdateModelRequest(UpdateModelRequest[Student, int]):
        name: str
        age: int

    @dataclass
    class PatchModelRequest(PatchModelRequest[Student, int]):
        name: Optional[str] = None
        age: Optional[int] = None

    def __init__(self):
        super().__init__(Student)
