# Topic 18: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Sheet 5 has no printed answers. The full working here is mine (unofficial), checked in Python (sympy `dsolve`).

---

## Part A: Tutorial questions

### Q6a (Tutorial Sheet 5 Q6 a)

Use variation of parameters: y″ − 9y′ + 20y = 3.

<details><summary>Answer</summary>

y₁ = e^(4x), y₂ = e^(5x), W = e^(9x).

u₁′ = −3e^(−4x) ⟹ u₁ = (3/4)e^(−4x). u₂′ = 3e^(−5x) ⟹ u₂ = −(3/5)e^(−5x).

y_p = 3/4 − 3/5 = 3/20.

$$y = C_1e^{4x} + C_2e^{5x} + \frac{3}{20}$$

From: §3

</details>

---

### Q6b (Tutorial Sheet 5 Q6 b)

Use variation of parameters: y″ − 5y′ + 6y = 5x + 1.

<details><summary>Answer</summary>

r² − 5r + 6 = (r − 2)(r − 3): y₁ = e^(2x), y₂ = e^(3x). W = e^(2x)·3e^(3x) − 2e^(2x)·e^(3x) = e^(5x).

u₁′ = −(5x + 1)e^(−2x), u₂′ = (5x + 1)e^(−3x).

By parts:

$$u_1 = \frac{5x+1}{2}e^{-2x} + \frac54e^{-2x}, \qquad u_2 = -\frac{5x+1}{3}e^{-3x} - \frac59e^{-3x}$$

$$y_p = u_1e^{2x} + u_2e^{3x} = \frac{5x+1}{2} + \frac54 - \frac{5x+1}{3} - \frac59 = \frac{5x}{6} + \frac{31}{36}$$

$$y = C_1e^{2x} + C_2e^{3x} + \frac{5x}{6} + \frac{31}{36}$$

From: §1

</details>

---

### Q6c (Tutorial Sheet 5 Q6 c)

Use variation of parameters: 2y″ + y′ − y = 4x.

<details><summary>Answer</summary>

2r² + r − 1 = (2r − 1)(r + 1): y₁ = e^(x/2), y₂ = e^(−x).

**Divide by the leading 2**: g = 4x/2 = 2x.

W = e^(x/2)(−e^(−x)) − ½e^(x/2)e^(−x) = −(3/2)e^(−x/2).

$$u_1' = -\frac{y_2g}{W} = \frac{4x}{3}e^{-x/2}, \qquad u_2' = \frac{y_1g}{W} = -\frac{4x}{3}e^x$$

$$u_1 = -\frac83(x + 2)e^{-x/2}, \qquad u_2 = -\frac43(x - 1)e^x$$

$$y_p = -\frac83(x+2) - \frac43(x-1) = -4x - 4$$

$$y = C_1e^{x/2} + C_2e^{-x} - 4x - 4$$

Check: y_p″ = 0, y_p′ = −4: 0 − 4 + 4x + 4 = 4x ✓.

From: §1

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. In variation of parameters, y_p = u₁y₁ + u₂y₂ with u₁, u₂ functions.
2. We require u₁′y₁ + u₂′y₂ = 0.
3. The second equation is u₁′y₁′ + u₂′y₂′ = f(x), whatever the coefficient of y″.
4. You must include integration constants when integrating u₁′, u₂′.
5. Variation of parameters works even when f(x) = 1/x.

<details><summary>Answer</summary>

1. **True.** (§1)
2. **True.** It's the extra condition we're allowed to choose. (§1)
3. **False.** It's f(x)/a₂. (§1)
4. **False.** They'd just add multiples of y₁, y₂, which are already in y_h. (§1)
5. **True.** That's its advantage. (§1)

</details>

---

### M2: Multiple choice

For y″ − y = f(x) with y₁ = eˣ, y₂ = e^(−x), the Wronskian W = y₁y₂′ − y₁′y₂ is:

- A. 2
- B. −2
- C. 0
- D. e^(2x)

<details><summary>Answer</summary>

**B.** eˣ(−e^(−x)) − eˣe^(−x) = −1 − 1 = −2.

From: §1

</details>

---

### M3: Calculate

Use variation of parameters for y″ − y = eˣ.

<details><summary>Answer</summary>

y₁ = eˣ, y₂ = e^(−x), W = −2, g = eˣ.

u₁′ = −e^(−x)eˣ/(−2) = 1/2 ⟹ u₁ = x/2.

u₂′ = eˣeˣ/(−2) = −e^(2x)/2 ⟹ u₂ = −e^(2x)/4.

y_p = (x/2)eˣ − (1/4)eˣ. The −eˣ/4 part is already in y_h, so drop it:

$$y = C_1e^x + C_2e^{-x} + \frac{x}{2}e^x$$

From: §1

</details>

---

### M4: Sketch

Write the variation-of-parameters system as a 2 × 2 matrix equation for (u₁′, u₂′).

<details><summary>Answer</summary>

$$\begin{pmatrix} y_1 & y_2 \\ y_1' & y_2' \end{pmatrix}\begin{pmatrix} u_1' \\ u_2' \end{pmatrix} = \begin{pmatrix} 0 \\ f/a_2 \end{pmatrix}$$

The determinant of the matrix is the Wronskian W.

From: §1

</details>

---

### M5: Explain

Why do the u₁y₁″ + u₂y₂″ terms disappear when you substitute y_p into the ODE?

<details><summary>Answer</summary>

Collecting terms gives u₁(a₂y₁″ + a₁y₁′ + a₀y₁) + u₂(a₂y₂″ + a₁y₂′ + a₀y₂).

y₁ and y₂ solve the homogeneous equation, so both brackets are 0.

Only the a₂(u₁′y₁′ + u₂′y₂′) term survives, and it must equal f.

From: §1

</details>
