import requests
from bs4 import BeautifulSoup
import smtplib
import time
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

now = datetime.datetime.now()

connect = ''



def extract_jobs_from_dev_bg(url,city, seniority):
    print('Extracting Jobs from DEV-BG...... $$ fingers crossed $$')
    time.sleep(1)
    print(f'Searching for jobs in: {city} -Level:{seniority}')
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
def get_city_from_input(input_num):
    cities = {
        '1': 'sofiya',
        '2': 'varna',
        '3': 'remote'
    }
    return cities.get(input_num, 'remote')  # Default to 'remote' if input is not valid


def get_seniority_from_input(input_num):
    seniority_levels = {
        '1': 'intern',
        '2': 'mid',
        '3': 'senior'
    }
    return seniority_levels.get(input_num, 'intern')  # Default to 'intern' if input is not valid


city_input = input('Enter city number (1 for Sofia, 2 for Varna, 3 for Remote): ')
city = get_city_from_input(city_input)

seniority_input = input('Enter seniority number (1 for Intern/Junior, 2 for Mid, 3 for Senior): ')
seniority = get_seniority_from_input(seniority_input)

url = f'https://dev.bg/company/jobs/python/?_job_location={city}&_seniority={seniority}'
cnt = extract_jobs_from_dev_bg(url, city, seniority)

connect += cnt
connect += ('-----------')
connect += ('End of Message')

print(connect)



