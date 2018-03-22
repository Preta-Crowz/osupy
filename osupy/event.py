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

from . import util,subdata
# from .beatmap import Beatmap

class Event(object):
    '''Represents osu! player event'''
    def __init__(self, **kwargs):
        super(Event, self).__init__()
        if json: self._insjson(json)
        else: self._insdat(**kwargs)
        
    def _insdat(self, **data):
        # self.__token__ = data.get('__token__','undefined')
        self.display_html = data.get('display_html','undefined')
        self.beatmap_id = int(data.get('beatmap_id',-1))
        self.beatmapset_id = int(data.get('beatmapset_id',-1))
        try: self.date = util.parse_time(data.get('date'))
        except: pass
        if not self.date: self.date = datetime.datetime(year=1, month=1, day=1, hour=0, minute=0, second=0)
        self.epicfactor = int(data.get('epicfactor',-1))
        # if self.beatmap_id == -1:
        #     self.beatmap = Beatmap()
        # else: self.beatmap = util.get_beatmap(beatmap_id=self.beatmap_id,token=self.__token__)

    def _insjson(self, json):
        try:
            self.display_html = json['display_html']
            self.beatmap_id = int(json['beatmap_id'])
            self.beatmapset_id = int(json['beatmapset_id'])
            try: self.date = util.parse_time(json['date'])
            except: pass
            if not self.date: self.date = datetime.datetime(year=1, month=1, day=1, hour=0, minute=0, second=0)
            self.epicfactor = int(json['epicfactor'])
        except KeyError: raise InvalidDataError('json')