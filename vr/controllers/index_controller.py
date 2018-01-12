from ..model import *
from .. import app
from ..logic.poll_service import find_poll
from ..logic.question_service import question_option_result
from flask import render_template
from flask import request
from flask import redirect
import requests
from pprint import pprint
import json

@app.route('/visres/<poll_id>')
def home(poll_id):
    session_id = request.cookies.get("session_id")

    if not session_id:
        return redirect("https://g1login.egc.duckdns.org/login")

    else:
        r = requests.get('https://g1login.egc.duckdns.org/cookies/'+str(session_id))
        r.json()
        d = json.loads(r.text.decode('ascii', 'ignore'))
        if d[codigo] == 0:
            return redirect("https://g1login.egc.duckdns.org/login")
        else:
            return render_template('result.html', poll=poll, count_question=count_question)
