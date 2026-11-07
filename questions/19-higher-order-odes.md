# Topic 19: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Sheet 5 has no printed answers. The full working here is mine (unofficial), checked in Python (sympy `dsolve`).

---

## Part A: Tutorial questions

### Q7 (Tutorial Sheet 5 Q7)

(a) y⁽⁴⁾ − 16y = 30 sin t, y(0) = 0, y′(0) = 2, y″(π) = 0, y‴(π) = −18.

(b) y⁽⁴⁾ − 16y = 30 sin 2t.

(c) y‴ + y″ + y′ + y = t, y(0) = y′(0) = y″(0) = 0.

<details><summary>Answer</summary>

**(a)** r⁴ − 16 = (r² − 4)(r² + 4): ±2, ±2i.

y_h = C₁e^(2t) + C₂e^(−2t) + C₃cos 2t + C₄sin 2t.

y_p = A cos t + B sin t. Since y_p⁽⁴⁾ = y_p: −15y_p = 30 sin t ⟹ y_p = −2 sin t.

Conditions:

- y(0): C₁ + C₂ + C₃ = 0
- y′(0): 2C₁ − 2C₂ + 2C₄ − 2 = 2
- y″(π): 4C₁e^(2π) + 4C₂e^(−2π) − 4C₃ = 0
- y‴(π): 8C₁e^(2π) − 8C₂e^(−2π) − 8C₄ − 2 = −18

C₁ = C₂ = C₃ = 0, C₄ = 2 satisfies all four (and the solution is unique).

$$y = 2\sin 2t - 2\sin t$$

**(b)** sin 2t clashes (±2i): y_p = t(A cos 2t + B sin 2t) ⟹ A = 15/16, B = 0.

$$y = C_1e^{2t} + C_2e^{-2t} + C_3\cos 2t + C_4\sin 2t + \frac{15}{16}t\cos 2t$$

**(c)** r³ + r² + r + 1 = (r + 1)(r² + 1): −1, ±i. y_p = At + B ⟹ A = 1, B = −1.

y = C₁e^(−t) + C₂cos t + C₃sin t + t − 1. Conditions: C₁ + C₂ = 1, −C₁ + C₃ = −1, C₁ − C₂ = 0 ⟹ C₁ = C₂ = 1/2, C₃ = −1/2.

$$y = \frac12e^{-t} + \frac12\cos t - \frac12\sin t + t - 1$$

From: §2, §3

</details>

---

### Q8a (Tutorial Sheet 5 Q8 a–d)

(a) y‴ + 4y″ − y′ − 4y = 0  (b) y‴ + 4y″ − 3y′ − 18y = 0  (c) y‴ + 6y″ + 12y′ + 8y = 0

(d) y‴ + 4y″ − 7y′ − 10y = 0, y(0) = −3, y′(0) = 12, y″(0) = −36

<details><summary>Answer</summary>

**(a)** r²(r + 4) − (r + 4) = (r + 4)(r − 1)(r + 1).

$$y = C_1e^x + C_2e^{-x} + C_3e^{-4x}$$

**(b)** r = 2 is a root: (r − 2)(r² + 6r + 9) = (r − 2)(r + 3)².

$$y = C_1e^{2x} + (C_2 + C_3x)e^{-3x}$$

**(c)** (r + 2)³: triple root −2.

$$y = (C_1 + C_2x + C_3x^2)e^{-2x}$$

**(d)** (r − 2)(r + 1)(r + 5). y = C₁e^(2x) + C₂e^(−x) + C₃e^(−5x).

C₁ + C₂ + C₃ = −3, 2C₁ − C₂ − 5C₃ = 12, 4C₁ + C₂ + 25C₃ = −36 ⟹ C₁ = 1, C₂ = −5/2, C₃ = −3/2.

$$y = e^{2x} - \frac52e^{-x} - \frac32e^{-5x}$$

From: §1, §2

</details>

---

### Q8e (Tutorial Sheet 5 Q8 e, f)

(e) y‴ + 4y″ − 7y′ − 10y = 100x² − 64e^(3x), y(0) = −20, y′(0) = −29/5, y″(0) = 19/5

(f) y‴ − 5y″ − y′ + 5y = 10x − 63e^(−2x) + 29 sin 2x

<details><summary>Answer</summary>

**(e)** Full working in notes §4.

$$y = -2e^{2x} - \frac15e^{-x} + 2e^{-5x} - 10x^2 + 14x - \frac{89}{5} - 2e^{3x}$$

**(f)** p(r) = r²(r − 5) − (r − 5) = (r − 5)(r − 1)(r + 1).

Guess y_p = Ax + B + Ce^(−2x) + D cos 2x + E sin 2x (no clashes).

- Polynomial: 5A = 10, −A + 5B = 0 ⟹ A = 2, B = 2/5.
- e^(−2x): C·p(−2) = C(−8 − 20 + 2 + 5) = −21C = −63 ⟹ C = 3.
- Trig: p(D)cos 2x = 25 cos 2x + 10 sin 2x and p(D)sin 2x = 25 sin 2x − 10 cos 2x. Matching 29 sin 2x: 25D − 10E = 0, 10D + 25E = 29 ⟹ E = 1, D = 2/5.

$$y = C_1e^{5x} + C_2e^x + C_3e^{-x} + 2x + \frac25 + 3e^{-2x} + \frac25\cos 2x + \sin 2x$$

From: §2, §4

</details>

---

### Q8g (Tutorial Sheet 5 Q8 g, h)

(g) y⁽⁴⁾ + 8y″ + 16y = 0, y(0) = −1, y′(0) = 5, y″(0) = −8, y‴(0) = −28

(h) y⁽⁴⁾ + 8y″ + 16y = 64x sin 2x

<details><summary>Answer</summary>

**(g)** (r² + 4)²: ±2i double. y = (C₁ + C₂x)cos 2x + (C₃ + C₄x)sin 2x.

At 0: y = C₁, y′ = C₂ + 2C₃, y″ = −4C₁ + 4C₄, y‴ = −12C₂ − 8C₃.

C₁ = −1. −4(−1) + 4C₄ = −8 ⟹ C₄ = −3. C₂ + 2C₃ = 5 and −12C₂ − 8C₃ = −28 ⟹ C₃ = 2, C₂ = 1.

$$y = (x - 1)\cos 2x + (2 - 3x)\sin 2x$$

**(h)** f = 64x sin 2x and ±2i has multiplicity 2, so multiply the usual guess by x²:

y_p = x²[(Ax + B)cos 2x + (Cx + D)sin 2x]. Matching (long) gives

$$y_p = -x^2\cos 2x - \frac23x^3\sin 2x$$

$$y = (C_1 + C_2x)\cos 2x + (C_3 + C_4x)\sin 2x - x^2\cos 2x - \frac23x^3\sin 2x$$

(Checked by substituting back.)

From: §2, §3

</details>

---

### Q8i (Tutorial Sheet 5 Q8 i, j)

(i) y⁽⁴⁾ + 2y‴ − 2y′ − y = 24xe^(−x) + 24eˣ − 8 sin x, y(0) = −2, y′(0) = 0, y″(0) = 6, y‴(0) = 10

(j) y⁽⁴⁾ + 18y″ + 81y = 64x cos x + 108x cos 3x

<details><summary>Answer</summary>

**(i)** p(r) = (r − 1)(r + 1)³: 1 (single), −1 (triple).

y_h = C₁eˣ + (C₂ + C₃x + C₄x²)e^(−x).

Guess: xe^(−x) clashes with a triple root → x³(Ax + B)e^(−x). eˣ clashes once → Cxeˣ. sin x → D cos x + E sin x.

Matching gives y_p = −(x⁴/2 + x³)e^(−x) + 3xeˣ − 2 cos x. The conditions then give C₁ = −1, C₂ = 1, C₃ = −1, C₄ = −2:

$$y = (3x - 1)e^x + \left(1 - x - 2x^2 - x^3 - \frac{x^4}{2}\right)e^{-x} - 2\cos x$$

**(j)** (r² + 9)²: ±3i double. cos x: no clash → (Ax + B)cos x + (Cx + D)sin x. x cos 3x: double clash → x²[(Ex + F)cos 3x + (Gx + H)sin 3x].

$$y_p = x\cos x + \frac12\sin x - \frac{x^3}{2}\cos 3x + \frac{x^2}{2}\sin 3x$$

$$y = (C_1 + C_2x)\cos 3x + (C_3 + C_4x)\sin 3x + y_p$$

(Checked by substituting back.)

From: §2, §3

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. A third order ODE has three arbitrary constants in its general solution.
2. A triple root r gives e^(rx), xe^(rx), x²e^(rx).
3. A cubic auxiliary polynomial can have no real roots.
4. If e^(2x) appears in f and 2 is a double root, guess Ax²e^(2x).
5. r⁴ − 16 = 0 has four real roots.

<details><summary>Answer</summary>

1. **True.** (§2)
2. **True.** (§2)
3. **False.** Every real cubic has at least one real root. (§1)
4. **True.** Multiply by x^k with k = 2. (§2)
5. **False.** ±2 and ±2i. (§1)

</details>

---

### M2: Multiple choice

The general solution of y‴ − y′ = 0 is:

- A. C₁ + C₂eˣ + C₃e^(−x)
- B. C₁eˣ + C₂e^(−x)
- C. (C₁ + C₂x + C₃x²)eˣ
- D. C₁ + C₂cos x + C₃sin x

<details><summary>Answer</summary>

**A.** r³ − r = r(r − 1)(r + 1): roots 0, 1, −1.

From: §2

</details>

---

### M3: Calculate

Solve y‴ − 3y″ + 3y′ − y = 0.

<details><summary>Answer</summary>

r³ − 3r² + 3r − 1 = (r − 1)³: triple root 1.

$$y = (C_1 + C_2x + C_3x^2)e^x$$

From: §2

</details>

---

### M4: Sketch

Draw a "root map": mark the roots of (r + 1)²(r² + 4) in the complex plane and write the solution each one gives.

<details><summary>Answer</summary>

- A double dot at −1 on the real axis: e^(−x) and xe^(−x).
- Dots at +2i and −2i on the imaginary axis: cos 2x and sin 2x.

y_h = (C₁ + C₂x)e^(−x) + C₃cos 2x + C₄sin 2x.

From: §2

</details>

---

### M5: Explain

How do you find a root of r³ + 4r² − 3r − 18 without a formula?

<details><summary>Answer</summary>

Any whole-number root must divide the constant term, 18. Try ±1, ±2, ±3, …

r = 2: 8 + 16 − 6 − 18 = 0 ✓. Then divide by (r − 2) to get r² + 6r + 9 = (r + 3)².

From: §1

</details>
