from ..model import Poll, session


def census_count(poll_id):
    poll = session.query(Poll).get(poll_id)
    if poll.participantes_admitidos==0:
        return 0
    res=poll.votos_actuales/poll.participantes_admitidos
    return res
