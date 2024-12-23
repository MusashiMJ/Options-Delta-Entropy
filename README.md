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

To find the change of delta entropy with respect to a price move in the underlying, we differentiate $H$ with respect to $S$:

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

where GEX is the gamma exposure. From now on we will just use $H$ interchangeable to $\hat{H}$.

# Showing positioning in Markets

Here is the weighted derivative vs underlying price for 9th December 2024

![Screenshot 2024-12-18 at 15-58-54 ](https://github.com/user-attachments/assets/68051fa0-273e-4dc3-a9c9-13b930d82ee2)

About a week later 18th December 2024

![Screenshot 2024-12-18 at 15-59-27 ](https://github.com/user-attachments/assets/757d4ed6-6c7f-4c10-bb89-72c7a564cd5f)

There is larger positive build up creating a wall around prices above and below the spot price, suggesting sensitivity to uncertainity built likely due to larger build up of calls or sold puts needing careful re-hedging if prices were to move in those directions. Notice it looks similar to call IV - put IV plotted:

![IVdiffvsStrikeSPX17:12:2024](https://github.com/user-attachments/assets/c8a8c9ff-54b8-4c04-b4b1-4d3b8a148cb9)

This is due to the fact that the derivative of delta entropy naturally contains the GEX term in there. GEX itself is a proxy for liquidity/volatility of markets due to its massive role in mechanisms of liquidity providing and how dealers are positioned, so it makes sense to see this. As an option delta gets closer to 1, the derivative of delta entropy becomes closer to net GEX. We can see the deltas with which there is larger sensitivity to uncertainty, likely where moves from re-hedging become exacerbated,

9th December 2024

![Screenshot 2024-12-18 at 16-40-47 ](https://github.com/user-attachments/assets/9ed4028a-7a3e-4190-945c-c04ffb0b6515)

18th December 2024

![Screenshot 2024-12-18 at 19-11-01 ](https://github.com/user-attachments/assets/9537a760-7190-4c18-81b6-efbd0ff53a1a)

At the time, the spot gamma levels indicated that the underlying price of SPX was at the zero-gex level (where it reverses long-short gamma), and taking a look above we can see that the spot was at the largest negative sensitivity level. A catalyst would cause an exacerbated price move, especially since we were nearing an expiration date with high associated delta entropy (20th December 2024) as can be seen ![deltaoptionsentropyFigure_1](https://github.com/user-attachments/assets/0604a586-c543-4fe8-8655-a065b2ff584f)

The FED announced rate cuts slightly after all of this data was calculated being a perfect example of a catalyst, and the markets moved as the models suggested.

![Screenshot 2024-12-18 at 20-18-35 S P 500 Index Chart — SPX Quote — TradingView](https://github.com/user-attachments/assets/b0a58c56-e6eb-40c2-b805-f624e0d7abc6)


# Tau

We introduce another function, $\tau$, that quantifies the weighted $H$ without signed contribution of delta-exposure (DEX). This can be realized as

$$
\tau = H - \sum_i OI_i \delta_i
$$

Without wights, Shannon entropy would yield the analog of $\tau$ as $\sum_i p_i \ln(p_i) - \sum_i p_i = H_{\text{Shannon}}-1$. Obviously, $\sum_i \Delta_i \neq 1$ except specific coincidental cases. The derivative of $\tau$ with respect to $S$ paints a very interesting picture; the sensitivity to unceratinty at certain prices minus the GEX.

$$
\tau' = H' - GEX = - \sum_{i} OI_i \Gamma_i \left( \ln(\Delta_i) + 1 \right) - \sum_i OI_i \Gamma_i = - \sum_{i} OI_i \Gamma_i \left( \ln(\Delta_i) + 2 \right)
$$
