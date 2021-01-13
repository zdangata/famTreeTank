import os
import json
from flask import Flask, request, abort, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import random

from models import *
#----------------------------------------------------------------------------#
# Creating the app
#----------------------------------------------------------------------------#

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # Set up CORS. Allow '*' for origins.
    cors = CORS(app)

    # Use the after_request decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, PATCH, DELETE, OPTIONS')
        return response

    #----------------------------------------------------------------------------#
    # Defining routes
    #----------------------------------------------------------------------------#

    @app.route('/')
    def index():
        return 'Hello world!'

    @app.route('/tanko')
    def tanko():
        tanko = Tanko.query.all()
        
        if len(tanko == 0):
            abort(404)

        return jsonify({
            'success': True,
            'tanko_entries': formatted_tanko,
            'total_tanko_entries': len(tanko)
        })


    # ----------------------------------------------------------------------------#
    # Error Handlers
    # ----------------------------------------------------------------------------#
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(401)
    def unauthorised_error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorised"
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "access forbidden"
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    @app.errorhandler(422)
    def not_processed(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable entity"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500


    return app

app = create_app()