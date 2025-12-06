import os 
from dotenv import load_dotenv

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'da**1D23%342@J$knni&&21'
    SQL_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join('app.db')
    SQL_TRACK_MODIFICATIONS = False