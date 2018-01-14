from functools import wraps
from flask import g, request, redirect, url_for
import requests
import json
from flask import request, redirect

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_id = request.cookies.get("session_id")

        if not session_id:
            return redirect("https://g1login.egc.duckdns.org/login")

        else:
            r = requests.get('https://g1login.egc.duckdns.org/cookies/'+str(session_id))
            r.json()
            d = json.loads(r.text.decode('ascii', 'ignore'))
            if d['codigo'] == 0:
                return redirect("https://g1login.egc.duckdns.org/login")
            else:
                return f(*args, **kwargs)
    return decorated_function