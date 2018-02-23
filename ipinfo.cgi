#!/bin/bash
#TERM=tty1
#export TERM=${TERM:-dumb}

echo "Content-type: text/html"
echo ""
echo "<html>"
echo "<head>"
echo "<title>RaspberryPi IP info</title>"
echo "</head>"
echo "<body>"
echo "<h2>ifconfig</h2>"
echo "<pre> $(ifconfig) </pre>"
echo "<br/><br/>"
echo "<h2>Public IP</h2>"
echo "<pre> $(curl ipinfo.io) </pre>"
echo "</body>"
echo "</html>"

