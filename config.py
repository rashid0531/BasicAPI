class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rashid:1@localhost:5433/smilebook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False