# Topic 5: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Tutorial questions

### Q3 (Tutorial Sheet 2 Q3)

w = xy²e²ᶻ, with x = 3t² + 1, y = 6t, z = t³ − 1. Find w′(t) in terms of t.

<details><summary>Answer</summary>

$w_x = y^2e^{2z}$, $w_y = 2xye^{2z}$, $w_z = 2xy^2e^{2z}$; $x_t = 6t$, $y_t = 6$, $z_t = 3t^2$.

$$w'(t) = w_xx_t + w_yy_t + w_zz_t$$

$$= 216t^3e^{2(t^3-1)} + 72t(3t^2+1)e^{2(t^3-1)} + 216t^4(3t^2+1)e^{2(t^3-1)}$$

From: §2

</details>

---

### Q4 (Tutorial Sheet 2 Q4)

x = r³ − 3rs², y = 3r²s − s³. Express $w_r$, $w_s$ in terms of $w_x$, $w_y$, r, s. Hence show $w_r^2 + w_s^2 = 9(r^2+s^2)^2(w_x^2+w_y^2)$.

<details><summary>Answer</summary>

$x_r = 3r^2 - 3s^2$, $x_s = -6rs$, $y_r = 6rs$, $y_s = 3r^2 - 3s^2$.

$$w_r = 3(r^2-s^2)w_x + 6rs\,w_y$$

$$w_s = -6rs\,w_x + 3(r^2-s^2)w_y$$

Square both. The cross terms are $+36(r^2-s^2)rs\,w_xw_y$ and $-36(r^2-s^2)rs\,w_xw_y$: they cancel when you add.

$$w_r^2 + w_s^2 = 9\left((r^2-s^2)^2 + 4r^2s^2\right)(w_x^2+w_y^2) = 9(r^2+s^2)^2(w_x^2+w_y^2)$$

since $(r^2-s^2)^2 + 4r^2s^2 = (r^2+s^2)^2$.

From: §3

</details>

---

### Q5 (Tutorial Sheet 2 Q5)

x = eʳ cosh s, y = eʳ sinh s. Express $w_r$, $w_s$. Hence show $w_r^2 - w_s^2 = e^{2r}(w_x^2 - w_y^2) = (x^2-y^2)(w_x^2-w_y^2)$.

<details><summary>Answer</summary>

$x_r = e^r\cosh s$, $x_s = e^r\sinh s$, $y_r = e^r\sinh s$, $y_s = e^r\cosh s$.

$$w_r = e^r\cosh s\,w_x + e^r\sinh s\,w_y$$

$$w_s = e^r\sinh s\,w_x + e^r\cosh s\,w_y$$

Square and **subtract**. The cross terms are equal, so they cancel:

$$w_r^2 - w_s^2 = e^{2r}(\cosh^2 s - \sinh^2 s)(w_x^2 - w_y^2) = e^{2r}(w_x^2 - w_y^2)$$

using cosh² s − sinh² s = 1. Also x² − y² = e²ʳ(cosh² s − sinh² s) = e²ʳ.

From: §3

</details>

---

### Q6 (Tutorial Sheet 2 Q6)

x = r² − s², y = 2rs. Find $w_r$, $w_s$. Hence show

$$w_x = \frac{rw_r - sw_s}{2(r^2+s^2)}, \quad w_y = \frac{sw_r + rw_s}{2(r^2+s^2)}, \quad w_r^2 + w_s^2 = 4(r^2+s^2)(w_x^2+w_y^2)$$

<details><summary>Answer</summary>

$$w_r = 2rw_x + 2sw_y, \qquad w_s = -2sw_x + 2rw_y$$

r × first − s × second: $rw_r - sw_s = 2(r^2+s^2)w_x$. Divide.

s × first + r × second: $sw_r + rw_s = 2(r^2+s^2)w_y$. Divide.

Square and add the two chain-rule lines: the ±8rs cross terms cancel, giving $4(r^2+s^2)(w_x^2+w_y^2)$.

From: §3, §4

</details>

---

### E1 (Tutorial Sample exam Q2 b)

Use the chain rule to find w′(1) if w = sin(xyz), x = 1 + t², y = 1 − 2t, z = t³ − 2.

<details><summary>Answer</summary>

$$w'(t) = \cos(xyz)\left[yz(2t) + xz(-2) + xy(3t^2)\right]$$

At t = 1: x = 2, y = −1, z = −1, xyz = 2.

$$w'(1) = 2\cos 2 + 4\cos 2 - 6\cos 2 = 0$$

From: §5

</details>

---

### E2 (Tutorial Sample exam Q2 c)

x = r² + s², y = cos(rs). Find $w_x$ if r = 2, s = π/4, $w_r = 8$, $w_s = \pi$.

<details><summary>Answer</summary>

$$w_r = 2r\,w_x - s\sin(rs)\,w_y, \qquad w_s = 2s\,w_x - r\sin(rs)\,w_y$$

At the point: $8 = 4w_x - \frac{\pi}{4}w_y$ and $\pi = \frac{\pi}{2}w_x - 2w_y$.

Eliminating $w_y$ gives $\frac12(64-\pi^2)w_x = 64 - \pi^2$, so

$$w_x = 2$$

From: §6

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. If w = f(x, y) and x, y depend on t, then $\frac{dw}{dt}$ has two terms.
2. If w = f(x, y, z) and x, y, z depend on r and s, then $w_r$ has two terms.
3. The chain rule gives the same answer as substituting first and differentiating.
4. In $w_r = w_xx_r + w_yy_r$, you can always compute $w_x$ as a formula.
5. When squaring and adding $w_r$, $w_s$, the $w_xw_y$ terms often cancel.

<details><summary>Answer</summary>

1. **True.** One term per middle variable. (§1)
2. **False.** Three middle variables, so three terms. (§1)
3. **True.** It must. But use the chain rule when the question says so. (§1)
4. **False.** If w is a general function you leave $w_x$ as a letter. (§3)
5. **True.** That's the point of those "hence show" questions. (§3)

</details>

---

### M2: Multiple choice

w = x²y, x = cos t, y = sin t. What is w′(0)?

- A. 0
- B. 1
- C. −1
- D. 2

<details><summary>Answer</summary>

**B.** $w' = 2xy\,x_t + x^2\,y_t = 2xy(-\sin t) + x^2\cos t$.

At t = 0: x = 1, y = 0. So w′(0) = 0 + 1·1 = 1.

From: §2

</details>

---

### M3: Calculate

w = x² + y², x = rs, y = r + s. Use the chain rule to find $w_r$ and $w_s$ at r = 1, s = 2.

<details><summary>Answer</summary>

$w_x = 2x$, $w_y = 2y$. $x_r = s$, $x_s = r$, $y_r = y_s = 1$.

At r = 1, s = 2: x = 2, y = 3.

$w_r = 2x\cdot s + 2y\cdot1 = 2(2)(2) + 2(3) = 14$

$w_s = 2x\cdot r + 2y\cdot1 = 2(2)(1) + 6 = 10$

From: §3

</details>

---

### M4: Sketch

Draw the tree diagram for w = f(x, y, z) with x = g(t), y = h(t), z = k(t), and write the chain rule it gives.

<details><summary>Answer</summary>

w at the top, three branches down to x, y, z, then each of x, y, z has one branch down to t.

Three routes, so

$$\frac{dw}{dt} = w_x\frac{dx}{dt} + w_y\frac{dy}{dt} + w_z\frac{dz}{dt}$$

From: §1

</details>

---

### M5: Explain

In sample exam Q2(b), why should you work out x, y, z at t = 1 **before** substituting into w′(t)?

<details><summary>Answer</summary>

w′(t) contains $w_x$, $w_y$, $w_z$, which are in terms of x, y, z.

Working out x = 2, y = −1, z = −1 first means you substitute plain numbers, and xyz = 2 appears in every cos term. Much less algebra and fewer mistakes.

From: §5

</details>
