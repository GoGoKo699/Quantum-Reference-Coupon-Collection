# Source model and exact recovery

A label is a known computational-basis state of an $n$-dimensional register. An unknown set $M\subset[n]$ of $m$ labels is missing, with $1\le m\lt n$. The present set is $S=[n]\setminus M$ and $k=n-m$. We know $n$ and $m$.

The two sources supply

```math
|s_{S,\phi}\rangle=\frac{1}{\sqrt{k}}\sum_{i\in S} e^{\mathrm i\phi_i}|i\rangle,
\qquad
|r_\phi\rangle=\frac{1}{\sqrt n}\sum_{i=1}^n e^{\mathrm i\phi_i}|i\rangle.
```

The phase vector $\phi$ is unknown and shared between the two sources. Conditional on $S,\phi$, the input is the product of $T$ signal copies and $R$ reference copies. The two registers of each pair have the same label convention. The receiver gets state copies, the type of each copy, and the known values of $n,m,T,R$. The model supplies neither a description of $\phi$ nor unitary access to either source.

A receiver outputs an $m$-element set $\widehat M$. The exact minimax success at a fixed budget is

```math
P^*_{n,m}(T,R)=\max_{\mathsf E}\min_{M,\phi}
\Pr_{\mathsf E}\{\widehat M=M\}.
```

The maximum permits every collective positive operator-valued measure (POVM) independent of the hidden $M,\phi$. Deterministic or randomized processing of the outcomes is part of the receiver. Distinguish three questions.

| Question | Result |
| --- | --- |
| What does a small receiver achieve? | A [pair measurement](paired-receiver.md) and classical degree counts give a finite exact-recovery guarantee. |
| What can any receiver do at finite budgets? | The [histogram converse](histogram-converse.md) gives a bound in terms of unseen labels. The [histogram Gram formulation](linear-budget.md) determines the exact optimum by finite-dimensional optimization. |
| What is the leading cost for fixed $m$? | The [linear-budget law](linear-budget.md) determines success when each count grows linearly. The [block receiver](block-receiver.md) achieves the separate sharp reference limit below the classical coupon threshold and across its critical window. |

The label axis is known even though coherent relative phases are unknown. Averaging over $\phi$ mixes the state between sectors with different total label counts and leaves same-count alternatives coherent. A joint measurement can use such alternatives. Exact matching of phases is meaningful at the copy interface, and the [mismatch analysis](phase-mismatch.md) specifies how results change when the source phases differ.

This is a copy-access result. State production, shared source calibration, receiver gates and memory have [separate costs](resources.md).
