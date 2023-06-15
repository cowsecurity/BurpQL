"""
Author: Yash Singh Chauhan yashsinghchauhanformal@gmail.comj
BurpQL.py (c) 2023
Desc: Automate and control BurpSuite Enterprise effortlessly with this Python library, leveraging its GraphQL API.
"""

import json
import requests

class BurpQL:
    """
    Main Controller for Burp Enterprise GraphQL API
    Arguments :
    - URL The URL (https://IP:PORT/graphql/v1) of your Burp Enterprise server. 
    - AUTH - API authorization key.

    Methods:
        To Be Done    
    
    """

    def __init__(self,URL:str,AUTH:str)-> None:
        """
        Initialization function: Takes Burp URL and Authorization token as input.
        """
        self.URL = URL
        self.AUTH = AUTH
        try:
            self.headers = {
                    "Authorization":self.AUTH
                            }
            self.session = requests.get(url=URL,headers=self.headers)
        except:
            print("Unknown error occured!")

    def getJSONResponse(self,msg)->str:
        """
        Parameters: 
            msg 
            self
        Returns: jsonified format of response
        """
        response = {"message":msg}
        return json.dumps(response,indent=4,sort_keys=True)

    def run_query(self, Query)-> str:
        """
        Takes queries as input and returns their response
        """
        if(self.burp_online):
            try:
                response = self.client.execute(Query)
                return response # JSON
            except Exception as e:
                print(not_ok + " Error  : " + str(e))
        else:
            print(not_ok + " Error Burpsuite is not online/available.")

def create_site(self, target_url)-> str:
    """
    """
    if self.burp_online:
        try:
            query_variables = {
                'name': target_url,
                'parentID': self.parent_id,
                'includedUrls': target_url,
                'emailRecipients': []
            }
            response = requests.post(self.URL, json={'query': NEW_SITE, 'variables': query_variables})
            data = response.json()
            return data
        except Exception as e:
            print(not_ok + " Error: " + str(e))
    else:
        print(not_ok + " Error connecting with Burp Server")

def cancel_scan(self,scan_id):
    """
    """
    if self.burp_online:
        try:
            query_variables = {

            }

    # TO do : Handle scans under a single function, improve queries