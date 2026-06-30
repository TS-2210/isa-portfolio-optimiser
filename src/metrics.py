import numpy as np

def sharpe_ratio(returns, risk_free=0.02):
    annual_return = returns.mean()*252
    annual_volatility = returns.std()*np.sqrt(252)
    sharpe = (annual_return-risk_free) / annual_volatility
    return round(sharpe,2)