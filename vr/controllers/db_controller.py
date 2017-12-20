from ..model import *
from .. import app
from ..logic.poll_service import find_poll,votes_per_day,votes_per_platform
from ..logic.census_service import census_count
from flask import render_template
from flask import jsonify


@app.route('/visres/data/day/<poll_id>')
def votes_per_day_data(poll_id):
    vpd = votes_per_day(poll_id);
    res= jsonify(
        len=vpd[0].__len__(),
        labels=vpd[0],
        data=vpd[1]
    )
    return res


@app.route('/visres/data/census/<poll_id>')
def participation_data(poll_id):
    poll = find_poll(poll_id)
    participantsN = census_count(poll.census.id);
    res= jsonify(
        participation=participantsN/poll.votos_actuales
    )
    return res


@app.route('/visres/data/platform/<poll_id>')
def votes_per_platform_data(poll_id):
    vpp = votes_per_platform(poll_id);
    res = jsonify(
        len=vpp[0].__len__(),
        labels=vpp[0],
        data=vpp[1]
    )
    return res