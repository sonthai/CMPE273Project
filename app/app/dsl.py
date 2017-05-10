# coding: utf-8

"""
Domain specific language for app quepy.
"""

from quepy.dsl import FixedDataRelation, FixedType, FixedRelation


class IsInstructorInfoRelated(FixedType):
    fixedtype = "table:InstructorTable"


class IsClassRelated(FixedType):
    fixedtype = "table:ClassTable"


class IsExamRelated(FixedType):
    fixedtype = "table:ExamTable"


class HasFields(FixedDataRelation):
    relation = "key:fields"


class HasCourse(FixedDataRelation):
    relation = "key:course"


class HasAnswer(FixedDataRelation):
    relation = "key:answer"
