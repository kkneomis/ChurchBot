import atexit
from datetime import datetime
from apscheduler.scheduler import Scheduler

from Jarvis import Jarvis
from flask import Flask

app = Flask(__name__)

jarvis = Jarvis(app.logger)

cron = Scheduler(daemon=True)
# Explicitly kick off the background thread
cron.start()
now = str(datetime.now())
print "Starting bot......"
print "TIme now is", now


@cron.cron_schedule(day_of_week='sun', hour=18 , minute=11)
def job_function():
    # This happens every Sunday at 9:30 am central time
    message = "Good morning class, here is the hangout link!"
    print "Sending link....."
    link = "Test, please ignore this"
    #link = "https://hangouts.google.com/hangouts/_/cfrz4i5iuzhfddbwoos23ji6xee"
    jarvis.postLink(link)
    print "Link %s sent at %s" % (link, str(datetime.now()))


@cron.cron_schedule(day='1st mon', hour=1, minute=00)
def job_function():
    # This happens on the last Sunday of every month at 7:00pm central time
    message = "Good evening class, please use this link to join the hangout at 7:00pm"
    link = "https://hangouts.google.com/hangouts/_/cfrz4i5iuzhfddbwoos23ji6xee"
    jarvis.postLink(link)
    print "Link %s sent at %s" % (link, str(datetime.now()))



# Shutdown your cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == '__main__':
    app.run()  
    
    
 
