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


"""Titta på if search and search_fields"""
def search(db, sort_by='start_date', sort_order='desc', techniques=None, search=None, search_fields=None):
        fields = []
        
        def matches(project):
                if search and search_fields:
                        found = False
                        for value in project.items():
                                if search == value:
                                        found = True
                                
                                
                if search and not search_fields:
                        found = False
                        for value in project.values():
                                if search == value:
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


"""Resultat: course_name: HOHO ska ej inkluderas."""
#[{'start_date': '2009-09-08', 'short_description': 'no', 'course_name': 'OKÄNT', 'long_description': 'no no no', 'group_size': 6, 'academic_credits': 'WUT?', 'lulz_had': 'medium', 'external_link': 'YY', 'small_image': 'X', 'techniques_used': ['ada', 'python'], 'project_name': '2007', 'course_id': 'TDP003', 'end_date': '2009-09-09', 'project_id': 2, 'big_image': 'XXX'}, 

#{'start_date': '2009-09-07', 'short_description': 'no', 'course_name': 'OKÄNT', 'long_description': 'no no no', 'group_size': 4, 'academic_credits': 'WUT?', 'lulz_had': 'few', 'external_link': 'YY', 'small_image': 'X', 'techniques_used': ['c++', 'csv', 'python'], 'project_name': 'NEJ', 'course_id': 'TDP003', 'end_date': '2009-09-08', 'project_id': 3, 'big_image': 'XXX'}, 

#{'start_date': '2009-09-06', 'short_description': 'no', 'course_name': 'HOHO', 'long_description': 'no no no', 'group_size': 8, 'academic_credits': 'WUT?', 'lulz_had': 'over 9000', 'external_link': 'YY', 'small_image': 'X', 'techniques_used': [], 'project_name': ',', 'course_id': ' "', 'end_date': '2009-09-07', 'project_id': 4, 'big_image': 'XXX'}, 

#{'start_date': '2009-09-05', 'short_description': 'no', 'course_name': 'OKÄNT', 'long_description': 'no no no', 'group_size': 2, 'academic_credits': 'WUT?', 'lulz_had': 'many', 'external_link': 'YY', 'small_image': 'X', 'techniques_used': ['python'], 'project_name': 'python data-module test script', 'course_id': 'TDP003', 'end_date': '2009-09-06', 'project_id': 1, 'big_image': 'XXX'}]
