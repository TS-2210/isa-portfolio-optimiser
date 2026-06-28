import numpy as np
from scipy.optimize import minimize

def portfolio_volatility(weights,cov):
    return np.sqrt(weights.T @ cov @ weights) #formula for portfolio volatility, where weights is a vector of asset weights and cov is the covariance matrix of asset returns, take transpose of weights to multiply w/covariance matrix and weights to get portfolio variance, then take square root to get volatility

def optimise_portfolio(returns):
    mean_returns = returns.mean()
    cov = returns.cov()
    num_assets = len(mean_returns)
    constraints = ({"type":"eq", "fun":lambda x: np.sum(x)-1}) #constraint that sum of weights must equal 1
    bounds = [(0,1)]*num_assets #this is a list of tuples, where each tuple represents the lower and upper bounds for each asset weight, in this case, all weights must be between 0 and 1
    initial = np.ones(num_assets)/num_assets
    result = minimize(portfolio_volatility,initial,args=(cov,), method="SLSQP",bounds=bounds, constraints=constraints) #minimize portfolio volatility using the SLSQP method, with the initial guess for weights being equal allocation to all assets, and the bounds and constraints defined above
    return result.x