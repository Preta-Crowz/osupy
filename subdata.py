# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2017-2018 CrowZ

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the 'Software'),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
'''
import datetime

approvedstat = ['pending','ranked','approved','qualified','undefined','loved','graveyard','WIP']
genre = ['any','unspecified','video game','anime','rock','pop','other','novelty','undefined','hip hop','electronic']
language = ['any','other','english','japanese','chinese','instrumental','korean','french','german','swedish','spanish','italian']
nulldate = datetime.datetime(year=1, month=1, day=1, hour=0, minute=0, second=0)
modetonum = {'osu':0,'taiko':1,'ctb':2,'mania':3}
api_url = {'beatmap':'https://osu.ppy.sh/api/get_beatmaps','player':'https://osu.ppy.sh/api/get_user'}