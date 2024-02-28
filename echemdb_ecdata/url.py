r"""
URL to a ZIP containing the latest echemdb electrochemistry data.
"""
# ********************************************************************
#  This file is part of electrochemistry-data.
#
#        Copyright (C) 2024 Albert Engstfeld
#
#  electrochemistry-data is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  electrochemistry-data is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with electrochemistry-data. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************

import os

ECHEMDB_DATABASE_URL = os.environ.get(
    "ECHEMDB_DATABASE_URL",
    "https://github.com/echemdb/electrochemistry-data/releases/download/0.2.0/data-0.2.0.zip",
)