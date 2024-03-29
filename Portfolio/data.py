import json
import operator
#import json to load the json-file and import operator to get the value of the key "project_id" and sort it

#returns all projects in the json-file
def load(filename):
	try:
		with open(filename, "r") as f:
			projects = list(json.load(f))
			projects.sort(key=operator.itemgetter("project_id"))
		
			return projects
	
	except:
		return None

#returns the total number of projects
def get_project_count(db):
	print(len(db))
	return len(db)

#searches and returns one specific project based on id
def get_project(db, id):
	for project in db:
		if project["project_id"] == id:
			return project
	
	return None

#searches through all projects and if they match, adds to an empty list and sort them according to sort_by and sort_order
#matches() looks if one project matches search_techniques and search_fields. If it does, it returns True. If it doesn't, it returns False
def search(db, sort_by='start_date', sort_order='desc', techniques=None, search=None, search_fields=None):
	fields = []
        
	def matches(project):
		if search and search_fields:
			for search_field in search_fields:
				if search.lower() in str(project[search_field]).lower():
					return True
				
		if search and not search_fields:
			found = False
		
			for value in project.values():
				if search.lower() in str(value).lower():
					found = True
					return True
					
			if not found:
				return False

		if techniques:
			for tech in techniques:
				if not tech in project["techniques_used"]:
					return False
				
			else:
				return True
		
		if not search and not search_fields and not techniques:
			return True

		return False

	for project in db:
		if matches(project):
			fields.append(project)
	
	if sort_order == "desc":
		fields = sorted(fields, key=lambda x: x[sort_by], reverse = True)
                
	elif sort_order == "asc":
		fields = sorted(fields, key=lambda x: x[sort_by])

	return fields

#searches and returns a list of all techniques used
def get_techniques(db):
	slist = []
	for project in db:
		for technique in project["techniques_used"]:
			if technique in slist:
				pass
		   	     
			else:
				slist.append(technique)
				slist.sort()
	return slist

#searches for all projects that contain techniques and returns them in lists in dictionary
def get_technique_stats(db):
	all_techniques = get_techniques(db)
	dic = {}
	for techniques in all_techniques:
 		dic[techniques] = []
	
	for techniques in all_techniques:
		for project in db:
			if techniques in project["techniques_used"]:
				dic[techniques].append({"id":project["project_id"],"name":project["project_name"]})

	return dic

#db = load("data.json")

