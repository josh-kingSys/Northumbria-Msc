from pywebio.input import *
from pywebio.output import *

correct_answers = 0
wrong_answers = 0

INTRODUCTION = """
<P>Welcome, to the Python super fun quiz. We are going to test your Python knowledge
 by giving you 20 statements about the Python programming language.
 Then you may answer each statement with either True or False.</P>

<hr>

"""

put_html("<h1>ThePython Quiz</h1>")
put_html(INTRODUCTION)

questions= ["In Python, indentation is optional.",  "Python uses dynamic Typing.", "Python is a compiled language.", "Python lists are immutable"]

correct_answers_list = ["False", "True", "False", "True"]


for i in range(len(questions)):
    answer_i = actions(questions[i], ['True', 'False'])
    if answer_i == correct_answers_list[i]:
        toast(f"Your answer was {answer_i}, which is Correct.", color='success', position='center', duration=3)
        correct_answers += 1

    else:
        toast(f"Your answer was {answer_i}, which is Incorrect.", color='error', position='center', duration=3)
        wrong_answers += 1


put_text(f"you have answered {correct_answers} questions correctly and {wrong_answers} questions incorrectly.")

