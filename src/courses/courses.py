import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class Courses:
    def __init__(self,fullstack,data_analysis,big_data):
        self._fullstack = fullstack
        self._data_analysis = data_analysis
        self._big_data = big_data

    # setter and Gatter method using here
    def set_fullstack(self, fullstack1):
        self._fullstack = fullstack1
    def get_fullstack(self):
        return self._fullstack

    def set_data_analysis(self, data_analysis):
        self._data_analysis = data_analysis
    def get_data_analysis(self):
        return self._data_analysis

    def set_big_data(self,big_data):
        self._big_data = big_data
    def get_big_data(self):
        return self._big_data
#
# def course_fees(Course, category):
#     logging.info("Course fees are structured here:")
#
#
#     """Course structured will provide fees after discount as per your required, """
#     """Here is the category Handicap/Alumni/Army"""
#
#     a = {"fullstack": 17770, "data analysis":12000, "big data": 11000 }
#     b = {"Ews":12, "Handicap":14,"Alumni":25,"Normal":5,"Army":40}
#     c = str(course)
#     d = str(category).upper()
#     try:
#         for i in a:
#             if i == c:
#                 r = a[i]
#                 break
#         for j in b:
#             if j == d:
#                 f = b[j]
#                 print("fees for {} program for others is {} INR." .format(c , r))
#             else:
#                 pass
#             print("This offer is only for you.Pay : {} INR.".format(dis_fees))
#     except Exception as e:
#         print("please enter correct program and category details")
