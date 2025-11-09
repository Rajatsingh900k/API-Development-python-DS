from flask import Flask,jsonify, request
import ipl
app=Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/api/teams')
def teams():
    teams=ipl.teamsApi()
    return jsonify(teams)

@app.route('/api/teamvteam')
def teamvteam():
    team1=request.args.get('team1')
    team2=request.args.get('team2')
    temp=ipl.teamVteamApi(team1,team2)
    return jsonify(temp)

app.run(debug=True)