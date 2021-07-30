from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_share import Share
app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://ashutoshdikshit:1234@cluster0.akjxa.mongodb.net/todo?retryWrites=true&w=majority'
mongo = PyMongo(app)
share=Share(app)
todos = mongo.db.todos

@app.route('/')
def index():
    saved_todos = todos.find()
    return render_template('index.html', todos=saved_todos)

@app.route('/add',methods=['POST'])
def add():
    list1=request.form["new-todo"]
    todos.insert_one({'text':list1,'complete':False})
    return redirect(url_for('index'))

@app.route('/complete/<oid>')
def complete(oid):
    todo_item=todos.find_one({'_id': ObjectId(oid)})
    if(todo_item['complete']==False):
        todo_item['complete']=True
        todos.save(todo_item)
        return redirect(url_for('index'))
    else:
        todo_item['complete']=False
        todos.save(todo_item)
        return redirect(url_for('index'))


@app.route('/delete_completed')
def delete_completed():
    todos.delete_many({'complete':True})
    return redirect(url_for('index'))


@app.route('/delete_all')
def delete_all():
    todos.delete_many({})
    return redirect(url_for('index'))

# def create_app():
#     app=Flask(__name__)
#     share.init_app(app)



if __name__=='__main__':
    app.run(debug=True)