from flask import Flask, render_template, url_for, request
import sys
import data
import os

app = Flask(__name__)

"""404"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template("pagenotfound.html")

"""Home"""
@app.route('/')
def index():
	try:
		db = data.load('data.json')
		return render_template('index.html', db=db)
		
	except:
		return render_template('pagenotfound.html')

"""Techniques"""
@app.route('/techniques', methods=['POST','GET'])
def techniques():
	db = data.load('data.json')
	
	if request.method == 'GET':
		chosen_techniques = request.form.getlist('techniques')
		technique_list = data.search(db, techniques=chosen_techniques)
		return render_template("techniques.html", techniques=technique_list)
		
	elif request.method == 'POST':
		chosen_techniques = request.form.getlist('techniques')
		technique_list = data.search(db, techniques=chosen_techniques)
		
		return render_template("techniques.html", techniques=technique_list)

"""Projects"""
@app.route('/list', methods=['POST','GET'])
def get_search_fields():
	db = data.load('data.json')
	
	if request.method == 'GET':
		sort_by = request.form.get('sort_by')
		sort_order = request.form.get('sort_order')
		search = request.form.get('search')
		
		get_search_fields = data.search(db, sort_by=sort_by, sort_order=sort_order, search=search)
		
		return render_template('projects.html', get_search=get_search_fields)
			
	if request.method == 'POST':
		sort_by = request.form.get('sort_by')
		sort_order = request.form.get('sort_order')
		search = request.form.get('search')
		search_fields = request.form.getlist('search_fields')
		
		get_search_fields = data.search(db, sort_by=sort_by, sort_order=sort_order, search=search, search_fields=search_fields)
		
		print(sort_by, file=sys.stderr)
		print(sort_order, file=sys.stderr)
		print(search, file=sys.stderr)
		print(search_fields, file=sys.stderr)
		
		return render_template('projects.html', get_search=get_search_fields)

"""Project IDs"""
@app.route('/project/<int:project_id>')
def project_site(project_id):
	try:
		db = data.load('data.json')
		project = data.get_project(db, project_id)
		return render_template('project.html', project=project, id=project_id)
		
	except:
		return render_template('pagenotfound.html')
	
if __name__ == "__main__":
	app.run(debug=True)

