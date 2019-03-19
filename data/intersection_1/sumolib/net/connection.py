"""
@file    connection.py
@author  Daniel Krajzewicz
@author  Laura Bieker
@author  Karol Stosiek
@author  Michael Behrisch
@date    2011-11-28
@version $Id: connection.py 14677 2013-09-11 08:30:08Z behrisch $

This file contains a Python-representation of a single connection.

SUMO, Simulation of Urban MObility; see http://sumo-sim.org/
Copyright (C) 2008-2013 DLR (http://www.dlr.de/) and contributors

This file is part of SUMO.
SUMO is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
"""
class Connection:
    """edge connection for a sumo network"""
    def __init__(self, fromEdge, toEdge, fromLane, toLane, direction, tls, tllink):
        self._from = fromEdge
        self._to = toEdge
        self._fromLane = fromLane
        self._toLane = toLane
        self._tls = tls
        self._tlLink = tllink
