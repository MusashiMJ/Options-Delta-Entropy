#Main idea of a simple possible strategy using delta entropy, hence without any hedging, stop loss, take profit,...
from AlgorithmImports import *
import numpy as np

class DeltaEntropyWeighted(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2024, 11, 1)
        self.SetCash(100000)
        self.spy = self.AddEquity("SPY", leverage=1)
        self.spy.SetDataNormalizationMode(DataNormalizationMode.Adjusted)
        self.option = self.AddOption("SPY")
        self.option.SetFilter(self.OptionFilter)
        
        self.position_open = False
        self.dHDS_calculated_today = False

    def OptionFilter(self, universe):
        return universe.Strikes(-5, 5).Expiration(0, 180)

    def OnData(self, data):
        if not data.HasData or self.spy is None:
            return
        if not self.dHDS_calculated_today and self.Time.hour == 15 and self.Time.minute == 10:
            self.CalculateDHDS(data)
            self.dHDS_calculated_today = True
        if self.Time.hour == 16 and self.Time.minute == 0:
            self.dHDS_calculated_today = False

    def CalculateDHDS(self, data):
        option_chain = data.OptionChains.get(self.option.Symbol)
        if option_chain is None:
            return

        dHDS = 0
        for option in option_chain:
            if option.Expiry <= self.Time:
                continue
            if option.Greeks is None or option.OpenInterest is None:
                continue
            delta = option.Greeks.Delta
            gamma = option.Greeks.Gamma
            open_interest = option.OpenInterest

            if delta > 0:
                dHDS += open_interest * gamma * (np.log(delta) + 1)

        self.Debug(f"dH/dS Value: {dHDS}")
        if dHDS < 0.01 and not self.position_open:
            self.SetShortPosition() 
        elif dHDS > 0.0999 and self.position_open and self.Portfolio.Invested and self.Portfolio['SPY'].IsShort:
            self.SetFlatPosition()
        elif dHDS > 0.01 and not self.position_open:
            self.SetLongPosition()
        elif dHDS < 0.0100001 and self.position_open and self.Portfolio.Invested and self.Portfolio['SPY'].IsLong:
            self.SetFlatPosition()

    def SetLongPosition(self):
        self.SetHoldings("SPY", 1)
        self.position_open = True
        self.Debug("Going Long")
    
    def SetShortPosition(self):
        self.SetHoldings("SPY", -1)
        self.position_open = True
        self.Debug("Going Short")

    def SetFlatPosition(self):
        self.Liquidate("SPY")
        self.position_open = False
        self.Debug("Selling")
