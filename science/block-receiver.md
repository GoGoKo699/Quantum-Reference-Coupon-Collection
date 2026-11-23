# Block receiver near the classical threshold

The paired receiver needs only two registers at a time. A receiver with a larger buffer can spend a near-minimal number of reference copies when many signals are available. Its starting point is the same histogram upper bound as in the [collective converse](histogram-converse.md).

Reserve $T_0$ signal copies for basis measurements. Form $R$ disjoint blocks, each with one reference and $b$ further signals, so $T_0+Rb\le T$. In each block, test the projector $P_{\rm sym}$ onto the permutation-symmetric subspace and record whether it accepts or rejects. Also record the block's total label histogram. These observables commute. Measure leftover signals in the basis as well.

## How a block identifies a missing label

If the reference belongs to the present support, its normalized component is identical to the signal. The block accepts. The combined histogram has $b+1$ present draws. If its reference label is a missing $j$, the block contains exactly one $j$. With the histogram fixed, the $b+1$ possible positions of $j$ lie in orthogonal subspaces. The block has equal norm in each position after symmetrization, which has squared overlap $1/(b+1)$ with its original position sector. Hence any particular missing $j$ produces a rejected histogram with probability $b/[n(b+1)]$. Conditional on that event, its other labels are distributed as $b$ independent present draws, with repetitions retained.

A possible output of a three-register block is the rejected histogram $`\{1,1,4\}`$. If the reserved basis sample has already seen 1, then the rejected block identifies 4. Repetitions carry no additional information about 1 in this decoding step.

## Recover observed memberships, then complete

Let $K$ be the set of labels found in the reserved raw basis sample. Delete members of $K$ from each rejected histogram. Ignore any empty remainder and mark a singleton label as missing. If a larger remainder occurs, return an arbitrary $m$-set. On the event that every missing reference draw rejects and every present label in a rejected block lies in $K$, this labels precisely the missing labels observed anywhere. Treat other observed labels as present, then complete the missing set uniformly among globally unseen labels.

The failure of this event has probability at most

```math
\varepsilon_{\rm dec}=\frac{Rm}{n}
\left[\frac{1}{b+1}+b(1-1/k)^{T_0}\right].
```

The first term is the union bound for symmetrization accepting a missing reference draw. For the second, each of its $b$ present labels is independently unseen by the reserved batch with probability $(1-1/k)^{T_0}$. Independence between labels within the union bound is unnecessary. All recorded histograms together have the ordinary two-source count law. Couple the completion choice to the hypothetical decoder with true observed memberships. They coincide on the good event, giving achieved success at least the histogram bound minus $\varepsilon_{\rm dec}$, uniformly over the hidden support and phases.

For fixed $m$, $R/n\to\beta>0$ and $T/n\to\infty$, take $T_0=\lfloor T/2\rfloor$ and $b=\lfloor(T-T_0)/R\rfloor$. The bound tends to zero because $b$ diverges and $b(1-1/k)^{T_0}\to0$. In the subcritical regime $T=o(n\log n)$, the optimum converges to $(1-e^{-\beta})^m$. The limiting reference ratio needed to approach success $1-\delta$ in this regime is $-\log[1-(1-\delta)^{1/m}]$. This also gives the correct index in the [critical coupon window](histogram-converse.md#fixed-number-of-missing-labels). Fully linear budgets use a [different receiver](linear-budget.md) and a different success curve.

## Circuit for the promised block

The signal registers are identical, so permutations fixing the reference position act trivially on the incoming state and its histogram sectors. Averaging over the $b+1$ cyclic shifts acts as $P_{\rm sym}$ on that promised subspace, since the shifts are coset representatives for the permutations fixing the reference position.

Prepare a control register uniformly over $b+1$ choices, apply the corresponding register rotation coherently, undo the preparation and measure whether the control is zero. The zero-control Kraus operator is the cyclic average. Measuring the block registers in the basis afterward and discarding their order yields the histogram. Every controlled rotation preserves it. This specifies the same flag/histogram statistics as full symmetrization on the model inputs, including when the reference phases are mismatched but signal copies remain identical. The [resource account](resources.md) gives a direct circuit size bound.
