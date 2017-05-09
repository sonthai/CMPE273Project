from refo import Question, Plus
from quepy.parsing import QuestionTemplate, Lemmas, Lemma, Pos
from dsl import *

from course import Course


class InstructorQuestion(QuestionTemplate):
    """
        Ex: "Who is the instructor of cmpe 273?"
            "Who teaches cmpe 273?"
            "By whom is cmpe 273 taught?"
    """
    regex = Lemmas("who be") + Question(Pos("DT")) + Lemma("instructor") + Pos("IN") + Course() + Question(Pos(".")) | \
            Lemma("who") + Lemma("teach") + Course() + Question(Pos("."))| \
            Pos("IN") + Lemmas("whom be") + Course() + Lemma("taught") + Question(Pos("."))

    def interpret(self, match):
        answer = "The instructor for %s is %s"
        instructor = IsInstructorInfoRelated() + match.course + HasFields('name'.decode('utf-8')) + HasAnswer(answer.decode('utf-8'))
        return instructor


class InstructorEmailQuestion(QuestionTemplate):
    """
       Ex: "What is the email of instructor of cmpe 273?"
           "Which email is used to communicate with instructor of cmpe 273?"
    """
    regex = Lemmas("what be") + Question(Pos("DT")) + Lemma("email") + Pos("IN") + Lemma("instructor") + Pos("IN") + Course() + Question(Pos(".")) | \
            Lemmas("which email be ") + Lemma("use") + Pos("TO") + Lemma("communicate") + Pos("IN") + Lemma("instructor") + Pos("IN") + Course() + Question(Pos("."))

    def interpret(self, match):
        answer = "The instructor's email of %s is %s"
        email = IsInstructorInfoRelated() + match.course + HasFields('email'.decode('utf-8')) + HasAnswer(answer.decode('utf-8'))
        return email
