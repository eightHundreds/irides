from flask import render_template, flash, redirect, url_for, request, \
    current_app, abort, make_response, jsonify
from flask.ext.login import login_required, current_user
from flask.ext.sqlalchemy import get_debug_queries