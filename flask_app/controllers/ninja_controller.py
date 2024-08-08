from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.ninja_model import Ninjas 


@app.route('/')
def index():
    return redirect('/ninjas')

@app.route('/ninjas/')
def ninja_page():
    ninja_list = Ninjas.get_all()
    return render_template("main_page.html", ninjas = ninja_list)

@app.route('/ninja/new')
def new_page():
    return render_template("create_ninja.html")

#CREATE
@app.route('/ninja/create', methods=['POST'])
def create():
    print(request.form)
    Ninjas.save(request.form)
    return redirect('/ninjas')

@app.route('/ninja/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_ninja.html",ninja =Ninjas.get_one(data))

@app.route('/ninja/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("read_ninja.html",user=Ninjas.get_one(data))


@app.route('/ninja/update',methods=['POST'])
def update():
    Ninjas.update(request.form)
    return redirect('/users')

@app.route('/ninja/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Ninjas.destroy(data)
    return redirect('/users')