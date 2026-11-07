# Topic 16: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Sheet 5 has no printed answers. The full working here is mine (unofficial), checked in Python (sympy `dsolve`).

---

## Part A: Tutorial questions

### Q3 (Tutorial Sheet 5 Q3)

Find the general solution.

(a) y″ + 3y′ + 2y = 0  (b) y″ − 9y′ = 0  (c) y″ + 10y′ + 25y = 0  (d) y″ + 2y′ + 2y = 0

<details><summary>Answer</summary>

**(a)** r² + 3r + 2 = (r + 1)(r + 2) = 0. r = −1, −2.

$$y = C_1e^{-x} + C_2e^{-2x}$$

**(b)** r² − 9r = r(r − 9) = 0. r = 0, 9.

$$y = C_1 + C_2e^{9x}$$

**(c)** r² + 10r + 25 = (r + 5)² = 0. Double root r = −5.

$$y = (C_1 + C_2x)e^{-5x}$$

**(d)** r = (−2 ± √(4 − 8))/2 = −1 ± i. k = −1, ω = 1.

$$y = e^{-x}(C_1\cos x + C_2\sin x)$$

From: §2

</details>

---

### Q5a (Tutorial Sheet 5 Q5 a)

Solve y″ − 16y = 0, y(0) = 1, y′(0) = 20.

<details><summary>Answer</summary>

r = ±4, y = C₁e^(4x) + C₂e^(−4x).

C₁ + C₂ = 1 and 4C₁ − 4C₂ = 20 ⟹ C₁ = 3, C₂ = −2.

$$y = 3e^{4x} - 2e^{-4x}$$

From: §4

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. The auxiliary equation of y″ − 2y′ + y = 0 has a double root.
2. A double root r gives y = C₁e^(rx) + C₂e^(rx).
3. Roots 3 ± 2i give y = e^(3x)(C₁cos 2x + C₂sin 2x).
4. A second-order IVP needs two conditions.
5. y″ + 9y = 0 has solutions that grow exponentially.

<details><summary>Answer</summary>

1. **True.** (r − 1)² = 0. (§2)
2. **False.** That's really only one constant. You need (C₁ + C₂x)e^(rx). (§2)
3. **True.** (§2)
4. **True.** (§1)
5. **False.** r = ±3i, y = C₁cos 3x + C₂sin 3x: they just oscillate. (§2)

</details>

---

### M2: Multiple choice

The general solution of y″ + 6y′ + 9y = 0 is:

- A. C₁e^(3x) + C₂e^(−3x)
- B. (C₁ + C₂x)e^(−3x)
- C. (C₁ + C₂x)e^(3x)
- D. C₁cos 3x + C₂sin 3x

<details><summary>Answer</summary>

**B.** r² + 6r + 9 = (r + 3)² = 0, double root −3.

From: §2

</details>

---

### M3: Calculate

Solve y″ + 4y = 0 with y(0) = 2, y′(0) = 6.

<details><summary>Answer</summary>

r = ±2i: y = C₁cos 2x + C₂sin 2x.

y(0) = C₁ = 2. y′ = −2C₁sin 2x + 2C₂cos 2x, so y′(0) = 2C₂ = 6, C₂ = 3.

$$y = 2\cos 2x + 3\sin 2x$$

From: §2, §4

</details>

---

### M4: Sketch

Roughly sketch one typical solution for each case: (a) roots −1, −2; (b) roots ±2i; (c) roots −1 ± 2i.

<details><summary>Answer</summary>

(a) A curve that decays smoothly to 0, like the curves in the notes figure.

(b) A steady wave (cos/sin) that keeps the same height forever.

(c) A wave whose height shrinks: oscillation inside an e^(−x) envelope, dying away to 0.

From: §3

</details>

---

### M5: Explain

Why is y = e^(rx) a solution of ay″ + by′ + cy = 0 exactly when ar² + br + c = 0?

<details><summary>Answer</summary>

y′ = re^(rx) and y″ = r²e^(rx). Plugging in gives e^(rx)(ar² + br + c).

e^(rx) is never 0, so this is 0 exactly when ar² + br + c = 0.

From: §2

</details>
