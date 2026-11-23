# Exact collective receiver and linear-budget limit

Fix an alphabet of size $n$, an unknown missing set $M$ of known size $m$, and $k=n-m>0$. The receiver gets $T$ signal registers and $R$ reference registers. The signal is uniform on the complement of $M$, the reference is uniform on the full alphabet, and both carry the same unknown diagonal phases. The budget counts state copies. Write $P^*_{n,m}(T,R)$ for the maximum worst-case probability of returning $M$ exactly, allowing collective measurements.

For fixed positive $m$ and $T/n\to\alpha>0$, $R/n\to\beta>0$, the exact limit is

```math
\lim_{n\to\infty} P^*_{n,m}(T,R)
=
\left(1-e^{-\alpha\beta/(\alpha+\beta)}\right)^m .
```

Measuring the total label histogram and then applying the square-root measurement in that histogram sector attains the limit.

## Exact finite reduction

Let $N=T+R$, $D=\binom{n}{m}$ and $c=(c_1,\ldots,c_n)$ be a histogram of total size $N$. Its number of words is $W_c=N!/\prod_j c_j!$. Let $v_{M,c}$ be the sum of the computational basis words of histogram $c$ in which all occurrences of labels in $M$ are in reference registers, divided by $\sqrt{W_c}$. The projected pure input is $\sqrt{W_c/(k^T n^R)}v_{M,c}$ times a scalar phase common to that sector.

Averaging over independent uniform angles for the common diagonal phase removes coherences between different histograms. Conversely the receiver may measure the histogram first and make the subsequent measurement independent of those phases. Permutation averaging relabels both the measurement and its output, giving identical success on every missing set while preserving average success. Together these two observations identify the uniform-prior Bayes optimum with the minimax optimum.

For $a\ge 0$ put $q_a=(R)_a/(N)_a$ when $a\le R$, with $q_0=1$, and put $q_a=0$ when $a>R$. Here $(x)_a$ denotes the falling factorial. Uniformly permuting a word assigns its fixed positions of any prescribed labels to uniformly random registers. It follows that the Gram matrix in sector $c$ is

```math
(G_c)_{M,M'}
=
\left\langle v_{M,c},v_{M',c}\right\rangle
=
q_{\sum_{j\in M\cup M'}c_j}.
```

Let $C$ be the histogram of $N$ independent uniform alphabet draws, so $\Pr(C=c)=W_c/n^N$. For any positive semidefinite $D$ by $D$ Gram matrix $G$, take $a_M=\sqrt G\,e_M$, where $e_M$ is the coordinate vector for hypothesis $M$. Let $F(G)$ denote the unnormalized optimum discrimination score for these columns. Then

```math
P^*_{n,m}(T,R)
=
\left(\frac{n}{k}\right)^T \frac{\mathbb E_C F(G_C)}{D}.
```

The finite discrimination problem has primal and dual forms

```math
\begin{aligned}
F(G)
&=
\max_{E_M\succeq 0,\,\sum_M E_M=I}
\sum_M\langle a_M,E_M a_M\rangle,\\
&=
\min_{Y=Y^*,\,Y\succeq a_M a_M^*\,\forall M}
\mathrm{Tr}Y.
\end{aligned}
```

The identity and trace may be taken on the span of the columns. In positive dimension, the uniformly split identity is strictly primal feasible and a sufficiently large multiple of the identity is strictly dual feasible. The zero-dimensional score is zero. Equality follows from semidefinite programming duality. [Eldar, Megretski and Verghese, minimum-error detection by semidefinite programming](https://arxiv.org/abs/quant-ph/0205178)

The square-root measurement has sector score

```math
F_{\mathrm{sq}}(G)=\sum_M \left| (\sqrt G)_{M,M} \right|^2.
```

In the actual register space it uses effects $S^{-1/2}|v_{M,c}\rangle\langle v_{M,c}|S^{-1/2}$, where $S=\sum_M|v_{M,c}\rangle\langle v_{M,c}|$ and the inverse is on the support. Complete the measurement arbitrarily outside the support. Polar decomposition of the matrix with columns $v_{M,c}$ gives the displayed score. Its dependence on $c$ and on $n,m,T,R$ makes the receiver independent of the unknown phases. It is permutation covariant on the occupied sector support. The number of copies is the resource bounded by this result. The sector matrix can have size $D$, and the prescription entails a collective measurement on $T+R$ registers. [Hausladen and Wootters, pretty-good measurement](https://doi.org/10.1080/09500349414552221) · [Eldar and Forney, square-root measurement](https://arxiv.org/abs/quant-ph/0005132)

## Independent assignment approximation

Fix $c$ and give the $N$ abstract word positions labels with multiplicities $c$. Mark a uniformly random subset $Y$ of $R$ positions as reference positions. The vectors whose Gram matrix is $G_c$ can be realized as indicator functions $f_M(Y)$ that every position labeled in $M$ belongs to $Y$.

Put $r=R/N$ for $N>0$. Let $X$ be an independent Bernoulli-$r$ marking of the same positions. Couple $X$ to $Y$ by removing uniformly chosen marked positions when $|X|>R$ and adding uniformly chosen unmarked positions when $|X|\lt R$. Exchangeability makes $Y$ uniform. The expected number of changed positions is $\mathbb E\bigl[\bigl||X|-R\bigr|\bigr]\le\sqrt{Nr(1-r)}$. By exchangeability and a union bound,

```math
\mathbb E\left|f_M(Y)-f_M(X)\right|^2
\le
\left(\sum_{j\in M}c_j\right)\sqrt{\frac{r(1-r)}{N}}.
```

Write $A$ and $B$ for the column operators of $f_M(Y)$ and $f_M(X)$ in the common space of the coupling. Both have Hilbert–Schmidt norm at most $\sqrt{D}$. Since $\mathbb E_C\sum_{j\in M}C_j=Nm/n$, the average squared distance per hypothesis is at most $m\sqrt{Nr(1-r)}/n$, which tends to zero when $m$ is fixed and $N$ is linear in $n$.

For any measurement, the absolute difference in the two scores is at most the sum of the trace norms of the differences of the corresponding pure-state operators. That sum is at most $(\|A\|_2+\|B\|_2)\|A-B\|_2$. Taking the two optima in the common ambient space and averaging over $C$ shows that $\mathbb E_C|F(G_C)-F(\widetilde G_C)|/D\to 0$, where $\widetilde G_c=B^*B$ is the Gram matrix from independent marking. Here and below $\|\cdot\|_2$ is Hilbert–Schmidt norm and $\|\cdot\|_1$ is trace norm.

For the square-root score, the matrix estimate

```math
\left\|\sqrt{G_c}-\sqrt{\widetilde G_c}\right\|_2^2
\le\|G_c-\widetilde G_c\|_1
\le(\|A\|_2+\|B\|_2)\|A-B\|_2
```

follows from the Powers–Størmer inequality and Cauchy–Schwarz for trace norm products. The squared diagonal score changes by at most $2\sqrt D\,\|\sqrt{G_c}-\sqrt{\widetilde G_c}\|_2$. Averaging and using the same coupling bound gives $\mathbb E_C|F_{\mathrm{sq}}(G_C)-F_{\mathrm{sq}}(\widetilde G_C)|/D\to 0$. [Powers and Størmer, matrix square-root inequality](https://doi.org/10.1007/BF01645492)

## Discriminating the independent ensemble

The independent-marking event for label $j$ has probability $p_j=r^{c_j}$. Use the convention $r^0=1$. Its indicator, resolved into its constant and centered parts, is represented by $p_j|0\rangle+\sqrt{p_j-p_j^2}|1\rangle$. The indicator column for $M$ is the tensor product of those vectors at labels in $M$ and $|0\rangle$ elsewhere. Its component on the basis vector $|M\rangle$ has squared norm

```math
d_M=\prod_{j\in M}(p_j-p_j^2).
```

The remaining component lies in the subspace indexed by subsets of size less than $m$. All $|M\rangle$ components are orthogonal. Projecting onto them attains total score at least $\sum_M d_M$. For any measurement the lower-subspace components contribute at most its dimension $L=\sum_{\ell\lt m}\binom{n}{\ell}$, because every column has norm at most one and the compressed effects sum to the subspace identity. Cauchy–Schwarz bounds the absolute cross contribution by $2\sqrt{LD}$. Therefore

```math
\sum_M d_M
\le F(\widetilde G_c)
\le \sum_M d_M+L+2\sqrt{LD}.
```

The same lower bound holds for the square-root score. The orthogonal $|M\rangle$ components give $\widetilde G_c\succeq\mathrm{diag}(d_M)$. Operator monotonicity of square root gives $\sqrt{\widetilde G_c}\succeq\mathrm{diag}(\sqrt{d_M})$, hence $F_{\mathrm{sq}}(\widetilde G_c)\ge\sum_M d_M$. For fixed $m$, $L/D\to 0$.

## Taking the limit

For any fixed $M$, the baseline histogram entries $(C_j:j\in M)$ converge jointly to independent Poisson variables of mean $\alpha+\beta$, and $r\to\beta/(\alpha+\beta)$. This follows from the multinomial probability generating function. Boundedness and symmetry give

```math
\begin{aligned}
\frac1D\mathbb E_C\sum_M d_M
&\longrightarrow
\left[
e^{-(\alpha+\beta)(1-r_\infty)}-
e^{-(\alpha+\beta)(1-r_\infty^2)}
\right]^m\\
&=
e^{-m\alpha}\left(1-e^{-\alpha\beta/(\alpha+\beta)}\right)^m,
\qquad r_\infty=\frac{\beta}{\alpha+\beta}.
\end{aligned}
```

The likelihood factor $(n/k)^T$ tends to $e^{m\alpha}$. The same argument for $F$ and $F_{\mathrm{sq}}$ proves both the exact collective limit and its attainment. If either budget coefficient is zero and the other is finite, the limit is zero. To see this, increase every zero budget coefficient to any positive constant, use monotonicity in the copy budget, and let that constant decrease to zero.

For fixed total linear budget $\alpha+\beta=s$, the exact limiting success is maximized by $\alpha=\beta=s/2$. A target limiting success $1-\delta$, with $0\lt \delta\lt 1$, requires total budget coefficient $s\ge 4\log[1/(1-(1-\delta)^{1/m})]$ under this equal-price copy count.
