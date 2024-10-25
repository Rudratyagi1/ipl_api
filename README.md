# IPL Team Comparison API

This project is a Flask web application that provides APIs to fetch and compare IPL teams' statistics, including team records, batting records, and bowling records. It pulls data from Google Sheets, processes it, and returns the results in JSON format.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Fetch a list of IPL teams.
- Compare two IPL teams based on historical match data.
- Retrieve overall records of a specific team.
- Get individual batting and bowling records of players.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ipl-team-comparison-api.git
   cd ipl-team-comparison-api




Here’s a structured requirements.txt and a README.md file for your project. These will help others understand how to set up and use your Flask application.

requirements.txt
This file lists all the necessary packages for your project:

makefile
Copy code
Flask==2.0.3
pandas==1.5.3
numpy==1.24.2
README.md
Here's a comprehensive README.md file for your project:

markdown
Copy code
# IPL Team Comparison API

This project is a Flask web application that provides APIs to fetch and compare IPL teams' statistics, including team records, batting records, and bowling records. It pulls data from Google Sheets, processes it, and returns the results in JSON format.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Fetch a list of IPL teams.
- Compare two IPL teams based on historical match data.
- Retrieve overall records of a specific team.
- Get individual batting and bowling records of players.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ipl-team-comparison-api.git
   cd ipl-team-comparison-api
   
Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


Install the requirements:
pip install -r requirements.txt


Usage

To run the application, use the following command:
python app.py
The application will start at http://127.0.0.1:5000.

API Endpoints
1. Home
Endpoint: /
Method: GET
Description: Returns a simple greeting.
2. Get Teams
Endpoint: /api/teams
Method: GET
Description: Returns a list of all IPL teams.
3. Compare Teams
Endpoint: /api/teamvteam
Method: GET
Query Parameters:
team1: Name of the first team.
team2: Name of the second team.
Description: Compares the two specified teams and returns their match statistics.
4. Team Record
Endpoint: /api/team-record
Method: GET
Query Parameters:
team: Name of the team.
Description: Returns the overall match record of the specified team.
5. Batsman Record
Endpoint: /api/batting-record
Method: GET
Query Parameters:
batsman: Name of the batsman.
Description: Returns the batting record of the specified player.
6. Bowler Record
Endpoint: /api/bowling-record
Method: GET
Query Parameters:
bowler: Name of the bowler.
Description: Returns the bowling record of the specified player.
Contributing
Contributions are welcome! Please feel free to submit a pull request or raise an issue if you have any suggestions or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

markdown:
### Key Points in the README
- **Features Section**: Lists the capabilities of the API.
- **Installation Section**: Provides clear instructions for setting up the environment.
- **Usage Section**: Explains how to run the application.
- **API Endpoints Section**: Details each API endpoint for easy reference.
