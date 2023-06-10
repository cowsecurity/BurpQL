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

    def run_query(self,Query)->str:
        """
        """