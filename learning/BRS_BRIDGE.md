# From quantum reference frames to support recovery

The educational anchor is Stephen D. Bartlett, Terry Rudolph, and Robert W. Spekkens, *Reference frames, superselection rules, and quantum information*, **Reviews of Modern Physics 79**, 555–609 (2007). Section numbers below follow the published text. The authors' open version is arXiv v3, dated 10 April 2007. [Journal article](https://doi.org/10.1103/RevModPhys.79.555) · [Open text](https://arxiv.org/pdf/quant-ph/0610030v3)

## Targeted reading

| Review section | What to carry into this project | Project development |
|---|---|---|
| II.B and II.C | A shared unknown phase acts on all registers jointly. Averaging over the group removes coherence between charges and retains coherence within a charge sector. | [Model](../science/model.md) and [histogram converse](../science/histogram-converse.md) |
| III.A.1 | A fixed-charge space can encode information about how excitations are distributed. | [Paired receiver](../science/paired-receiver.md) |
| IV.A.1 and IV.A.4 | Include a physical reference as part of the joint quantum description. Relative amplitudes can survive a common phase action. | [Sources and copy access](../science/model.md) |
| VI.A.2 | A joint measurement can extract relative information with a bounded reference. | [Block receiver](../science/block-receiver.md) and [linear copy budgets](../science/linear-budget.md) |

## From one charge to a histogram

In the review's phase example, a basis state with charge $`q`$ acquires a factor $`e^{iq\theta}`$. Here a known coordinate $`i`$ has its own phase $`\phi_i`$. A word formed by placing labels in signal and reference registers acquires $`e^{i\sum_i c_i\phi_i}`$, where $`c_i`$ is the total number of occurrences of $`i`$. Thus the role of charge is played by the vector $`c`$. A common increment to all phases contributes the same global phase to every word of the same length.

The joint phase average removes coherence between different histograms. It preserves the relative amplitudes of every pair of words with the same histogram, even when one word moves a label from a signal register to a reference register. A histogram measurement retains those amplitudes. Recording the label of each individual register would resolve the words themselves and remove their interference.

The full-support reference shares the entire unknown phase profile with the signal. The receiver consumes a specified number of reference copies and never needs the phase values. The support-recovery decoder, its copy-budget estimates, and the converse under arbitrary collective measurements follow from the project analysis. [Histogram proof](../science/histogram-converse.md) · [Copy and operation costs](../science/resources.md)

## One missing label, two ways to compare

Take $`n=4`$, with present set $`S=\{1,2,3\}`$ and missing set $`\{4\}`$. The receiver knows the register order and the size of $`S`$. In this example the order is reference first. The receiver does not know which label is missing.

### A pair records a cross edge

Consider the joint histogram with one occurrence each of labels 1 and 4. The word $`|4,1\rangle`$ has amplitude $`e^{i(\phi_1+\phi_4)}/\sqrt{12}`$. The word $`|1,4\rangle`$ has amplitude zero because the signal register never carries label 4. The measurement that distinguishes the symmetric and antisymmetric combinations of these two words fires the antisymmetric outcome with probability $`1/24`$ per pair.

For the histogram containing labels 1 and 2, both orders occur with equal amplitudes. The antisymmetric amplitude cancels. Thus an antisymmetric outcome names an unordered edge with exactly one missing endpoint. If two of the outcomes are $`\{1,4\}`$ and $`\{2,4\}`$, their common endpoint identifies the sole missing label. Each attempt spends one signal and one reference copy, including attempts with a symmetric outcome. [Pair measurement and degree decoder](../science/paired-receiver.md)

### A block increases the rejection probability

Take one reference and two signals. In the histogram with labels 1, 2, and 4, only two of the six permutations are initially present, $`|4,1,2\rangle`$ and $`|4,2,1\rangle`$. Their amplitudes agree. For the normalized sum of those two words, the squared overlap with the normalized symmetric sum of all six is $`2/6=1/3`$. The block rejects the symmetric sector with conditional probability $`2/3`$.

The receiver can obtain this result and the three labels together because the histogram projector and the symmetric projector commute. If separately measured signal copies have already shown labels 1 and 2, a rejection with this histogram identifies 4. If either present label has yet to be confirmed, the histogram alone leaves ambiguity. The block analysis charges the extra signal copies, and gives a bound on the chance that the raw sample fails to certify a needed present label. [Block receiver and error bound](../science/block-receiver.md)

## From individual outcomes to the estimates

The pair proof repeats the edge measurement and separates the missing and present degree distributions. The histogram converse counts assignments still possible after granting membership information about every observed label. The block receiver acquires that information with high probability when signal copies per reference grow. With a fixed number of missing labels and both budgets linear, the conditional Gram matrix describes how much a joint receiver can distinguish among the possible missing sets within the same histogram. [Finite pair guarantee](../science/paired-receiver.md) · [Occupancy bound](../science/histogram-converse.md) · [Collective linear law](../science/linear-budget.md)

Return to the [milestone map](MILESTONES.md) for the order in which these ideas build on one another.
