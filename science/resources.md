# Copies, gates, storage and interpretation

The unknown support is physically encoded in a supplied state. A reference copy carries the same phase profile and has full support. We count its cost as one emitted $n$-dimensional state, just as for a signal copy. The number of reference copies does not depend on a particular state-loading circuit. A laboratory assessment must separately account for how the source establishes common phases and prepares and transfers each copy.

| Receiver | Quantum data stored at once | Work after copies arrive |
| --- | --- | --- |
| Basis sampling | One $\lceil\log_2 n\rceil$-qubit label register | A basis measurement, classical label accounting and completion. |
| Paired | Two label registers | A reversible comparison, controlled swaps and an orientation Hadamard for each pair, with $O(\log n)$ basic quantum gates and work bits per pair. |
| Block | $b+1$ label registers | A controlled cyclic rotation, its preparation and unpreparation, then basis measurements and classical filtering. |
| Fully collective | $T+R$ label registers in a direct implementation | A total histogram measurement, then the conditional Gram-based POVM. No efficient compile-time or gate-count bound is established for this POVM. |

A block rotation by a control value can be implemented by applying binary powers of a register shift. Each fixed shift permutes $b+1$ registers and decomposes into at most $b$ swaps. With binary controls this gives $O(b\log(b+1)\log n)$ controlled bit swaps per block. An ideal uniform control over $b+1$ options can be prepared by a tree of controlled rotations with $O(b)$ rotations before elementary decomposition. This count separates finite-precision compilation from exact ideal probabilities.

Classical processing need not materialize an $n$ by $n$ table. The pair receiver tracks endpoint counts. The block receiver indexes the reserved labels and filters observed histograms. Outputting the missing list costs reporting $m$ labels. Outputting the entire present set adds the cost of listing $n-m$ labels.

The exact collective law optimizes **copies**. With equal copy prices and both counts linear, the [limiting law](linear-budget.md) is largest at balanced budgets. The paired receiver uses less coherent memory and achieves the same linear scaling at fixed error for fixed $m$. Its explicit finite probability bounds remain useful without implementing the collective POVM.

One measurement in the computational basis per specimen yields the same classical baseline with or without reference specimens, because reference label outcomes are uniform and independent of the hidden support. The established gap concerns useful relational coherence in the specified copy interface. Preparation, communication, memory, and latency can change an implementation comparison. See [phase mismatch](phase-mismatch.md) for the consequence of weakening source alignment.
