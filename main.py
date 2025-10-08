# AUthor: Justin Alvey
# Date Created: 10/7/25
# Date Last Modified: 10/7/25

# The purpose of this project is to web scrape data from leading job posting boards and gather information on the leading skills that employers are looking for

# Are welders living large in Cleveland?
# What skills can someone learn to break into IT?
# We can answer these sorts of questions and more!

# Actual coding:
# I will start with using data entry. But long term web-scraping is the plan and to convert the useful data to sql.

class JobPosting():
	def __init__(self):
		self.title=""
		self.company=""
		self.description=""
		self.skills=[]
		self.highlight=""
		self.salary =0
		self.date=""
	def get_title(self):
		return self.title
	def get_company_name(self):
		return self.company
	def get_description(self):
		return self.description
	def get_skills(self):
		return self.skills
	def get_highlight(self):
		return self.highlight
	def get_salary(self):
		return self.salary
	def set_title(self,tle):
		self.company = tle
	def set_company_name(self,cmp):
		self.company = cmp
	def set_description(self,desc):
		self.description = desc
	def add_skill_to_list(self,skill):
		self.skills.append(skill)
	def set_highlight(self,hi):
		self.highlight = hi
	def set_salary(self,sl):
		self.salary = sl

job1 = JobPosting()
job1.set_title("Principal Software Engineer")
job1.set_company_name("Tyler Technologies")
job1.add_skill_to_list("Software deployment")
job1.add_skill_to_list("Scalable systems")
job1.add_skill_to_list("Socalability")
job1.add_skill_to_list("High availability")
job1.add_skill_to_list("High availability architecture")
job1.add_skill_to_list("Docker")
job1.add_skill_to_list("Agile software development")
job1.add_skill_to_list("Automation")
job1.add_skill_to_list("Continuous Delivery")
job1.set_highlight("Mentor and coach engineers, providing opportunities for growth and ensuring excellence in software engineering practices.Engage in high-level strategic discussions while also contributing to technical execution (80% hands-on coding, 20% strategy).")

job2 = JobPosting()
job2.set_title("Full Stack Developer")
job2.set_company_name("Burnout Brands")
job2.add_skill_to_list("Scalability")

job3 = JobPosting()
job3.set_title("")
job3.set_company_name("Software Developer")
job3.add_skill_to_list("TherapyNotes.com")

job4 = JobPosting()
job4.set_title("Sr. QNXT Developer")
job4.set_company_name("Compest Solutions Inc")
job4.add_skill_to_list("")

job5 = JobPosting()
job5.set_title("Senior Python Developer")
job5.set_company_name("Compest Solutions Inc")
job5.add_skill_to_list("")
