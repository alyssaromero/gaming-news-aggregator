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
    ### Base Case ... First Run ... Files DNE ###
    if (len(os.listdir("spiders/spider_files")) == 0):
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        data = {}
        data["utc_old"] = []
        data["utc_old"].append(
            {'FullTime': utc_now,
             'Day': utc_now.day,
             'Month': utc_now.month,
             'Year': utc_now.year,
             'Hour': utc_now.hour,
             'Minute': utc_now.minute,
             'Second': utc_now.second
             }
        )
        with open("spiders/spider_files/time.json", "w") as file:
            json.dump(data, file)
        spiders = ['gameInformer', 'gamesRadar', 'polygon']
        for s in spiders:
            subprocess.check_output(['scrapy', 'crawl', s, '-o', 'spiders/spider_files/'+s+'.json'])
    else:
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        with open("spiders/spider_files/time.json") as json_file:
            jsontime = json.load(json_file)
            hour = jsontime['utc_old'][0]['Hour']
            if (utc_now.hour - hour >= 5):
                spiders = ['gameInformer', 'gamesRadar', 'polygon']

                ## Remove Previous JSON files and Update ##
                for s in spiders:
                    os.remove('spiders/' + s + '.json')
                for s in spiders:
                    subprocess.check_output(['scrapy', 'crawl', s, '-o', 'spiders/spider_files/'+s+'.json'])
                os.remove('spiders/time.json')

                ## Edit the Timestamp for JSON file uploads ##
                data = {}
                data["utc_old"] = []
                data["utc_old"].append(
                    {'FullTime': utc_now,
                     'Day': utc_now.day,
                     'Month': utc_now.month,
                     'Year': utc_now.year,
                     'Hour': utc_now.hour,
                     'Minute': utc_now.minute,
                     'Second': utc_now.second
                     }
                )
                with open("spiders/spider_files/time.json", "w") as file:
                    json.dump(data, file)

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

    return render_template("home.html", gameInformer=gameInformer, gamesRadar=gamesRadar, polygon=polygon, len=20)

if __name__ == "__main__":
    app.run(debug=True)
