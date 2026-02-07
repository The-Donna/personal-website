import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime

load_dotenv()
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)

db = client.portfolio_db
messages_collection = db.messages

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/resume')
def resume():
    return render_template('resume.html', title="Resume")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        contact_entry = {
            "name": name,
            "email": email,
            "message": message,
            "date": datetime.now() 
        }

        messages_collection.insert_one(contact_entry)
        
        print(f"Message from {name} saved to MongoDB!")
        return render_template('contact.html', title="Contact", success=True)
    
    return render_template('contact.html', title="Contact")

if __name__ == '__main__':
    app.run(debug=True)
    
