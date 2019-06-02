
from flask import Flask, jsonify, render_template, request, flash, redirect


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc,select

import pandas as pd
import numpy as np



engine = create_engine("sqlite:///DataSets/nfl.db",connect_args={'check_same_thread': False})


Base = automap_base()

Base.prepare(engine, reflect=True)

data_bar = Base.classes.dataForBarGraph

session = Session(engine)

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("myindex.html")

@app.route('/names')
def names():
    """Return a list of sample names."""

    stmt = session.query(data_bar).statement
    df = pd.read_sql_query(stmt, session.bind)
    df.set_index('index', inplace=True)
    
    return jsonify(list(df.Year))

@app.route('/otu')
def otu():
    """Return a list of OTU descriptions."""
    results = session.query(OTU.lowest_taxonomic_unit_found).all()

    otu_list = list(np.ravel(results))
    return jsonify(otu_list)

@app.route('/metadata/<year>')
def sample_metadata(year):
    """Return the MetaData for a given Year."""
    sel = [data_bar.avg_Humidity, data_bar.avg_Temp,
           data_bar.avg_Wind_Chill, data_bar.avg_Wind_Mph]

    results = session.query(*sel).\
        filter(data_bar.Year == year).all()

    game_metadata = {}
    for result in results:
        game_metadata['Avg Humidity'] = result[0]
        game_metadata['Avg. Temp'] = result[1]
        game_metadata['Avg. Wind Chill'] = result[2]
        game_metadata['Avg. Wind Mph'] = result[3]
              
        

    return jsonify(game_metadata)
    
@app.route('/homedata/<year>')
def sample_homedata(year):
    """Return the homeData for a given Year."""
    sel = [data_bar.homeTeam_winsWith_belowAvg_Humidity, data_bar.homeTeam_winsWith_belowAvg_Temp,
           data_bar.homeTeam_winsWith_belowAvg_WindChill, data_bar.homeTeam_winsWith_belowAvg_WindMph,
           data_bar.homeTeam_winsWith_aboveAvg_Humidity, data_bar.homeTeam_winsWith_aboveAvg_Temp,
           data_bar.homeTeam_winsWith_aboveAvg_WindChill, data_bar.homeTeam_winsWith_aboveAvg_WindMph]

    results = session.query(*sel).\
        filter(data_bar.Year == year).all()

    game_homedata = {}
    for result in results:
        game_homedata['Homes Wins Count With Below Avg Humidity'] = result[0]
        game_homedata['Homes Wins Count With Below Avg Temp'] = result[1]
        game_homedata['Homes Wins Count With Below Avg Wind Chill'] = result[2]
        game_homedata['Homes Wins Count With Below Avg Wind Mph'] = result[3]
        game_homedata['Homes Wins Count With Above Avg Humidity'] = result[4]
        game_homedata['Homes Wins Count With Above Avg Temp'] = result[5]
        game_homedata['Homes Wins Count With Above Avg Wind Chill'] = result[6]
        game_homedata['Homes Wins Count With Above Avg Wind Mph'] = result[7] 
        

    return jsonify(result)  

@app.route('/awaydata/<year>')
def sample_awaydata(year):
    """Return the awayData for a given Year."""
    sel = [data_bar.awayTeam_winsWith_belowAvg_Humidity, data_bar.awayTeam_winsWith_belowAvg_Temp,
           data_bar.awayTeam_winsWith_belowAvg_WindChill, data_bar.awayTeam_winsWith_belowAvg_WindMph,
           data_bar.awayTeam_winsWith_aboveAvg_Humidity, data_bar.awayTeam_winsWith_aboveAvg_Temp,
           data_bar.awayTeam_winsWith_aboveAvg_WindChill, data_bar.awayTeam_winsWith_aboveAvg_WindMph]

    results = session.query(*sel).\
        filter(data_bar.Year == year).all()

    game_awaydata = {}
    for result in results:
        game_awaydata['aways Wins Count With Below Avg Humidity'] = result[0]
        game_awaydata['aways Wins Count With Below Avg Temp'] = result[1]
        game_awaydata['aways Wins Count With Below Avg Wind Chill'] = result[2]
        game_awaydata['aways Wins Count With Below Avg Wind Mph'] = result[3]
        game_awaydata['aways Wins Count With Above Avg Humidity'] = result[4]
        game_awaydata['aways Wins Count With Above Avg Temp'] = result[5]
        game_awaydata['aways Wins Count With Above Avg Wind Chill'] = result[6]
        game_awaydata['aways Wins Count With Above Avg Wind Mph'] = result[7] 
        

    return jsonify(result)
    
@app.route('/entiredata/<year>')
def sample_entiredata(year):
    """Return the entireData for a given Year."""
    sel = [data_bar.avg_Humidity, data_bar.avg_Temp,
           data_bar.avg_Wind_Chill, data_bar.avg_Wind_Mph,
           data_bar.homeTeam_winsWith_belowAvg_Humidity, data_bar.homeTeam_winsWith_belowAvg_Temp,
           data_bar.homeTeam_winsWith_belowAvg_WindChill, data_bar.homeTeam_winsWith_belowAvg_WindMph,
           data_bar.homeTeam_winsWith_aboveAvg_Humidity, data_bar.homeTeam_winsWith_aboveAvg_Temp,
           data_bar.homeTeam_winsWith_aboveAvg_WindChill, data_bar.homeTeam_winsWith_aboveAvg_WindMph,
           data_bar.awayTeam_winsWith_belowAvg_Humidity, data_bar.awayTeam_winsWith_belowAvg_Temp,
           data_bar.awayTeam_winsWith_belowAvg_WindChill, data_bar.awayTeam_winsWith_belowAvg_WindMph,
           data_bar.awayTeam_winsWith_aboveAvg_Humidity, data_bar.awayTeam_winsWith_aboveAvg_Temp,
           data_bar.awayTeam_winsWith_aboveAvg_WindChill, data_bar.awayTeam_winsWith_aboveAvg_WindMph]

    results = session.query(*sel).\
        filter(data_bar.Year == year).all()

    game_entiredata = {}
    for result in results:
        game_entiredata['Avg Humidity'] = result[0]
        game_entiredata['Avg. Temp'] = result[1]
        game_entiredata['Avg. Wind Chill'] = result[2]
        game_entiredata['Avg. Wind Mph'] = result[3]
        game_entiredata['Home Wins Count With Below Avg Humidity'] = result[4]
        game_entiredata['Home Wins Count With Below Avg Temp'] = result[5]
        game_entiredata['Home Wins Count With Below Avg Wind Chill'] = result[6]
        game_entiredata['Home Wins Count With Below Avg Wind Mph'] = result[7]
        game_entiredata['Home Wins Count With Above Avg Humidity'] = result[8]
        game_entiredata['Home Wins Count With Above Avg Temp'] = result[9]
        game_entiredata['Home Wins Count With Above Avg Wind Chill'] = result[10]
        game_entiredata['Home Wins Count With Above Avg Wind Mph'] = result[11]
        game_entiredata['Away Wins Count With Below Avg Humidity'] = result[12]
        game_entiredata['Away Wins Count With Below Avg Temp'] = result[13]
        game_entiredata['Away Wins Count With Below Avg Wind Chill'] = result[14]
        game_entiredata['Away Wins Count With Below Avg Wind Mph'] = result[15]
        game_entiredata['Away Wins Count With Above Avg Humidity'] = result[16]
        game_entiredata['Away Wins Count With Above Avg Temp'] = result[17]
        game_entiredata['Away Wins Count With Above Avg Wind Chill'] = result[18]
        game_entiredata['Away Wins Count With Above Avg Wind Mph'] = result[19]
              
        

    return jsonify(game_entiredata)
    
@app.route('/wfreq/<sample>')
def sample_wfreq(sample):
    """Return the Weekly Washing Frequency as a number."""

    results = session.query(Samples_Metadata.WFREQ).\
        filter(Samples_Metadata.SAMPLEID == sample[3:]).all()
    wfreq = np.ravel(results)

    return jsonify(int(wfreq[0]))

@app.route('/samples/<sample>')
def samples(sample):
    """Return a list dictionaries containing `otu_ids` and `sample_values`."""
    stmt = session.query(Samples).statement
    df = pd.read_sql_query(stmt, session.bind)

    if sample not in df.columns:
        return jsonify(f"Error! Sample: {sample} Not Found!"), 400

    df = df[df[sample] > 1]

    df = df.sort_values(by=sample, ascending=0)

    data = [{
        "otu_ids": df[sample].index.values.tolist(),
        "sample_values": df[sample].values.tolist()
    }]
    return jsonify(data)
if __name__ == "__main__":
    app.run(debug=True)
   
    