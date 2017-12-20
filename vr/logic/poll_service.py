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

    start_date = poll.startDate
    end_date = poll.endDate
    for single_date in daterange(start_date, end_date):
        res[0].extend(single_date.strftime("%Y-%m-%d"))
        res[1].extend(1)


    for q in poll.question_collection:
        for op in q.question_option_collection:
            for opv in op.option_per_vote_collection:
                for vo in opv.vote_collection:
                    if(res[0].__contains__(vo.voteDate)):
                        i=res[0].index(vo.voteDate)
                        res[1].__setitem__(i,res[1].__getitem__(i))
    return res


def votes_per_platform(poll_id):
    res = [[],[]]
    poll= session.query(Poll).get(poll_id)
    for q in poll.question_collection:
        for op in q.question_option_collection:
            for opv in op.option_per_vote_collection:
                for vo in opv.vote_collection:
                    if(res[0].__contains__(vo.voteType)):
                        i=res[0].index(vo.voteType)
                        res[1]=res[1].__getitem__(i)+1
                    else:
                        res[0].extend(vo.voteType)
                        res[1].extend(1)
    return res