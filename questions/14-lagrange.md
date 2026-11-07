# Topic 14: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Sheet 4 has short answers only. The full working here is mine (unofficial), checked in Python.

---

## Part A: Tutorial questions

### Q16 (Tutorial Sheet 4 Q16)

Find the max and min of f = xy⁶ subject to x² + y⁴ = 4.

<details><summary>Answer</summary>

∇f = ⟨y⁶, 6xy⁵⟩, ∇g = ⟨2x, 4y³⟩.

$$y^6 = 2\lambda x \quad (1), \qquad 6xy^5 = 4\lambda y^3 \quad (2)$$

**y = 0:** x = ±2, f = 0.

**y ≠ 0:** (2) ÷ y³: λ = 3xy²/2. Into (1): y⁶ = 3x²y², so y⁴ = 3x².

Constraint: x² + 3x² = 4 ⟹ x = ±1, y⁴ = 3, y = ±3^(1/4).

f = x·y⁶ = x·3^(3/2) = ±3√3.

**Max 3√3** at (1, ±3^(1/4)). **Min −3√3** at (−1, ±3^(1/4)).

(The constraint curve is closed and bounded, so these exist.)

From: §2

</details>

---

### Q17 (Tutorial Sheet 4 Q17)

Max and min of f = x²yz subject to x² + y² + z² = 2.

<details><summary>Answer</summary>

$$2xyz = 2\lambda x, \quad x^2z = 2\lambda y, \quad x^2y = 2\lambda z$$

**x = 0:** f = 0.

**x ≠ 0:** first equation gives λ = yz. Then

- x²z = 2y²z ⟹ z(x² − 2y²) = 0
- x²y = 2yz² ⟹ y(x² − 2z²) = 0

If y or z is 0, f = 0. Otherwise x² = 2y² = 2z².

Constraint: 2y² + y² + y² = 2 ⟹ y² = z² = 1/2, x² = 1.

f = x²yz = yz = ±1/2.

**Max 1/2** (y, z same sign). **Min −1/2** (opposite signs). The sphere is compact.

From: §2

</details>

---

### Q18 (Tutorial Sheet 4 Q18)

Show the max of x²y²z² subject to x + y + z = 0 and x² + y² + z² = 1 is 1/54.

<details><summary>Answer</summary>

Let p = xyz. ∇f = ⟨2xy²z², 2x²yz², 2x²y²z⟩, ∇g₁ = ⟨1, 1, 1⟩, ∇g₂ = ⟨2x, 2y, 2z⟩.

$$2xy^2z^2 = \lambda + 2\mu x, \text{ and the same for } y, z$$

Multiply the x-equation by x (and similarly for y, z):

$$2p^2 = \lambda x + 2\mu x^2, \quad 2p^2 = \lambda y + 2\mu y^2, \quad 2p^2 = \lambda z + 2\mu z^2$$

So x, y and z are all roots of the same quadratic 2μt² + λt − 2p² = 0. A quadratic has at most two roots, so two of x, y, z are equal. (All three equal would force x = y = z = 0, which isn't on the sphere.)

Say x = y. Then z = −2x, and x² + x² + 4x² = 1 ⟹ x² = 1/6.

$$f = x^2 \cdot x^2 \cdot 4x^2 = 4x^6 = \frac{4}{216} = \frac{1}{54}$$

Any candidate with a zero coordinate gives f = 0. The constraint set (a circle) is compact, so the max is **1/54**.

From: §3

</details>

---

### Q19 (Tutorial Sheet 4 Q19)

Find the minimum of x² + y² + z² subject to x + y + z = 1 and x − y + 2z = 1.

<details><summary>Answer</summary>

$$2x = \lambda + \mu, \quad 2y = \lambda - \mu, \quad 2z = \lambda + 2\mu$$

Put x, y, z into the constraints:

- (3λ + 2μ)/2 = 1 ⟹ 3λ + 2μ = 2
- (2λ + 6μ)/2 = 1 ⟹ λ + 3μ = 1

So μ = 1/7, λ = 4/7. Then x = 5/14, y = 3/14, z = 3/7.

$$f = \frac{25 + 9 + 36}{196} = \frac{70}{196} = \frac{5}{14}$$

The constraints are a line. f is the squared distance from the origin, which has a smallest value but no largest. **Min 5/14.**

From: §3

</details>

---

### Q20 (Tutorial Sheet 4 Q20)

Find the minimum of x² + y² + z² subject to x + y + z = 5 and xyz = 4.

<details><summary>Answer</summary>

$$2x = \lambda + \mu yz, \text{ and the same for } y, z$$

Multiply by x: 2x² = λx + 4μ (since xyz = 4). Same for y, z.

So x, y, z are roots of 2t² − λt − 4μ = 0: two of them are equal. Say x = y.

z = 5 − 2x and x²(5 − 2x) = 4 ⟹ 2x³ − 5x² + 4 = 0 ⟹ (x − 2)(2x² − x − 2) = 0.

| x = y | z | f |
|---|---|---|
| 2 | 1 | 9 |
| (1 + √17)/4 ≈ 1.28 | ≈ 2.44 | ≈ 9.23 |
| (1 − √17)/4 ≈ −0.78 | ≈ 6.56 | ≈ 44.2 |

f gets arbitrarily large far out along the constraint, so the smallest candidate is the min.

**Min 9**, at (2, 2, 1) and its rearrangements.

From: §3

</details>

---

### Q15 (Tutorial Sheet 4 Q15)

A wire of length 2 cm is bent into a five-sided shape: three sides of a rectangle, topped by the two equal sides of an isosceles triangle. Find the maximum area.

<details><summary>Answer</summary>

Let the rectangle have width 2a and height h. Let the triangle's base angle be θ, so its equal sides are a/cos θ and its height is a tan θ.

Wire: 2a + 2h + 2a/cos θ = 2, so h = 1 − a − a sec θ.

$$A = 2ah + a^2\tan\theta = 2a - 2a^2 - 2a^2\sec\theta + a^2\tan\theta$$

Two variables, a and θ. Critical point (Topic 11):

$$A_\theta = -2a^2\sec\theta\tan\theta + a^2\sec^2\theta = a^2\sec\theta(\sec\theta - 2\tan\theta) = 0$$

⟹ 1 = 2 sin θ ⟹ θ = 30°. Then sec θ = 2/√3, tan θ = 1/√3:

$$A = 2a - a^2(2 + \sqrt3)$$

$$A_a = 2 - 2a(2 + \sqrt3) = 0 \implies a = \frac{1}{2+\sqrt3} = 2 - \sqrt3$$

$$A_{max} = a = 2 - \sqrt3 = \frac{\sqrt3}{3 + 2\sqrt3} \approx 0.268 \text{ cm}^2$$

(Same as the sheet's short answer.)

From: §5

</details>

---

### E1 (Tutorial Sample exam Q6 a)

Max and min of f = x²yz + 1 subject to z = 1 and x² + y² + z² = 10.

<details><summary>Answer</summary>

Candidates (0, ±3, 1): f = 1. (±√6, √3, 1): f = 1 + 6√3. (±√6, −√3, 1): f = 1 − 6√3.

**Max 1 + 6√3. Min 1 − 6√3.**

Full working in notes §4.

From: §4

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. At a constrained max, ∇f and ∇g are parallel.
2. You need the value of λ in the final answer.
3. On a sphere, a continuous f always has a max and a min.
4. Every point found by Lagrange is a max or a min.
5. With two constraints you need two multipliers.

<details><summary>Answer</summary>

1. **True.** (§1)
2. **False.** λ is a helper. (§2)
3. **True.** A sphere is compact. (§2)
4. **False.** They're candidates. Compare f to find which is which. Some may be neither. (§2)
5. **True.** (§3)

</details>

---

### M2: Multiple choice

Using Lagrange on f = x + y with x² + y² = 2, the max value is:

- A. 1
- B. 2
- C. √2
- D. 4

<details><summary>Answer</summary>

**B.** 1 = 2λx, 1 = 2λy ⟹ x = y. 2x² = 2 ⟹ x = ±1. f(1, 1) = 2 (max), f(−1, −1) = −2 (min).

From: §2

</details>

---

### M3: Calculate

Find the max and min of f = x² + 2y² on the circle x² + y² = 4.

<details><summary>Answer</summary>

2x = 2λx ⟹ x(1 − λ) = 0. 4y = 2λy ⟹ y(2 − λ) = 0.

- x = 0: y = ±2, f = 8.
- λ = 1: then y = 0, x = ±2, f = 4.

**Max 8** at (0, ±2). **Min 4** at (±2, 0).

From: §2

</details>

---

### M4: Sketch

Sketch the circle x² + y² = 4 and the level curves x² + 2y² = 4 and x² + 2y² = 8. Mark where each touches the circle.

<details><summary>Answer</summary>

x² + 2y² = 4 is an ellipse through (±2, 0) and (0, ±√2). It sits inside the circle and touches it at (±2, 0).

x² + 2y² = 8 is an ellipse through (±2√2, 0) and (0, ±2). It sits outside and touches the circle at (0, ±2).

The touching points are exactly the min (f = 4) and max (f = 8) from M3. At each touch, the curves share a tangent, so the gradients are parallel.

From: §1

</details>

---

### M5: Explain

Why can't Lagrange give a maximum for x² + y² + z² on the plane x + y + z = 1?

<details><summary>Answer</summary>

The plane goes on forever (not bounded, so not compact). You can move further and further from the origin on it, so x² + y² + z² has no largest value.

Lagrange still finds the one candidate, but it's the **minimum** (the closest point to the origin).

From: §2

</details>
