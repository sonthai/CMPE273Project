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


class GradingQuestion(QuestionTemplate):
    """
        Ex: "How is the grading for cmpe 273"
        Ex: "What is the grading for cmpe 273"
    """
    grading = Group(Lemma("grading"), "grading")
    regex = Lemmas("How be") + Question(Pos("DT")) + grading + Pos("IN") + Course() + Question(Pos(".")) | \
    Lemmas("what be") + Question(Pos("DT")) + Lemma("grading") + Pos("IN") + Course() + Question(Pos("."))

    def interpret(self, match):
        answer = "%s has %s ."
        grading = IsClassRelated() + match.course + HasFields('grading'.decode('utf-8')) \
                       + HasAnswer(answer.decode('utf-8'))
        return grading

class GradingPolicy(QuestionTemplate):
    """
        Ex: "What is the assignment breakdown for cmpe 273?"
        Ex: "What is the grading policy for cmpe 273"
    """
    gradingpolicy = Group(Lemma("gradingpolicy"), "gradingpolicy")
    regex = Lemmas("What be") + Question(Pos("DT")) + Lemma("grading") + Lemma("policy") + Pos("IN") + Course() + Question(Pos(".")) | \
    Lemmas("what be") + Question(Pos("DT")) + Lemma("assignment") + Lemma("breakdown") + Pos("IN") + Course() + Question(Pos("."))

    def interpret(self, match):
        answer = "%s has the following weightage: %s."
        gradingpolicy = IsClassRelated() + match.course + HasFields('GradingPolicy'.decode('utf-8')) \
                       + HasAnswer(answer.decode('utf-8'))
        return gradingpolicy