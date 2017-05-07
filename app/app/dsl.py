# coding: utf-8

"""
Domain specific language for app quepy.
"""

from quepy.dsl import FixedDataRelation, FixedType, FixedRelation


class IsTime(FixedType):
    fixedtype = "table:Time"


class HasFields(FixedDataRelation):
    relation = "key:fields"


class HasCourse(FixedDataRelation):
    relation = "key:course"


class IsLocation(FixedType):
    fixedtype = "table:Location"

class IsPerson(FixedType):
    fixedtype = "table:Person"


class IsInfo(FixedType):
    fixedtype = "table:Info"

class HasAnswer(FixedDataRelation):
    relation = "key:answer"
