# Topic 17: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Sheet 5 has no printed answers. The full working here is mine (unofficial), checked in Python (sympy `dsolve`).

---

## Part A: Tutorial questions

### Q4a (Tutorial Sheet 5 Q4 a–c)

Find the general solution.

(a) y″ − y = 3x²  (b) y″ + 4y′ − 5y = x²  (c) y″ − y′ − 2y = eˣ + x

<details><summary>Answer</summary>

**(a)** y_h = C₁eˣ + C₂e^(−x). Guess Ax² + Bx + C:

2A − Ax² − Bx − C = 3x² ⟹ A = −3, B = 0, C = 2A = −6.

$$y = C_1e^x + C_2e^{-x} - 3x^2 - 6$$

**(b)** r² + 4r − 5 = (r + 5)(r − 1). y_h = C₁eˣ + C₂e^(−5x). Guess Ax² + Bx + C:

−5A = 1, 8A − 5B = 0, 2A + 4B − 5C = 0 ⟹ A = −1/5, B = −8/25, C = −42/125.

$$y = C_1e^x + C_2e^{-5x} - \frac{x^2}{5} - \frac{8x}{25} - \frac{42}{125}$$

**(c)** Roots 2, −1. y_h = C₁e^(2x) + C₂e^(−x). Guess Aeˣ + Bx + C (no clash).

eˣ: A − A − 2A = 1 ⟹ A = −1/2. x: −2B = 1 ⟹ B = −1/2. const: −B − 2C = 0 ⟹ C = 1/4.

$$y = C_1e^{2x} + C_2e^{-x} - \frac12e^x - \frac x2 + \frac14$$

From: §1, §2

</details>

---

### Q4d (Tutorial Sheet 5 Q4 d–f)

(d) y″ + 6y′ + 9y = 16teᵗ (y a function of t)  (e) y″ − 2y′ + y = x³ + x²  (f) y″ − 4y′ + 4y = (3x² + 2)eˣ

<details><summary>Answer</summary>

**(d)** Double root −3: y_h = (C₁ + C₂t)e^(−3t). Guess (At + B)eᵗ (no clash).

Substituting: (16At + 8A + 16B)eᵗ = 16teᵗ ⟹ A = 1, B = −1/2.

$$y = (C_1 + C_2t)e^{-3t} + \left(t - \frac12\right)e^t$$

**(e)** Double root 1: y_h = (C₁ + C₂x)eˣ. Guess Ax³ + Bx² + Cx + D.

x³: A = 1. x²: −6A + B = 1 ⟹ B = 7. x: 6A − 4B + C = 0 ⟹ C = 22. const: 2B − 2C + D = 0 ⟹ D = 30.

$$y = (C_1 + C_2x)e^x + x^3 + 7x^2 + 22x + 30$$

**(f)** Double root 2: y_h = (C₁ + C₂x)e^(2x). Guess (Ax² + Bx + C)eˣ (no clash: eˣ ≠ e^(2x)).

Shortcut y = ueˣ: the equation becomes u″ − 2u′ + u = 3x² + 2. With u = Ax² + Bx + C: A = 3, −4A + B = 0 ⟹ B = 12, 2A − 2B + C = 2 ⟹ C = 20.

$$y = (C_1 + C_2x)e^{2x} + (3x^2 + 12x + 20)e^x$$

From: §1, §3

</details>

---

### Q5b (Tutorial Sheet 5 Q5 b, c)

(b) y″ − y′ − 2y = 3e^(2x), y(0) = 0, y′(0) = −2.

(c) y″ − 4y′ + 3y = 4e^(3x), y(0) = −1, y′(0) = 3.

<details><summary>Answer</summary>

**(b)** Roots 2, −1: y_h = C₁e^(2x) + C₂e^(−x). e^(2x) clashes, so y_p = Axe^(2x).

y_p′ = A(1 + 2x)e^(2x), y_p″ = A(4 + 4x)e^(2x). Substituting: 3Ae^(2x) = 3e^(2x), A = 1.

y = C₁e^(2x) + C₂e^(−x) + xe^(2x).

y(0) = C₁ + C₂ = 0. y′(0) = 2C₁ − C₂ + 1 = −2. So C₁ = −1, C₂ = 1.

$$y = (x - 1)e^{2x} + e^{-x}$$

**(c)** Roots 1, 3: y_h = C₁eˣ + C₂e^(3x). e^(3x) clashes: y_p = Axe^(3x).

Substituting: 2Ae^(3x) = 4e^(3x), A = 2.

y = C₁eˣ + C₂e^(3x) + 2xe^(3x). C₁ + C₂ = −1 and C₁ + 3C₂ + 2 = 3 ⟹ C₂ = 1, C₁ = −2.

$$y = -2e^x + (2x + 1)e^{3x}$$

From: §1, §3

</details>

---

### E1 (Tutorial Sample exam Q6 b)

Find the general solution of y″ + 4y = t² + cos t.

<details><summary>Answer</summary>

y_h = c₁cos 2t + c₂sin 2t. y_p = At² + Bt + C + D cos t + E sin t.

A = 1/4, B = 0, C = −1/8, D = 1/3, E = 0.

$$y = c_1\cos 2t + c_2\sin 2t + \frac14t^2 - \frac18 + \frac13\cos t$$

From: §4

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. For f(x) = x², the guess Ax² is enough.
2. For f(x) = sin 3x, the guess must include both cos 3x and sin 3x.
3. If eˣ is in y_h and f = eˣ, guess Axeˣ.
4. y_p contains the arbitrary constants C₁, C₂.
5. For an IVP, use the initial conditions on y_h only.

<details><summary>Answer</summary>

1. **False.** Use Ax² + Bx + C. (§1)
2. **True.** (§1)
3. **True.** Modification rule. (§3)
4. **False.** y_p has no arbitrary constants; y_h does. (§1)
5. **False.** Use them on the full y = y_h + y_p. (§1)

</details>

---

### M2: Multiple choice

The correct guess for y_p in y″ + y = sin x is:

- A. A sin x
- B. A cos x + B sin x
- C. x(A cos x + B sin x)
- D. Ax sin x

<details><summary>Answer</summary>

**C.** y_h = C₁cos x + C₂sin x already contains cos x and sin x, so multiply the usual guess by x.

From: §3

</details>

---

### M3: Calculate

Find the general solution of y″ − 3y′ + 2y = 4e^(3x).

<details><summary>Answer</summary>

y_h = C₁eˣ + C₂e^(2x). Guess Ae^(3x) (no clash).

9A − 9A + 2A = 4 ⟹ A = 2.

$$y = C_1e^x + C_2e^{2x} + 2e^{3x}$$

From: §1

</details>

---

### M4: Sketch

Write the guess for y_p (don't solve) for y″ − y = x + e^(−x) + cos 2x. Underline any part you had to modify.

<details><summary>Answer</summary>

y_h = C₁eˣ + C₂e^(−x).

- x → Ax + B
- e^(−x) → clashes with y_h, so <u>Cxe^(−x)</u>
- cos 2x → D cos 2x + E sin 2x

y_p = Ax + B + <u>Cxe^(−x)</u> + D cos 2x + E sin 2x.

From: §1, §3

</details>

---

### M5: Explain

Why does the guess Ce^(2x) fail for y″ − y′ − 2y = 3e^(2x)?

<details><summary>Answer</summary>

e^(2x) solves the homogeneous equation (r = 2 is a root). So plugging in Ce^(2x) gives 0 on the left, never 3e^(2x).

Multiplying by x gives a new function that isn't a homogeneous solution, so it can work.

From: §3

</details>
