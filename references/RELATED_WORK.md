# Related work

## Coupon collection with quantum samples

[Arunachalam et al.](https://arxiv.org/abs/2002.07688) study exact support recovery from equal-positive-amplitude quantum samples. Access to the known full-support direction gives a copy advantage for sparse missing sets. [Bab Hadiashar, Nayak and Sinha](https://arxiv.org/abs/2301.02227) sharpen sample lower bounds, and [Nayak and Sinha](https://arxiv.org/abs/2403.03295) obtain a matching leading-order algorithm under that phase convention. We inherit the task and the idea of learning the complement. Here the full-support direction is unknown and each supplied reference copy counts.

Nayak and Sinha also study padded coupons, where unknown basis-valued tags occupy a separate register. Their nuisance average approximately restores classical sample complexity. That occupancy reduction is a precedent for the converse. Here averaging scalar phases shared by both sources leaves useful coherence within the total-count sectors. The exact limiting optimum depends jointly on signal and reference rates. [Nayak and Sinha, Secs. 3–4](https://arxiv.org/abs/2403.03295)

[Zhou et al.](https://doi.org/10.34133/2022/9798679) demonstrate optical coupon collection by interfering against a local full-support reference pulse train. Missing labels carry opposite-sign coherent pulses, and the accounting uses photon numbers. Their protocol anticipates coupon recovery with a reference, while the supplied states here have zero signal amplitude at missing labels. The two-source pure-copy tradeoff and collective converse concern this latter interface.

## State comparison and reference frames

[The two-state test of Barnett, Chefles and Jex](https://arxiv.org/abs/quant-ph/0202087) detects a difference with an antisymmetric projection. [The multi-state test of Chefles, Andersson and Jex](https://arxiv.org/abs/quant-ph/0402125) detects that pure inputs cannot all be the same via the complement of the symmetric subspace. The comparison projectors are inherited. The present decoders use the observed label histogram along with the test outcome to recover the missing set.

[Bartlett, Rudolph and Spekkens](https://doi.org/10.1103/RevModPhys.79.555) develop group twirling, relational encodings and finite quantum references. Total label counts give the twirl sectors for the diagonal group here. The [learning bridge](../learning/BRS_BRIDGE.md) applies those concepts to the two-source copy model.

## Conditional quantum discrimination

The [minimum-error semidefinite program](https://arxiv.org/abs/quant-ph/0205178), [square-root measurement](https://arxiv.org/abs/quant-ph/0005132) and [Powers–Størmer inequality](https://doi.org/10.1007/BF01645492) are standard tools. The histogram Gram matrix and its random-assignment approximation determine when the square-root measurement attains the limiting minimax optimum. The mismatch converse compares a separate input class with the same copy accounting.

See the [structured bibliography](references.bib) for reference details.
