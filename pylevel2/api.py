#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urlparse
from datetime import datetime, date
import os
import json


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat(' ')
        elif isinstance(obj, date):
            return obj.isoformat()
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


class PyLevel2(object):

    def __init__(self, base_url='https://level2.lu'):
        """
            Query the Level 2 API.
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'content-type': 'application/json'})

    def events(self, count=None, year=None, month=None, json_dump=False):
        """
            Get the events.
        """
        path = 'events'
        response = None
        if count is None and year is None and month is None:
            path = os.path.join(path, 'json')
            url = urlparse.urljoin(self.base_url, path)
            response = self.session.get(url)
        elif count is not None:
            path = os.path.join(path, '{}.json'.format(count))
            url = urlparse.urljoin(self.base_url, path)
            response = self.session.get(url)
        elif year is not None and month is not None:
            path = os.path.join(path, str(year), '{}.json'.format(month))
            url = urlparse.urljoin(self.base_url, path)
            response = self.session.get(url)
        else:
            # Invalid requests
            pass
        if response.status_code == 200:
            to_return = []
            data = response.json()
            if data:
                for event in data:
                    if event.get('start'):
                        event['start'] = datetime.fromtimestamp(event['start'])
                    if event.get('end'):
                        event['end'] = datetime.fromtimestamp(event['end'])
                    if event.get('date'):
                        # This value does not contains the year, so it is not really usable
                        # Get the day from the start time instead
                        event['date'] = event['start'].date()
                    to_return.append(event)
            else:
                # invalid query
                pass
            if json_dump:
                return json.dumps(to_return, cls=DatetimeEncoder)
            return to_return
        else:
            # Something bad happened
            pass

    def spaceapi(self, json_dump=False):
        """
            Gives information about Level2.
        """
        url = urlparse.urljoin(self.base_url, 'spaceapi')
        response = self.session.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                data['state']['lastchange'] = datetime.fromtimestamp(data['state']['lastchange'])
            else:
                # invalid query
                pass
            if json_dump:
                return json.dumps(data, cls=DatetimeEncoder)
            return data
        else:
            # Something bad happened
            pass
