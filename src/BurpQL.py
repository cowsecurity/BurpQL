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

    def __init__(self,URL,AUTH):
        self.URL = URL
        self.AUTH = AUTH
        try:
            self.headers = {"Authorization":self.AUTH}