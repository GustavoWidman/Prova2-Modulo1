from flask import Blueprint, Response, request, jsonify

from utils.logger import log

router = Blueprint('echo', __name__)


@router.route('/echo', methods=['POST'])
def echo():
	log( str(request.remote_addr), 'echo', request.json if request.json else {} )

	data = request.json

	if not data or 'dados' not in data: return Response(status=400, response='{"erro": "Requisição inválida"}', content_type='application/json')

	return jsonify({"resposta": data['dados']})