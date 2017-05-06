from refo import Question
from quepy.parsing import QuestionTemplate, Lemmas, Lemma, Particle, Pos
from quepy.dsl import HasKeyword

from dsl import *

from course import Course


class FinalExamLocation(Particle):
    regex = Question(Pos("DT")) + Lemma("final")

    def interpret(self, match):
        final = match.words.tokens
        return HasKeyword(final)


class FinalExamLocationQuestion(QuestionTemplate):
    """
    Ex: "Where is the final exam for cmpe 273?"
        "Which location is the final exam for cmpe 273?"
    """
    opening = Lemmas("where be") | (Question(Pos("IN")) + Lemmas("which location be"))
    regex = opening + FinalExamLocation() + Pos("IN") + Course() + Question(Pos("."))

    def interpret(self, match):
        final = IsLocation() + FinalExamLocationOf(match.course)
        return final
