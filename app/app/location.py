from refo import Question, Plus
from quepy.parsing import QuestionTemplate, Lemmas, Lemma, Pos, Group
from dsl import *

from course import Course


class FinalExamLocationQuestion(QuestionTemplate):
    """
        Ex: "Where is the final exam for cmpe 273?"
            "Where is the midterm exam for cmpe 273?"
            "Which location is the final exam for cmpe 273?"
            "Which location is the midterm exam for cmpe 273?"
    """
    opening = Lemmas("where be") | (Question(Pos("IN")) + Lemmas("which location be"))
    exam = Group(Plus(Lemmas("final exam") | Lemmas("midterm exam")), "exam")
    regex = opening + Question(Pos("DT")) + exam + Pos("IN") + Course() + Question(Pos("."))

    def interpret(self, match):
        exam_location = IsLocation() + match.course + HasFields(match.exam.tokens)
        return exam_location


class ClassLocationQuestion(QuestionTemplate):
    """
        Ex: "What is the class location of cmpe 273?"
            "At which location is cmpe 273 located?"
            "Where is cmpe 273?"
            "Where is cmpe 273 located?"
    """

    regex = Lemmas("what be") + Question(Pos("DT") + Question(Lemma("class"))) + Lemmas("location") + Pos("IN") + Course() + Question(Pos(".")) | \
            Lemmas("where be") + Course() + Question(Lemma("locate")) + Question(Pos(".")) | \
            Question(Pos("IN")) + Lemmas("which location be") + Course() + Question(Lemma("locate")) + Question(Pos("."))

    def interpret(self, match):
        class_location = IsLocation() + match.course + HasFields('classroom'.decode('utf-8'))
        return class_location


class InstructorOfficeLocation(QuestionTemplate):
    """
        Ex: "What is the office location of cmpe 273 instructor?"
            "Where is the office of cmpe 273 instructor?"
            "Where is the office of cmpe 273 instructor located?"
    """
    regex = Pos("WP") + Lemma("be") + Question(Pos("DT")) + Lemma("office") + Question(Lemma("location")) + Pos("IN") + Course()  + Lemma("instructor") + Question(Lemma("locate")) + Question(Pos("."))

    def interpret(self, match):
        instructor_office = IsLocation() + match.course + HasFields('office_location'.decode('utf-8'))
        return instructor_office
