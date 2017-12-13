from ..model import Question, QuestionOption, OptionPerVote, session

def find_question(id):
    return session.query(Question).get(id)

def question_option_result(id):
    res = 0
    for op in session.query(OptionPerVote).all():
        if op.id == id:
            res += 1
    return res