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

print "Starting bot......"

@cron.cron_schedule(day_of_week='mon', hour=3 , minute=30)
def job_function():
    # Do your work here
    message = "Good morning class, here is the hangout link!"
    link = "https://hangouts.google.com/hangouts/_/cfrz4i5iuzhfddbwoos23ji6xee"
    jarvis.postLink(link)
    print "Link %s sent at %s" % (link, str(datetime.now()))



# Shutdown your cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == '__main__':
    app.run()  
    
    
 