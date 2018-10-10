from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from braham_flask.db import get_db

from braham import acquirers_multiple_valutaion as ame

import asyncio

bp = Blueprint('ame', __name__, url_prefix='/ame')

@bp.route('/ame', methods=('GET', 'POST'))
def render_acquirers_multiple_valutaion():
    ame_factory = ame.factory()
    return render_template("ame/analysis.html", data=x.to_html())