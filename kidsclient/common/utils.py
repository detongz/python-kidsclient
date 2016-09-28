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

import os
import uuid

from oslo_utils import importutils
import prettytable
import six
from oslo_utils import encodeutils

from kidsclient import exc


def args(*args, **kwargs):
    """Decorator for CLI args.
    """
    def _decorator(func):
        func.__dict__.setdefault('arguments', []).insert(0,(args, kwargs))
        return func
    return _decorator


def print_list(objs, fields, formatters=None, field_labels=None):
    formatters = formatters or {}
    field_labels = field_labels or fields
    pt = prettytable.PrettyTable(field_labels)
    pt.align = 'l'

    for o in objs:
        row = []
        for field in fields:
            if field in formatters:
                row.append(formatters[field](o))
            else:
                field_name = field.lower().replace(' ', '_')
                data = getattr(o, field_name, '')
                row.append(data)
        pt.add_row(row)

    print(encodeutils.safe_encode(pt.get_string()))


def import_versioned_module(version,submodule=None):
    module='kidsclient.v%s' % version
    if submodule:
        module='.'.join((module,submodule))
    return importutils.import_module(module)
