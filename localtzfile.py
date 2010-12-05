#!/usr/bin/env python
# coding=utf8
#
# Copyright ©2010  Simon Arlott
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License (Version 2) as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from __future__ import print_function

import argparse
import struct
import sys

def create(file, longitude):
	(tzh_ttisgmtcnt, tzh_ttisstdcnt, tzh_leapcnt, tzh_timecnt, tzh_typecnt, tzh_charcnt) = (1, 1, 0, 0, 1, 4)

	# header
	file.write("TZif")
	file.write(struct.pack('16x'))
	file.write(struct.pack('>6L', tzh_ttisgmtcnt, tzh_ttisstdcnt, tzh_leapcnt, tzh_timecnt, tzh_typecnt, tzh_charcnt))

	# tzh_timecnt (0)

	# tzh_typecnt (1)
	file.write(struct.pack('>l', round(float(longitude)/360 * 86400)))
	file.write(struct.pack('>b', 0))
	file.write(struct.pack('>B', 0))

	# tzh_charcnt (4)
	file.write("LCL")
	file.write(struct.pack('x'))

	# tzh_leapcnt (0)

	# tzh_ttisstdcnt (1)
	file.write(struct.pack('>B', 0))

	# tzh_ttisgmtcnt (1)
	file.write(struct.pack('>B', 0))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Create longitude-based tzfile(5)')
	parser.add_argument('longitude', help='Longitude (decimal)')
	parser.add_argument('filename', help='Output file (e.g. /usr/share/zoneinfo/Local)')
	args = parser.parse_args()

	with open(args.filename, "wb") as f:
		create(f, args.longitude)
