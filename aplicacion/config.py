import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True # En despliegue esto pasa a FALSE
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
# SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ejemplo basico de postgresql
#Comparalo con ejemplo de Mysql
SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://despliegue_tienda_user:m9WlbrI5PcPjLVemlKTeJNMBfduTqqGb@dpg-cu1rr7pu0jms738li7hg-a.frankfurt-postgres.render.com/despliegue_tienda'
SQLALCHEMY_TRACK_MODIFICATIONS=False

