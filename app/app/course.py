from refo import Question
from quepy.parsing import Particle, Pos, Lemma

from dsl import *

course = Pos("CD")


class Course(Particle):
    regex = Question(Pos("DT")) + Lemma("cmpe") + course

    def interpret(self, match):
        name = "keyword:" + match.words.tokens
        return HasCourse(name)