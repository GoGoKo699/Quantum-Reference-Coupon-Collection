# Collective converse from unseen labels

Let $c=(c_1,\ldots,c_n)$ be the label-count vector across all $T+R$ slots. Two basis words with distinct count vectors acquire different characters under the common diagonal phase action. Averaging over independent uniform phases therefore leaves separate count sectors.

For a fixed support $S$ and sector $c$, define $v_{S,c}$ as the sum of all basis words with counts $c$ whose signal slots lie in $S$. Each such word has the same amplitude in that sector, so the averaged density matrix is

```math
\overline{\rho}_S
=\bigoplus_c \frac{|v_{S,c}\rangle\langle v_{S,c}|}{k^Tn^R}.
```

The histogram law is the same as for independent classical draws, $T$ from $S$ and $R$ from $[n]$. The internal states within sectors can still be different and are important for the [collective receiver](linear-budget.md).

## Reveal the observed memberships

Use the uniform prior on the missing set. Denote the set of labels present in the histogram by $O$. For fixed $c$ and $Z=S\cap O$, the set of allowed words in $v_{S,c}$ depends only on $Z$. Suppose an auxiliary source reveals $Z$ after the histogram is known. Every remaining support has exactly the same probability of this histogram and the same conditional state. The posterior is uniform over all completions.

If $A$ counts unseen missing labels and $B$ counts unseen present labels, there are $\binom{A+B}{A}$ completions. Worst-case success is at most average success under the chosen prior, and revealing memberships can only help. Hence

```math
 P^*_{n,m}(T,R)\le
 \mathbb E\!\left[\binom{A+B}{A}^{-1}\right].
```

The expectations here and below use the two independent groups of classical draws. Their means are

```math
\mathbb EA=m(1-1/n)^R,\qquad
\mathbb EB=k(1-1/n)^R(1-1/k)^T.
```

Within each count of unseen labels, the absence indicators have nonpositive pairwise covariances. For two fixed labels, the per-draw term for neither appearing is at most the product of the one-label terms. Thus each count has variance at most its mean.

## Zero reference and scarce references

At $R=0$, every observed label belongs to $S$, so the auxiliary information is redundant. A basis measurement and random uniform completion attain the displayed upper bound for every support and phase vector. This makes the worst-case quantum experiment at zero reference exactly as informative for this task as sampling labels, at every finite budget.

If $m$ is fixed and nonzero and $n$ grows, $B$ diverges in probability at $T\le(1-\epsilon)k\log k$, and success tends to zero. All present labels are seen with high probability at $T\ge(1+\epsilon)k\log k$. These conclusions use the variance bound and the first moment, respectively, and recover the classical leading threshold.

For $1\le m\le n/3$ and $T\le(1-\epsilon)k\log k$, a receiver achieving at least $2/3$ success needs $R=\Omega_\epsilon(n\log(m+1))$. To see this, assume $R\le c_\epsilon n\log(m+1)$ for a sufficiently small positive constant. Then $\mathbb EA\ge1/\sqrt 2$ and $\mathbb EB$ diverges uniformly as $n$ grows. The second-moment bound gives $\Pr(A>0)\ge\mathbb EA/(1+\mathbb EA)$. On $A>0$, the success bound is at most $1/(B+1)$, and its expectation on this event vanishes. This separates the two resources even when extra signals are allowed below the classical threshold.

## Fixed number of missing labels

If $m$ is fixed, $R/n\to\beta\lt \infty$ and $T=o(n\log n)$, then $A$ converges in law to $\mathrm{Binomial}(m,e^{-\beta})$ while $B$ diverges in probability. The converse tends to $\Pr(A=0)=(1-e^{-\beta})^m$. The [block receiver](block-receiver.md) matches it when $T/n$ diverges.

In the coupon threshold window $T/k+R/n-\log k\to t$ with $R/n\to\beta$, the limits are independent $\mathrm{Binomial}(m,e^{-\beta})$ and $\mathrm{Poisson}(e^{-t})$. Indeed, for fixed nonnegative $a,b$ their finite joint falling factorial moments are

```math
\mathbb E[(A)_a(B)_b]=(m)_a(k)_b
   (1-(a+b)/n)^R(1-b/k)^T .
```

Convergence of the moments gives the claimed limits and the limiting success bound. The block receiver attains it for finite positive $\beta$. At $\beta=0$ the reference-free decoder already attains the limiting bound.
