Start application on local machine 
1. git clone git@github.com:Kv-062-DevOps/frontend.git
2. cd frontend/app/
3. virtualenv flask
4. source flask/bin/activate
5. pip3 install -r requirements.txt
6. python3 app.py
7. Follow link http://localhost:8080/

Run application with docker 
1. git clone git@github.com:Kv-062-DevOps/frontend.git
2. cd frontend/
3. docker build -t front .
4. docker run -p 8080:8080 -d -e URL_GET="get_url" -e POST_URL="post_url" front:latest
5. Follow link http://localhost:8080/

Run application with docker form dockerhub
1. docker run -p 8080:8080 -d -e URL_GET="get_url" -e POST_URL="post_url" dimeder13/frontend:latest

