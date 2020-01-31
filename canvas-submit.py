# Import the Canvas class
from canvasapi import Canvas
from canvasapi.assignment import Assignment
from canvasapi.requester import Requester
import config #please don't ever show anyone your key. they'd be able to submit on your behalf

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../submission.zip')

#This is provided with NO WARRANTY WHATSOEVER.
#1) If your computer explodes, I take no responsibility.
#2) If your dog bites you and your cat leaves you, it's not my problem.
#3) If you use this code and all your stuff uploads to my private server, it's deeply unintentional.
#4) In all honesty, I'd be tickled if it helped anyone at all.

### UNCOMMENT AS NECESSARY FOR EACH 593 ASSIGNMENT
#HW01 Part01
ASSIGNMENT_ID = 7454616
#HW01 Part02
# ASSIGNMENT_ID = 7454618
#HW01 Part03
#ASSIGNMENT_ID = 7454620
#HW02
#ASSIGNMENT_ID = 7454621
#HW03
# ASSIGNMENT_ID = 7454622
#HW04
# ASSIGNMENT_ID = 7454623

### You may wish to change this
# your file name of choice
FILE = "submission.zip"
### Everything below is unlikely to change

# Canvas API URL
API_URL = "https://canvas.upenn.edu/api/v1/"
# Canvas API key
API_KEY = config.API_KEY
#HW01 Part01
ASSIGNMENT_ID = 7454616
#596 course id
COURSE_ID = 1488863

# Initialize a new Requester
requester = Requester(API_URL, API_KEY)

# Make an Assignment for this course and this assignment
assignment = Assignment(requester, {'course_id': COURSE_ID, 'id': ASSIGNMENT_ID})
# print(assignment.to_json())

#if you go into the plain REST api, you'll see the python library is combining two steps:
#   1) upload a file named whatever you named yours
#   2) submit the assignment using the id of canvas id for the uploaded file in 1
response = assignment.submit({
    'submission_type': 'online_upload',
    }, filename
)

print(response)
print("nothing eventful happened but you should always check the site")
