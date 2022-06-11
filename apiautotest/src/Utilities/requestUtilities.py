
import requests
from apiautotest.src.configs.host_config import API_HOSTS
from requests_oauthlib import OAuth1
from apiautotest.src.Utilities.CredentialsUtility import creds_utility
import os
import json
import logging as logger

class RequestUtility(object):

    def __init__(self):
        self.envir=os.environ.get('ENV', 'test')
        self.base_url=API_HOSTS[self.envir]
        obj=creds_utility()
        cred_util=obj.wc_api_keys()
        self.auth=OAuth1(cred_util['wc_key'], cred_util['wc_secret'])

    def assert_status(self):
        assert self.st  == self.expected_status_code2, f"Bad Status code." \
        f"Expected {self.expected_status_code2}, Actual Status code: {self.st}," \
        f"URL {self.usrl}, Response JSON: {self.rs_json}"


    def apost(self, endpoint, payload=None, headers=None, expected_status_code=800):
         if not headers:
            headers = {"Content-Type": "application/json"}

         self.usrl = self.base_url + endpoint

         rs_api = requests.post(url=self.usrl, data=json.dumps(payload), headers=headers, auth=self.auth)
         logger.debug(f"POST API Response: {rs_api.json()}")
         response_dict = json.loads(rs_api.text)
         # response_dict['message']

  #       import pdb
  #       pdb.set_trace()

         self.st = rs_api.status_code
         self.expected_status_code2 = expected_status_code
         self.rs_json = rs_api.json()

      #   self.assert_status()
#         logger.debug(f"POST API Response: {rs_api.json()}")

#         assert self.st == 200
#         assert response_dict['message'] == 'User Access Token successfully generated and saved into database.'
         return self.rs_json



    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
           headers = {"Content-Type": "application/json"}

        self.usrl= self.base_url + endpoint
        rs_api=requests.get(url=self.usrl, data=json.dumps(payload), headers=headers, auth=self.auth)
        #self.st=rs_api.status_code
        #self.expected_status_code2 = expected_status_code
        self.rs_json=rs_api.json()
        #self.assert_status()
        #logger.debug(f"GET API Response: {rs_api.json()}")
        return self.rs_json


    def delete(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
           headers = {"Content-Type": "application/json"}

        self.usrl= self.base_url + endpoint
        rs_api=requests.delete(url=self.usrl, data=json.dumps(payload), headers=headers, auth=self.auth)
        #str=rs_api.status_code
        # import pdb;        pdb.set_trace()
        data2 = dict()
        data2['code']=rs_api.status_code
        data2['message']=rs_api.text
        return data2
