# Topic 9: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Tutorial questions

### Q9 (Tutorial Sheet 3 Q9)

Find the tangent line to the curve at the point.

(a) x² + y² = 4 at (√2, √2)  (b) x² − y = 1 at (√2, 1)

<details><summary>Answer</summary>

**(a)** ∇f = ⟨2x, 2y⟩ → ⟨2√2, 2√2⟩.

2√2(x − √2) + 2√2(y − √2) = 0 ⟹ **√2 x + √2 y = 4** (or x + y = 2√2).

**(b)** ∇f = ⟨2x, −1⟩ → ⟨2√2, −1⟩.

2√2(x − √2) − (y − 1) = 0 ⟹ **y = 2√2 x − 3**.

From: §2

</details>

---

### Q10 (Tutorial Sheet 3 Q10)

Find the tangent plane to the surface at the point.

(a) x² + y² − z² = 18 at (3, 5, −4)

(b) 2z − x² = 0 at (2, 0, 2)

(c) cos(πx) − x²y + e^(xz) + yz = 4 at (0, 1, 2)

(d) x² + y² − 2xy − x + 3y − z = −4 at (2, −3, 18)

<details><summary>Answer</summary>

**(a)** ∇F = ⟨2x, 2y, −2z⟩ → ⟨6, 10, 8⟩.

6(x − 3) + 10(y − 5) + 8(z + 4) = 0 ⟹ **3x + 5y + 4z = 18**.

**(b)** ∇F = ⟨−2x, 0, 2⟩ → ⟨−4, 0, 2⟩.

−4(x − 2) + 2(z − 2) = 0 ⟹ **−2x + z + 2 = 0**.

**(c)** ∇F = ⟨−π sin(πx) − 2xy + ze^(xz), −x² + z, xe^(xz) + y⟩ → ⟨2, 2, 1⟩.

2x + 2(y − 1) + (z − 2) = 0 ⟹ **2x + 2y + z − 4 = 0**.

**(d)** ∇F = ⟨2x − 2y − 1, 2y − 2x + 3, −1⟩ → ⟨9, −7, −1⟩.

9(x − 2) − 7(y + 3) − (z − 18) = 0 ⟹ **9x − 7y − z = 21**.

From: §4

</details>

---

### E1 (Tutorial Sample exam Q5 a)

Find the tangent plane Π to the level surface cos(x + 2y + 3z) = 0 at Q = (π/2, π, π).

<details><summary>Answer</summary>

∇F(Q) = −sin(11π/2)⟨1, 2, 3⟩ = ⟨1, 2, 3⟩.

$$\Pi: \left(x - \frac{\pi}{2}\right) + 2(y - \pi) + 3(z - \pi) = 0 \iff x + 2y + 3z = \frac{11\pi}{2}$$

From: §5

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. ∇f(a, b) is perpendicular to the level curve of f through (a, b).
2. The tangent plane to F(x, y, z) = c has normal vector ∇F.
3. For z = f(x, y), the tangent plane is z − c = f_x(x − a) + f_y(y − b).
4. The tangent line to x² + y² = 25 at (3, 4) is 3x + 4y = 25.
5. To use the tangent-plane formula, the right-hand side of the surface equation must be 0.

<details><summary>Answer</summary>

1. **True.** (§1)
2. **True.** (§4)
3. **True.** (§4)
4. **True.** ∇f = ⟨6, 8⟩: 6(x − 3) + 8(y − 4) = 0 ⟹ 3x + 4y = 25. (§2)
5. **False.** Any constant is fine. Constants vanish when you differentiate. (§4)

</details>

---

### M2: Multiple choice

What is a normal vector to the surface xyz = 6 at (1, 2, 3)?

- A. ⟨1, 2, 3⟩
- B. ⟨6, 3, 2⟩
- C. ⟨3, 2, 1⟩
- D. ⟨2, 3, 6⟩

<details><summary>Answer</summary>

**B.** ∇F = ⟨yz, xz, xy⟩ = ⟨6, 3, 2⟩.

From: §3

</details>

---

### M3: Calculate

Find the tangent plane to z = x² + 3y² at (1, 1, 4).

<details><summary>Answer</summary>

Explicit form. f_x = 2x = 2, f_y = 6y = 6.

z − 4 = 2(x − 1) + 6(y − 1) ⟹ **2x + 6y − z = 4**.

Check: 2 + 6 − 4 = 4 ✓.

From: §4

</details>

---

### M4: Sketch

Sketch the circle x² + y² = 4. At (√2, √2) draw the gradient vector and the tangent line from Q9(a).

<details><summary>Answer</summary>

Circle of radius 2 centred at the origin.

At (√2, √2) (45° up and right) draw the arrow ⟨2√2, 2√2⟩ pointing straight outwards, away from the centre.

Draw the tangent line x + y = 2√2 just touching the circle there, at right angles to the arrow. It crosses both axes at 2√2 ≈ 2.83.

From: §1, §2

</details>

---

### M5: Explain

Why is the gradient perpendicular to a level curve?

<details><summary>Answer</summary>

Moving along a level curve, f stays the same, so the rate of change in the tangent direction t is 0.

That rate is ∇f · t (Topic 8). So ∇f · t = 0, which means ∇f is perpendicular to t.

From: §1

</details>
