# Author: Hongbo Tian / tianhongbo1@gmail.com
# Created: June 3, 2013
# Updated: June 3, 2013
# Code version: 0.0.1
# Python version: 2.7.5
# Purpose: The file is the collection of OpenStack API common function
# Function:
#     1. Common API Func
#     2. Get API configuration from config file - "OpenStackApi.conf"

import httplib
import json
import urllib

# Define the OpenStack API configuration Class
# All the configuration data will store at hard disk named as "OpenStackApi.conf"
class OpenStackApiConf:
    # Singleton protection
    __singleton = None
    __FileName = "OpenStackApi.conf"
    
    def __init__(self):
        # Only do one time initialization
        if OpenStackApiConf.__singleton:
            print "warning...try to read configration data again..."
            #raise OpenStackApiConf.__singleton
        OpenStackApiConf.__singleton = self
    
        # Initial Data as the local host
        self.__nova_api_server = "127.0.0.1:8774"
        self.__quantum_api_server = "127.0.0.1:9696"
        self.__keystone_api_server = "127.0.0.1:5000"
        self.__glance_api_server = "127.0.0.1:9292"
        self.__admin_api_server = "127.0.0.1:35357"

        # Read configuration data from file
        OpenStackApiConf.ReLoad(self)

    # Define the func read configuration from file
    def ReLoad(self):
        with open(OpenStackApiConf.__FileName, 'r') as f:
            for line in f:
                # Remove all the whitespaces and '\n' firstly
                s = line.replace(' ', '')
                s = s.replace('\n', '')
                
                if (s == ''):
                    # Skip the blank lines
                    continue
                elif (s[0] == '#'):
                    # Skip the comments lines
                    continue
                elif 'nova_api_server=' in s:
                    self.__nova_api_server = s.replace('nova_api_server=', '')
                elif 'quantum_api_server=' in s:
                    self.__quantum_api_server = s.replace('quantum_api_server=', '')
                elif 'keystone_api_server=' in s:
                    self.__keystone_api_server = s.replace('keystone_api_server=', '')
                elif 'glance_api_server=' in s:
                    self.__glance_api_server = s.replace('glance_api_server=', '')
                elif 'admin_api_server=' in s:
                    self.__admin_api_server = s.replace('admin_api_server=', '')
                else:
                    print "something is wrong: " + line

    # Get the singleton instance
    def get_instance():
        return OpenStackApiConf.__singleton

    def get_nova_api_server(self):
        return self.__nova_api_server

    def get_quantum_api_server(self):
        return self.__quantum_api_server
    
    def get_keystone_api_server(self):
        return self.__keystone_api_server

    def get_glance_api_server(self):
        return self.__glance_api_server

    def get_admin_api_server(self):
        return self.__admin_api_server

def OpenStackApiUtilGet(Token, Host, Uri):
    Headers= {"X-Auth-Token": Token, "Content-Type": "application/json"}

    # HTTP Connection
    conn = httplib.HTTPConnection(Host)
    conn.request("GET", Uri, None, Headers)

    # HTTP response
    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)

    # HTTP Close
    conn.close()
    return dd

def OpenStackApiUtilReqDataJson(Host, Headers, Method, Uri, Params):
    # Open HTTP Connection
    conn = httplib.HTTPConnection(Host)
    conn.request(Method, Uri, Params, Headers)

    # HTTP response
    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)

    # HTTP Close
    conn.close()

    # return the JSON data
    return dd
