from ..model import Poll, session
import datetime
from datetime import timedelta, date


def find_poll(id):
    return session.query(Poll).get(id)


def votes_per_day(poll_id):
    res = [[],[]]
    poll= session.query(Poll).get(poll_id)

    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)


    for single_date in daterange(poll.startDate, poll.endDate):
        res[0].append(single_date.strftime("%Y-%m-%d"))
        res[1].append(0)

    for q in poll.question_collection:
        for op in q.question_option_collection:
            for opv in op.option_per_vote_collection:
                if(res[0].__contains__(opv.vote.vote_date.strftime("%Y-%m-%d"))):
                    i=res[0].index(opv.vote.vote_date.strftime("%Y-%m-%d"))
                    res[1].__setitem__(i, res[1].__getitem__(i) + 1)
    return res


def votes_per_platform(poll_id):
    res = [["Web","Slack","Telegram"],[0,0,0]]
    poll= session.query(Poll).get(poll_id)
    for q in poll.question_collection:
        for op in q.question_option_collection:
            for opv in op.option_per_vote_collection:
                i=opv.vote.vote_type_id-1
                res[1].__setitem__(i, res[1].__getitem__(i) + 1)
    return res