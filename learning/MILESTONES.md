# Project understanding map

The map has **11 background/preliminaries milestones** and **19 narrative/innovation milestones**. The first phase connects the two sources, the common phase action and exact-set inference. The second develops the pair receiver, the collective occupancy ceiling and two receivers for different copy regimes, then relates their conclusions. The [Bartlett–Rudolph–Spekkens bridge](BRS_BRIDGE.md) identifies the review sections and works through a pair and a block using the same four labels.

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | [M01](#m01-present-and-missing-labels)–[M04](#m04-basis-sampling-and-coupons) | Inputs, output and the basis-sampling task |
| Background/preliminaries | [M05](#m05-a-shared-phase-profile)–[M08](#m08-permutations-and-symmetric-states) | Relative amplitudes, histogram sectors and symmetry measurements |
| Background/preliminaries | [M09](#m09-worst-case-success-and-symmetry)–[M11](#m11-the-operational-question) | Minimax reasoning and the full resource question |
| Narrative/innovation | [M12](#m12-the-antisymmetric-edge)–[M16](#m16-the-finite-pair-guarantee) | A label-resolved pair measurement becomes a support decoder |
| Narrative/innovation | [M17](#m17-twirling-the-whole-input)–[M21](#m21-the-occupancy-ceiling) | Histogram ambiguity bounds every measurement |
| Narrative/innovation | [M22](#m22-a-block-rejects-a-missing-label)–[M25](#m25-the-sharp-reference-budget) | Larger blocks attain the ceiling with growing signal budget per label |
| Narrative/innovation | [M26](#m26-fixed-missing-count-at-linear-budgets)–[M30](#m30-the-complete-copy-tradeoff) | Collective linear-budget discrimination, phase stability and full synthesis |

## Phase I. Background and preliminaries

### M01 Present and missing labels

**Central question.** What is unknown when the coordinate basis is known?

**Understanding target.** From the known alphabet size $`n`$ and present-set size $`k`$, define the unknown present set $`S`$, its complement $`M`$ and the missing count $`m=n-k`$. Explain why identifying $`M`$ gives the entire support.

**Prerequisites.** None within this map.

**Conceptual connection.** A missing label has zero signal amplitude. The receiver's measurement basis and the index assigned to each possible label are fixed in advance.

**Canonical sources.** [Model](../science/model.md).

### M02 The two sources

**Central question.** What does a single specimen from each source contain?

**Understanding target.** Read the signal as a normalized sum over $`S`$ and the reference as a normalized sum over all $`n`$ labels. Explain how the shared unknown phase for a label relates its coefficients across the two states.

**Prerequisites.** M01.

**Conceptual connection.** The reference has a known basis distribution with an unknown phase profile. With $`S`$ and the phases fixed, the received state is a tensor product, so independence conditional on those parameters is consistent with a single unknown profile shared by every register.

**Canonical sources.** [State-copy model](../science/model.md) · [Reference as a quantum system](BRS_BRIDGE.md#targeted-reading).

### M03 The exact-set score and cost

**Central question.** What constitutes one successful run, and what does it spend?

**Understanding target.** Score an output by whether the whole missing set is correct, and keep sample counts $`T`$ and $`R`$ attached to the signal and reference sources. Explain which resources would change the access model, including a source preparation unitary and its inverse.

**Prerequisites.** M01–M02.

**Conceptual connection.** Copy counts are distinct from circuit gates and quantum storage. Rejection outcomes and reference copies used for calibration or comparison still incur costs.

**Canonical sources.** [Model and admissible measurements](../science/model.md) · [Resources](../science/resources.md).

### M04 Basis sampling and coupons

**Central question.** What can be inferred from a list of labels measured one register at a time in the coordinate basis?

**Understanding target.** Explain why a signal outcome certifies a present label, while a reference outcome is uniform over the full alphabet and independent of $`S`$. Recognize the usual waiting time to see the last few present labels.

**Prerequisites.** M01–M03.

**Conceptual connection.** An unobserved label in the signal record could be missing or merely unseen. Exact recovery lets the receiver guess among completions when sufficient evidence has not arrived.

**Canonical sources.** [Sources and score](../science/model.md) · [No-reference optimum](../science/histogram-converse.md).

### M05 A shared phase profile

**Central question.** How does the phase nuisance act on multiple registers?

**Understanding target.** Represent the unknown action by a diagonal unitary with entries $`e^{i\phi_i}`$ on the label basis, and apply the same unitary to all source copies. Explain why a single common increment to every $`\phi_i`$ is physically irrelevant.

**Prerequisites.** M01–M02.

**Conceptual connection.** The model has one phase per label, shared between the signal and reference. Its joint average differs from independent dephasing of each register.

**Canonical sources.** [Shared profile](../science/model.md) · [Review §§II.B–II.C](BRS_BRIDGE.md#targeted-reading).

### M06 Interference between ordered words

**Central question.** How can a receiver compare two amplitudes without estimating the phase profile?

**Understanding target.** For two distinct labels $`i,j`$, calculate the phase of the words $`|i,j\rangle`$ and $`|j,i\rangle`$. Explain how sum and difference measurements can depend on amplitude magnitudes and support membership even when the common factor is unknown.

**Prerequisites.** M02, M05.

**Conceptual connection.** The ordered words have the same total count of every label. Swapping the positions preserves their joint phase and lets their amplitudes interfere.

**Canonical sources.** [Worked pair](BRS_BRIDGE.md#a-pair-records-a-cross-edge) · [Paired receiver](../science/paired-receiver.md).

### M07 Histograms and phase sectors

**Central question.** Which coherent amplitudes survive the joint phase average?

**Understanding target.** Relate a word's phase to its histogram $`c`$ and explain why averaging over every label phase removes cross-histogram matrix elements. Distinguish a measurement of $`c`$ from reading the full ordered word.

**Prerequisites.** M05–M06.

**Conceptual connection.** Histogram sectors play the role of fixed-charge spaces. The receiver can learn a sector label and still act on its internal superpositions.

**Canonical sources.** [One charge to a histogram](BRS_BRIDGE.md#from-one-charge-to-a-histogram) · [Histogram decomposition](../science/histogram-converse.md).

### M08 Permutations and symmetric states

**Central question.** What does a projection onto the symmetric subspace keep?

**Understanding target.** Interpret the group-average projector onto states fixed by every register permutation. Identify the normalized sum over distinct words in a fixed histogram as its symmetric direction, including histograms containing repeated labels.

**Prerequisites.** M06–M07.

**Conceptual connection.** Permuting registers preserves the histogram, so a symmetry measurement can retain the labels that the decoder needs.

**Canonical sources.** [Worked block](BRS_BRIDGE.md#a-block-increases-the-rejection-probability) · [Symmetric test](../science/block-receiver.md).

### M09 Worst-case success and symmetry

**Central question.** How can an average-case argument certify a worst-case bound?

**Understanding target.** Explain why the average success under a chosen prior upper-bounds the worst-case success of each strategy. Explain why a phase-invariant, label-symmetric receiver with a fixed success value over the parameters can give a matching minimax guarantee.

**Prerequisites.** M03, M05, M07.

**Conceptual connection.** Averaging the nuisance in a proof grants no phase data to the learner. Symmetrizing a receiver by known relabelings can provide the same performance for every possible support of the promised size.

**Canonical sources.** [Model](../science/model.md) · [Converse and uniform support prior](../science/histogram-converse.md).

### M10 Unseen labels as counting variables

**Central question.** How do draws with replacement produce estimates for the number of unseen labels?

**Understanding target.** Express the number unseen as a sum of absence indicators. Compute the probability that a specified group of labels is absent from a sequence of independent draws, then connect this event to first and factorial moments.

**Prerequisites.** M04, M07.

**Conceptual connection.** A present label may appear in either source, while a missing label can appear only in the reference. This difference produces separate unseen counts with different behavior as $`T`$ and $`R`$ grow.

**Canonical sources.** [Occupancy estimates](../science/histogram-converse.md).

### M11 The operational question

**Central question.** Where can a quantum receiver improve the copy budget for exact support recovery?

**Understanding target.** Assemble the model and distinguish three relevant cases: individual basis readout, collective measurements without reference copies, and collective measurements using both sources. Formulate the search for an achievable success and an upper bound in the same budget model.

**Prerequisites.** M03–M10.

**Conceptual connection.** The reference changes what can interfere within a histogram. Whether that matters for learning depends on keeping the coordinates and translating their joint outcomes into a correct set.

**Canonical sources.** [Model](../science/model.md) · [Overview](../science/README.md) · [Converse](../science/histogram-converse.md).

## Phase II. Narrative and innovation

### M12 The antisymmetric edge

**Central question.** Why can a pair measurement certify that exactly one of two labels is missing?

**Understanding target.** Compute the antisymmetric outcome probability for two present labels, two missing labels and a cross edge. Explain why a specified cross edge occurs with probability $`1/(2nk)`$ per pair.

**Prerequisites.** M01–M02, M06–M07.

**Conceptual connection.** Two present labels supply equal ordered amplitudes, two missing labels supply neither, and a cross edge supplies exactly one. The measurement makes that pattern into observable evidence.

**Canonical sources.** [Worked pair](BRS_BRIDGE.md#a-pair-records-a-cross-edge) · [Pair probabilities](../science/paired-receiver.md).

### M13 Keeping both label identities

**Central question.** Why is the two-outcome symmetry test alone insufficient for the edge decoder?

**Understanding target.** Distinguish the binary symmetric/antisymmetric record from the refined record that also names both endpoints. Describe how coherent sorting and an orientation measurement retain interference before the labels are recorded.

**Prerequisites.** M07–M08, M12.

**Conceptual connection.** A binary result can compare the two states. Support learning needs coordinate-specific evidence so it can merge information across repeated pairs.

**Canonical sources.** [Measurement and receiver](../science/paired-receiver.md) · [Gate and storage resources](../science/resources.md).

### M14 Local evidence for one missing label

**Central question.** When do two edge outcomes identify a missing label exactly?

**Understanding target.** For $`m=1`$, recover the label by intersecting two distinct edge records. Explain why repeating the same edge leaves an ambiguity about its endpoints.

**Prerequisites.** M01, M12–M13.

**Conceptual connection.** An isolated edge only certifies a relation. Distinct edges can turn the relation into membership evidence even before every present label has been seen.

**Canonical sources.** [Worked pair](BRS_BRIDGE.md#a-pair-records-a-cross-edge) · [Paired receiver](../science/paired-receiver.md).

### M15 Degree frequencies with several missing labels

**Central question.** Which evidence replaces edge intersection when several labels can be missing?

**Understanding target.** Sum the edge probability over valid partners. From $`L`$ independent pairs, obtain expected degrees $`L/(2n)`$ for missing labels and $`Lm/(2nk)`$ for present labels.

**Prerequisites.** M12–M14.

**Conceptual connection.** Each label's degree is a sum of independent indicators across pair attempts. Degrees at different labels can be dependent because one edge updates two labels.

**Canonical sources.** [Degree analysis](../science/paired-receiver.md).

### M16 The finite pair guarantee

**Central question.** When do all empirical degrees separate at the same time?

**Understanding target.** Explain how concentration for each degree and a union bound give exact support recovery with $`O(n\log(m/\delta))`$ copies of each source for $`k\geq 2m`$ and target failure probability $`\delta`$. Describe why the present-label tail can be much smaller when $`k/m`$ is large.

**Prerequisites.** M03, M14–M15.

**Conceptual connection.** A small expected degree at a present label reduces its tail enough to control false positives over a large alphabet. The total guarantee is for the whole set, at the advertised copy count for both sources.

**Canonical sources.** [Paired receiver and finite estimates](../science/paired-receiver.md).

### M17 Twirling the whole input

**Central question.** What state must an arbitrary receiver distinguish after averaging over the phase nuisance?

**Understanding target.** Build the vector in a given total histogram by summing every allowed ordered word in it, with the restriction that signal slots contain present labels. Identify the squared norm of this unnormalized vector as the count of its allowed words.

**Prerequisites.** M02, M07, M09.

**Conceptual connection.** Each histogram block is rank one when it has positive probability. The same formula retains sector probabilities and the coherent vectors needed for collective discrimination.

**Canonical sources.** [Collective histogram decomposition](../science/histogram-converse.md).

### M18 What a histogram leaves ambiguous

**Central question.** What would remain unknown if the receiver were told the true membership of every observed label?

**Understanding target.** Given the histogram and these memberships, describe the residual choices of the missing set. With $`A`$ unseen missing labels and $`B`$ unseen present labels, explain why there are $`\binom{A+B}{A}`$ equiprobable completions.

**Prerequisites.** M01, M09, M17.

**Conceptual connection.** Changing unseen memberships while holding their counts fixed leaves the allowed words and the likelihood unchanged. Even joint measurements of all the copies cannot distinguish those residual choices.

**Canonical sources.** [Side information and indistinguishable completions](../science/histogram-converse.md).

### M19 The exact no-reference benchmark

**Central question.** Why are there no extra recoverable coupon identities when $`R=0`$?

**Understanding target.** Show that every observed label must be present in this case. Conclude that basis sampling and a uniform guess over completions attain the upper bound from the histogram argument.

**Prerequisites.** M04, M09, M17–M18.

**Conceptual connection.** The benchmark applies to arbitrary collective measurements in the unreferenced common-phase model. A receiver with a known phase profile belongs to a different access model.

**Canonical sources.** [No-reference result](../science/histogram-converse.md) · [Calibrated coupon collection](../references/RELATED_WORK.md).

### M20 Two occupancy scales

**Central question.** How do the two sources change which labels remain unseen?

**Understanding target.** Derive the means $`m(1-1/n)^R`$ for unseen missing labels and $`k(1-1/n)^R(1-1/k)^T`$ for unseen present labels. Explain how simultaneous absence probabilities yield concentration and identify the coupon threshold.

**Prerequisites.** M10, M17–M19.

**Conceptual connection.** Additional signal copies lower the number of unseen present labels. They cannot directly reveal any missing label. Additional reference copies change both unseen counts.

**Canonical sources.** [Occupancy calculation and lower bound](../science/histogram-converse.md).

### M21 The occupancy ceiling

**Central question.** When does success require every missing label to have appeared at least once in the reference record?

**Understanding target.** If the number of unseen present labels diverges, use the completion bound to show that runs with an unseen missing label contribute vanishing success. For fixed $`m`$ and $`R/n\to\beta`$, identify $`(1-e^{-\beta})^m`$ as the resulting upper bound.

**Prerequisites.** M18, M20.

**Conceptual connection.** The upper bound gives the receiver the true memberships of observed labels. Attaining it requires a measurement and inference procedure that can recover those memberships using the copies actually supplied.

**Canonical sources.** [Subcritical occupancy ceiling](../science/histogram-converse.md).

### M22 A block rejects a missing label

**Central question.** What changes when one reference is compared with $`b`$ signal copies together?

**Understanding target.** In a histogram containing a missing label, partition the words by the register holding its single occurrence. Derive the symmetric projection probability $`1/(b+1)`$, including when some present labels repeat. Explain why all-present components accept the symmetric test.

**Prerequisites.** M08, M12, M17.

**Conceptual connection.** The missing label can occupy only the reference slot in the input but any slot in the symmetrized vector. The ratio is set by the number of slots.

**Canonical sources.** [Worked block](BRS_BRIDGE.md#a-block-increases-the-rejection-probability) · [Block measurement](../science/block-receiver.md).

### M23 Putting a name to the rejection

**Central question.** How does a block rejection become evidence about a particular label?

**Understanding target.** Combine the block's histogram with a reserved sample of basis-measured signals. Explain when removing the certified present labels leaves precisely the missing label in the block.

**Prerequisites.** M04, M08, M22.

**Conceptual connection.** The raw signal sample is an independent membership witness. The overall decoder also keeps accepted block histograms and any remaining raw labels to determine which labels have been seen at all.

**Canonical sources.** [Block decoder](../science/block-receiver.md).

### M24 Comparing the block receiver with the converse

**Central question.** What errors can prevent the practical decoder from reproducing the converse's side information?

**Understanding target.** Decompose the possible gap into missed block rejections and present labels absent from the reserved sample. Explain why the expected number of missing reference draws is $`Rm/n`$ and how it weights the finite error bound.

**Prerequisites.** M20–M23.

**Conceptual connection.** A coupling compares the real receiver and the side-information decoder under the same total histogram. On successful membership reconstruction they can use the same guess for unseen labels.

**Canonical sources.** [Finite block guarantee](../science/block-receiver.md) · [Histogram bound](../science/histogram-converse.md).

### M25 The sharp reference budget

**Central question.** When can the block receiver attain the occupancy ceiling, and how many references does it then need?

**Understanding target.** For fixed $`m`$, $`T/n\to\infty`$, $`T/(n\log n)\to 0`$ and $`R/n\to\beta`$, connect the vanishing gap to the limiting success $`(1-e^{-\beta})^m`$. Solve that expression for the reference coefficient at a target success.

**Prerequisites.** M21, M24.

**Conceptual connection.** Increasing available signals per reference removes the measurement loss, while a finite reference rate leaves a separate chance that a missing label was never represented.

**Canonical sources.** [Asymptotic attainability](../science/block-receiver.md) · [Subcritical occupancy estimate](../science/histogram-converse.md).

### M26 Fixed missing count at linear budgets

**Central question.** Why does fixed signal density require a different analysis?

**Understanding target.** For a fixed positive missing count $`m`$, describe the two simultaneous limits $`T/n\to\alpha>0`$ and $`R/n\to\beta>0`$. Explain why one cannot enlarge each reference block without reducing the number of references processed, and why the histogram still leaves several candidate missing sets.

**Prerequisites.** M17–M18, M22, M25.

**Conceptual connection.** An occupancy upper bound with perfect membership side information fails to account for the distinct quantum states that a finite-density receiver must actually discriminate.

**Canonical sources.** [Linear-budget model](../science/linear-budget.md) · [Block resources](../science/block-receiver.md).

### M27 Candidate states and their Gram matrix

**Central question.** What makes two candidate missing sets hard to distinguish within a fixed histogram?

**Understanding target.** For a candidate set, require every occurrence of every member to occupy a reference slot. Show why the overlap between two unnormalized candidate vectors is the fraction of words satisfying this restriction for their union. Distinguish that overlap from the sector probability or the overlap of the normalized states.

**Prerequisites.** M07, M17, M26.

**Conceptual connection.** A Gram calculation compares which source-slot allocations are permitted without needing to learn the label phases. The histogram-dependent square-root measurement uses this information to assign a missing-set guess.

**Canonical sources.** [Histogram Gram matrices and receiver](../science/linear-budget.md).

### M28 The collective linear-budget law

**Central question.** How do the two linear copy budgets combine in the optimal success?

**Understanding target.** Interpret the limit $`(1-\exp[-\alpha\beta/(\alpha+\beta)])^m`$ for fixed positive $`m`$. Explain how approximating fixed-size reference-slot assignment by independent assignment isolates distinguishable components for competing missing sets. Compare the limit with the occupancy ceiling it approaches as the signal density grows.

**Prerequisites.** M09, M21, M26–M27.

**Conceptual connection.** A fixed total rate has the largest exponent at equal signal and reference densities. The theorem concerns fixed $`m`$ and a receiver that may jointly access all copies. The size of its measurement and the cost of supplying copies are separate resources.

**Canonical sources.** [Optimal linear-budget success](../science/linear-budget.md) · [Copy resources](../science/resources.md).

### M29 Phase matching as a model assumption

**Central question.** What changes if the two sources use different phases for the same label?

**Understanding target.** Compare the two amplitudes for a present–present pair and explain how relative mismatch creates false edges. Distinguish a fixed positive bound on arbitrary labelwise mismatch from a bound $`\eta_n`$ that shrinks fast enough that $`T\eta_n^2\to 0`$.

**Prerequisites.** M05–M06, M12, M16, M22.

**Conceptual connection.** At fixed positive mismatch width the optimum worst-case success vanishes at linear budgets, even with collective access. In the stated shrinking regime, continuity in trace distance preserves the matched-phase limit. A common shift of all labelwise mismatches only changes a global phase.

**Canonical sources.** [Phase mismatch](../science/phase-mismatch.md) · [Exact shared-profile model](../science/model.md).

### M30 The complete copy tradeoff

**Central question.** How do the source promise, measurements, inference and lower bounds fit together?

**Understanding target.** Relate the exact $`R=0`$ benchmark, the finite paired construction, the sharp subcritical reference coefficient and the fixed-missing-count linear-budget law. Identify the assumptions and resource costs of each, including the consequence of phase mismatch, and use the worked example to explain what a coherent comparison preserves.

**Prerequisites.** M16, M19, M25, M28–M29.

**Conceptual connection.** The common label phases determine what can interfere. The receiver converts that interference to evidence about membership, and the converse identifies which distinctions remain inaccessible with the supplied samples. Finite verification checks the formulas on enumerated instances alongside the analytic proofs of the scaling limits.

**Canonical sources.** [Scientific account](../science/README.md) · [Verification](../verification/README.md) · [Related work](../references/RELATED_WORK.md).
