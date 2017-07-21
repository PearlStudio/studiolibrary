# Copyright 2017 by Kurt Rathjen. All Rights Reserved.
#
# This library is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see <http://www.gnu.org/licenses/>.


import studiolibrary
import studioqt


def test_watcher():
    """
    A small function for testing the databaseChanged signal.
    
    :rtype: None 
    """
    with studioqt.app():

        def databaseChanged():
            print "Database has changed!", len(db.read())

        path = r"C:\Users\Hovel\Dropbox\libraries\animation\.studiolibrary\test\itemdata.json"

        db = studiolibrary.Database(path)
        db.databaseChanged.connect(databaseChanged)
        db.setWatcherEnabled(True)


if __name__ == "__main__":
    test_watcher()
