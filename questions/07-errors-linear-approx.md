# Topic 7: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Tutorial questions

### Q9 (Tutorial Sheet 2 Q9)

The rigidity of a wire is η = kx/z⁴. Estimate the percentage error in η if x is overestimated by 0.5% and z is underestimated by 1%.

<details><summary>Answer</summary>

η = kx¹z⁻⁴.

$$100\frac{\Delta\eta}{\eta} \approx 1(0.5) - 4(-1) = 4.5$$

**4.5%** (too big).

From: §3

</details>

---

### Q10 (Tutorial Sheet 2 Q10)

D = kHL/V^(1/2). Find the approximate % error in D if H and V both increase by 1% and L decreases by 2%.

<details><summary>Answer</summary>

D = kH¹L¹V^(−1/2).

$$100\frac{\Delta D}{D} \approx 1(1) + 1(-2) - \frac12(1) = -\frac32$$

A **1.5% decrease** (−3/2 %).

From: §3

</details>

---

### Q11 (Tutorial Sheet 2 Q11)

Use linear approximation on f(x, y) = (x² + y³)^(1/2) to estimate ((1.02)² + (2.01)³)^(1/2), to two decimals.

<details><summary>Answer</summary>

At (1, 2): f = 3, $f_x = \frac13$, $f_y = 2$.

$$L(x,y) = 3 + \frac13(x-1) + 2(y-2)$$

$$L(1.02, 2.01) = 3 + \frac{0.02}{3} + 0.02 \approx 3.03$$

From: §4, §5

</details>

---

### Q12 (Tutorial Sheet 2 Q12)

Estimate ((3.8)² + 2(2.1)³)^(1/5).

<details><summary>Answer</summary>

f(x, y) = (x² + 2y³)^(1/5). Nice point (4, 2): f = (16 + 16)^(1/5) = 32^(1/5) = 2.

$$f_x = \frac{2x}{5}(x^2+2y^3)^{-4/5}, \quad f_y = \frac{6y^2}{5}(x^2+2y^3)^{-4/5}$$

$32^{-4/5} = \frac{1}{16}$. So $f_x(4,2) = \frac{8}{5}\cdot\frac{1}{16} = \frac{1}{10}$, $f_y(4,2) = \frac{24}{5}\cdot\frac1{16} = \frac{3}{10}$.

$$L(3.8, 2.1) = 2 + \frac{1}{10}(-0.2) + \frac{3}{10}(0.1) = 2 - 0.02 + 0.03 = 2.01$$

From: §4

</details>

---

### E1 (Tutorial Sample exam Q3 c)

L = 4πR²σT⁴. Find the approximate % error in L if R increases by 4% and T decreases by 1%.

<details><summary>Answer</summary>

$$100\frac{\Delta L}{L} \approx 2(4) + 4(-1) = 4$$

A **4% increase**.

From: §6

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. In the power law shortcut, the constant k affects the answer.
2. "Underestimated by 2%" means a percentage change of −2.
3. The linearisation of f at (a, b) equals f(a, b) at (a, b).
4. For z = x + y, the % error in z is the % error in x plus the % error in y.
5. Linear approximation works best close to the chosen point.

<details><summary>Answer</summary>

1. **False.** It cancels. (§3)
2. **True.** (§2)
3. **True.** (§4)
4. **False.** The shortcut is only for products of powers. Use Δz ≈ Δx + Δy and divide by z. (§3)
5. **True.** (§4)

</details>

---

### M2: Multiple choice

The volume of a cone is V = (1/3)πr²h. r increases by 2% and h decreases by 3%. The approximate % change in V is:

- A. −1%
- B. +1%
- C. +7%
- D. −5%

<details><summary>Answer</summary>

**B.** 2(2) + 1(−3) = 4 − 3 = +1%.

From: §3

</details>

---

### M3: Calculate

Find the linearisation of f(x, y) = x²y at (2, 1), and use it to estimate (2.05)²(0.97).

<details><summary>Answer</summary>

f(2, 1) = 4. $f_x = 2xy = 4$, $f_y = x^2 = 4$.

$$L(x,y) = 4 + 4(x-2) + 4(y-1)$$

$$L(2.05, 0.97) = 4 + 4(0.05) + 4(-0.03) = 4 + 0.2 - 0.12 = 4.08$$

(The true value is 4.0764…)

From: §4

</details>

---

### M4: Sketch

On one sketch, draw the curve y = √x and its tangent line at x = 4. Mark where the line gives the estimate of √4.1.

<details><summary>Answer</summary>

The tangent at (4, 2) has slope 1/(2√4) = 1/4: y = 2 + (x − 4)/4.

Draw the curve rising and flattening out, with the straight line touching it at (4, 2).

At x = 4.1 the line gives 2.025. The curve is just below the line there (√4.1 ≈ 2.0248), because √x bends downwards.

From: §4

</details>

---

### M5: Explain

Why do we choose (1, 2) and not (1.02, 2.01) as the point (a, b) in Sheet 2 Q11?

<details><summary>Answer</summary>

We need f(a, b), f_x(a, b) and f_y(a, b) exactly and easily, with no calculator tricks.

At (1, 2), x² + y³ = 9, so the square root is exactly 3. At (1.02, 2.01) it's the ugly number we're trying to find.

From: §4

</details>
