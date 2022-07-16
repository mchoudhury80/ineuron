class Ineuron:
    """This assignment is an ineuron priject using OOPS concept: This part is data encapulation"""
    # All getter and setter are part of encapsulation
    def __init__(self, about_us, contact_us,terms_and_condition, job_assistance):
        self._contact_us = contact_us
        self._about_us = about_us
        self._contact_us = contact_us
        self._terms_and_condition = terms_and_condition
        self._job_assistance = job_assistance


    #setter method
    def set_about_us(self,x):
        self._about_us = x

    #getter method
    def get_about_us(self):
        return self._about_us

    #setter method
    def set_contact_us(self,y):
        self._contact_us = y

    #getter method
    def get_contact_us(self):
        return self._contact_us

    def set_terms_and_condition(self,t):
        self._terms_and_condition = t
    def get_terms_and_condition(self):
        return self._terms_and_condition

    def set_job_assistance(self,j):
        self._job_assistance = j
    def get_job_assistance(self):
        return self._job_assistance

    def inenurn_details(self):
        return "It is a great company to work and grow"

class Jobs:
    """here is another class"""

    def __init__(self, stream, city, job_type, title, skill, experience, company_name ):
        self._stream = stream
        self._city = city
        self._job_type = job_type
        self._title = title
        self._skill = skill
        self._experience = experience
        self._company_name = company_name

    #setter and Gatter method using here
    def set_stream(self,stream1):
        self._stream = stream1
    def get_stream(self):
        return self._stream

    def set_city(self,city1):
        self._city =city1
    def get_city(self):
        return self._city

    def set_job_type(self,job1):
        self._job_type = job1
    def get_job_type(self):
        return self._job_type

    def set_title(self,title1):
        self._title = title1
    def get_title(self):
        return self._title

    def set_skill(self,skill1):
        self._skill = skill1
    def get_skill(self):
        return self._skill

    def set_experience(self,experience1):
        self._experience = experience1
    def get_experience(self):
        return self._experience

    def set_company_name(self,company_name1):
        self._company_name = company_name1
    def get_company_name(self):
        return self._company_name
#Inerheritance
class Carrier(Ineuron):

    def __init__(self,about_us, contact_us,terms_and_condition, job_assistance, application_status):
        self._application_status = application_status
        Ineuron.__init__(self,about_us, contact_us,terms_and_condition, job_assistance)
    def set_application_status(self,application_status):
        self._application_status = application_status

    def get_application_status(self):
        return self._application_status

    """class inharitance is applyed here"""
    def filter(self,job_type,job_list):
        list =[]
        for job in job_list:
            if job.get_job_type() == job_type:
                list.append(job)
        return list

    def apply(self,job):
        print(self.inenurn_details())
        print("You have successfully applied in the company ",job.get_company_name() ," for the position of:", job.get_title())
        print( "Thanks from Ineuran, about us:", self.get_about_us(), "our Address:", self.get_contact_us(),"Your application Satus ",self.get_application_status())

    #Method overloading/Polymorphism
    def inenurn_details(self):
        return "Ineuran is a great company to work and grow. Also you will get 100% job guarantee. "

#"Its is educational company", "Bangalore","Terms & condition", "Fully Supported","
r = Carrier("Its is educational company", "Bangalore","Terms & condition", "Fully Supported","pending")
j1 = Jobs("Developer", "Pune", "full_time", "Software Engineer", "Java, Python", "Experienced", "Infosys")
j2 = Jobs("Testing", "Mumbai", "part_time", "Test Engineer", "Automation", "ETL", "TCS")
list = []
list.append(j1)
list.append(j2)

jobs = r.filter("full_time",list)
for  job in jobs:
    r.apply(job)




