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
        prerequisite = IsInfo() + match.course + HasFields('prerequisite'.decode('utf-8'))
        return prerequisite
