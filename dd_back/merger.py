import dd_back.dd_calc as dd
import json

class Merger(object):
    AGING = 1.0
    TRASH = 1.0
    UPGRADES = {}
    QUALITY = 100

    def __init__(self, jargs):
        self.args = json.loads(jargs)
        # setup tokens
        for t in self._extract_types(self.args['db_map'], self.args['profileset_map']):
            token = dd.FeatureFab.create(t, upgrades = self.UPGRADES, aging = self.AGING, trash = self.TRASH)
        # setup db
        self.db = dd.Database(int(self.args['db_amount']), 'database', quality = self.QUALITY)
        self.db.maximum = int(self.args['db_max'])
        for t in self.args['db_map']:
            self.db[t['type']].setShare(float(t['amount']))
        # setup profileset
        self.pset = dd.ProfileSet(float(self.args['profileset_amount']), 'profileset', quality = self.QUALITY)
        for t in self.args['profileset_map']:
            self.pset[t['type']].setShare(float(t['amount']))

    def _extract_types(self, dbmap, profmap):
        z = [x['type'] for x in (dbmap+profmap)]
        return list(set(z))

    def merge(self):
        self.db.merge(self.pset)
        out = {}
        out['amount'] = self.db.number
        out['mapping'] = [{'type':z.name, 'amount':z.share} for z in self.db.realFeatures().values()]
        out['increment'] = self.db.number - int(self.args['db_amount'])
        out['dup'] = int(self.args['profileset_amount']) - out['increment']
        return out
