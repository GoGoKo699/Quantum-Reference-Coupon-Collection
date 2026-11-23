#!/usr/bin/env python3
"""Check finite coupon-receiver identities by exact word enumeration."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial, prod


ROOTS = (1, 1j, -1, -1j)


def histogram(word, n):
    return tuple(word.count(label) for label in range(n))


def word_sectors(n, length):
    sectors = defaultdict(list)
    for word in product(range(n), repeat=length):
        sectors[histogram(word, n)].append(word)
    return sectors


def label_sets(n, k):
    return [frozenset(labels) for labels in combinations(range(n), k)]


def squared_magnitude(value):
    return int(value.real) ** 2 + int(value.imag) ** 2


def check_pairs():
    checked = 0
    for n in range(2, 7):
        phase_profiles = ([0] * n, [i % 4 for i in range(n)],
                          [(3 * i * i + 2 * i + 1) % 4 for i in range(n)])
        for k in range(1, n):
            for support in label_sets(n, k):
                for phases in phase_profiles:
                    denominator = n * k
                    reference = [ROOTS[exponent] for exponent in phases]
                    signal = [amplitude if i in support else 0 for i, amplitude in enumerate(reference)]
                    mass = Fraction(sum(squared_magnitude(s * r) for s, r in zip(signal, reference)),
                                    denominator)
                    degrees = [Fraction() for _ in range(n)]
                    for i, j in combinations(range(n), 2):
                        a = signal[i] * reference[j]
                        b = signal[j] * reference[i]
                        minus = Fraction(squared_magnitude(a - b), 2 * denominator)
                        plus = Fraction(squared_magnitude(a + b), 2 * denominator)
                        present = (i in support) + (j in support)
                        assert minus == Fraction(present == 1, 2 * denominator)
                        assert plus == Fraction(present ** 2, 2 * denominator)
                        mass += minus + plus
                        degrees[i] += minus
                        degrees[j] += minus
                    assert mass == 1
                    for i, degree in enumerate(degrees):
                        expected = n - k if i in support else k
                        assert degree == Fraction(expected, 2 * denominator)
                    checked += 1
    return checked


def check_histogram_gram():
    sector_count, gram_entries, posterior_classes = 0, 0, 0
    for n in range(2, 6):
        for length in range(5):
            sectors = word_sectors(n, length)
            phases = [(i * i + i + 1) % 4 for i in range(n)]
            for counts, words in sectors.items():
                phase = sum(c * p for c, p in zip(counts, phases)) % 4
                assert all(sum(phases[i] for i in word) % 4 == phase for word in words)
            for signals in range(length + 1):
                references = length - signals
                for k in range(1, n):
                    supports = label_sets(n, k)
                    normalizer = k ** signals * n ** references
                    total_word_count = dict.fromkeys(supports, 0)
                    oracle_success = dict.fromkeys(supports, Fraction())
                    aggregate_success = Fraction()
                    for counts, words in sectors.items():
                        observed = frozenset(i for i, count in enumerate(counts) if count)
                        head_labels = [frozenset(word[:signals]) for word in words]
                        legal = {
                            support: {i for i, head in enumerate(head_labels) if head <= support}
                            for support in supports
                        }
                        factor = Fraction(factorial(signals) * factorial(references),
                                          prod(factorial(count) for count in counts))
                        for left, right in combinations_with_replacement(supports, 2):
                            available = sum(counts[i] for i in left & right)
                            assert len(legal[left] & legal[right]) == factor * comb(available, signals)
                            gram_entries += 1

                        classes = defaultdict(list)
                        for support in supports:
                            classes[support & observed].append(support)
                        for known_present, members in classes.items():
                            choices = comb(n - len(observed), k - len(known_present))
                            first = legal[members[0]]
                            assert len(members) == choices
                            assert all(legal[support] == first for support in members)
                            aggregate_success += Fraction(len(first), normalizer * len(supports))
                            for support in members:
                                total_word_count[support] += len(first)
                                oracle_success[support] += Fraction(len(first), normalizer * choices)
                            if not references and first:
                                assert known_present == observed
                            if not signals:
                                assert len(first) == len(words)
                            posterior_classes += 1
                        sector_count += 1
                    assert all(count == normalizer for count in total_word_count.values())
                    assert all(value == aggregate_success for value in oracle_success.values())
    return sector_count, gram_entries, posterior_classes


def check_symmetric_blocks():
    checked = 0
    for n in range(2, 5):
        for block_size in range(1, 6):
            for counts, words in word_sectors(n, block_size).items():
                for k in range(1, n):
                    support = frozenset(range(k))
                    allowed = {word for word in words if set(word[:-1]) <= support}
                    if not allowed:
                        continue
                    projected = Fraction(len(allowed), len(words))
                    cyclic = {
                        word: Fraction(sum(word[j:] + word[:j] in allowed
                                           for j in range(block_size)), block_size)
                        for word in words
                    }
                    assert all(amplitude == projected for amplitude in cyclic.values())
                    acceptance = sum(amplitude ** 2 for amplitude in cyclic.values()) / len(allowed)
                    missing_count = sum(counts[i] for i in range(k, n))
                    assert missing_count in (0, 1)
                    expected = Fraction(1, block_size) if missing_count else Fraction(1)
                    assert acceptance == expected
                    checked += 1
    return checked


def block_outcomes(n, k, b):
    """Enumerate outcomes at support {0, ..., k-1} with one reference draw."""
    masses = defaultdict(Fraction)
    draw_mass = Fraction(1, k ** b * n)
    for signal_word in product(range(k), repeat=b):
        for reference in range(n):
            labels = frozenset((*signal_word, reference))
            acceptance = Fraction(1, b + 1) if reference >= k else Fraction(1)
            masses[labels, False] += draw_mass * acceptance
            if acceptance < 1:
                masses[labels, True] += draw_mass * (1 - acceptance)
    assert sum(masses.values()) == 1
    return tuple(masses.items())


def decoder_success(n, true_missing, observed, candidates):
    """Use uniform fallback if rejected blocks do not specify singletons."""
    m = len(true_missing)
    if any(len(candidate) != 1 for candidate in candidates):
        return Fraction(1, comb(n, m))
    detected = frozenset().union(*candidates)
    unseen = n - len(observed)
    labels_to_fill = m - len(detected)
    if not 0 <= labels_to_fill <= unseen:
        return Fraction(1, comb(n, m))
    return Fraction(detected == true_missing & observed, comb(unseen, labels_to_fill))


def check_block_decoder():
    settings, checked = 0, 0
    for n in range(2, 5):
        for k in range(1, n):
            missing = frozenset(range(k, n))
            m = len(missing)
            for b, references, raw_signals in product(range(3), range(3), range(3)):
                outcomes = block_outcomes(n, k, b)
                received_mass, total_success, genie_success, bad_mass = (Fraction(),) * 4
                for raw_word in product(range(k), repeat=raw_signals):
                    known_present = frozenset(raw_word)
                    for blocks in product(outcomes, repeat=references):
                        mass = prod(probability for _, probability in blocks) / Fraction(k ** raw_signals)
                        observed = known_present.union(*(labels for (labels, _), _ in blocks))
                        candidates = [labels - known_present for (labels, rejected), _ in blocks if rejected]
                        true_seen = missing & observed
                        genie = Fraction(1, comb(n - len(observed), m - len(true_seen)))
                        success = decoder_success(n, missing, observed, candidates)
                        bad = any((not rejected and bool(labels & missing))
                                  or (rejected and bool((labels - missing) - known_present))
                                  for (labels, rejected), _ in blocks)
                        if not bad:
                            assert success == genie
                        received_mass += mass
                        total_success += mass * success
                        genie_success += mass * genie
                        bad_mass += mass * bad
                        checked += 1
                bound = Fraction(references * m, n) * (
                    Fraction(1, b + 1) + b * Fraction(k - 1, k) ** raw_signals)
                assert received_mass == 1
                assert bad_mass <= bound
                assert genie_success - bad_mass <= total_success <= genie_success
                if not references:
                    assert total_success == genie_success
                settings += 1
    return settings, checked


def main():
    pairs = check_pairs()
    sectors, entries, classes = check_histogram_gram()
    blocks = check_symmetric_blocks()
    settings, decoder_outcomes = check_block_decoder()
    print(f"Pair receiver: {pairs} support and phase settings")
    print(f"Histogram Gram: {sectors} sectors, {entries} entries, {classes} posterior classes")
    print(f"Symmetric-block test: {blocks} supported sectors")
    print(f"Block decoder: {settings} settings, {decoder_outcomes} outcome combinations")


if __name__ == "__main__":
    main()
