import json
import operator

def load(filename):
	try:
		with open(filename, "r") as f:
			projects = list(json.load(f))
			projects.sort(key=operator.itemgetter("project_id"))
		
			return projects
	
	except:
		return None

def get_project_count(db):
	print(len(db))
	return len(db)

def get_project(db, id):
	for project in db:
		if project["project_id"] == id:
			return project
	
	return None

def search(db, sort_by=None, sort_order=None, techniques=None, search=None, search_fields=None):
        fields = []
        
        def matches(project):
                if search_fields and search:
                        found = False
                        for value in range(len(search_fields)):
                                if search in str(value):
                                        found = True

                if search and not search_fields:
                        found = False
                        for value in project.values():
                                if search in str(value):
                                        found = True

                        if not found:
                                return False

                if techniques:
                        found = False
                        for tech in techniques:
                                if tech not in project["techniques_used"]:
                                        return False        

                return True

        for project in db:
                if matches(project):
                        fields.append(project)
        
        if sort_by == None:
                return fields
        
        if sort_order == "desc":
                fields = sorted(fields, key=lambda x: x[sort_by], reverse = True)
                
        elif sort_order == "asc":
                fields = sorted(fields, key=lambda x: x[sort_by])

        return fields

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
