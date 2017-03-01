from andrewbberger.util.oanda_fx_api.config import Config
import os


class Account:
    def __init__(self, account=0): 
        _file = '/var/www/andrewbberger/andrewbberger/util/oanda_fx_api/keys'
        self.id, self.token = open(_file, 'r').read().strip().split(',')
        
        self.venue = Config.practice_venue  # api endpoint
        self.candles_venue = self.venue + "/v1/candles"
        self.streaming = Config.streaming_venue
        self._id_url = Config.account_url + self.id
        
        self.orders =  self._id_url + '/orders/'
        self.positions = self._id_url + "/positions/"
        self.headers = {'Authorization': 'Bearer %s' % self.token,
                        'X-Accept-Datetime-Format': 'UNIX'}

    def __str__(self):
        return "[=> %s (%s)" % (self.venue, self.id)

    def __repr__(self):
        return self.__str__()
