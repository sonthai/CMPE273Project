# coding: utf-8

"""
Domain specific language for app quepy.
"""

from quepy.dsl import FixedDataRelation, FixedType, FixedRelation


class IsTime(FixedType):
    fixedtype = "table:Time"


class FinalExamTimeOf(FixedRelation):
    relation = "field:final_time"


class HasCourse(FixedDataRelation):
    relation = "key:course"

class ClassTimeOf(FixedRelation):
    relation = "field:start,end"


class IsLocation(FixedType):
    fixedtype = "table:Location"


class FinalExamLocationOf(FixedRelation):
    relation = "field:final_exam_location"