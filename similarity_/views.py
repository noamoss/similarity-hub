from flask import Blueprint

simple_page = Blueprint('simple_page', __name__)


@simple_page.route('/')
def hello_world():
    return 'Hello, World!?'
