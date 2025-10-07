# AUthor: Justin Alvey
# Date Created: 10/7/25
# Date Last Modified: 10/7/25

# The purpose of this project is to web scrape data from leading job posting boards and gather information on the leading skills that employers are looking for

# Are welders living large in Cleveland?
# What skills can someone learn to break into IT?
# We can answer these sorts of questions and more!

# Actual coding:
# I will start with using data entry, then will convert to sql. But long term web-scraping is the plan and to convert the useful data to sql.

class JobPosting():
	def __init__():
		self.title=""
		self.company=""
		self.description=""
		self.skills=[]
	def get_title(self):
		return self.title
	def get_company_name(self):
		return self.company
	def get_description(self):
		return self.description
	def get_skills(self):
		return self.skills
	def set_title(self,tle):
		self.company = tle
	def set_company_name(self,cmp):
		self.company = cmp
	def set_description(self,desc):
		self.description = desc
	def add_skill_to_list(self,skill):
		self.skills.append(skill)


