
## Running MySQL in a Docker container for local development

- Make sure [Docker](https://docs.docker.com/install/ "Docker") & [Docker-Compose](https://docs.docker.com/compose/install/ "Docker-Compose") are installed
- cd into the location of the docker-compose.yml file & run the following
```bash
$ docker-compose up -d
```
- Use the following configurations for DB connection
```python
DB_HOST = 'localhost:3306'
DB_NAME = 'db_test'
DB_USERNAME = 'root'
DB_PASSWORD = 'secretPassword'
```
<br>

## Testing the connection

- Make sure python3 & pip3 are installed
- install the following packages
```bash
$ pip3 install flask flask-sqlalchemy pymysql
```
- cd into the location of the app.py file & run the following
```bash
$ python3 app.py
```
- Open up Browser and hit http://127.0.0.1:5000/

<br>
