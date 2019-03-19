"""
@file    options.py
@author  Jakob Erdmann
@date    2012-03-15
@version $Id: options.py 14677 2013-09-11 08:30:08Z behrisch $

Provides utility functions for dealing with program options

SUMO, Simulation of Urban MObility; see http://sumo-sim.org/
Copyright (C) 2008-2013 DLR (http://www.dlr.de/) and contributors

This file is part of SUMO.
SUMO is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
"""

import os, sys
import subprocess
import re
from xml.sax import saxutils, parse, handler
from xml.dom import pulldom


def get_long_option_names(application):
    # using option --save-template and parsing xml would be prettier 
    # but we do not want to rely on a temporary file
    output,error = subprocess.Popen(
            [application, '--help'], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE).communicate()
    reprog = re.compile('(--\S*)\s')
    result = []
    for line in output.split(os.linesep):
        m = reprog.search(line)
        if m:
            result.append(m.group(1))
    return result




