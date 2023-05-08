virtualenv -p python3 env <<<
.\env\Scripts\activate
pip install flask flask-login flask-mysqldb flask-
pip install flask_sqlalchemy
python .\src\models\entities\User.py