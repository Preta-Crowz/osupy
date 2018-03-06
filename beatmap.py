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

import datetime,requests
import json as jmodule
from . import util,subdata
from .error import *

class Beatmap:
    '''Represents osu! beatmap'''
    def __init__(self, **kwargs):
        super(Beatmap, self).__init__()
        json = kwargs.get('json',None)
        try:
            if json: self._insjson(json)
            else: self._insdat(**kwargs)
        except NameError: self._insdat(**kwargs)

    def _insdat(self, **data):
        # self.__token__ = data.get('__token__','undefined')
        self.approved = int(data.get('approved',-3))
        if self.approved < -3:
            self.stat = 'undefined'
        else:
            try:
                self.stat = subdata.approvedstat[self.approved]
            except IndexError: self.stat = 'undefined'

        try: self.approved_date = util.parse_time(data.get('approved_date'))
        except: pass
        if not self.approved_date: self.approved_date = subdata.nulldate

        try: self.last_update = util.parse_time(data.get('last_update'))
        except: pass
        if not self.last_update: self.last_update = subdata.nulldate

        self.artist = data.get('artist','undefined')
        self.beatmap_id = int(data.get('beatmap_id',-1))
        self.beatmapset_id = int(data.get('beatmapset_id',-1))
        self.bpm = int(data.get('bpm',-1))
        self.creator = data.get('creator')
        self.difficultyrating = float(data.get('difficultyrating',-1))
        self.diff_size = int(data.get('diff_size',-1))
        self.diff_overall = int(data.get('diff_overall',-1))
        self.diff_approach = int(data.get('diff_approach',-1))
        self.diff_drain = int(data.get('diff_drain',-1))
        self.hit_length = int(data.get('hit_length',-1))
        self.source = data.get('source','undefined')

        self.genre_id = int(data.get('genre_id',-1))
        if self.genre_id < 0:
            self.genre = 'undefined'
        else:
            try:
                self.genre = subdata.genre[self.genre_id]
            except IndexError: self.genre = 'undefined'

        self.language_id = int(data.get('language_id',-1))
        if self.language_id < 0:
            self.language = 'undefined'
        else:
            try:
                self.language = subdata.language[self.language_id]
            except IndexError: self.language = 'undefined'

        self.title = data.get('title','undefined')
        self.total_length = int(data.get('total_length',-1))
        self.version = int(data.get('version',-1))
        self.file_md5 = data.get('file_md5','undefined')
        self.mode = int(data.get('mode',-1))
        self.tags = list('[' + data.get('tags','').replace(' ',',') + ']')
        self.favourite_count = int(data.get('favourite_count',-1))
        self.playcount = int(data.get('playcount',-1))
        self.passcount = int(data.get('passcount',-1))
        self.max_combo = int(data.get('max_combo',-1))

    def _insjson(self, json):
        try:
            self.approved = int(json['approved'])
            if self.approved < -3:
                self.stat = 'undefined'
            else:
                try:
                    self.stat = subdata.approvedstat[self.approved]
                except IndexError: self.stat = 'undefined'

            try: self.approved_date = util.parse_time(json['approved_date'])
            except: pass
            if not self.approved_date: self.approved_date = subdata.nulldate

            try: self.last_update = util.parse_time(json['last_update'])
            except: pass
            if not self.last_update: self.last_update = subdata.nulldate

            self.artist = json['artist']
            self.beatmap_id = int(json['beatmap_id'])
            self.beatmapset_id = int(json['beatmapset_id'])
            self.bpm = int(json['bpm'])
            self.creator = json['creator']
            self.difficultyrating = float(json['difficultyrating'])
            self.diff_size = int(json['diff_size'])
            self.diff_overall = int(json['diff_overall'])
            self.diff_approach = int(json['diff_approach'])
            self.diff_drain = int(json['diff_drain'])
            self.hit_length = int(json['hit_length'])
            self.source = json['source']

            self.genre_id = int(json['genre_id'])
            if self.genre_id < 0:
                self.genre = 'undefined'
            else:
                try:
                    self.genre = subdata.genre[self.genre_id]
                except IndexError: self.genre = 'undefined'

            self.language_id = int(json['language_id'])
            if self.language_id < 0:
                self.language = 'undefined'
            else:
                try:
                    self.language = subdata.language[self.language_id]
                except IndexError: self.language = 'undefined'

            self.title = json['title']
            self.total_length = int(json['total_length'])
            self.version = int(json['version'])
            self.file_md5 = json['file_md5']
            self.mode = int(json['mode'])
            self.tags = list('[' + json['tags'].replace(' ',',') + ']')
            self.favourite_count = int(json['favourite_count'])
            self.playcount = int(json['playcount'])
            self.passcount = int(json['passcount'])
            self.max_combo = int(json['max_combo'])
        except KeyError: raise InvalidDataError('json')

def get_beatmap(beatmap_id,**kwargs):
    #0
    token = kwargs.get('token','undefined')
    if token == 'undefined': raise NoTokenError()
    else: req_url = subdata.api_url['beatmap'] + '?k=' + token
    #1
    since = parse_time(kwargs.get('since',subdata.nulldate))
    if since == subdata.nulldate: pass
    else: req_url += '&since=' + str(since)
    #2
    s = int(kwargs.get('beatmapset_id',-1))
    if s == -1: pass
    else: req_url += '&s=' + str(s)
    #3
    try:
        b = int(beatmap_id)
        if b == -1: pass
        else: req_url += '&b=' + str(b)
    except NameError: pass
    #4,5
    try:
        u = kwargs.get('userinfo','undefined')
        if u == 'undefined': pass
        else:
            req_url += '&u=' + str(u)
            try:
                u = int(u)
                utype = 'id'
                req_url += '&type=' + str(utype)
            except ValueError:
                utype = 'string'
                req_url += '&type=' + str(utype)
            if utype != 'string' and utype != 'id': raise SyntaxCollisionError()
    except NameError: pass
    #6
    m = kwargs.get('mode',-1)
    if m == -1: pass
    else:
        try:
            m = int(m)
            req_url += '&m=' + str(m)
        except ValueError:
            try:
                m = subdata.modetonum[m]
                req_url += '&m=' + str(m)
            except KeyError:
                m = -1
                pass
    #7
    a = int(kwargs.get('converted',-1))
    if a == -1: pass
    else:
        if a == 1 and ( m < 1 or m > 3 ): raise SyntaxCollisionError()
        else: req_url += '&a=' + str(a)
    
    r = requests.get(req_url)
    r = r.text
    jdata = jmodule.loads(r)

    beatmaps = []
    global Beatmap
    for j in jdata:
        beatmaps += [Beatmap(json=j)]
    return beatmaps