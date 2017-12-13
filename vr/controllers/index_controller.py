from ..model import *
from .. import app

@app.route('/')
def home():
    print("fff")
    polls = session.query(base.classes['poll']).all()
    str = ""
    for p in polls:
        str = str + p.title + "\n<br\>"
    return str