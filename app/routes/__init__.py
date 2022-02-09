from flask import Flask
from app.routes.leads_routes import bp as bp_lead

def init_app(app: Flask):
    app.register_blueprint(bp_lead)    