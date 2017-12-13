from sqlalchemy.ext.automap import automap_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from . import *


db = SQLAlchemy(app)
base = automap_base()
base.prepare(db.engine, reflect=True)

session = Session(db.engine)


Census = base.classes['census']
Poll = base.classes['poll']
Question = base.classes['question']
QuestionOption = base.classes['question_option']
OptionPerVote = base.classes['option_per_vote']
Vote = base.classes['vote']
VoteType = base.classes['vote_type']
Role = base.classes['role']
User = base.classes['user']