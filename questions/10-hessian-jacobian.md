# Topic 10: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Sheet 4 has short answers only. The full working here is mine (unofficial), checked in Python.

---

## Part A: Tutorial questions

### Q1 (Tutorial Sheet 4 Q1)

Find $f_{xx}$, $f_{yy}$, $f_{xy}$.

(a) x²y³  (b) (x + 1)³ ln y  (c) e³ʸ sin 2x  (d) (xy + 1)/(y + 2)

<details><summary>Answer</summary>

**(a)** $f_{xx} = 2y^3$, $f_{yy} = 6x^2y$, $f_{xy} = 6xy^2$

**(b)** $f_x = 3(x+1)^2\ln y$, $f_y = \frac{(x+1)^3}{y}$.

$f_{xx} = 6(x+1)\ln y$, $f_{yy} = -\frac{(x+1)^3}{y^2}$, $f_{xy} = \frac{3(x+1)^2}{y}$

**(c)** $f_x = 2e^{3y}\cos 2x$, $f_y = 3e^{3y}\sin 2x$.

$f_{xx} = -4e^{3y}\sin 2x$, $f_{yy} = 9e^{3y}\sin 2x$, $f_{xy} = 6e^{3y}\cos 2x$

**(d)** $f_x = \frac{y}{y+2}$, so $f_{xx} = 0$ and $f_{xy} = \frac{(y+2) - y}{(y+2)^2} = \frac{2}{(y+2)^2}$.

$f_y = \frac{x(y+2) - (xy+1)}{(y+2)^2} = \frac{2x-1}{(y+2)^2}$, so $f_{yy} = -\frac{2(2x-1)}{(y+2)^3}$.

From: §1

</details>

---

### Q2 (Tutorial Sheet 4 Q2, Q3)

Q2: Find the Hessian of x²y³ and show det H = 0 only if x = 0 or y = 0.

Q3: Find the Hessian of eˣ sin y. Can det H be 0?

<details><summary>Answer</summary>

**Q2:**

$$H = \begin{pmatrix} 2y^3 & 6xy^2 \\ 6xy^2 & 6x^2y \end{pmatrix}$$

det H = 12x²y⁴ − 36x²y⁴ = −24x²y⁴. This is 0 ⟺ x = 0 or y = 0.

**Q3:**

$$H = \begin{pmatrix} e^x\sin y & e^x\cos y \\ e^x\cos y & -e^x\sin y \end{pmatrix}$$

det H = −e²ˣ(sin² y + cos² y) = −e²ˣ < 0. **Never 0.**

From: §2

</details>

---

### Q4 (Tutorial Sheet 4 Q4)

f₁ = 2x₁ + 3x₂ + x₃, f₂ = 3x₁ + x₂ + 2x₃, f₃ = x₁ + 2x₂ + 3x₃. Find J and det J.

<details><summary>Answer</summary>

$$J = \begin{pmatrix} 2 & 3 & 1 \\ 3 & 1 & 2 \\ 1 & 2 & 3 \end{pmatrix}$$

det J = 2(3 − 4) − 3(9 − 2) + 1(6 − 1) = −2 − 21 + 5 = **−18**.

From: §3

</details>

---

### Q5 (Tutorial Sheet 4 Q5, Q6)

Q5: f₁ = x₁² + x₂², f₂ = 2x₁x₂. Find J and the relation when det J = 0.

Q6: f₁ = cos x₁ cos x₂, f₂ = sin x₁ sin x₂. Find J and show det J = 0 when tan² x₁ = tan² x₂.

<details><summary>Answer</summary>

**Q5:**

$$J = \begin{pmatrix} 2x_1 & 2x_2 \\ 2x_2 & 2x_1 \end{pmatrix}$$

det J = 4(x₁² − x₂²) = 0 ⟺ **x₁² = x₂²**, i.e. x₁ = ±x₂.

**Q6:**

$$J = \begin{pmatrix} -\sin x_1\cos x_2 & -\cos x_1\sin x_2 \\ \cos x_1\sin x_2 & \sin x_1\cos x_2 \end{pmatrix}$$

det J = −sin² x₁ cos² x₂ + cos² x₁ sin² x₂.

det J = 0 ⟺ sin² x₁ cos² x₂ = cos² x₁ sin² x₂. Divide both sides by cos² x₁ cos² x₂:

$$\tan^2 x_1 = \tan^2 x_2$$

From: §3

</details>

---

### E1 (Tutorial Sample exam Q3 b)

f₁ = x + 2y + 3z, f₂ = eʸ + eᶻ, f₃ = ln(xyz). (i) Jacobian matrix. (ii) Jacobian determinant at (1, 1, 1).

<details><summary>Answer</summary>

$$J = \begin{pmatrix} 1 & 2 & 3 \\ 0 & e^y & e^z \\ x^{-1} & y^{-1} & z^{-1} \end{pmatrix}$$

det J(1, 1, 1) = **−e**. (Working in notes §4.)

From: §4

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. The Hessian of f(x, y, z) is a 3 × 3 matrix.
2. The Hessian is always symmetric (for our functions).
3. Row 2 of a Jacobian matrix is the gradient of f₂.
4. If det J = 0, the functions are independent.
5. $f_{xy}$ means differentiate in y first, then x.

<details><summary>Answer</summary>

1. **True.** (§2)
2. **True.** Clairaut: $f_{xy} = f_{yx}$. (§1, §2)
3. **True.** (§3)
4. **False.** det J ≠ 0 means independent. det J = 0 means there's a relationship. (§3)
5. **False.** $f_{xy} = (f_x)_y$: x first, then y. (§1)

</details>

---

### M2: Multiple choice

f = x³ + 2xy² + y. What is $f_{xy}$?

- A. 4y
- B. 4x
- C. 6x
- D. 2y²

<details><summary>Answer</summary>

**A.** $f_x = 3x^2 + 2y^2$, then ∂/∂y gives 4y.

From: §1

</details>

---

### M3: Calculate

Find the Hessian of f(x, y, z) = x²y + yz² − 3xz and evaluate it at (1, 1, 1).

<details><summary>Answer</summary>

$f_x = 2xy - 3z$, $f_y = x^2 + z^2$, $f_z = 2yz - 3x$.

$$H = \begin{pmatrix} 2y & 2x & -3 \\ 2x & 0 & 2z \\ -3 & 2z & 2y \end{pmatrix} \to \begin{pmatrix} 2 & 2 & -3 \\ 2 & 0 & 2 \\ -3 & 2 & 2 \end{pmatrix}$$

From: §2

</details>

---

### M4: Sketch

Draw an empty 3 × 3 grid and label where each of $f_{xx}, f_{yy}, f_{zz}, f_{xy}, f_{xz}, f_{yz}$ goes in the Hessian. Shade the entries that are equal in pairs.

<details><summary>Answer</summary>

Diagonal (top-left to bottom-right): $f_{xx}$, $f_{yy}$, $f_{zz}$.

Off the diagonal: $f_{xy}$ at (1,2) and (2,1), $f_{xz}$ at (1,3) and (3,1), $f_{yz}$ at (2,3) and (3,2).

The three pairs are mirror images across the diagonal: shade each pair the same colour.

From: §2

</details>

---

### M5: Explain

Explain the difference between the Hessian and the Jacobian.

<details><summary>Answer</summary>

The Hessian belongs to **one** function f. It holds all the **second** partial derivatives of f. It's square and symmetric. You use it to classify critical points.

The Jacobian belongs to a **system** of functions f₁, …, fₘ. It holds all their **first** partial derivatives, one row per function. Its determinant tells you whether the functions are independent.

From: §2, §3

</details>
