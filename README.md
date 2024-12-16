# Options-Delta-Entropy
It is well-known that Shannon entropy for a random variable $X$ is a measure of uncertainty, quantifying the average amount of "information" or "surprise" inherent in the possible outcomes of $X$. The Shannon entropy is defined as:

$$
H(X) = - \sum_{i} p_i \ln(p_i)
$$

where $p_i$ represents the probability of the $i$-th outcome of $X$. This formulation shows how entropy is related to the probability distribution of the random variable: the more uncertain the outcome, the higher the entropy.

In the context of options trading, the delta $\Delta$ of an option can be interpreted as a proxy for probability. Specifically, the delta measures the sensitivity of the option's price to changes in the underlying asset's price, and can be viewed as an estimate of the probability that the option will finish in-the-money. Thus, the delta of an option can be treated as the probability of a certain event occurring (option expiring in-the-money).

One can represent an entire options chain as a random variable where the deltas of individual options represent the values of this random variable. If $\Delta_i$ is the delta of the $i$-th option in the chain, we can conceptualize the entropy of this 'delta portfolio' as a measure of the uncertainty across the various options in the chain. The entropy of the options chain can thus be written as:

$$
H = - \sum_{i} \Delta_i \ln(\Delta_i)
$$

This can be used to quantify 'uncertainty' in markets regarding expiration of certain options, and consequently $H$ can be used as a proxy to larger price moves due to the markets needing to re-hedge more.

To find the rate of change of entropy with respect to \( S \), we differentiate \( H \) with respect to \( S \):

$$
\frac{dH}{dS} = - \sum_{i} \left( \frac{d\Delta_i}{dS} \ln(\Delta_i) + \Delta_i \frac{d}{dS}\ln(\Delta_i) \right)
$$

Using the chain rule, the derivative of \( \ln(\Delta_i \) with respect to \( S \) is:

$$
\frac{d}{dS}[\ln(\Delta_i] = \frac{1}{\Delta_i} \frac{d\Delta_i}{dS}
$$

Substituting this into the expression for \( \frac{dH}{dS} \), we get:

$$
\frac{dH}{dS} = - \sum_{i} \left( \frac{d\Delta_i}{dS} \ln(\Delta_i) + \frac{1}{\Delta_i(S)} \Delta_i \frac{d\Delta_i}{dS} \right)
$$

Simplifying:

$$
\frac{dH}{dS} = - \sum_{i} \frac{d\Delta_i}{dS} \left( \ln(\Delta_i) + 1 \right)
$$

The term $\frac{d\Delta_i(S)}{dS}$ represents the sensitivity of the options delta to changes in the underlying asset price $S$. This is commonly known as gamma $\Gamma$ giving us the final formula

$$
\frac{dH}{dS} = - \sum_{i} \Gamma_i \left( \ln(\Delta_i) + 1 \right)
$$
