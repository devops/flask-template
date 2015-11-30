#!/usr/bin/env python2
# -*- coding: UTF-8 -*-


from flask import Blueprint, render_template

mod = Blueprint('core', __name__)


@mod.route('/')
def index():
    return render_template('index.html')
