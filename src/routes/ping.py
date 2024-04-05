from flask import Blueprint, request, jsonify

from utils.logger import log

router = Blueprint('ping', __name__)


@router.route('/', methods=['GET'])
def ping():
	log( str(request.remote_addr), 'ping', {} )
	return jsonify({"resposta": "pong"})