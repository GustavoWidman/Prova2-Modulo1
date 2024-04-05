from flask import Blueprint, render_template

router = Blueprint('dash', __name__)


@router.route('/', methods=['GET'])
def index_page():
	return render_template("dash.html")