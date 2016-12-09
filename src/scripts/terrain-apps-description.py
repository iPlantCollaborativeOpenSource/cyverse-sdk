#!/usr/bin/env python

import terrainpy
import argparse
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if __name__ == '__main__':

    # arguments
    parser = argparse.ArgumentParser(description = 'Return app description for the specified appID.')
    parser.add_argument('-a', '--appID', dest = 'appID', nargs = '?', help = 'app ID with which to generate template')
    parser.add_argument('-v', '--verbose', dest = 'verbose', action = 'store_true', help = 'verbose output')
    parser.add_argument('-z', '--accesstoken', dest = 'accesstoken', nargs = '?', help = 'access token')
    args = parser.parse_args()

    # if token not supplied, get from token_cache
    if args.accesstoken is None:
    	args.accesstoken = terrainpy.get_cached_token()

    # build header
    header = {'Authorization': 'Bearer ' + args.accesstoken}

    # if -a not given
    if args.appID is None:
        args.appID = terrainpy.prompt_user('appID')

    # get app description
    url = 'https://agave.iplantc.org/terrain/v2/apps/de/' + args.appID
    description = requests.get(url, headers = header, verify = False)
    description.raise_for_status
    description = description.json()

    print json.dumps(description, sort_keys = True, indent = 4, separators = (',', ': '))