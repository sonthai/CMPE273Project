from refo import Question, Plus
from quepy.parsing import QuestionTemplate, Lemmas, Group, Pos, Lemma

from dsl import *

from course import Course


class ExamQuestion(QuestionTemplate):
    """
        Ex: "When is the final exam for cmpe 273?"
            "When is the midterm exam for cmpe 273?"
            "What time is the final exam for cmpe 273?"
            "What time is the midterm exam for cmpe 273?"
    """
    opening = Lemmas("what time be") | Lemmas("when be")
    exam = Group(Plus(Lemmas("final exam") | Lemmas("midterm exam")), "exam")
    regex = opening + Question(Pos("DT")) + exam + Pos("IN") + Course() + Question(Pos("."))

    def interpret(self, match):
        exam_time = IsTime() + match.course + HasFields(match.exam.tokens)
        return exam_time


class ClassTimeQuestion(QuestionTemplate):
    """
        Ex: "What is the class time for cmpe 273?"
            "What are the class days for cmpe 273?"
    """
    classTime = Group(Plus(Lemmas("class time") | Lemmas("class days")), "classTime")
    regex = Lemmas("what be") + Question(Pos("DT")) + classTime + Pos("IN") + Course() + Question(Pos("."))

    def interpret(self, match):
        class_time = IsTime() + match.course + HasFields(match.classTime.tokens)
        return class_time


class InstructorOfficeHour(QuestionTemplate):
    """
        Ex: "What time does the cmpe 273 instructor have office hours?"
            "When does the cmpe 273 instructor have office hours?"
    """
    regex = Plus(Lemmas("what time") | Lemma("when")) + Lemma("do") + Question(Pos("DT")) + Course() + Lemma("instructor") \
            + Lemma("have") + Lemmas("office hours") + Question(Pos("."))


    def interpret(self, match):
        instructor_office_hour = IsTime() + match.course + HasFields('office hour'.decode('utf-8'))
        return instructor_office_hour