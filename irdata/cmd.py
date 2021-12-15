#!/usr/bin/env python

"""
Command line utilities.

--------

Copyright (C) 2012 Ian Donaldson <ian.donaldson@biotek.uio.no>
Original author: Paul Boddie <paul.boddie@biotek.uio.no>

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os, sys

def get_progname():
    return os.path.split(sys.argv[0])[-1]

def get_lists(arg):

    """
    Split 'arg' into lists of lists, with ':' separating the lists and ','
    separating elements in each list. The special element 'all', if found on its
    own in a list, will occur instead of an actual list in the result.
    """

    if not arg:
        return []

    lists = []
    for liststr in arg.split(":"):
        l = liststr.split(",")
        if l == ["all"]:
            l = "all"
        lists.append(l)
    return lists

# vim: tabstop=4 expandtab shiftwidth=4
