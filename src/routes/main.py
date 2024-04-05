from flask import Blueprint

from routes.ping import router as ping_router
from routes.info import router as info_router
from routes.echo import router as echo_router
from routes.dash import router as dash_router


router = Blueprint('router', __name__, url_prefix='')
router.register_blueprint(ping_router, url_prefix='/ping')
router.register_blueprint(echo_router, url_prefix='/echo')
router.register_blueprint(info_router, url_prefix='/info')
router.register_blueprint(dash_router, url_prefix='/dash')