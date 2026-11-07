# Topic 3: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Tutorial questions

### Q3 (Tutorial Sheet 1 Q3)

By considering different paths, show these have no limit as (x, y) → (0, 0):

(a) $-\frac{x}{\sqrt{x^2+y^2}}$  (b) $\frac{x^4}{x^4+y^2}$  (c) $\frac{x-y}{x+y}$  (d) $\frac{xy}{|xy|}$

<details><summary>Answer</summary>

**(a)** Positive x-axis (y = 0, x > 0): $-\frac{x}{\sqrt{x^2}} = -\frac{x}{|x|} = -1 \to -1$.

y-axis (x = 0): $\frac{0}{|y|} = 0 \to 0$. Different, so no limit.

<br>

**(b)** x-axis (y = 0): $\frac{x^4}{x^4} = 1 \to 1$.

y-axis (x = 0): $\frac{0}{y^2} = 0 \to 0$. No limit.

<br>

**(c)** Line y = x: $\frac{0}{2x} = 0 \to 0$.

x-axis (y = 0): $\frac{x}{x} = 1 \to 1$. No limit.

<br>

**(d)** The axes don't work here (xy = 0 is outside the domain). Use lines.

y = 2x: $\frac{2x^2}{|2x^2|} = 1 \to 1$.

y = −2x: $\frac{-2x^2}{|-2x^2|} = -1 \to -1$. No limit.

From: §2

</details>

---

### Q4 (Tutorial Sheet 1 Q4)

Where in the plane are these continuous?

(a) sin(x + y)  (b) ln(x² + y²)  (c) $\frac{x+y}{x-y}$  (d) $\frac{x^2+y^2}{x^2-3x+2}$

<details><summary>Answer</summary>

**(a)** ℝ². x + y is a polynomial, and sin is continuous on all of ℝ.

**(b)** ln needs x² + y² > 0: $\{(x,y) \in \mathbb{R}^2 \mid (x,y) \neq (0,0)\}$.

**(c)** Rational, bottom ≠ 0: $\{(x,y) \in \mathbb{R}^2 \mid x \neq y\}$.

**(d)** x² − 3x + 2 = (x − 1)(x − 2), so $\{(x,y) \in \mathbb{R}^2 \mid x \neq 1 \text{ and } x \neq 2\}$.

From: §3

</details>

---

### Q5 (Tutorial Sheet 1 Q5)

Where in space are these continuous?

(a) x² + y² − 2z²  (b) $\sqrt{x^2+y^2-1}$  (c) $\frac{1}{x^2+z^2-1}$  (d) $\frac{1}{|y|+|z|}$

<details><summary>Answer</summary>

**(a)** All of ℝ³ (polynomial).

**(b)** $\{(x,y,z) \in \mathbb{R}^3 \mid x^2+y^2 \geq 1\}$: everything except the inside of the infinite cylinder x² + y² = 1.

**(c)** $\{(x,y,z) \in \mathbb{R}^3 \mid x^2+z^2 \neq 1\}$: everything except the cylinder x² + z² = 1 (its axis is the y-axis).

**(d)** |y| + |z| = 0 only when y = 0 and z = 0: $\{(x,y,z) \mid (y,z) \neq (0,0)\}$, i.e. ℝ³ without the x-axis.

From: §3

</details>

---

### Q6 (Tutorial Sheet 1 Q6)

Find the limits.

(a) $\lim_{(0,0)} \frac{3x^2-y^2+5}{x^2+y^2+2}$  (b) $\lim_{(3,4)} \sqrt{x^2+y^2-1}$  (c) $\lim_{(1,0)} \frac{x\sin y}{x^2+1}$

(d) $\lim_{(1,1)} \frac{x^2-2xy+y^2}{x-y}$  (e) $\lim_{(1,1)} \frac{xy-y-2x+2}{x-1}$

(f) $\lim_{(2,-4)} \frac{y+4}{x^2y-xy+4x^2-4x}$  (g) $\lim_{(0,0)} \frac{x-y+2\sqrt{x}-2\sqrt{y}}{\sqrt{x}-\sqrt{y}}$

<details><summary>Answer</summary>

**(a)** Continuous at (0,0) (bottom = 2). Substitute: **5/2**.

**(b)** Continuous (inside = 24 > 0): √24 = **2√6**.

**(c)** Continuous: 1·sin 0 / 2 = **0**.

**(d)** 0/0. $\frac{(x-y)^2}{x-y} = x-y \to$ **0**.

**(e)** 0/0. Top = y(x − 1) − 2(x − 1) = (y − 2)(x − 1). So y − 2 → **−1**.

**(f)** 0/0. Bottom = xy(x − 1) + 4x(x − 1) = x(x − 1)(y + 4).

So f = 1/(x(x − 1)) → 1/(2·1) = **1/2**.

**(g)** 0/0. Top = (√x − √y)(√x + √y) + 2(√x − √y) = (√x − √y)(√x + √y + 2).

So f = √x + √y + 2 → **2**.

From: §4

</details>

---

### Q7 (Tutorial Sheet 1 Q7)

Find the continuous extension g of f at (a, b).

(a) $f = \frac{x^3-2x^2-xy^2+2y^2}{x^3-2x^2+xy^2-2y^2+x-2}$ at (2, 1)

(b) $f = \frac{x^3-x^2-xy^2+y^2}{x^3-x^2+xy^2-y^2+2x-2}$ at (1, 1)

<details><summary>Answer</summary>

**(a)** f(2, 1) = 0/0.

Top = x²(x − 2) − y²(x − 2) = (x − 2)(x² − y²).

Bottom = x²(x − 2) + y²(x − 2) + (x − 2) = (x − 2)(x² + y² + 1).

$$\lim = \lim \frac{x^2-y^2}{x^2+y^2+1} = \frac{4-1}{4+1+1} = \frac{1}{2}$$

g(x, y) := f(x, y) when (x, y) ≠ (2, 1), and **g(2, 1) := 1/2**.

<br>

**(b)** f(1, 1) = 0/0.

Top = (x − 1)(x² − y²). Bottom = (x − 1)(x² + y² + 2).

$$\lim = \frac{1-1}{1+1+2} = 0$$

g(x, y) := f(x, y) when (x, y) ≠ (1, 1), and **g(1, 1) := 0**.

From: §5

</details>

---

### E1 (Tutorial Sample exam Q1 c)

$$\lim_{(x,y)\to(1,0)} \frac{\ln(x)}{\sqrt{4-x^2-y^2}}$$

<details><summary>Answer</summary>

(1, 0) is in dom(f) and f is continuous on its domain. Substitute:

$$\frac{\ln 1}{\sqrt{3}} = 0$$

From: §4, §6

</details>

---

## Part B: Exam-style questions

---

### M1: True or false

1. If f → 0 along the x-axis and along the y-axis, then the limit at (0,0) is 0.
2. Every polynomial in x and y is continuous on ℝ².
3. If f(a, b) = 0/0, the limit at (a, b) does not exist.
4. $\sqrt{x^2} = x$ for every real x.
5. A rational function is continuous wherever its denominator is non-zero.

<details><summary>Answer</summary>

1. **False.** Two paths agreeing proves nothing. Another path may disagree, as in $\frac{2xy}{x^2+y^2}$. (§2)
2. **True.** (§3)
3. **False.** 0/0 just means "simplify first". The limit may well exist. (§4)
4. **False.** √(x²) = |x|. (§2)
5. **True.** (§3)

</details>

---

### M2: Multiple choice

$$\lim_{(x,y)\to(0,0)} \frac{x^2 y}{x^4 + y^2}$$

Along y = 0 it's 0. Along y = x² it's:

- A. 0
- B. 1/2
- C. 1
- D. undefined

So does the limit exist?

<details><summary>Answer</summary>

**B.** Put y = x²: $\frac{x^4}{x^4+x^4} = \frac{1}{2}$.

0 ≠ 1/2, so the limit does **not** exist.

Lesson: sometimes you need a curved path, not a straight line.

From: §2

</details>

---

### M3: Calculate

$$\lim_{(x,y)\to(2,2)} \frac{x^2-y^2}{x-y}$$

<details><summary>Answer</summary>

0/0. Factor: $\frac{(x-y)(x+y)}{x-y} = x + y \to 4$.

From: §4

</details>

---

### M4: Sketch

Sketch the set where $f(x,y) = \frac{1}{x^2+y^2-4}$ is **not** continuous.

<details><summary>Answer</summary>

f fails where x² + y² = 4.

Draw the circle of radius 2 centred at the origin. f is continuous everywhere else.

From: §3

</details>

---

### M5: Explain

Explain why, in Q6(d), we are allowed to cancel (x − y) from top and bottom.

<details><summary>Answer</summary>

The limit only looks at points (x, y) in the domain of f.

In the domain x − y ≠ 0, so dividing by it is fine.

The point (1, 1) itself is never used, only points near it.

From: §4

</details>
