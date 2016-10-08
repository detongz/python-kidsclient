# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import copya
import logging
import socket

from keystoneclient import adapter
from oslo_utils import encodeutils
from oslo_utils import importutils
import requests
import six

from kidsclient.common import utils
from kidsclient import exc

LOG=logging.getLogger(__name__)
USER_AGENT='python-keystoneclient'
CHUNKSIZE=1024*64 # 64kB

class HTTPClient(object):

    def __init__(self, endpoint, **kwargs):
        self.endpoint=endpoint
        self.auth_token=kwargs.get('token')

class SessionClient(adapter.LegacyJsonAdapter):

    def request(self, url, method, **kwargs):
        kwargs.setdefault('user_agent',USER_AGENT)

def get_http_client(endpoint=None, session=None, **kwargs):
    # referencing glanceclient
    if session:
        return SessionClient(session, **kwargs)
    elif endpoint:
    else:
        return HTTPClient(endpoint=endpoint, username=username,
                          password=password, include_pass=include_pass,
                          endpoint_type=endpoint_type, auth_url=auth_url,
                          **kwargs)
