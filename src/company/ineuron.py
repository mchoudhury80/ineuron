import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
class Ineuron:
    """This assignment is an Ineuron project using OOPS concept: This part is data encapulation"""
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
        logging.info( "It is a great company to work and grow.")