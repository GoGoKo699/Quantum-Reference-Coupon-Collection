# Fixed unknown phase mismatch

The [matched-phase receiver](linear-budget.md) uses one unknown phase vector for both sources. Suppose instead that the reference carries phases $\phi_j$ and the signal carries phases $\phi_j+\theta_j$ on its support, with individual mismatches bounded by $|\theta_j|\le\eta$. The receiver knows $\eta$. The mismatches are arbitrary and remain fixed throughout the run.

Fix $\eta>0$ and a positive missing-set size $m$. If $T,R=O(n)$, the optimal worst-case success over the missing set, common phases and mismatches tends to zero as $n\to\infty$, even for a collective measurement. This holds for every fixed positive $\eta$.

## A reference state for the converse

Use an auxiliary full-support input to compare the possible missing-set states. In this input the signal has amplitude $1/\sqrt n$ on every label, and the reference is unchanged. Average over independent uniform common phases and independent mismatches uniform on $[-\eta,\eta]$. Denote the resulting density by $\rho_0$. Apply the same averaging to the true input for each missing set $M$, obtaining $\rho_M$.

The common-phase average is block diagonal in the total label histogram $c$. Fix one sector and a test vector in that sector. For fixed values of the mismatches outside $M$, its inner product with the full-support input is a polynomial in the variables $z_j=e^{i\theta_j}$ for $j\in M$. The exponent of $z_j$ counts the signal slots carrying label $j$, so it lies between zero and $c_j$. The constant coefficient is the inner product for the true input multiplied by $(k/n)^{T/2}$, with $k=n-m$. Indeed, extracting the constant coefficient keeps exactly the words with no occurrence of $M$ in the signal slots.

Let $H_K$ be the single-angle moment matrix with entries $(H_K)_{a,b}=\mathbb E\,e^{i(b-a)\theta}$ for $0\le a,b\le K$. It is positive definite. A polynomial of degree at most $K$ that vanishes on the full arc has all coefficients zero. Write $\lambda_K>0$ for its least eigenvalue. On any sector satisfying $c_j\le K$ for all $j\in M$, the product of the moment matrices bounds the integral of the squared modulus below by $\lambda_K^m$ times the squared modulus of the constant coefficient.

Let $\rho_M^{\le K}$ keep only the sectors with $c_j\le K$ for each $j\in M$. The squared-amplitude bound, integrated over the mismatches outside $M$, holds for every test vector in each retained sector. After taking the direct sum over sectors, it gives

```math
\rho_M^{\le K}\preceq\left(\frac{n}{k}\right)^T\lambda_K^{-m}\rho_0.
```

## Bounding collective success

For any measurement with missing-set effects $E_M$, its uniform-prior success under the phase and mismatch distribution obeys

```math
\frac{1}{\binom{n}{m}}\sum_M\operatorname{Tr}(E_M\rho_M)
\le
\frac{(n/k)^T\lambda_K^{-m}}{\binom{n}{m}}
+
m\Pr\left\{\operatorname{Bin}\!\left(R,\frac1n\right)>K\right\}.
```

For the first term use the positive-semidefinite bound and $\sum_M E_M=I$. For the second term use that each missing label appears only in reference registers, so its total histogram count has the indicated binomial distribution. This statement about counts holds even when the phase mismatch is unknown.

For fixed $K$, the first term tends to zero because $m$ is fixed and $T=O(n)$. The second term can be made uniformly small by increasing $K$ because $R/n$ stays bounded. Worst-case success is bounded above by this prior-averaged success. The argument accommodates any fixed interval width $\eta>0$, with the limit in $n$ taken before the bound on the count cutoff is removed.

## Shrinking mismatch

If the allowed width $\eta_n$ shrinks with $n$ and $T\eta_n^2\to0$, the matched-phase receiver retains its limiting success. The squared overlap of the signals with and without mismatch is at least $1-\eta_n^2$ for all sufficiently large $n$, because the real part of the average of $e^{i\theta_j}$ over the signal support is at least $\cos\eta_n$. The trace distance between the two pure $T$-copy inputs is at most $\sqrt{T}\,\eta_n$. The reference is identical in the two inputs. Alternatively, choose the matched model to have the signal's phases on the support. Extend those phases to missing labels by the reference phases there. Only the reference then changes, with a distance bound of $\sqrt{R}\,\eta_n$. Thus $\min(T,R)\eta_n^2\to0$ suffices, uniformly over supports and mismatches. The fixed-width converse and this shrinking-width guarantee leave a range of intermediate scalings open.

## Independently unknown source phases

If the signal and reference phase vectors range independently over all
diagonal phases, the minimax success probability equals the classical
coupon-collector success with $T$ signal draws for every $R$. Average over
independent uniform phase vectors for the two sources and a uniform prior
on size-$k$ supports. The averaged input factors into the twirled signal
input and a reference state independent of the support. Any measurement on
this product induces a measurement on the signal alone, since the same
fixed reference state could be appended for every hypothesis. In a signal
histogram sector, the state is identical for every support containing all
observed labels. Measuring those labels and uniformly completing them to
size $k$ attains the resulting uniform-prior bound at every support and
phase vector. [Signal-only converse](histogram-converse.md)

## Spurious rejections in a block

Write $z_S=k^{-1}\sum_{i\in S}e^{i\theta_i}$ and $v_S=1-|z_S|^2$. A block
contains one reference and $b$ signals. Its label histogram has the
matched-model distribution, because all word probabilities are unchanged.
If the histogram contains a missing label, that label occurs exactly once
in the reference. Every word in the sector then acquires the same total
mismatch phase, so the conditional rejection probability is still
$b/(b+1)$.

For an all-present histogram $c$, the fraction of words with reference
label $i$ is $c_i/(b+1)$. Their mismatch phases coincide up to a common
factor with $e^{-i\theta_i}$, because the total of the mismatches over all
slots is fixed by the histogram. Projecting onto the normalized symmetric
sum gives conditional acceptance probability

```math
\left|\sum_{i\in S}\frac{c_i}{b+1}e^{-i\theta_i}\right|^2.
```

Conditioned on all labels being present, the histogram has the law of
$b+1$ independent uniform draws from $S$. Its mean acceptance probability
is $(1+b|z_S|^2)/(b+1)$. The probability of an all-present rejection is

```math
q_b=\frac{k}{n}\frac{b}{b+1}v_S.
```

This is also the exact total variation distance between the matched and
mismatched one-block laws of the histogram and comparison flag.
For a pair, the antisymmetric probability for a present-present edge
$\{i,j\}$ is $(1-\cos(\theta_i-\theta_j))/(nk)$. Every missing-present edge
keeps probability $1/(2nk)$. The total false-edge probability is $q_1$.
[Paired receiver](paired-receiver.md)

## Recovery with signal samples for validation

Use the block decoder with $T_0$ independent basis-measured signals, $R$
blocks, and $b$ signals per reference. Strip each rejected histogram of every label seen in the basis sample.
Ignore an empty remainder. An all-present rejection can only mislead
the decoder if at least one of its labels was not seen among the
$T_0$ signals. Given the rejected histogram, this occurs with probability
at most $(b+1)(1-1/k)^{T_0}$ by a union bound and independence.

The decoder agrees with the decoder told all observed memberships, using the same completion randomness, when
every block containing a missing label rejects, all present labels in
such blocks were seen in the basis sample, and the basis sample contains
all the labels of each spurious rejection. The probability of disagreement
is at most

```math
\frac{Rm}{n}\left[\frac{1}{b+1}+b(1-1/k)^{T_0}\right]
+
R\frac{k}{n}\,b v_S(1-1/k)^{T_0}.
```

The first term is the matched-model gap bound. The joint histogram law
is unchanged, so subtracting the displayed bound from the
[finite histogram bound](histogram-converse.md) gives a lower bound on
this decoder's probability of success. The same construction retains
the matched-model limit when the first term vanishes and the mismatch
class satisfies

```math
Rb\sup_{S,\theta}v_S(1-1/k)^{T_0}\longrightarrow 0.
```

The phase variance $v_S$ is at most $k^{-1}\sum_{i\in S}|\theta_i|^2$,
since the complex mean minimizes the sum of squared distances to
$e^{i\theta_i}$ and the chord from $1$ is at most $|\theta_i|$.

For example, fix $m$, take $R/n\to\beta>0$, and use
$T_0=\lfloor\gamma k\log k\rfloor$ with $0<\gamma<1$ and
$1\ll b\ll\log n$. If $\sup_{S,\theta}v_S=o(n^{\gamma-1}/b)$, the
receiver attains the matched-model limit $(1-e^{-\beta})^m$ throughout
the mismatch class. When this class includes the matched model, its
minimax value has the same limit by the matched-model converse.
[Block decoder](block-receiver.md)
