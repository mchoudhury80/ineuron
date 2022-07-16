import logging
from company.carrier import Carrier
from jobs.jobs import Jobs
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
#"Its is educational company", "Bangalore","Terms & condition", "Fully Supported","
r = Carrier("Its is educational company", "Bangalore","Terms & condition", "Fully Supported","pending")
j1 = Jobs("Developer", "Pune", "full_time", "Software Engineer", "Java, Python", "Experienced", "Infosys")
j2 = Jobs("Testing", "Mumbai", "part_time", "Test Engineer", "Automation", "ETL", "TCS")
list = []
list.append(j1)
list.append(j2)

jobs = r.filter("full_time",list)
for job in jobs:
    r.apply(job)


