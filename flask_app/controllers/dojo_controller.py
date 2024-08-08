from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo_model import Dojos 


# # @app.route('/')
# def index():
#     return redirect('/dojos')

# @app.route('/dojos/')
# def ninja_page():
#     dojo_list = Dojos.get_all()
#     return render_template("main_page.html", dojos = dojo_list)

# @app.route('/dojos/new')
# def new_page():
#     return render_template("create_ninja.html")

# #CREATE
# @app.route('/dojos/create', methods=['POST'])
# def create():
#     print(request.form)
#     Dojos.save(request.form)
#     return redirect('/dojos')