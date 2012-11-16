# -*- coding: utf-8 -*-

"""This blueprint defines all URLs and answers."""

import flask
import flask.helpers

blueprint = flask.Blueprint('v1', __name__)

@blueprint.route('/')
def welcome():
    """Returns detailed information about this specific version of the API."""
    return 'Welcome to Kwapi!'

@blueprint.route('/probes/')
def list_probes():
    """Returns a list of all the known probes."""
    return flask.jsonify(probes=flask.request.database.keys())

@blueprint.route('/probes/<probe>/')
def probe_info(probe):
    """Returns all information about this probe (id, timestamp, kWh, W)."""
    try:
        result = {probe: flask.request.database[probe]}
    except KeyError:
        flask.abort(404)
    return flask.jsonify(result)

@blueprint.route('/probes/<probe>/<meter>/')
def probe_value(probe, meter):
    """Returns the probe meter value."""
    try:
        result = {meter: flask.request.database[probe][meter]}
    except KeyError:
        flask.abort(404)
    return flask.jsonify(result)
