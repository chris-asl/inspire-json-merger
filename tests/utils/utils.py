# -*- coding: utf-8 -*-
#
# This file is part of INSPIRE.
# Copyright (C) 2014-2017 CERN.
#
# INSPIRE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

from __future__ import absolute_import, division, print_function

import json
from json_merger.conflict import Conflict

from inspire_schemas.api import load_schema, validate


def assert_ordered_conflicts(conflicts, expected_conflicts):
    # expected conflict is a Conflict class instance
    expected_conflict = [
        json.loads(Conflict(c[0], c[1], c[2]).to_json()) for c in expected_conflicts
    ]

    # order the lists to check if they match
    conflicts = sorted(conflicts, key=lambda c: c['path'])
    expected_conflict = sorted(expected_conflict, key=lambda c: c['path'])

    assert conflicts == expected_conflict


def validate_subschema(obj):
    schema = load_schema('hep')
    key = list(obj.keys())[0]  # python 3 compatibility
    sub_schema = schema['properties'].get(key)
    assert validate(obj.get(key), sub_schema) is None
