# Topic 6: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Tutorial questions

### Q7 (Tutorial Sheet 2 Q7)

z² − x² − 2y² + xz = 3 defines z as a function of x and y. Find $z_x$ and $z_y$ at (−1, 1, 3). Find the points where $z_x = z_y = 0$.

<details><summary>Answer</summary>

∂/∂x: $2zz_x - 2x + z + xz_x = 0$, so $z_x = \frac{2x - z}{x + 2z}$.

∂/∂y: $2zz_y - 4y + xz_y = 0$, so $z_y = \frac{4y}{x + 2z}$.

At (−1, 1, 3): x + 2z = 5.

$$z_x = \frac{-2-3}{5} = -1, \qquad z_y = \frac{4}{5}$$

**Both zero:** 2x − z = 0 and 4y = 0, so z = 2x, y = 0.

Into the equation: 4x² − x² + 2x² = 3, so 5x² = 3, x = ±√0.6.

Points: $(\sqrt{0.6}, 0, 2\sqrt{0.6})$ and $(-\sqrt{0.6}, 0, -2\sqrt{0.6})$.

From: §1, §4

</details>

---

### Q8 (Tutorial Sheet 2 Q8)

z³ − xy + yz + y³ − 2 = 0. Find $z_x$, $z_y$ in terms of x, y, z, their values at (1, 1, 1), and the point where $z_x = z_y = 0$.

<details><summary>Answer</summary>

∂/∂x: $3z^2z_x - y + yz_x = 0$, so $z_x = \frac{y}{3z^2 + y}$.

∂/∂y: $3z^2z_y - x + z + yz_y + 3y^2 = 0$, so $z_y = \frac{x - z - 3y^2}{3z^2 + y}$.

At (1, 1, 1): $z_x = \frac14$, $z_y = \frac{1-1-3}{4} = -\frac34$.

**Both zero:** y = 0, then x − z = 0 so x = z.

Into the equation with y = 0: z³ = 2, so z = 2^(1/3).

Point: $(2^{1/3}, 0, 2^{1/3})$.

From: §1, §4

</details>

---

### E1 (Tutorial Sample exam Q3 a)

xyz + e^(x+y+z) = 3 defines z implicitly. Find $z_x$ and $z_y$ at (2, −1, −1).

<details><summary>Answer</summary>

$$z_x = -\frac{yz + e^{x+y+z}}{xy + e^{x+y+z}} \implies z_x(2,-1,-1) = -\frac{1+1}{-2+1} = 2$$

By symmetry in x and y:

$$z_y = -\frac{xz + e^{x+y+z}}{xy + e^{x+y+z}} \implies z_y(2,-1,-1) = -\frac{-2+1}{-2+1} = -1$$

From: §5

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. When applying ∂/∂x to an implicit equation, the derivative of z² is 2z.
2. $z_x = -F_x / F_z$.
3. For a curve F(x, y) = c, $\frac{dy}{dx} = \frac{F_x}{F_y}$.
4. In ∂/∂x, the term y³ has derivative 0.
5. You need to solve the equation for z before you can find $z_x$.

<details><summary>Answer</summary>

1. **False.** It's 2z·z_x, because z depends on x. (§1)
2. **True.** (§1)
3. **False.** There's a minus sign: −F_x / F_y. (§2)
4. **True.** y is constant in ∂/∂x. (§1)
5. **False.** That's the whole point of implicit differentiation. (§1)

</details>

---

### M2: Multiple choice

x² + y² + z² = 9. What is $z_x$?

- A. x/z
- B. −x/z
- C. −z/x
- D. −2x

<details><summary>Answer</summary>

**B.** 2x + 2z·z_x = 0, so z_x = −x/z.

From: §1

</details>

---

### M3: Calculate

x²z + yz³ = 2. Find $z_x$ and $z_y$ at (1, 1, 1).

<details><summary>Answer</summary>

F = x²z + yz³ − 2. F_x = 2xz, F_y = z³, F_z = x² + 3yz².

At (1, 1, 1): F_x = 2, F_y = 1, F_z = 4.

$$z_x = -\frac{2}{4} = -\frac12, \qquad z_y = -\frac14$$

From: §1

</details>

---

### M4: Sketch

The curve x² + y² = 25. Use implicit differentiation to find dy/dx at (3, 4), and sketch the circle with that tangent line.

<details><summary>Answer</summary>

F = x² + y². dy/dx = −F_x/F_y = −2x/2y = −x/y = −3/4 at (3, 4).

Draw a circle of radius 5 centred at the origin. At (3, 4) (upper right) draw a line sloping down with slope −3/4, just touching the circle.

From: §2

</details>

---

### M5: Explain

Why does the term xz give z + x·z_x when you apply ∂/∂x?

<details><summary>Answer</summary>

xz is a product of two things that both depend on x (z does, secretly).

Product rule: (∂x/∂x)·z + x·(∂z/∂x) = 1·z + x·z_x.

From: §1

</details>
