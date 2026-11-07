# Mock Exam 1

**Covers:** everything (Topics 1–19). Same layout as the sample exam: 6 questions, equal marks. Every part is built on a tutorial or sample-exam question (shown in brackets), with new numbers or a twist.

**How to use it:**
- Do it on paper, closed book, **no formula sheet** (the real exam has none).
- 2 hours.
- Leave answers in exact form (√2, e, π), simplified.
- Mark yourself with the answers at the bottom. Each answer says which topic and § to go back to.

---

## Questions

### Q1. Domains and limits (Exam Q1, Sheet 1 Q1, Q3, Q6) — 20 marks

Consider

$$f(x,y) = \frac{\sqrt{x^2+y^2-1}}{\ln(4 - x^2 - y^2)}$$

a. Determine the domain of f. Give your answer in set notation. (6)

b. Sketch the domain. (4)

c. Show that $\lim_{(x,y)\to(0,0)} \frac{x^2-2y^2}{x^2+y^2}$ does not exist. (5)

d. Find $\lim_{(x,y)\to(2,1)} \frac{x^2-4y^2}{x-2y}$. (5)

---

### Q2. Partial derivatives and chain rules (Exam Q2, Sheet 2 Q1–Q6) — 20 marks

a. Find $f_x$ and $f_y$ for $f(x,y) = e^x\cos(xy^2)$. (6)

b. Use the chain rule to find w′(1) if w = ln(x² + y² + z²) and x = cos t, y = sin t, z = t. (7)

c. w is a function of x and y, where x = rs and y = r² − s². At r = 1, s = 1 you are told $w_r = 3$ and $w_s = 1$. Find $w_x$ and $w_y$ there. (7)

---

### Q3. Implicit differentiation, Jacobian, errors (Exam Q3, Sheet 2 Q7–Q10, Sheet 4 Q4) — 20 marks

a. The equation x² + yz + e^(x+z) = 3 defines z as a function of x and y. Find $z_x$ and $z_y$ at (−1, 1, 1). (7)

b. Let f₁ = x²y, f₂ = y + z², f₃ = e^(xz).
   (i) Find the Jacobian matrix. (ii) Find the Jacobian determinant at (1, 1, 0). (7)

c. The period of a pendulum is $T = 2\pi\sqrt{L/g}$. Find the approximate percentage change in T if L increases by 2% and g decreases by 1%. (6)

---

### Q4. Gradient and directional derivatives (Exam Q4, Sheet 3 Q1–Q7) — 20 marks

Let f(x, y, z) = xy² + yz³, P = (1, −1, 1), Q = (3, 1, 0).

a. Find ∇f at P. (4)

b. Find a unit vector u pointing from P towards Q. (3)

c. Find the rate of change of f at P in the direction of u. (4)

d. In which direction does f increase fastest at P, and what is that rate? (5)

e. Is there a direction in which the rate of change of f at P is 4? Explain. (4)

---

### Q5. Tangent plane and a 3-variable critical point (Exam Q5, Sheet 3 Q10, Sheet 4 Q9–Q11) — 20 marks

a. Find the tangent plane to the ellipsoid x² + 2y² + 3z² = 6 at (1, 1, 1). (6)

b. Let f(x, y, z) = x² + 2y² − z² + 2xy + 4z − 2x.
   (i) Find the unique critical point P. (5)
   (ii) Find the leading principal minors of the Hessian. (5)
   (iii) Is P a local max, local min or saddle point? (4)

---

### Q6. Lagrange and an ODE (Exam Q6, Sheet 4 Q17, Sheet 5 Q5) — 20 marks

a. Find the max and min of f(x, y, z) = xy²z + 2 subject to z = 2 and x² + y² + z² = 7. (10)

b. Find the general solution of y″ − y′ − 6y = 5e^(3x) + 6. (10)

---

## Answers

<details><summary>Q1 answers</summary>

**a.** Three conditions:
- √ needs x² + y² ≥ 1.
- ln needs 4 − x² − y² > 0, i.e. x² + y² < 4.
- ln is downstairs, so ln(4 − x² − y²) ≠ 0, i.e. 4 − x² − y² ≠ 1, i.e. x² + y² ≠ 3.

$$\text{dom}(f) = \{(x,y) \in \mathbb{R}^2 \mid 1 \leq x^2+y^2 < 4,\ x^2+y^2 \neq 3\}$$

**b.** A ring (annulus) between radius 1 and radius 2. Inner circle r = 1 **solid** (included). Outer circle r = 2 **dashed** (excluded). The circle r = √3 also **dashed** (removed). Shade the ring.

**c.** x-axis (y = 0): x²/x² = 1 → 1. y-axis (x = 0): −2y²/y² = −2 → −2. Different, so no limit.

**d.** 0/0. (x − 2y)(x + 2y)/(x − 2y) = x + 2y → 2 + 2 = **4**.

→ Topic 1 §3, §4; Topic 3 §2, §4

</details>

<details><summary>Q2 answers</summary>

**a.** Product rule and chain rule.

$$f_x = e^x\cos(xy^2) - y^2e^x\sin(xy^2), \qquad f_y = -2xye^x\sin(xy^2)$$

**b.** w_x = 2x/S, w_y = 2y/S, w_z = 2z/S with S = x² + y² + z². x_t = −sin t, y_t = cos t, z_t = 1.

$$w'(t) = \frac{-2\cos t\sin t + 2\sin t\cos t + 2t}{\cos^2 t + \sin^2 t + t^2} = \frac{2t}{1+t^2}$$

**w′(1) = 1.**

**c.** x_r = s, y_r = 2r, x_s = r, y_s = −2s. At (1, 1):

w_r = w_x + 2w_y = 3, w_s = w_x − 2w_y = 1.

Add: 2w_x = 4 ⟹ **w_x = 2**. Subtract: 4w_y = 2 ⟹ **w_y = 1/2**.

→ Topic 4 §3; Topic 5 §2, §4

</details>

<details><summary>Q3 answers</summary>

**a.** Check: 1 + 1 + e⁰ = 3 ✓. F = x² + yz + e^(x+z).

F_x = 2x + e^(x+z) = −1, F_y = z = 1, F_z = y + e^(x+z) = 2.

$$z_x = -\frac{F_x}{F_z} = \frac12, \qquad z_y = -\frac{F_y}{F_z} = -\frac12$$

**b.** (i)

$$J = \begin{pmatrix} 2xy & x^2 & 0 \\ 0 & 1 & 2z \\ ze^{xz} & 0 & xe^{xz} \end{pmatrix}$$

(ii) At (1, 1, 0): rows (2, 1, 0), (0, 1, 0), (0, 0, 1). Expand down column 1: 2·(1·1 − 0) = **2**.

**c.** T = 2πL^(1/2)g^(−1/2). % change ≈ ½(2) − ½(−1) = **1.5% increase**.

→ Topic 6 §1; Topic 10 §3; Topic 7 §3

</details>

<details><summary>Q4 answers</summary>

**a.** ∇f = ⟨y², 2xy + z³, 3yz²⟩ → **⟨1, −1, −3⟩**.

**b.** v = Q − P = ⟨2, 2, −1⟩, ‖v‖ = 3, **u = ⟨2/3, 2/3, −1/3⟩**.

**c.** ∇f · u = 2/3 − 2/3 + 1 = **1**.

**d.** Direction of ⟨1, −1, −3⟩ (unit: (1/√11)⟨1, −1, −3⟩). Rate **√11**.

**e.** No. The largest possible rate is √11 ≈ 3.32 < 4.

→ Topic 8 §3, §4

</details>

<details><summary>Q5 answers</summary>

**a.** ∇F = ⟨2x, 4y, 6z⟩ → ⟨2, 4, 6⟩.

2(x − 1) + 4(y − 1) + 6(z − 1) = 0 ⟹ **x + 2y + 3z = 6**.

**b.** (i) ∇f = ⟨2x + 2y − 2, 2x + 4y, −2z + 4⟩ = 0 ⟹ z = 2, and 2x + 2y = 2, 2x + 4y = 0 ⟹ y = −1, x = 2. **P = (2, −1, 2).**

(ii)

$$H = \begin{pmatrix} 2 & 2 & 0 \\ 2 & 4 & 0 \\ 0 & 0 & -2 \end{pmatrix}, \quad |H_1| = 2,\ |H_2| = 4,\ |H_3| = -8$$

(iii) Pattern + + −: neither + + + nor − + −, all non-zero: indefinite. **Saddle point.**

(Quick check: diagonal has 2 > 0 and −2 < 0.)

→ Topic 9 §4; Topic 13 §2, §3

</details>

<details><summary>Q6 answers</summary>

**a.** With z = 2 the second constraint is x² + y² = 3. Equations (μ for the sphere):

y²z = 2μx ⟹ 2y² = 2μx (1); 2xyz = 2μy ⟹ 4xy = 2μy (2).

(2): y(4x − 2μ) = 0 ⟹ y = 0 or μ = 2x.

- y = 0: x = ±√3, f = 2.
- μ = 2x: (1) gives y² = 2x². Then 3x² = 3, x = ±1, y = ±√2. f = 2·x·2 + 2 = 4x + 2.

**Max 6** at (1, ±√2, 2). **Min −2** at (−1, ±√2, 2). (The constraint set is a circle: compact.)

**b.** r² − r − 6 = (r − 3)(r + 2): y_h = C₁e^(3x) + C₂e^(−2x).

e^(3x) clashes: guess Axe^(3x) + B. Substituting: 5Ae^(3x) − 6B = 5e^(3x) + 6 ⟹ A = 1, B = −1.

$$y = C_1e^{3x} + C_2e^{-2x} + xe^{3x} - 1$$

→ Topic 14 §4; Topic 17 §3

</details>
