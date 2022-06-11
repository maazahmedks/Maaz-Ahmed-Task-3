
import os

class creds_utility(object):

    def __init__(self):
        pass
    @staticmethod
    def wc_api_keys():
        #        wc_key=os.environ.get('wc_key')
        wc_key="test"
        #        wc_secret=os.environ.get('wc_secret')
        wc_secret="test"
        if not wc_key or not wc_secret:
           raise Exception("The environment variables are empty")
        else:
           return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_creds():
        #        db_user=os.environ.get('DB_USER')
        db_user = ""
        #        db_pass=os.environ.get('DB_PASS')
        db_pass = ""
        if not db_user or not db_pass:
           raise Exception("The environment variables are empty")
        else:
           return {'db_user': db_user, 'db_pass': db_pass}