# Topic 4: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Tutorial questions

### Q1a (Tutorial Sheet 2 Q1 a–c)

Find $f_x$ and $f_y$.

(a) $x^2 - xy + 2y^2 - 3x + y$  (b) $x\cos 3y + \sin xy$  (c) $\frac{x+y}{x-y}$

<details><summary>Answer</summary>

**(a)** $f_x = 2x - y - 3$, $\quad f_y = -x + 4y + 1$

**(b)** $f_x = \cos 3y + y\cos xy$, $\quad f_y = -3x\sin 3y + x\cos xy$

**(c)** Quotient rule. For $f_x$: u = x + y, v = x − y, $u_x = 1$, $v_x = 1$.

$$f_x = \frac{(x-y) - (x+y)}{(x-y)^2} = -\frac{2y}{(x-y)^2}$$

For $f_y$: $u_y = 1$, $v_y = -1$.

$$f_y = \frac{(x-y) + (x+y)}{(x-y)^2} = \frac{2x}{(x-y)^2}$$

From: §3

</details>

---

### Q1d (Tutorial Sheet 2 Q1 d–f)

Find $f_x$ and $f_y$.

(d) $e^{2x-3y}$  (e) $x\ln(x^2+y^3)$  (f) $\sqrt{1+x^2-2y^2}$

<details><summary>Answer</summary>

**(d)** $f_x = 2e^{2x-3y}$, $\quad f_y = -3e^{2x-3y}$

**(e)** Product rule for $f_x$:

$$f_x = \ln(x^2+y^3) + x\cdot\frac{2x}{x^2+y^3} = \ln(x^2+y^3) + \frac{2x^2}{x^2+y^3}$$

$$f_y = x\cdot\frac{3y^2}{x^2+y^3} = \frac{3xy^2}{x^2+y^3}$$

**(f)** $f_x = \frac{2x}{2\sqrt{1+x^2-2y^2}} = \frac{x}{\sqrt{1+x^2-2y^2}}$, $\quad f_y = -\frac{2y}{\sqrt{1+x^2-2y^2}}$

From: §3

</details>

---

### Q2 (Tutorial Sheet 2 Q2)

Find $f_x$, $f_y$, $f_z$.

(a) $1 + xy^2 - 2z^2$  (b) $(x+1)(y+2)^2(z+3)^3$  (c) $\cos(xy) + \sin(2yz)$

<details><summary>Answer</summary>

**(a)** $f_x = y^2$, $f_y = 2xy$, $f_z = -4z$

**(b)** $f_x = (y+2)^2(z+3)^3$, $f_y = 2(x+1)(y+2)(z+3)^3$, $f_z = 3(x+1)(y+2)^2(z+3)^2$

**(c)** $f_x = -y\sin(xy)$, $f_y = -x\sin(xy) + 2z\cos(2yz)$, $f_z = 2y\cos(2yz)$

From: §4

</details>

---

### E1 (Tutorial Sample exam Q2 a)

Find $f_x$ and $f_y$ for $f(x,y) = \sqrt{\sin(x^2y^3)}$.

<details><summary>Answer</summary>

$$f_x = \frac{xy^3\cos(x^2y^3)}{\sqrt{\sin(x^2y^3)}}, \qquad f_y = \frac{3x^2y^2\cos(x^2y^3)}{2\sqrt{\sin(x^2y^3)}}$$

Full working in the notes.

From: §5

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. When finding $f_x$, you treat y as a constant.
2. $\frac{\partial}{\partial x}(y^3) = 3y^2$.
3. $f_x(a, b)$ is the slope of the surface in the x-direction at (a, b).
4. A function of 4 variables has 4 first-order partial derivatives.
5. $\frac{\partial}{\partial y}\left(e^{xy}\right) = e^{xy}$.

<details><summary>Answer</summary>

1. **True.** (§1)
2. **False.** y³ has no x in it, so it's a constant: the derivative is 0. (§3)
3. **True.** (§2)
4. **True.** (§4)
5. **False.** Chain rule: $x e^{xy}$. (§3)

</details>

---

### M2: Multiple choice

$f(x, y) = x^2 e^{3y}$. What is $f_y(1, 0)$?

- A. 0
- B. 1
- C. 2
- D. 3

<details><summary>Answer</summary>

**D.** $f_y = 3x^2e^{3y}$, so $f_y(1,0) = 3\cdot1\cdot1 = 3$.

From: §1, §3

</details>

---

### M3: Calculate

Find $f_x$ and $f_y$ for $f(x,y) = \ln(x^2 + xy + y^2)$, and evaluate both at (1, 1).

<details><summary>Answer</summary>

$$f_x = \frac{2x+y}{x^2+xy+y^2}, \qquad f_y = \frac{x+2y}{x^2+xy+y^2}$$

At (1, 1): both equal 3/3 = **1**.

From: §3

</details>

---

### M4: Sketch

f(x, y) = 4 − x² − y². Sketch the curve you get by slicing the surface with the plane y = 0, and mark the tangent line at x = 1. What is its slope?

<details><summary>Answer</summary>

With y = 0: z = 4 − x², a downward parabola with top at (0, 4).

The tangent at x = 1 touches the parabola at (1, 3).

Slope = $f_x(1, 0) = -2x = -2$. It goes down to the right.

From: §2

</details>

---

### M5: Explain

Explain in words why $\frac{\partial}{\partial x}(x\cos 3y) = \cos 3y$.

<details><summary>Answer</summary>

When differentiating in x, y is frozen, so cos 3y is just a number, like 5.

The derivative of 5x is 5, so the derivative of x·cos 3y is cos 3y.

From: §3

</details>
