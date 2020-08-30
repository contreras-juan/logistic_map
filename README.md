# logistic_map
The logistic difference equation is given by
$$ x_{n+1} = r*x_{n}*(1-x_{n}$$

where $x_{n} \in [0,1]$ and $r \in [0, 4]$. It is no hard to proof that the long run equilibrium is $x = \frac{1}{1/r}$. However, the interest part is analyzing the behavior of the equilibrium value of $x$ when $r > 3$.

The iteration provided in this repository is a visualization of a pitchfork bifurcation that happens when $r > 3$.
