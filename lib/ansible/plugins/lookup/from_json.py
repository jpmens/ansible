# (c) 2017, Jan-Piet Mens <jpmens(at)gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

import json

# ==============================================================
# from_json: return object parsed from JSON
#
# --------------------------------------------------------------

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        '''
        terms contains a string of JSON
        '''

        ret = []
        for t in terms:
            try:
                s = json.loads(t)
                ret.append(s)
            except Exception as e:
                raise AnsibleError("Cannot load JSON from string", str(e))

        return ret
