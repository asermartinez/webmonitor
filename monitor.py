import os
import smtplib
import requests
# import logging

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_TO = os.environ.get('EMAIL_TO')

# logging.basicConfig(filename='PATH_TO_DESIRED_LOG_FILE',
#                     level=logging.INFO,
#                     format='%(asctime)s:%(levelname)s:%(message)s')


def notify_user():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'YOUR SITE IS DOWN!'
        body = 'Make sure the server restarted and it is back up'
        msg = f'Subject: {subject}\n\n{body}'

        # logging.info('Sending Email...')
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_TO, msg)


# def reboot_server():
#     client = LinodeClient(LINODE_TOKEN)
#     my_server = client.load(Instance, 376715)
#     my_server.reboot()
    # logging.info('Attempting to reboot server...')


def check_site(site):
    try:
        r = requests.get(site, timeout=5)

        if r.status_code != 200:
            # logging.info('Website is DOWN!')
            print("Server {} is Down!".format(site))
            print("Email sent!")
            notify_user()
            # reboot_server()
        else:
            print("Server {} OK".format(site))
            # logging.info('Website is UP')
    except Exception as e:
        # logging.info('Website is DOWN!')
        print("Exception: {}".format(e))
        # notify_user()
        # reboot_server()


site1 = "https://metar.es/"
site2 = "http://helimer.es/"
check_site(site1)
check_site(site2)
