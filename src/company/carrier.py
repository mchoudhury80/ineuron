import logging
from ineuron import Ineuron
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

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
        try:
            for job in job_list:
                if job.get_job_type() == job_type:
                    list.append(job)
        except Exception as e:
            logging.exception("unable to filter" + "\n" + str(e))
        return list

    def apply(self,job):
        print(self.ineuron_details())
        logging.info("You have successfully applied in the company: %s ",job.get_company_name() ," for the position of:", job.get_title())
        logging.info( "Thanks from Ineuron, about us:", self.get_about_us(), "our Address:", self.get_contact_us(),"Your application Satus " "\n",self.get_application_status())

    #Method overloading/Polymorphism
    def inenurn_details(self):
        logging.info("Ineuron is a great company to work and grow. Also you will get 100% job guarantee. ")
