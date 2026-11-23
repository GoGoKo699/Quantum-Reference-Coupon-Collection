# Finite verification

From the repository root, run the following with Python 3.9 or newer.

```sh
python3 verification/check_coupon.py
```

The script uses the Python standard library. It enumerates finite computational words and evaluates real probabilities with exact rational arithmetic. The phase tests use fourth roots of unity, for which real and imaginary parts are exact integers. A failed check raises `AssertionError`.

| Check | Finite coverage | Identity checked |
|---|---|---|
| Pair receiver | All proper nonempty supports for 2–6 labels and three common phase profiles | Outcome probabilities, normalization and minus-edge incidences |
| Histogram Gram | All proper nonempty supports for 2–5 labels, up to four total copies and every split between the two sources | Phase factors depend only on the histogram. Exact word overlaps match the closed-form Gram entries. Supports with the same observed membership have identical word vectors. The class size gives the uniform-posterior completion probability. |
| Block receiver | 2–4 labels and up to four signals per reference | The cyclic-shift average coincides with the full symmetric projection on the promised input in each supported histogram. A histogram with a missing label is rejected with probability $`b/(b+1)`$. All-present histograms are accepted. |
| Block decoder | 2–4 labels, up to two references, up to two signals per block and up to two raw signals | The decoder achieves the oracle completion probability on the good event. The exact bad-event mass is bounded by the analytic union bound. At zero references, decoder and oracle probabilities agree. |

The occupancy limits and the general bounds follow from the analytic proofs. The finite checks exercise their combinatorial and measurement identities in small cases.
