# Copyright 2014, candidtim (https://github.com/candidtim)
#
# This file is part of Vagrant AppIndicator for Ubuntu.
#
# Vagrant AppIndicator for Ubuntu is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Foobar.
# If not, see <http://www.gnu.org/licenses/>.

import os
import json


__CONFIG_FILE_PATH = os.path.expanduser("~/.vgapplet")


show_notifications = True
check_for_updates = True


def __load():
    if not os.path.isfile(__CONFIG_FILE_PATH): return

    global show_notifications
    global check_for_updates

    with open(__CONFIG_FILE_PATH, 'r') as config_file:
        config_dict = json.load(config_file)
    show_notifications = config_dict.get("show_notifications", True)
    check_for_updates = config_dict.get("check_for_updates", True)


def persist():
    config_dict = {
        "show_notifications": show_notifications,
        "check_for_updates": check_for_updates
    }
    with open(__CONFIG_FILE_PATH, 'w') as config_file:
        json.dump(config_dict, config_file)


__load()
