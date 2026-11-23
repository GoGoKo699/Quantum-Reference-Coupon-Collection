# Paired receiver for sparse missing sets

On one signal and one reference measure in the orthonormal basis containing $|ii\rangle$ and, for $i<j$,

```math
|ij;\pm\rangle=\frac{|i\rangle|j\rangle\pm|j\rangle|i\rangle}{\sqrt 2}.
```

The minus amplitude is $e^{\mathrm i(\phi_i+\phi_j)}(\mathbf 1_{i\in S}-\mathbf 1_{j\in S})/\sqrt{2nk}$. Thus a minus outcome records an unordered edge $\{i,j\}$ with one endpoint present and the other missing. Each such edge occurs with probability $1/(2nk)$. All other minus outcomes have probability zero. The measurement resolves the label pair as well as the exchange sign.

For example, take four labels and $M=\{4\}$. The three minus outcomes $\{1,4\},\{2,4\},\{3,4\}$ each occur with probability $1/24$. Upon seeing two different edges, their common endpoint is 4. Under this decoding rule, after $L$ pairs failure means that zero or only one distinct edge was observed. For a single missing label and any $n\ge3$, the exact failure probability is

```math
k\left(1-\frac{k-1}{2nk}\right)^L
-(k-1)\left(1-\frac{1}{2n}\right)^L .
```

This follows by summing, over the $k$ possible edges, the probabilities of seeing no edge outside that singleton. The zero-edge event is counted $k$ times and is corrected to a single count.

## More than one missing label

Let $D_i$ count all minus outcomes incident on label $i$, with repetitions. From $L$ independently measured pairs, the marginal distribution of $D_i$ is binomial:

| Label type | Single-pair incidence | Mean after $L$ pairs |
| --- | --- | --- |
| Missing | $1/(2n)$ | $\mu=L/(2n)$ |
| Present | $m/(2nk)$ | $\mu/r$, with $r=k/m$ |

Suppose $k\ge 2m$. If $2\le r\le8$, classify degrees at or above $3\mu/4$ as missing. The binomial lower-tail bound gives at most $e^{-\mu/32}$ per missing vertex. A present degree is stochastically bounded by a binomial with mean $\mu/2$. The upper-tail exponent at $3\mu/4$ is at least $\mu/20$ since $(3\log(3/2)-1)/4>1/20$. There are at most $8m$ present vertices. If $r\ge8$, use threshold $\mu/2$. The two error contributions are bounded by

```math
m e^{-\mu/8}+mr(2e/r)^{\mu/2}\le 9m e^{-\mu/8},
\qquad \mu\ge2 .
```

The second inequality uses $r^{1-\mu/2}\le 8^{1-\mu/2}$. No independence of degrees within a shot is needed for the union bound. If the procedure returns the wrong output size, finish by an arbitrary $m$-set. This fallback never changes a correct classification.

Together, the two cases give error at most $\delta$ using $L=\lceil 64 n\log(9m/\delta)\rceil$ copies of **each** source. If $k<2m$, direct basis sampling instead recovers $S$ after $O(k\log(k/\delta))$ signals by collecting all present labels. The useful sample gap is in the sparse-missing regime. For fixed $m$ and fixed error, reference-assisted reception needs only a linear number of specimens, while the unrestricted [zero-reference optimum](histogram-converse.md) has the classical coupon scale.

## Implementation

Reversibly extract the orientation of a pair of distinct labels while sorting them. A Hadamard on the orientation bit then resolves plus or minus without revealing which input carried which label. Keep its Hadamard controlled on the labels being distinct and read out the sorted labels and sign. The orientation bit permits the comparison and conditional swap without erasing a register. A standard reversible comparator and controlled swaps cost $O(\log n)$ elementary reversible gates and use $O(\log n)$ work bits. The decoder stores counts only at observed endpoints. See [resource accounting](resources.md) for the output and source costs.
