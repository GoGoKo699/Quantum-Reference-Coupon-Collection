# Quantum Reference Coupon Collection

**How many quantum reference copies does it take to identify missing labels when the label phases are unknown?**

The signal is a uniform quantum superposition over an unknown support. A second source supplies full-support reference copies with the same unknown phase at each label. The receiver gets copies of both states and pays for each source separately. The task is to return all missing labels.

A two-register measurement turns each antisymmetric outcome into an edge joining a missing and a present label. For one missing label, two distinct edges identify it by their intersection. At fixed error this takes $O(n)$ copies from each source. With no reference, even an unrestricted collective measurement on the signals has classical coupon-collection performance and needs $\Theta(n\log n)$ signals for a fixed number of missing labels.

The exact minimax success law at linear budgets is

```math
P^*_{n,m}(T,R)\ \longrightarrow\
  \left(1-\exp\!\left[-\frac{\alpha\beta}{\alpha+\beta}\right]\right)^m,
\qquad
\frac{T}{n}\to\alpha>0,\quad
\frac{R}{n}\to\beta>0 ,
```

for fixed $m$, the number of missing labels. A histogram followed by a conditional square-root measurement attains the limit. With equal per-copy costs, balancing the two sources maximizes the limiting success at a fixed total budget. If $n\ll T\ll n\log n$ instead, a symmetry-block receiver attains the sharper reference-only limit $(1-e^{-\beta})^m$.

These limits assume that the two sources share the phase vector. An adversary allowed any fixed positive width of independent per-label mismatch drives the best linear-budget success to zero. The shared-phase model isolates a copy-resource advantage. State preparation and receiver hardware have their own costs.

## Run a receiver

1. **Pair receiver.** Take one fresh signal and one reference in the same label basis. Reversibly sort their labels into a consistent order while keeping one bit for the original order. Uncompute the comparison scratch, apply a Hadamard to the order bit for distinct labels, and read the sorted pair and sign. On a minus result, record an edge between the two labels. With one missing label and at least three labels in the alphabet, report the common endpoint of two distinct edges. With several missing labels and at least twice as many present labels, count both endpoints of every minus result, including repetitions, and apply the [degree thresholds](science/paired-receiver.md#more-than-one-missing-label). Each shot uses one copy from each source and two quantum label registers.
2. **Block receiver.** Reserve some signals for basis samples. Arrange each remaining block as `b` signals and one reference. Prepare a uniform control over the `b + 1` cyclic shifts, apply the controlled shift, undo the control preparation and test whether the control reads zero. Then measure the block labels and retain only their histogram. Measure any leftover signals in the label basis. In each rejected histogram, cross off labels seen in the reserved sample. A singleton remainder marks a missing label. Use the [completion rule](science/block-receiver.md#recover-observed-memberships-then-complete) to return exactly `m` labels. Each block uses one reference, `b` signals and `b + 1` quantum label registers, plus the control and work registers.
3. **Collective linear-budget receiver.** Hold all signal and reference registers and measure only their total histogram, preserving coherence among orderings of the same counts. Condition on the histogram, construct the specified Gram matrix for the missing-set hypotheses and perform the [square-root measurement](science/linear-budget.md#exact-finite-reduction) to read out the guess. This attains the linear-budget limiting success above. The construction specifies the collective measurement; its gate and compilation costs are separate from the copy law.

The sources supply the states with shared unknown label phases. Charge the signal and reference copies separately, including the reserved signals. See the [implementation resource account](science/resources.md) for receiver work and storage.

| Question | Scientific account |
| --- | --- |
| What do the two sources supply? | [Source model and recovery criterion](science/model.md) |
| How does an edge locate a missing label? | [Paired receiver](science/paired-receiver.md) |
| Why do unseen labels constrain all collective receivers? | [Histogram converse](science/histogram-converse.md) |
| When can extra signals reduce the reference cost? | [Symmetry-block receiver](science/block-receiver.md) |
| What is the optimal split at linear budgets? | [Finite Gram formulation and exact limiting law](science/linear-budget.md) |
| How does phase mismatch change the guarantee? | [Mismatch analysis](science/phase-mismatch.md) |
| Which physical and computational costs are counted? | [Resource accounting](science/resources.md) and [related work](references/RELATED_WORK.md) |

The [learning route](learning/README.md) connects Bartlett, Rudolph and Spekkens's review of reference frames to a four-label example, then proceeds through the receiver and converse in [30 milestones](learning/MILESTONES.md).

Run the [finite verification](verification/README.md) from the repository root with `python3 verification/check_coupon.py`.

## Purpose and contact

This repository records the science and supports self-directed learning. For discussion or potential collaboration, contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
