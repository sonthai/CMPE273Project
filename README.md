# CMPE273Project
## Package dependency requirements
These libabry can be installed into the system or virtualenv
#### Installing slackclient
- pip install slackclient
- Slack tutorial: https://www.fullstackpython.com/blog/build-first-slack-bot-python.html

Follow the tutorial to obtain SLACK_BOT_TOKEN and BOT_ID then put them in credentials.cfg file

#### Installing quepy and nltk
- pip install quepy
- quepy --version
- quepy nltkdata < specify path for directory to store nltk data>
- Quepy installing instruction: http://quepy.readthedocs.io/en/latest/installation.html
- nltk_data can be downloaded at https://drive.google.com/a/sjsu.edu/file/d/0BxzGNFHMxQu0S1ZOX1VudzhYU2M/view?usp=sharing

## Tools and teachnologies
- Python 2.7
- Slack API
- Quepy framework
- python-lambda librarty
- NLTK library
- DynamoDB, API Gateway, AWS Lambda

####Architecture of the system we implemented:

![alt text](https://raw.githubusercontent.com/sonthai/CMPE273Project/master/System%20Architect.png)
