from ..model import Question, QuestionOption, OptionPerVote, session

def find_question(id):
    return session.query(Question).get(id)

def question_option_result(id):
    return session.query(OptionPerVote).filter(OptionPerVote.question_option==id).count()