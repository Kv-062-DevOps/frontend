====== Start application on local machine ======
0. git clone git@github.com:Kv-062-DevOps/frontend.git
1. cd frontend/app/
2. virtualenv flask
3. source flask/bin/activate
4. pip3 install -r requirements.txt
5. python3 app.py
6. Follow link http://localhost:5000/

====== Run application with docker ==========
0. git clone git@github.com:Kv-062-DevOps/frontend.git
1. cd frontend/
2. docker build -t front .
3. docker run -p 5000:5000 -d front:latest
4. Follow link http://localhost:5000/


