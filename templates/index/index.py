from flask import Flask, Blueprint, render_template, request

index = Blueprint('index', __name__)


@index.route('/')
def _index():
    return render_template('./index/index.html')
