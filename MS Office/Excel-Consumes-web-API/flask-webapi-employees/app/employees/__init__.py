from flask import Blueprint

empbp = Blueprint('empbp', __name__, url_prefix='/employees')

from . import models
from . import views

