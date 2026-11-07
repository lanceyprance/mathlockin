# Topic 13: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Sheet 4 has short answers only. The full working here is mine (unofficial), checked in Python.

---

## Part A: Tutorial questions

### Q9 (Tutorial Sheet 4 Q9)

Show that w = x² + y² + z² + xy + yz + 2x − 4y + 6z has a minimum value of −42 at (−5, 8, −7).

<details><summary>Answer</summary>

∇w = ⟨2x + y + 2, x + 2y + z − 4, y + 2z + 6⟩.

At (−5, 8, −7): ⟨−10 + 8 + 2, −5 + 16 − 7 − 4, 8 − 14 + 6⟩ = ⟨0, 0, 0⟩. Critical point ✓.

$$H = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix}, \quad |H_1| = 2,\ |H_2| = 3,\ |H_3| = 2(3) - 1(2) = 4$$

All positive: local min.

w(−5, 8, −7) = 25 + 64 + 49 − 40 − 56 − 10 − 32 − 42 = **−42** ✓.

From: §3

</details>

---

### Q10 (Tutorial Sheet 4 Q10)

Find the local max and min values of $xyz + \frac{1}{2x} + \frac1y + \frac2z$.

<details><summary>Answer</summary>

$f_x = yz - \frac{1}{2x^2}$, $f_y = xz - \frac{1}{y^2}$, $f_z = xy - \frac{2}{z^2}$.

Setting them to 0 and multiplying by x, y, z: $xyz = \frac{1}{2x} = \frac1y = \frac2z = k$.

So x = 1/(2k), y = 1/k, z = 2/k, and xyz = 1/k³ = k. So k⁴ = 1, k = ±1.

Critical points: (1/2, 1, 2) and (−1/2, −1, −2).

$f_{xx} = \frac{1}{x^3}$, $f_{yy} = \frac{2}{y^3}$, $f_{zz} = \frac{4}{z^3}$, $f_{xy} = z$, $f_{xz} = y$, $f_{yz} = x$.

**At (1/2, 1, 2):**

$$H = \begin{pmatrix} 8 & 2 & 1 \\ 2 & 2 & 1/2 \\ 1 & 1/2 & 1/2 \end{pmatrix}, \quad 8,\ 12,\ 4$$

All positive: **local min, value 4**.

**At (−1/2, −1, −2):** H is minus the one above, minors −8, 12, −4: **local max, value −4**.

From: §3

</details>

---

### Q11 (Tutorial Sheet 4 Q11)

Show x² + y² + z² − xz − x + 4y − z has a single critical point at (1, −2, 1) and classify it.

<details><summary>Answer</summary>

∇f = ⟨2x − z − 1, 2y + 4, 2z − x − 1⟩ = 0.

y = −2. From the other two: z = 2x − 1 and 2(2x − 1) − x − 1 = 0 ⟹ x = 1, z = 1. Only one solution: (1, −2, 1).

$$H = \begin{pmatrix} 2 & 0 & -1 \\ 0 & 2 & 0 \\ -1 & 0 & 2 \end{pmatrix}, \quad 2,\ 4,\ 2(4) - 0 + (-1)(0 + 2) = 6$$

All positive: **local min**. f(1, −2, 1) = **−5**.

From: §3

</details>

---

### E1 (Tutorial Sample exam Q5 b)

f = −2x² − y² − 4z² − yz + 4x − y + 7z. (i) The unique critical point P. (ii) The leading principal minors of H. (iii) Local max, min or saddle?

<details><summary>Answer</summary>

**(i)** P = (1, −1, 1).

**(ii)** |H₁| = −4, |H₂| = 8, |H₃| = −60.

**(iii)** − + −: negative definite: **local maximum**.

From: §4

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. For a 3 × 3 Hessian, + + + means local minimum.
2. − + − means local maximum.
3. − − − means local maximum.
4. If the diagonal of H has a positive and a negative entry, the point is a saddle.
5. For f(x, y, z) you can use "D > 0 and f_xx > 0" from Topic 11.

<details><summary>Answer</summary>

1. **True.** (§2)
2. **True.** (§2)
3. **False.** For a max the signs must alternate. − − − (all non-zero) means indefinite: saddle. (§2)
4. **True.** Quick test. (§2)
5. **False.** That's only for two variables. Use the minors. (§3)

</details>

---

### M2: Multiple choice

At a critical point of f(x, y, z), the Hessian is

$$\begin{pmatrix} 3 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$$

The point is a:

- A. local min
- B. local max
- C. saddle point
- D. can't tell

<details><summary>Answer</summary>

**C.** The diagonal has 3 > 0 and −1 < 0: indefinite. (Minors 3, −3, −6: no pattern.)

From: §2

</details>

---

### M3: Calculate

Find and classify the critical point of f = x² + 2y² + 3z² − 2xy − 2z.

<details><summary>Answer</summary>

∇f = ⟨2x − 2y, 4y − 2x, 6z − 2⟩ = 0 ⟹ x = y, 4y − 2y = 0 ⟹ y = 0, x = 0, z = 1/3.

$$H = \begin{pmatrix} 2 & -2 & 0 \\ -2 & 4 & 0 \\ 0 & 0 & 6 \end{pmatrix}, \quad 2,\ 8 - 4 = 4,\ 6 \cdot 4 = 24$$

All positive: **local min** at (0, 0, 1/3), value 3/9 − 2/3 = −1/3.

From: §3

</details>

---

### M4: Sketch

Draw a 3 × 3 matrix and box the three blocks whose determinants are |H₁|, |H₂|, |H₃|.

<details><summary>Answer</summary>

|H₁|: box just the top-left entry.

|H₂|: box the top-left 2 × 2 square (rows 1–2, columns 1–2).

|H₃|: box the whole matrix.

The boxes are nested, all anchored in the top-left corner.

From: §1

</details>

---

### M5: Explain

In notes Example 6.43 the local max value is −4 and the local min value is 4. How can a max be smaller than a min?

<details><summary>Answer</summary>

"Local" only compares with nearby points.

The local max at (−1, −1, −1) is the highest point near (−1, −1, −1). The local min at (1, 1, 1) is the lowest near (1, 1, 1). They're in different places, and f blows up to ±∞ near the planes x = 0, y = 0, z = 0 in between, so nothing forces −4 > 4.

From: §5

</details>
