from flask import Flask, render_template, url_for, json
import subprocess
from DateTime import DateTime
import pytz
from pytz import timezone, datetime
import os
from os import listdir

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    """
        Run spider in another process and store items in files. Then issue
        command: scrapy crawl <nameOfSpider> -o spiders/<nameOfSpider>.json
        Wait for this command to finish, and read output to client
    """
    """
        should i just write all articles to single json file?
        grab UTC time, and insert into single json file. Each time app is called,
            check if currnt UTC is 6 hours ahead of previous UTC...
            if True: delete json file, insert current UTC in JSON file and rerun spiders
            if False: reuse old articles
    """

    """
    spiders = ['gamasutra', 'gameInformer', 'gamesRadar', 'polygon']
    for s in spiders:
        subprocess.check_output(['scrapy', 'crawl', s, '-o', 'spiders/spider_files/'+s+'.json'])
    """

    ### Base Case ... First Run ... Files DNE ###
    if (len(os.listdir("spiders/spider_files")) == 0):
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        data = {}
        data["utc_old"] = []
        data["utc_old"].append(
            {'Day': utc_now.day,
             'Month': utc_now.month,
             'Year': utc_now.year,
             'Hour': utc_now.hour,
             'Minute': utc_now.minute,
             'Second': utc_now.second
             }
        )
        #data["utc_old"].append(pytz.utc.localize(datetime.datetime.utcnow()))
        with open("spiders/spider_files/time.json", "w") as file:
            json.dump(data, file)
        spiders = ['gamasutra', 'gameInformer', 'gamesRadar', 'polygon']
        for s in spiders:
            subprocess.check_output(['scrapy', 'crawl', s, '-o', 'spiders/spider_files/'+s+'.json'])
    else:
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        with open("spiders/spider_files/time.json") as json_file:
            jsontime = json.load(json_file)
            



    #os.remove("spiders/gamesRadar.json") #to remove json file...this works
    """
    gamasutra = []
    with open('spiders/spider_files/gamasutra.json') as json_file:
        data = json.load(json_file)
        gamasutra.append(data)
    gameInformer = []
    with open('spiders/spider_files/gameInformer.json') as json_file:
        data = json.load(json_file)
        gameInformer.append(data)
    gamesRadar = []
    with open('spiders/spider_files/gamesRadar.json') as json_file:
        data = json.load(json_file)
        gamesRadar.append(data)
    polygon = []
    with open('spiders/spider_files/polygon.json') as json_file:
        data = json.load(json_file)
        polygon.append(data)
    """
    #return render_template("home.html", gamasutra=gamasutra, gameInformer=gameInformer, gamesRadar=gamesRadar, polygon=polygon, len=20)
    return render_template("index.html", utc_now=utc_now, time=jsontime, hour=jsonhour)

if __name__ == "__main__":
    app.run(debug=True)
