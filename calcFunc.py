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
