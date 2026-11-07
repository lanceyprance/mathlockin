# Topic 8: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Tutorial questions

### Q1 (Tutorial Sheet 3 Q1)

Find the gradient at the point.

(a) y − x, (2, 1)  (b) ln(x² + y²), (1, 1)  (c) x² + y² − 2z² + z ln x, (1, 1, 1)  (d) (x² + y² + z²)^(−1/2) + ln(xyz), (−1, 2, −2)

<details><summary>Answer</summary>

**(a)** ∇f = ⟨−1, 1⟩ everywhere, so ⟨−1, 1⟩.

**(b)** $\left\langle \frac{2x}{x^2+y^2}, \frac{2y}{x^2+y^2} \right\rangle \to \langle 1, 1 \rangle$.

**(c)** $\left\langle 2x + \frac{z}{x}, 2y, -4z + \ln x \right\rangle \to \langle 3, 2, -4 \rangle$.

**(d)** Each part is $-\frac{x}{(x^2+y^2+z^2)^{3/2}} + \frac1x$ (and the same with y, z). At the point x² + y² + z² = 9, so the power is 27.

$$\nabla f = \left\langle \frac{1}{27} - 1, -\frac{2}{27} + \frac12, \frac{2}{27} - \frac12 \right\rangle = \left\langle -\frac{26}{27}, \frac{23}{54}, -\frac{23}{54} \right\rangle$$

From: §2

</details>

---

### Q2 (Tutorial Sheet 3 Q2)

Find the directional derivative at P₀ in the direction of v.

(a) 2xy − 3y², (5, 5), ⟨4, 3⟩  (b) 2x² + y², (−1, 1), ⟨3, −4⟩

(c) xy + yz + zx, (1, −1, 2), ⟨3, 6, −2⟩  (d) cos(xy) + e^(yz) + ln(zx), (1, 0, 1/2), ⟨1, 2, 2⟩

<details><summary>Answer</summary>

**(a)** ∇f(5, 5) = ⟨10, −20⟩, u = ⟨4/5, 3/5⟩. D = 8 − 12 = **−4**.

**(b)** ∇f = ⟨4x, 2y⟩ → ⟨−4, 2⟩. u = ⟨3/5, −4/5⟩. D = −12/5 − 8/5 = **−4**.

**(c)** ∇f = ⟨y + z, x + z, x + y⟩ → ⟨1, 3, 0⟩. ‖v‖ = 7, u = ⟨3/7, 6/7, −2/7⟩. D = 3/7 + 18/7 = **3**.

**(d)** ∇f = ⟨−y sin(xy) + 1/x, −x sin(xy) + ze^(yz), ye^(yz) + 1/z⟩ → ⟨1, 1/2, 2⟩. ‖v‖ = 3, u = ⟨1/3, 2/3, 2/3⟩. D = 1/3 + 1/3 + 4/3 = **2**.

From: §3

</details>

---

### Q3 (Tutorial Sheet 3 Q3)

Find the directions of fastest increase and decrease at P₀, and the directional derivatives in those directions.

(a) x² + xy + y², (−1, 1)  (b) x²y + e^(xy) sin y, (1, 0)  (c) x/y − yz, (4, 1, 1)  (d) ln(x² + y² − 1) + y + 6z, (1, 1, 0)

<details><summary>Answer</summary>

**(a)** ∇f = ⟨2x + y, x + 2y⟩ → ⟨−1, 1⟩. u = ⟨−1/√2, 1/√2⟩ (increase), −u (decrease). Rates **√2** and **−√2**.

**(b)** ∇f(1, 0) = ⟨0, 2⟩. u = j = ⟨0, 1⟩, −u = −j. Rates **2** and **−2**.

**(c)** ∇f = ⟨1/y, −x/y² − z, −y⟩ → ⟨1, −5, −1⟩, length √27 = 3√3.

u = $\frac{1}{3\sqrt3}\langle 1, -5, -1 \rangle$, and −u. Rates **3√3** and **−3√3**.

**(d)** ∇f(1, 1, 0) = ⟨2, 3, 6⟩, length 7. u = ⟨2/7, 3/7, 6/7⟩, and −u. Rates **7** and **−7**.

From: §4

</details>

---

### Q4 (Tutorial Sheet 3 Q4, Q5)

In which directions is the directional derivative zero?

Q4: f = xy + y² at (3, 2).  Q5: f = (x² − y²)/(x² + y²) at (1, 1).

<details><summary>Answer</summary>

**Q4:** ∇f = ⟨y, x + 2y⟩ → ⟨2, 7⟩. Orthogonal: ⟨7, −2⟩.

$\mathbf u = \left\langle \frac{7}{\sqrt{53}}, -\frac{2}{\sqrt{53}} \right\rangle$ and $-\mathbf u$.

**Q5:** ∇f = $\left\langle \frac{4xy^2}{(x^2+y^2)^2}, -\frac{4x^2y}{(x^2+y^2)^2} \right\rangle$ → ⟨1, −1⟩. Orthogonal: ⟨1, 1⟩.

$\mathbf u = \left\langle \frac{1}{\sqrt2}, \frac{1}{\sqrt2} \right\rangle$ and $-\mathbf u$.

From: §4

</details>

---

### Q6 (Tutorial Sheet 3 Q6, Q7)

Q6: Is there a direction in which the rate of change of f = x² − 3xy + 4y² at (1, 2) equals 14?

Q7: In what direction does f = xy at (0, 2) have directional derivative −1? Can it ever be −3?

<details><summary>Answer</summary>

**Q6:** ∇f = ⟨2x − 3y, −3x + 8y⟩ → ⟨−4, 13⟩. Max rate = √185 ≈ 13.6 < 14. **No.**

**Q7:** ∇f(0, 2) = ⟨2, 0⟩. With u = ⟨a, b⟩, a² + b² = 1: D = 2a = −1, so a = −1/2, b = ±√3/2.

$\mathbf u = -\frac12\mathbf i + \frac{\sqrt3}{2}\mathbf j$ (or with −√3/2).

The rates go from −2 to 2, so **−3 is impossible**.

From: §4

</details>

---

### Q8 (Tutorial Sheet 3 Q8)

f has directional derivative 2 at (0, 0) parallel to i + 2j, and 3 parallel to 2i − j. Find the unit direction of fastest increase at (0, 0).

<details><summary>Answer</summary>

Let ∇f(0, 0) = ⟨r, s⟩. Unit vectors: (1/√5)⟨1, 2⟩ and (1/√5)⟨2, −1⟩.

$$\frac{r + 2s}{\sqrt5} = 2, \qquad \frac{2r - s}{\sqrt5} = 3$$

Solve: r = 8/√5, s = 1/√5. So ∇f ∥ ⟨8, 1⟩.

$$\mathbf u = \frac{8}{\sqrt{65}}\mathbf i + \frac{1}{\sqrt{65}}\mathbf j$$

From: §3, §4

</details>

---

### E1 (Tutorial Sample exam Q4)

$T = e^{x^2-4y^2-9z^2}$, P = (2, −1, 0), Q = (3, −3, 3).

(a) ∇T at P. (b) Unit vector u from P towards Q. (c) Rate of change at P in direction u. (d) Direction of fastest increase at P. (e) The maximum rate.

<details><summary>Answer</summary>

**(a)** ∇T(P) = ⟨4, 8, 0⟩

**(b)** u = (1/√14)⟨1, −2, 3⟩

**(c)** −12/√14 ≈ −3.207

**(d)** The direction of ⟨4, 8, 0⟩.

**(e)** √80 = 4√5 ≈ 8.944

From: §6

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. $D_{\mathbf v}f = \nabla f \cdot \mathbf v$ for any vector v.
2. The gradient points in the direction of fastest increase.
3. The maximum rate of increase is ‖∇f‖.
4. The rate of change of f in direction −∇f is −‖∇f‖.
5. In 2D, ⟨a, b⟩ and ⟨b, −a⟩ are orthogonal.

<details><summary>Answer</summary>

1. **False.** v must be a **unit** vector. (§3)
2. **True.** (§4)
3. **True.** (§4)
4. **True.** (§4)
5. **True.** Their dot product is ab − ba = 0. (§4)

</details>

---

### M2: Multiple choice

∇f(P) = ⟨3, 4⟩. What is the largest possible directional derivative of f at P?

- A. 3
- B. 4
- C. 5
- D. 7

<details><summary>Answer</summary>

**C.** ‖⟨3, 4⟩‖ = √(9 + 16) = 5.

From: §4

</details>

---

### M3: Calculate

f(x, y, z) = x²y + yz³. Find the rate of change of f at P = (1, 2, 1) in the direction from P towards Q = (3, 3, 3).

<details><summary>Answer</summary>

∇f = ⟨2xy, x² + z³, 3yz²⟩ → ⟨4, 2, 6⟩.

v = Q − P = ⟨2, 1, 2⟩, ‖v‖ = 3, u = ⟨2/3, 1/3, 2/3⟩.

D = 8/3 + 2/3 + 12/3 = **22/3**.

From: §3

</details>

---

### M4: Sketch

f(x, y) = x² + y². Sketch the level curves f = 1 and f = 4, and draw ∇f at (1, 0) and at (0, 2).

<details><summary>Answer</summary>

Circles of radius 1 and 2 centred at the origin.

∇f = ⟨2x, 2y⟩. At (1, 0): ⟨2, 0⟩, an arrow pointing right (outwards). At (0, 2): ⟨0, 4⟩, pointing up (outwards), twice as long.

Each arrow points straight out, at right angles to its circle.

From: §4

</details>

---

### M5: Explain

Using $D_{\mathbf u}f = \Vert \nabla f\Vert \cos\theta$, explain why f has no change in directions orthogonal to ∇f.

<details><summary>Answer</summary>

θ is the angle between u and ∇f.

Orthogonal means θ = 90°, and cos 90° = 0.

So $D_{\mathbf u}f = 0$: no change.

From: §4

</details>
