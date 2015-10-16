#!/usr/bin/env python
# python 2.7
# LCD clock script
# requires colorama, termcolor, and pyfiglet
# Created by Lance Brignoni
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import time
import sys
from time import gmtime, strftime
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format

while True:
	get_time =  strftime("%H : %M : %S")
	#If you want 12 hour time
	#get_time =  strftime("%I : %M : %S %p")
	cprint(figlet_format(get_time, font='starwars'), 'white')
	time.sleep(1)
	print "\033c"
