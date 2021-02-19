
import smtplib, requests, time, datetime

def send_emails(num_locations):
  gmail_user = 'email@gmail.com'
  gmail_password = 'P@ssw0rd'

  sent_from = gmail_user
  send_to = ['email@gmail.com']
  subject = f"Availability at {num_locations} locations!"
  body = f"Availability at {num_locations} locations! Go to https://curative.com/search#9/42.5751/-70.9301 for more info."

  email_text = """\
  From: %s
  To: %s
  Subject: %s

  %s
  """ % (sent_from, ", ".join(send_to), subject, body)

  try:
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.ehlo()
      server.login(gmail_user, gmail_password)
      server.sendmail(sent_from, send_to, email_text)
      server.close()
  except:
      print('Something went wrong sending email')

def get_danvers():
  try:
    danvers_url = 'https://labtools.curativeinc.com/api/v1/testing_sites/get_by_geolocation?h3=882a300c35fffff&radius=108.53039674302454'
    r = requests.get(danvers_url)
    return r.json()
  except:
    print('Something went wrong pulling data')
    return []

def check_availability():
  results_json = get_danvers()
  num_availability = len(results_json)
  if num_availability > 0:
    send_emails(num_availability)

def do_this_thing_forever(sec_between_check):
  while True:
    check_availability()
    print(f"Completed check at {datetime.datetime.today()}")
    # Code executed here
    time.sleep(sec_between_check)

sec_between_check = 60
do_this_thing_forever(sec_between_check)
