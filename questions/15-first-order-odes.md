# Topic 15: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Sheet 5 has no printed answers. The full working here is mine (unofficial), checked in Python (sympy `dsolve`).

---

## Part A: Tutorial questions

### Q1 (Tutorial Sheet 5 Q1)

Solve the IVPs. (a) y′ = ty, y(0) = 1. (b) y′ = 1 − y, y(0) = 0.

<details><summary>Answer</summary>

**(a)** Separable: dy/y = t dt ⟹ ln|y| = t²/2 + C ⟹ y = Ae^(t²/2). y(0) = 1 ⟹ A = 1.

$$y = e^{t^2/2}$$

**(b)** Linear: y′ + y = 1, G = eᵗ. (eᵗy)′ = eᵗ ⟹ eᵗy = eᵗ + C ⟹ y = 1 + Ce^(−t). y(0) = 0 ⟹ C = −1.

$$y = 1 - e^{-t}$$

From: §3, §4

</details>

---

### Q2a (Tutorial Sheet 5 Q2 a–c)

Solve. (a) y′ = (1 + x)(1 + y). (b) dy/dt = e^(−y)t². (c) y′ = 1 + x² + y + x²y.

<details><summary>Answer</summary>

**(a)** dy/(1 + y) = (1 + x) dx ⟹ ln|1 + y| = x + x²/2 + C.

$$y = Ae^{x + x^2/2} - 1$$

**(b)** eʸ dy = t² dt ⟹ eʸ = t³/3 + C.

$$y = \ln\left(\frac{t^3}{3} + C\right)$$

**(c)** Factor: 1 + x² + y + x²y = (1 + x²)(1 + y). Separable:

ln|1 + y| = x + x³/3 + C ⟹

$$y = Ae^{x + x^3/3} - 1$$

From: §3

</details>

---

### Q2d (Tutorial Sheet 5 Q2 d–f)

Solve. (d) y′ + 2xy = xe^(−x²). (e) y′ + 2y/x = 1/x². (f) y′ + xy = x/y.

<details><summary>Answer</summary>

**(d)** Linear, p = 2x, G = e^(x²).

(e^(x²)y)′ = x ⟹ e^(x²)y = x²/2 + C ⟹

$$y = \left(\frac{x^2}{2} + C\right)e^{-x^2}$$

**(e)** G = x². (x²y)′ = 1 ⟹

$$y = \frac{x + C}{x^2}$$

**(f)** Not linear (1/y). But y′ = x/y − xy = x(1 − y²)/y is **separable**:

$$\frac{y}{1-y^2}\,dy = x\,dx \implies -\frac12\ln|1-y^2| = \frac{x^2}{2} + C$$

⟹ 1 − y² = Ae^(−x²) ⟹

$$y = \pm\sqrt{1 - Ae^{-x^2}}$$

From: §3, §4, §6

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. y′ + y² = x is linear.
2. y′ = xy + x is separable.
3. For y′ + p(x)y = q(x), the integrating factor is e^(∫p dx).
4. A first-order general solution has two arbitrary constants.
5. The constant of integration should be added after dividing by G.

<details><summary>Answer</summary>

1. **False.** y² makes it non-linear. (§1)
2. **True.** xy + x = x(y + 1). (§3)
3. **True.** (§4)
4. **False.** One. (§5)
5. **False.** Add it when you integrate, before dividing. (§5)

</details>

---

### M2: Multiple choice

The integrating factor for xy′ + 3y = x² (x > 0) is:

- A. e^(3x)
- B. x³
- C. 3 ln x
- D. x

<details><summary>Answer</summary>

**B.** Divide by x: y′ + (3/x)y = x. ∫3/x dx = 3 ln x. G = e^(3 ln x) = x³.

From: §4

</details>

---

### M3: Calculate

Solve xy′ + 2y = 5x³ with y(1) = 5/4 (notes Ex 8.24).

<details><summary>Answer</summary>

Standard form: y′ + (2/x)y = 5x². G = x².

(x²y)′ = 5x⁴ ⟹ x²y = x⁵ + C ⟹ y = x³ + C/x².

y(1) = 1 + C = 5/4 ⟹ C = 1/4.

$$y = x^3 + \frac{1}{4x^2}$$

From: §4

</details>

---

### M4: Sketch

Sketch a few solutions of y′ = 1 − y (y = 1 + Ce^(−t)) for C = −1, 0, 1, and highlight the one with y(0) = 0.

<details><summary>Answer</summary>

C = 0: the flat line y = 1.

C = 1: starts at y = 2 when t = 0 and decays down towards 1.

C = −1: starts at y = 0 and rises up towards 1. That's the IVP solution 1 − e^(−t): highlight it.

All curves approach the line y = 1 as t grows.

From: §2

</details>

---

### M5: Explain

Why does multiplying y′ + p y = q by G = e^(∫p) make it solvable?

<details><summary>Answer</summary>

G′ = pG (chain rule). So G y′ + G p y = G y′ + G′ y, which is (G y)′ by the product rule.

The equation becomes (G y)′ = G q. Now both sides can be integrated directly.

From: §4

</details>
