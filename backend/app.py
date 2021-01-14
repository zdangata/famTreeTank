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
    # Defining simple 'get' request routes
    #----------------------------------------------------------------------------#

    @app.route('/')
    def index():
        return 'Hello world!'

    # get all tankos
    @app.route('/tanko')
    def tanko():
        tankos = Tanko.query.all()
        formatted_tanko = [tanko.format() for tanko in tankos]
        
        total_tanko_entries = len(tankos)
        if (total_tanko_entries == 0):
            abort(404)

        return jsonify({
            'success': True,
            'tanko_entries': formatted_tanko,
            'total_tanko_entries': total_tanko_entries
        })

    # get all children
    @app.route('/children')
    def child():
        children = Children.query.all()
        formatted_child = [child.format() for child in children]
        
        total_children_entries = len(children)
        if (total_children_entries == 0):
            abort(404)

        return jsonify({
            'success': True,
            'children_entries': formatted_child,
            'total_children_entries': total_children_entries
        })

    # get all grandchildren
    @app.route('/grandchildren')
    def grandchild():
        grand_children = Grandchildren.query.all()
        formatted_grand_child = [grand_child.format() for grand_child in grand_children]
        
        total_grand_children_entries = len(grand_children)
        if (total_grand_children_entries == 0):
            abort(404)

        return jsonify({
            'success': True,
            'children_entries': formatted_grand_child,
            'total_children_entries': total_grand_children_entries
        })

    # get all great grandchildren
    @app.route('/greatgrandchildren')
    def g_grandchild():
        g_grand_children = Greatgrandchildren.query.all()
        formatted_g_grand_child = [g_grand_child.format() for g_grand_child in g_grand_children]
        
        total_g_grandchildren_entries = len(g_grand_children)
        if (total_g_grand_children_entries == 0):
            abort(404)

        return jsonify({
            'success': True,
            'children_entries': formatted_g_grand_child,
            'total_children_entries': total_g_grand_children_entries
        })

    #----------------------------------------------------------------------------#
    # Defining simple 'post' request routes
    #----------------------------------------------------------------------------#

    @app.route('/children', methods=['POST'])
    def create_child():
        body=request.get_json()

        name = body.get('name', None)
        birthday = body.get('birthday', None)
        marital_status = body.get('marital_status', None)
        bio = body.get('bio', None)

        try:
            child = Children(name=name, birthday=birthday, marital_status=marital_status, bio=bio)
            child.insert()
        
            child_selection = Children.query.order_by(Children.id).all()
            formatted_child = child_selection.format()
            total_children_entries = len(Children.query.all())

            return jsonify({
                'success': True,
                'child': formatted_child,
                'total_children_entries': total_children_entries
            })

        except:
            abort(422)
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