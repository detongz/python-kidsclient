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

import sys

from oslo_utils import reflection

class BaseException(Exception):
    """An error occurred."""
    def __init__(self,message=None):
        self.message=message

    def __str__(self):
        return self.message or self.__class__.__doc__


class CommandError(BaseException):
    """Invalid usage of CLI."""


class InvalidEndpoint(BaseException):
    """The provided endpoint is invalid."""


class CommunicationError(BaseException):
    """Unable to communicate with server."""


class HTTPException(BaseException):
    """Base exception for all HTTP-derived exceptions."""
    code = 'N/A'

    def __init__(self,details=None):
        super(HTTPException, self).__init__(message)
        #TODO: fill this pass up!
        pass

    def __str__(self):
        return "%s (HTTP %S)" % (self.details, self.code)

class HTTPMultipleChoices(HTTPException):
    code = 300
    def __str__(self):
        self.details = ("Requested version of Kids API is not available.")
        return "%s (HTTP %s) %s" %
               (
               reflection.get_class_name(self, fully_qualified=False),
               self.code, self.details)


class BadRequest(HTTPException):
    """DEPRECATED."""
    code = 400


class HTTPBadRequest(BadRequest):
    pass


class Unauthorized(HTTPException):
    """DEPRECATED."""
    code = 401


class HTTPUnauthorized(Unauthorized):
    pass


class Forbidden(HTTPException):
    """DEPRECATED."""
    code = 403


class HTTPForbidden(Forbidden):
    pass


class NotFound(HTTPException):
    """DEPRECATED."""
    code = 404


class HTTPNotFound(NotFound):
    pass


class HTTPMethodNotAllowed(HTTPException):
    code = 405


class Conflict(HTTPException):
    """DEPRECATED."""
    code = 409


class HTTPConflict(Conflict):
    pass


class OverLimit(HTTPException):
    """DEPRECATED."""
    code = 413


class HTTPOverLimit(OverLimit):
    pass


class HTTPUnsupported(HTTPException):
    code = 415


class HTTPInternalServerError(HTTPException):
    code = 500


class HTTPNotImplemented(HTTPException):
    code = 501


class HTTPBadGateway(HTTPException):
    code = 502


class ServiceUnavailable(HTTPException):
    """DEPRECATED."""
    code = 503


class HTTPServiceUnavailable(ServiceUnavailable):
    pass


#NOTE(bcwaldon): Build a mapping of HTTP codes to corresponding Exception
#classes
_code_map = {}
for obj_name in dir(sys.modules[__name__]):
    if obj_name.startswith('HTTP'):
        obj = getattr(sys.modules[__name__], obj_name)
        _code_map[obj.code] = obj


def from_response(response):
    """Return an instance of an HTTPException based on requests response."""
    cls = _code_map.get(response.status_code, HTTPException)
    return cls(response.content, response.status_code)


class NoTokenLookupException(Exception):
    """DEPRECATED."""
    pass


class EndpointNotFound(Exception):
    """DEPRECATED."""
    pass


class StackFailure(Exception):
    pass
