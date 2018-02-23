### About

A simple web panel to control your Raspberry Pi on a local network.

### Features

* Info page with information about:
	* uptime
	* load average
	* temperature
	* memory
	* disks
	* network I/O*
	* logged in users
	* running processes
* Support for CUPS
	* print queue
	* control panel
* Support for transmission torrent client

(*) It may require days (or even weeks) for network I/O info to be displayed. A first bucket of data needs to be collected for statistical reasons. See network

### Installation

```
$ git clone https://github.com/pirafrank/raspberrypi-web-panel.git
$ cd raspberrypi-web-panel
$ sudo su
# cp info.cgi /usr/local/cgi-bin/
# chmod 755 /usr/local/cgi-bin/info.cgi
# cp ipinfo.cgi /usr/local/cgi-bin/
# chmod 755 /usr/local/cgi-bin/ipinfo.cgi
# cp tempC.sh /usr/local/bin/
# chmod +x /usr/local/bin/tempC
# cp tempF.sh /usr/local/bin/
# chmod +x /usr/local/bin/tempF
# cp index.html /var/www/
# exit
$ exit
```

### Usage

Simply visit your raspberry on your local network via IP address (e.g. http://192.168.0.102).

### License
The software in this repository is released under the GNU GPLv3 License by Francesco Pira (dev[at]fpira[dot]com, fpira.com). You can read the terms of the license [here](http://www.gnu.org/licenses/gpl-3.0.html).

### Credits

* Standart built-in tools.
* [vnStat](http://humdi.net/vnstat/)
