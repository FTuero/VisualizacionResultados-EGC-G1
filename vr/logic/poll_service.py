from ..model import Poll, session

def find_poll(id):
    return session.query(Poll).get(id)

def votes_per_day(poll_id):
    res = [[],[]]
    poll= session.query(Poll).get(poll_id)
    for q in poll.question_collection:
        for op in q.question_option_collection:
            for opv in op.option_per_vote_collection:
                for vo in opv.vote_collection:
                    if(res[0].__contains__(vo.voteDate)):
                        i=res[0].index(vo.voteDate)
                        res[1]=res[1].__getitem__(i)+1
                    else:
                        res[0].extend(vo.voteDate)
                        res[0].extend(1)
    return res

