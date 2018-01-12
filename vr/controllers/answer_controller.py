from ..logic.poll_service import find_poll
from flask import render_template
from .. import app
from ..logic.question_service import question_option_result

@app.route('/visres/<poll_id>/anwsers')
@login_required
def anwsers(poll_id):

    poll = find_poll(poll_id)

    def votes_question(qo_id):
        votes =  question_option_result(qo_id)
        return votes

    return render_template('answer.html', poll=poll,votes_question=votes_question)



