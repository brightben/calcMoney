import logging

class calcFunc():
    def __init__(self, config):
        """ initial config """
        self.logger = logging.getLogger(__name__)
        self.N = config['initialMoney']
        self.M = config['ROA']
        self.Y = config['year']
        self.X = config['savedPerMonth']
        self.Z = config['raisePerYear']

    def calcTotalMoney(self):
        self.logger.info("InitialMoney: %d, ROA: %d%%, Year: %d, SavedPerMonth: %d, RaisedPerYer: %d%%",
                          self.N, self.M*100, self.Y, self.X, self.Z*100)
        self.logger.info("Start calculate total money...")
        totalMoney = self.N
        for i in range(self.Y):
            earnMoney = totalMoney * ( self.M ) + self.X * 12 * pow(( 1 + self.Z ), i)
            totalMoney += earnMoney
            self.logger.warning("Year: %d, earnThisYear: %.3fw, totalMoney: %.3fw",
                                i+1, earnMoney/10000 , totalMoney/10000)
        return totalMoney

    def convert_size_to_bytes(self, size_str):
        """Convert human filesizes to bytes.
        """
        multipliers = {
            'kilobyte':  1024,
            'megabyte':  1024 ** 2,
            'gigabyte':  1024 ** 3,
            'terabyte':  1024 ** 4,
            'kb': 1024,
            'mb': 1024**2,
            'gb': 1024**3,
            'tb': 1024**4,
        }

        for suffix in multipliers:
            size_str = size_str.lower().strip().strip('s')
            if size_str.lower().endswith(suffix):
                return int(float(size_str[0:-len(suffix)]) * multipliers[suffix])
        else:
            if size_str.endswith('b'):
                size_str = size_str[0:-1]
            elif size_str.endswith('byte'):
                size_str = size_str[0:-4]
        return int(size_str)
