from flask import Flask, jsonify, request
import ipl
import jugaad

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)

@app.route('/api/teamvteam')
def teamvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    if not team1 or not team2:
        return jsonify({"error": "Please provide both team1 and team2 as query parameters"}), 400

    response = ipl.teamVteamAPI(team1, team2)
    return jsonify(response)

@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')
    if not team_name:
        return jsonify({"error": "Please provide a team name"}), 400

    response = json.loads(jugaad.teamAPI(team_name))
    return jsonify(response)

@app.route('/api/batting-record')
def batting_record():
    batsman_name = request.args.get('batsman')
    if not batsman_name:
        return jsonify({"error": "Please provide a batsman name"}), 400

    response = json.loads(jugaad.batsmanAPI(batsman_name))
    return jsonify(response)

@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = request.args.get('bowler')
    if not bowler_name:
        return jsonify({"error": "Please provide a bowler name"}), 400

    response = json.loads(jugaad.bowlerAPI(bowler_name))
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
