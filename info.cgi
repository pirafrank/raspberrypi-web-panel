#!/bin/bash

#############################################################################
# raspberrypi-web-panel <https://github.com/pirafrank/raspberrypi-web-panel>
# A simple web panel to control your Raspberry Pi on a local network.
#
# Copyright (C) 2015 Francesco Pira <dev@fpira.com>
#
# This file is part of raspberrypi-web-panel
#
# raspberrypi-web-panel is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# raspberrypi-web-panel is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with raspberrypi-web-panel. If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

#TERM=tty1
#export TERM=${TERM:-dumb}

echo "Content-type: text/html"
echo ""
echo "<html>"
echo "<head>"
echo "<title>RaspberryPi info</title>"
echo "</head>"
echo "<body>"
echo "<h1>General system information for host $(hostname -s)</h1>"
echo "<center>Information generated on $(date)</center>"
echo "<h2></h2>"
echo "<pre> Uptime: $(uptime) </pre>"
echo "<pre> Temperature: $(tempC), $(tempF)</pre>"
echo "<h2>Memory Info</h2>"
echo "<pre> $(free -m) </pre>"
echo "<h2>Disk Info</h2>"
echo "<pre> $(df -h) </pre>"
echo "<h2>Network info</h2>"
echo "<pre> $(vnstat -i eth0) </pre>"
echo "<h2>Logged in users</h2>"
echo "<pre> $(w) </pre>"
echo "<h2>Processes</h2>"
echo "<pre> $(ps aux) </pre>"
echo "</body>"
echo "</html>"
