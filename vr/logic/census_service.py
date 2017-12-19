from ..model import Census, session


def census_count(census_id):
    res = 0
    census = session.query(Census).get(census_id)
    for us in census.user_account_per_census:
        res += 1
    return res
