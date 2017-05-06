from refo import Question
from quepy.parsing import QuestionTemplate, Lemmas, Lemma, Particle, Pos
from quepy.dsl import HasKeyword

from dsl import *

from course import Course


class FinalExamTime(Particle):
    regex = Question(Pos("DT")) + Lemma("final")

    def interpret(self, match):
        final = match.words.tokens
        return HasKeyword(final)


class FinalExamQuestion(QuestionTemplate):
    """
    Ex: "When is the final exam for cmpe 273?"
        "What time is the final exam for cmpe 273?"
    """
    opening = Lemmas("what time be") | Lemmas("when be")
    regex = opening + FinalExamTime() + Pos("IN") + Course() + Question(Pos("."))

    def interpret(self, match):
        final = IsTime() + FinalExamTimeOf(match.course)
        return final

class ClassTime(Particle):
    regex = Question(Pos("DT")) + Lemmas("class time")

    def interpret(self, match):
        class_time = match.words.tokens
        return HasKeyword(class_time)


class ClassTimeQuestion(QuestionTemplate):
    """
    Ex: "What is the class time for cmpe 273?"
    """
    regex = Lemmas("what be") + ClassTime() + Pos("IN") + Course() + Question(Pos("."))


    def interpret(self, match):
        class_time = IsTime() + ClassTimeOf(match.course)
        return class_time
