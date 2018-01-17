from ..model import *
from .. import app
from ..logic.poll_service import find_poll
from ..logic.question_service import question_option_result
from flask import render_template
from .login_required import login_required

@app.route('/visres/<poll_id>')
@login_required
def home(poll_id):
    poll = find_poll(poll_id)
    def count_question(id):
        return question_option_result(id)
    return render_template('result.html', poll=poll, count_question=count_question)
