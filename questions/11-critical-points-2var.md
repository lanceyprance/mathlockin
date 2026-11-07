# Topic 11: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Sheet 4 has short answers only. The full working here is mine (unofficial), checked in Python.

---

## Part A: Tutorial questions

### Q7 (Tutorial Sheet 4 Q7)

Find the critical points.

(a) x³ + y³ − 3xy  (b) x³ + 3xy² − 12x − 6y  (c) x⁴ + y⁴ − 3x³ − y³

<details><summary>Answer</summary>

**(a)** y = x² and x = y², so x⁴ = x: **(0, 0), (1, 1)**.

**(b)** $f_x = 3x^2 + 3y^2 - 12 = 0 \Rightarrow x^2 + y^2 = 4$. $f_y = 6xy - 6 = 0 \Rightarrow xy = 1$.

Then (x + y)² = 4 + 2 = 6 and (x − y)² = 4 − 2 = 2. So x + y = ±√6, x − y = ±√2.

Four points (a = √(2 + √3) = (√6 + √2)/2, b = √(2 − √3) = (√6 − √2)/2):

**(a, b), (b, a), (−a, −b), (−b, −a)**.

**(c)** $f_x = x^2(4x - 9)$, $f_y = y^2(4y - 3)$. x ∈ {0, 9/4}, y ∈ {0, 3/4}:

**(0, 0), (0, 3/4), (9/4, 0), (9/4, 3/4)**.

From: §2

</details>

---

### Q8 (Tutorial Sheet 4 Q8)

Find and classify the critical points.

(a) x² − y²  (b) x² + 2y² − 4x + 4y  (c) y(x − 1) + 8/x  (d) xy e^(−(x² + y²)/2)

<details><summary>Answer</summary>

**(a)** (0, 0). $f_{xx} = 2$, $f_{yy} = -2$, $f_{xy} = 0$. D = −4 < 0: **saddle**.

**(b)** (2, −1). D = 2·4 − 0 = 8 > 0, $f_{xx}$ = 2 > 0: **local min**.

**(c)** $f_x = y - 8/x^2$, $f_y = x - 1$. So x = 1, y = 8: (1, 8).

$f_{xx} = 16/x^3 = 16$, $f_{yy} = 0$, $f_{xy} = 1$. D = −1 < 0: **saddle**.

**(d)** (0, 0) saddle. (1, 1) and (−1, −1) local max (value 1/e). (1, −1) and (−1, 1) local min (value −1/e). Full working in notes §5.

From: §4, §5

</details>

---

### Q12 (Tutorial Sheet 4 Q12)

Investigate the critical points of x⁴ + y⁴ − 2x² + 4xy − 2y², and find the local minimum values.

<details><summary>Answer</summary>

$f_x = 4x^3 - 4x + 4y$, $f_y = 4y^3 + 4x - 4y$.

Add them: 4x³ + 4y³ = 0, so y = −x.

Into $f_x$: 4x³ − 8x = 0, so x = 0 or x = ±√2.

Points: (0, 0), (√2, −√2), (−√2, √2).

$f_{xx} = 12x^2 - 4$, $f_{yy} = 12y^2 - 4$, $f_{xy} = 4$.

**(±√2, ∓√2):** $f_{xx} = f_{yy} = 20$. D = 400 − 16 = 384 > 0, $f_{xx}$ > 0: **local min**. Value 4 + 4 − 4 − 8 − 4 = **−8**.

**(0, 0):** D = (−4)(−4) − 16 = 0. **Test fails.** Check paths:

- along y = 0: f = x⁴ − 2x² < 0 for small x ≠ 0
- along y = x: f = 2x⁴ > 0

f takes values above and below f(0, 0) = 0 nearby: **saddle**.

From: §4

</details>

---

### Q13 (Tutorial Sheet 4 Q13)

Find the real critical points of 4xy − x² − y² − x²y² and classify them.

<details><summary>Answer</summary>

$f_x = 4y - 2x - 2xy^2$, $f_y = 4x - 2y - 2x^2y$.

Subtract: 4(y − x) − 2(x − y) − 2xy(y − x) = (y − x)(6 − 2xy) = 0.

- y = x: 4x − 2x − 2x³ = 0, so x(1 − x²) = 0: (0, 0), (1, 1), (−1, −1).
- xy = 3: then $f_x$ = 4y − 2x − 6y = −2(x + y) = 0, so y = −x, giving −x² = 3. No real solution.

$f_{xx} = -2 - 2y^2$, $f_{yy} = -2 - 2x^2$, $f_{xy} = 4 - 4xy$.

**(0, 0):** D = 4 − 16 = −12: **saddle**.

**(±1, ±1):** $f_{xx}$ = −4, $f_{yy}$ = −4, $f_{xy}$ = 0. D = 16 > 0, $f_{xx}$ < 0: **local max** (value 1).

From: §2, §4

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. Every critical point is a local max or a local min.
2. If D < 0 at a critical point, it's a saddle.
3. If D = 0, the point is a saddle.
4. A local max must have $f_x = f_y = 0$ (if the partials exist and the point is interior).
5. If D > 0 and $f_{xx}$ > 0, it's a local minimum.

<details><summary>Answer</summary>

1. **False.** It could be a saddle. (§3)
2. **True.** (§4)
3. **False.** D = 0 means the test tells you nothing. (§4)
4. **True.** Theorem 6.14. (§2)
5. **True.** (§4)

</details>

---

### M2: Multiple choice

At a critical point, $f_{xx} = -3$, $f_{yy} = -2$, $f_{xy} = 1$. The point is a:

- A. local minimum
- B. local maximum
- C. saddle point
- D. can't tell

<details><summary>Answer</summary>

**B.** D = 6 − 1 = 5 > 0 and $f_{xx}$ < 0.

From: §4

</details>

---

### M3: Calculate

Find and classify the critical points of f = x³ − 3x + y² − 4y.

<details><summary>Answer</summary>

$f_x = 3x^2 - 3 = 0 \Rightarrow x = \pm1$. $f_y = 2y - 4 = 0 \Rightarrow y = 2$.

$f_{xx} = 6x$, $f_{yy} = 2$, $f_{xy} = 0$. D = 12x.

**(1, 2):** D = 12 > 0, $f_{xx}$ = 6 > 0: local min, value 1 − 3 + 4 − 8 = −6.

**(−1, 2):** D = −12 < 0: saddle.

From: §2, §4

</details>

---

### M4: Sketch

Sketch rough level curves near (a) a local minimum and (b) a saddle point.

<details><summary>Answer</summary>

(a) Closed loops (circles or ovals) nested around the point, heights increasing outwards.

(b) Two families of hyperbola-shaped curves, crossing in an X at the point. Heights go up in two opposite regions and down in the other two (like the contour plot of x² − y²).

From: §3

</details>

---

### M5: Explain

Why must you factor rather than divide when solving $x(y - 2) = 0$?

<details><summary>Answer</summary>

Dividing by x assumes x ≠ 0 and throws away the solution x = 0.

Factoring keeps both cases: x = 0 **or** y = 2. Each case can give critical points.

From: §2

</details>
