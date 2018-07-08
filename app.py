import atexit
from datetime import datetime
from apscheduler.scheduler import Scheduler

from models import Bot
from flask import Flask, render_template, url_for, flash, \
            redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "#knfewfnNJ*#@#J#KN"

jarvis = Bot(app.logger, "9d2619675f5521bb6ffba65270")

cron = Scheduler(daemon=True)
# Explicitly kick off the background thread
cron.start()
now = str(datetime.now())

print "Starting bot......"
print "Time now is", now


def send_link():
    # This happens every Sunday at 9:30 am central time
    message = "Good morning class, here is the hangout link for today!"
    print "Sending link....."
    link = "https://hangouts.google.com/hangouts/_/cfrz4i5iuzhfddbwoos23ji6xee"
    jarvis.speak(link)
    print "Link %s sent at %s" % (link, str(datetime.now()))


# This happens every Sunday at 9:30 am central time
cron.add_cron_job(send_link, day_of_week='sun', hour=14 , minute=25)
# This happens on the last Sunday of every month at 7:00pm central time
cron.add_cron_job(send_link, day='1st mon', hour=1, minute=00)
    
@app.route("/")
def start():
    running_jobs = cron.get_jobs()
    return render_template("index.html", running_jobs = running_jobs)


@app.route("/sendmessage", methods=["GET", "POST"])
def sendMessage():
    message = request.form.get('message', 'Oops there was no messasge')
    password = request.form.get('password', 'Invalid')
    if password == "BTSquad":
        jarvis.speak(message)
        flash("Message Delivered")
    else:
        flash("invalid password")
    return redirect(url_for('start'))


# Shutdown your cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == '__main__':
    app.run()  
    
    
 
