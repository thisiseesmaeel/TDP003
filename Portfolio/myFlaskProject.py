from flask import Flask, render_template, url_for, request
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
@app.route('/techniques')
def techniques():
	db = data.load('data.json')
	tech_list = data.get_techniques(db)
	return render_template("techniques.html", db=db, techniques=tech_list)

"""Projects"""
@app.route('/list', methods=['POST','GET'])
def get_search_fields():
	db = data.load('data.json')
	
	#search_fields = request.form.getlist('search_fields')
	
	get_search_fields = data.search(db, request.form.get('sort_by'), request.form.get('sort_order'), request.form.get('search'))
	return render_template('projects.html', get_search=get_search_fields)

#	if not search_fields and not techniques:
#		get_search_fields = data.search(db, sort_by=sort_by, sort_order=sort_order, techniques=None, search=search, search_fields=None)
#		return render_template("techniques.html", result=get_search_fields, techniques=techniques)
	
#	if not search_fields:
#		get_search_fields = data.search(db, sort_by=sort_by, sort_order=sort_order, techniques=techniques, search=search, search_fields=None)
#		return render_template("techniques.html", result=get_search_fields, techniques=techniques)
		
#	if not techniques:
#		get_search_fields = data.search(db, sort_by=sort_by, sort_order=sort_order, techniques=None, search=search, search_fields=search_fields)
#		return render_template("techniques.html", result=get_search_fields, techniques=techniques)







#project/1 och project/2 funkar ej
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






"""Pseudokod"""
#Importera json-filen (alla våra projekt)
#skriv for-loop för att lista alla projekt



"""Presentationslager"""

"""Template"""
#navbar
#copyright
#projektlista (från search och techniques)

"""Home"""
"""Main"""
#lista över senaste projekt
"""sidebar"""
#search
#pfp
#bio
#sociala medier


"""Techniques"""
#knappar för varje teknik
#visa alla projekt (get project?)


"""Projects"""
#search
#filters:
	#klicka techniques
	#klicka fields
	#klicka sort by (start_date, project name etc)
	
#visa alla projekt från search





	
	

	


	
	
	    
	  
	  
	
	

      
    


