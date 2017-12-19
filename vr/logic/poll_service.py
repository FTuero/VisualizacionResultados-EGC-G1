from ..model import Poll, session

def find_poll(id):
    return session.query(Poll).get(id)
