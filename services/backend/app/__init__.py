from flask import Flask
import os


def create_app(script_info=None):

    app = Flask(__name__)

    app.url_map.strict_slashes = False

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # register api
    from app.api import api

    api.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
