import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

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