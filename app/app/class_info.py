from refo import Question, Plus
from quepy.parsing import QuestionTemplate, Lemmas, Lemma, Pos, Group
from dsl import *

from course import Course


class ClassPrerequisiteQuestion(QuestionTemplate):
    """
        Ex: "What are the prerequisites for cmpe 273?"
    """
    prerequisite = Group(Lemma("prerequisite"), "prerequisite")
    regex = Lemmas("what be") + Question(Pos("DT")) + prerequisite + Pos("IN") + Course() + Question(Pos("."))

    def interpret(self, match):
        answer = "The prerequisites for %s are %s"
        prerequisite = IsClassRelated() + match.course + HasFields('prerequisites'.decode('utf-8')) \
                       + HasAnswer(answer.decode('utf-8'))
        return prerequisite


class UnitsQuestion(QuestionTemplate):
    """
        Ex: "How many units are there for cmpe 273?"
            How many credits are there for cmpe 287?
            What number of units are there for cmpe 273?
    """
    regex = Lemmas("what be") + Lemma("number") + Question(Pos("DT")) + Lemma("units") +Pos("IN") + Course() + Question(Pos("."))
            # Lemma("who") + Lemma("teach") + Course() + Question(Pos("."))| \
            # Pos("IN") + Lemmas("whom be") + Course() + Lemma("taught") + Question(Pos("."))

    def interpret(self, match):
        answer = "The units awarded for %s is %s"
        units = IsClassRelated() + match.course + HasFields('units'.decode('utf-8')) + HasAnswer(answer.decode('utf-8'))
        return units
