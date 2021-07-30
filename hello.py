from flask import *
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://ashutoshdikshit:1234@cluster0.akjxa.mongodb.net/todo?retryWrites=true&w=majority'
mongo = PyMongo(app)

todos = mongo.db.todos


@app.route('/')
def index():
    saved_todos=todos.find()
    return render_template('index.html',todos=saved_todos)

if __name__=='__main__':
    app.run(debug=True)