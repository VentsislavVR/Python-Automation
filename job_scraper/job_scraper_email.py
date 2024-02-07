import requests
from bs4 import BeautifulSoup
import smtplib
import time
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

now = datetime.datetime.now()

connect = ''



def extract_jobs_from_dev_bg(url):
    print('Extracting Jobs from DEV-BG...... $$ fingers crossed $$')
    time.sleep(1)
    print(f'Searching for jobs in: Varna -Level: Intern / Junior')
    cnt = ''
    cnt += ('<b>Jobs:</b>\n' + '<br>' + '-' * 50 + '<br>\n')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    job_listings = soup.find_all('div', class_='title-date-wrap')
    cnt += f'Number of jobs found: {len(job_listings)}\n'  # Add job count here

    for i, tag in enumerate(job_listings):
        cnt += tag.text.strip().replace('\n', '') + " "
        if i == 50:
            break

    return cnt


connect = ''


url = f'https://dev.bg/company/jobs/python/?_job_location=varna&_seniority=intern'
cnt = extract_jobs_from_dev_bg(url)

connect += cnt
connect += ('<br>-------<br>')
connect += ('<br><br>End of Message')
# print(connect)
print('Composing email...')

SERVER = os.getenv('SERVER') # Gmail SMTP server
PORT = os.getenv('PORT')
FROM = os.getenv('FROM')  # Sender's email address
TO =os.getenv('TO')  # Receiver's email address
PASS = os.getenv('PASS')  # Sender's email password

msg = MIMEMultipart()
msg['Subject'] = f'Python Jobs update - Varna - Level: Intern from {now.strftime("%Y-%m-%d %H:%M:%S")}'
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(connect, 'html'))

print('Initiating email server...')
server = smtplib.SMTP(SERVER, int(PORT))
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email sent!')
server.quit()

