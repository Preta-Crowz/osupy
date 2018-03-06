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
from .event import Event
from .error import *

class Player:
    '''Represents osu! player'''
    def __init__(self, **kwargs):
        super(Player, self).__init__()
        json = kwargs.get('json',None)
        try:
            if json: self._insjson(json)
            else: self._insdat(**kwargs)
        except NameError: self._insdat(**kwargs)

    def _insdat(self, **data):
        # self.__token__ = data.get('__token__','undefined')
        self.user_id = data.get('user_id',-1)
        self.username = data.get('username','undefined')
        self.count300 = data.get('count300',-1)
        self.count100 = data.get('count100',-1)
        self.count50 = data.get('count50',-1)
        self.playcount = data.get('playcount',-1)
        self.ranked_score = data.get('ranked_score',-1)
        self.total_score = data.get('total_score',-1)
        self.pp_rank = data.get('pp_rank',-1)
        self.level = data.get('level',-1)
        self.pp_raw = data.get('pp_raw',-1)
        self.accuracy = data.get('accuracy',-1)
        self.count_rank_ss = data.get('count_rank_ss',-1)
        self.count_rank_ssh = data.get('count_rank_ssh',-1)
        self.count_rank_s = data.get('count_rank_s',-1)
        self.count_rank_sh = data.get('count_rank_sh',-1)
        self.count_rank_a = data.get('count_rank_a',-1)
        self.country = data.get('country','undefined')
        self.pp_country_rank = data.get('pp_country_rank',-1)
        events = data.get('events',[])
        self.events = []
        for event in events:
            self.events += Event(event)

    def _insjson(self, json):
        try:
            self.user_id = json['user_id']
            self.username = json['username']
            self.count300 = json['count300']
            self.count100 = json['count100']
            self.count50 = json['count50']
            self.playcount = json['playcount']
            self.ranked_score = json['ranked_score']
            self.total_score = json['total_score']
            self.pp_rank = json['pp_rank']
            self.level = json['level']
            self.pp_raw = json['pp_raw']
            self.accuracy = json['accuracy']
            self.count_rank_ss = json['count_rank_ss']
            self.count_rank_ssh = json['count_rank_ssh']
            self.count_rank_s = json['count_rank_s']
            self.count_rank_sh = json['count_rank_sh']
            self.count_rank_a = json['count_rank_a']
            self.country = json['country']
            self.pp_country_rank = json['pp_country_rank']
            events = json['events']
            self.events = []
            for event in events:
                self.events += Event(event)
        except KeyError: raise InvalidDataError('json')
        
def get_player(userinfo,**kwargs):
    #0
    token = kwargs.get('token','undefined')
    if token == 'undefined': raise NoTokenError()
    else: req_url = subdata.api_url['player'] + '?k=' + token
    #1,2
    try:
        u = userinfo
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
    #3
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
    event_days = kwargs.get('event_days',-1)
    if m == -1: pass
    else: req_url += '&event_days=' + str(event_days)

    r = requests.get(req_url)
    r = r.text
    jdata = jmodule.loads(r)

    players = []
    global Player
    for j in jdata:
        players += [Player(json=j)]
    return players