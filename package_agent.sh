mkdir my_agent
touch my_agent/__init__.py
python3 -m compileall TournamentPlayers.py
cp __pycache__/TournamentPlayers.*.pyc my_agent/TournamentPlayers.pyc
tar -zcf my_agent.tar.gz my_agent/
