+++++++ Start application on local machine ++++++++
1. git clone git@github.com:Kv-062-DevOps/frontend.git
2. cd frontend/app/
3. virtualenv flask
4. source flask/bin/activate
5. pip3 install -r requirements.txt
6. python3 app.py
7. Follow link http://localhost:5000/

+++++++ Run application with docker ++++++++++++++
1. git clone git@github.com:Kv-062-DevOps/frontend.git
2. cd frontend/
3. docker build -t front .
4. docker run -p 5000:5000 -d front:latest
5. Follow link http://localhost:5000/


