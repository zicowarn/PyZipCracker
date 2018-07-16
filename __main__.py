#!/usr/bin/env python
# -*- coding:utf8 -*
# The Mozilla Public License 2.0 (MPL 2.0)

# Copyright (c) 2015 Zhichao Wang

# This Source Code Form is subject to the terms of the Mozilla Public
#   License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# 
# If it is not possible or desirable to put the notice in a particular
# file, then You may include the notice in a location (such as a LICENSE
# file in a relevant directory) where a recipient would be likely to look
# for such a notice.
# 
# You may add additional accurate notices of copyright ownership.
#

"""
.. Use Python to crack Zip encrypted files with password dictionary files. 
.. The project is created to understand Python's multi threading programming.
"""

__author__ = 'zhichao,wang'
__email__ = 'ziccowarn@gmail.com'
__url__ = 'http://www.me-lot.com/'
__version__ = '0.1'
__license__ = 'MPL 2.0'
__status__ = 'Beta'
__revision__ = '$Rev: 01 $'
__updated__ = '2018-07-16'

import sys


if 'PyZipCracker' not in sys.modules and __name__ == '__main__':
    from PyZipCracker import main as _main

from PyZipCracker import main as _main

if __name__ == '__main__':
    sys.exit(_main())

