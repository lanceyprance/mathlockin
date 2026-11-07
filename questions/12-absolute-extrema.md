# Topic 12: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Sheet 4 has short answers only. The full working here is mine (unofficial), checked in Python.

---

## Part A: Tutorial questions

### Q14 (Tutorial Sheet 4 Q14)

A circular plate is x² + y² ≤ 1. The temperature is T = x² + 2y² − x. Find the hottest and coldest points (check the boundary).

<details><summary>Answer</summary>

**Interior:** (1/2, 0), T = −1/4.

**Boundary:** T = 2 − x² − x on −1 ≤ x ≤ 1. Max at x = −1/2: T = 9/4 at (−1/2, ±√3/2). Endpoints: T(1, 0) = 0, T(−1, 0) = 2.

**Hottest:** (−1/2, √3/2) and (−1/2, −√3/2), T = **9/4**.

**Coldest:** (1/2, 0), T = **−1/4**.

From: §3, §4

</details>

---

### N1 (Tutorial Notes Example 6.22)

Find the absolute max and min of f = x² − 2xy + 2y on the rectangle 0 ≤ x ≤ 3, 0 ≤ y ≤ 2.

<details><summary>Answer</summary>

**Interior:** $f_x = 2x - 2y = 0$, $f_y = -2x + 2 = 0$ → (1, 1), f = 1.

**Boundary:**

| Edge | f becomes | max | min |
|---|---|---|---|
| L₁: y = 0, 0 ≤ x ≤ 3 | x² | 9 at (3, 0) | 0 at (0, 0) |
| L₂: x = 3, 0 ≤ y ≤ 2 | 9 − 4y | 9 at (3, 0) | 1 at (3, 2) |
| L₃: y = 2, 0 ≤ x ≤ 3 | x² − 4x + 4 = (x − 2)² | 4 at (0, 2) | 0 at (2, 2) |
| L₄: x = 0, 0 ≤ y ≤ 2 | 2y | 4 at (0, 2) | 0 at (0, 0) |

**Compare:** absolute max **9** at (3, 0). Absolute min **0** at (0, 0) and (2, 2).

From: §3

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. The closed unit disk is compact.
2. The open unit disk is compact.
3. A continuous function on a compact region always has an absolute max and min.
4. You must classify interior critical points with the second derivatives test.
5. The absolute max can be on the boundary.

<details><summary>Answer</summary>

1. **True.** Closed and bounded. (§1)
2. **False.** Not closed. (§1)
3. **True.** Extreme Value Theorem. (§2)
4. **False.** Just compare values. (§3)
5. **True.** Often it is. (§3)

</details>

---

### M2: Multiple choice

f = x + y on the closed unit disk. The absolute max is:

- A. 1
- B. 2
- C. √2
- D. 0

<details><summary>Answer</summary>

**C.** No interior critical points (∇f = ⟨1, 1⟩ ≠ 0). On the circle, the largest x + y is at (1/√2, 1/√2), giving √2.

From: §3

</details>

---

### M3: Calculate

Find the absolute max and min of f = x² + y² − 2x on the disk x² + y² ≤ 4.

<details><summary>Answer</summary>

**Interior:** $f_x = 2x - 2 = 0$, $f_y = 2y = 0$ → (1, 0), inside. f = −1.

**Boundary:** x² + y² = 4, so f = 4 − 2x with −2 ≤ x ≤ 2. It's a straight line in x: max 8 at x = −2, min 0 at x = 2.

**Compare:** absolute max **8** at (−2, 0). Absolute min **−1** at (1, 0).

From: §3

</details>

---

### M4: Sketch

Sketch the triangle D with corners (0, 0), (2, 0), (0, 2). Label its three boundary pieces and write the equation of each.

<details><summary>Answer</summary>

Right-angled triangle in the first quadrant.

- L₁: bottom, y = 0, 0 ≤ x ≤ 2
- L₂: left side, x = 0, 0 ≤ y ≤ 2
- L₃: slanted side, y = 2 − x, 0 ≤ x ≤ 2

On L₃ you'd substitute y = 2 − x to get a function of x alone.

From: §3

</details>

---

### M5: Explain

Why do we need to check the endpoints (corners) of each boundary piece, not just where the derivative is 0?

<details><summary>Answer</summary>

On a closed interval, a one-variable function can take its max or min at an endpoint, where the derivative needn't be 0.

E.g. on L₁ in N1, f = x² has its max at the endpoint x = 3, where f′ = 6 ≠ 0.

From: §3

</details>
