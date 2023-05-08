
class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'




class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'mypassword'
    MYSQL_DB = 'flask'





config = {
    'development': DevelopmentConfig,
}