# Options-Delta-Entropy
The well-known Shannon entropy for a random variable $X$ is a measure of uncertainty, quantifying the average amount of "information" or "surprise" inherent in the possible outcomes of $X$. The Shannon entropy is defined as:

$$
H(X) = - \sum_{i} p_i \ln(p_i)
$$

where $p_i$ represents the probability of the $i$-th outcome of $X$. This formulation shows how entropy is related to the probability distribution of the random variable: the more uncertain the outcome, the higher the entropy.

In the context of options trading, the delta $\Delta$ of an option can be interpreted as a proxy for probability. Specifically, the delta measures the sensitivity of the option's price to changes in the underlying asset's price, and can be viewed as a proxy for the probability that the option will finish in-the-money. Thus, the delta of an option can be treated as the probability of a certain event occurring (option expiring in-the-money).

One can represent an entire options chain as a random variable where the deltas of individual options represent the values of this random variable. If $\Delta_i$ is the delta of the $i$-th option in the chain, we can conceptualize the entropy  as a measure of the uncertainty across the various options in the chain regarding in-the-money-expirations. The entropy of the options chain can thus be written as:

$$
H = - \sum_{i} \Delta_i \ln(\Delta_i)
$$

This can be used to quantify 'uncertainty' in markets regarding expiration of certain options, and consequently $H$ can be used as a proxy to certain price moves due to the markets needing to re-hedge more.

To find the change of delta entropy with respect to $S$, we differentiate $H$ with respect to $S$:

$$
\frac{dH}{dS} = - \sum_{i} \left( \frac{d\Delta_i}{dS} \ln(\Delta_i) + \Delta_i \frac{d}{dS}\ln(\Delta_i) \right)
$$
$$
 = - \sum_{i} \left( \frac{d\Delta_i}{dS} \ln(\Delta_i) + \frac{1}{\Delta_i(S)} \Delta_i \frac{d\Delta_i}{dS} \right)
$$

Simplifying this expression gives us

$$
\frac{dH}{dS} = - \sum_{i} \frac{d\Delta_i}{dS} \left( \ln(\Delta_i) + 1 \right)
$$

The term $\frac{d\Delta_i(S)}{dS}$ is commonly known as gamma $\Gamma$

$$
\frac{dH}{dS} = - \sum_{i} \Gamma_i \left( \ln(\Delta_i) + 1 \right)
$$

# Weighted-Options-Delta-Entropy

Consider some weight $w$ affecting the overall contribution of an option to $H$, i.e

$$
\hat{H} = - \sum_{i} w_i \Delta_i \ln(\Delta_i)
$$

If we pick $w_i$ to represent the current open interest of the $i$-th option, then we find it a metric of appropriate contribution proportionate to its size-contribution to the options chain. Taking the derivative, we get

$$
\frac{d \hat{H}}{dS} = - \sum_{i} OI_i \Gamma_i \left( \ln(\Delta_i) + 1 \right)
$$

Curiously, one might notice that this can be simplified as

$$
\frac{d \hat{H}}{dS} = - \sum_{i} GEX_i \left( \ln(\Delta_i) + 1 \right)
$$

where GEX is the gamma exposure
