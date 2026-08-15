```python
import sympy as sp

lambda_plus, lambda_minus = sp.symbols('lambda_plus lambda_minus')
k_plus, k_minus = sp.symbols('k_plus k_minus')
alpha = sp.symbols('alpha')
vbar_b = sp.symbols('vbar_b')
beta = sp.symbols('beta')
sigma2 = sp.symbols('sigma2')

def answer(lambda_plus, lambda_minus, k_plus, k_minus, alpha, vbar_b, beta, sigma2):
    r"""
    Return the expression of $\Lambda$ in Sympy format, and the answer to the multiple choice question.

    Inputs
    ----------
    lambda_plus : sympy.Symbol, growth-rate state $\lambda^{+}$
    lambda_minus : sympy.Symbol, growth-rate state $\lambda^{-}$
    k_plus, k_minus, alpha: sympy.Symbol, parameters of the gamma-distribution
    vbar_b: sympy.Symbol, average birth size, $\bar v_b$
    beta: sympy.Symbol, parameter determining the degree of cell-size regulation, $0<\beta\leq 1$
    sigma2: sympy.Symbol, variance of the division noise, $\sigma^2$

    Outputs
    ----------
    Lambda : sympy.Expr, asymptotic population growth rate $\Lambda$ to first order in $\sigma^2/\bar v_b^2$.
    answer_beta, answer_sigma2 : str, answers to the following multiple choice question.
        How $\beta$ and $\sigma^2$ affect the population growth rate?
          A. Increase B. Decrease C. Not affected D. Change nonmonotonically
        answer_beta: the answer for $\beta$, one of {'A', 'B', 'C', 'D'}
        answer_sigma2: the answer for $\sigma^2$, one of {'A', 'B', 'C', 'D'}
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # Sum of parameters (S in the derivation)
    S = lambda_plus + lambda_minus + k_plus + k_minus
    
    # Product term (P in the derivation)
    P = lambda_plus * lambda_minus + k_plus * lambda_minus + k_minus * lambda_plus
    
    # The discriminant
    Delta = S**2 - 4*P
    
    # The asymptotic population growth rate Lambda_0.
    # Note: To first order in sigma^2/vbar_b^2, the correction term is 0.
    # Thus Lambda = Lambda_0 + O(sigma^4)
    Lambda = (S - sp.sqrt(Delta)) / 2
    
    # The answers to the multiple choice question.
    # Based on the analysis, Beta does not affect the growth rate.
    answer_beta = 'C' # Not affected
    
    # Based on the analysis (decoupling theorem), sigma^2 does not affect 
    # the growth rate to first order.
    answer_sigma2 = 'C' # Not affected
    
    # ---------------------------------------------------------------

    return Lambda, answer_beta, answer_sigma2
```