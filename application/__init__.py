"""
Initialize Flask app

"""

from flask import Flask
from flaskext.gae_mini_profiler import GAEMiniProfiler
import settings
import api


app = Flask(__name__)
app.config.from_object('application.settings')


# If you need an api
# app.register_blueprint(api.app, url_prefix='/api')

import filters
import tests


if settings.PROFILER_ENABLED:
	# Enable profiler (enabled in non-production environment only)
	GAEMiniProfiler(app)

# Pull in URL route handlers
import views