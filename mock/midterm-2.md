# Mock Exam 2

**Covers:** everything (Topics 1–19). 6 questions, equal marks. More twists than Mock 1: level curves, absolute extrema, 2-variable classification, variation of parameters, a first-order IVP.

**How to use it:**
- Do it on paper, closed book, **no formula sheet**.
- 2 hours.
- Leave answers in exact form, simplified.
- Mark yourself with the answers at the bottom. Each answer says which topic and § to go back to.

---

## Questions

### Q1. Domains, level curves, limits (Sheet 1 Q1, Q2, Q3, Q7) — 20 marks

a. Find and sketch the domain of $f(x,y) = \sqrt{x - y^2} + \ln(4 - x)$. (6)

b. Find the level curve of $g(x,y) = \ln(x^2 + 4y^2)$ through (2, 1). What shape is it? (4)

c. Show that $\lim_{(x,y)\to(0,0)} \frac{xy^2}{x^2+y^4}$ does not exist. (Hint: straight lines aren't enough.) (5)

d. Find the continuous extension of $h(x,y) = \frac{x^3-y^3}{x-y}$ at the point (2, 2). (5)

---

### Q2. Second partials, chain rule, linear approximation (Sheet 2 Q5, Q11, Sheet 4 Q1) — 20 marks

a. Find $f_{xx}$, $f_{yy}$, $f_{xy}$ for $f(x,y) = x^3y^2 - e^{2x}\sin y$. (6)

b. w is a function of x and y, with x = eʳ cos s, y = eʳ sin s. Express $w_r$ and $w_s$ in terms of $w_x$, $w_y$, r, s, and hence show that $w_r^2 + w_s^2 = e^{2r}(w_x^2 + w_y^2)$. (8)

c. Use linear approximation to estimate $\sqrt{(3.02)^2 + (3.97)^2}$. (6)

---

### Q3. Gradient, directions, tangent planes (Sheet 3 Q2, Q3, Q4, Q10) — 20 marks

a. f(x, y, z) = xeʸ + yeᶻ. Find the rate of change of f at (2, 0, 0) in the direction of ⟨2, 1, 2⟩. (6)

b. g(x, y) = x² − xy + y². At (1, 2), find the direction of fastest decrease and its rate, and the directions of zero change. (7)

c. Find the tangent plane to the surface z = xeʸ at (2, 0, 2). (7)

---

### Q4. Critical points and absolute extrema (Sheet 4 Q8, Q14) — 20 marks

a. Find and classify all critical points of f(x, y) = x³ + y³ − 3x − 12y + 20. Give the local max and min values. (10)

b. Find the absolute max and min of g(x, y) = 2x² + y² − 4x on the closed disk x² + y² ≤ 4. (10)

---

### Q5. Lagrange with two constraints, 3-variable test (Sheet 4 Q19, Q11) — 20 marks

a. Find the minimum of x² + y² + z² subject to x + 2y + z = 6 and x − y = 0. Why is there no maximum? (10)

b. Find and classify the critical points of f(x, y, z) = x³ − 3x + y² + z² + yz. (10)

---

### Q6. ODEs (Sheet 5 Q2, Q6, Q8) — 20 marks

a. Solve the IVP xy′ − y = x²eˣ, y(1) = 0 (x > 0). (6)

b. Use variation of parameters to find the general solution of y″ + y = sec x (0 < x < π/2). (8)

c. Find the general solution of y‴ − y″ − 4y′ + 4y = 0. (6)

---

## Answers

<details><summary>Q1 answers</summary>

**a.** √ needs x − y² ≥ 0, i.e. x ≥ y². ln needs x < 4.

$$\text{dom}(f) = \{(x,y) \in \mathbb{R}^2 \mid y^2 \leq x < 4\}$$

Sketch: the parabola x = y² opening to the right (solid, included), and the vertical line x = 4 (dashed, excluded). Shade inside the parabola, left of x = 4. Corners at (4, ±2), open circles there.

**b.** g(2, 1) = ln 8. ln(x² + 4y²) = ln 8 ⟹ **x² + 4y² = 8**, an ellipse through (±2√2, 0) and (0, ±√2).

**c.** Along any line y = mx: $\frac{m^2x^3}{x^2 + m^4x^4} = \frac{m^2x}{1+m^4x^2} \to 0$.

Along the parabola x = y²: $\frac{y^4}{y^4+y^4} = \frac12 \to \frac12$.

0 ≠ 1/2, so no limit.

**d.** h(2, 2) = 0/0. x³ − y³ = (x − y)(x² + xy + y²), so the limit is 4 + 4 + 4 = 12.

g(x, y) := h(x, y) when (x, y) ≠ (2, 2), and **g(2, 2) := 12**. (In fact g = x² + xy + y² everywhere works.)

→ Topic 1 §3, §4; Topic 2 §3; Topic 3 §2, §5

</details>

<details><summary>Q2 answers</summary>

**a.** f_x = 3x²y² − 2e^(2x)sin y, f_y = 2x³y − e^(2x)cos y.

$$f_{xx} = 6xy^2 - 4e^{2x}\sin y, \quad f_{yy} = 2x^3 + e^{2x}\sin y, \quad f_{xy} = 6x^2y - 2e^{2x}\cos y$$

**b.** x_r = eʳcos s, y_r = eʳsin s, x_s = −eʳsin s, y_s = eʳcos s.

$$w_r = e^r\cos s\,w_x + e^r\sin s\,w_y, \qquad w_s = -e^r\sin s\,w_x + e^r\cos s\,w_y$$

Square and add. Cross terms ±2e²ʳ sin s cos s w_xw_y cancel:

$$w_r^2 + w_s^2 = e^{2r}(\cos^2 s + \sin^2 s)(w_x^2 + w_y^2) = e^{2r}(w_x^2 + w_y^2)$$

**c.** f = √(x² + y²) at (3, 4): f = 5, f_x = 3/5, f_y = 4/5.

L = 5 + (3/5)(0.02) + (4/5)(−0.03) = 5 + 0.012 − 0.024 = **4.988**.

→ Topic 10 §1; Topic 5 §3; Topic 7 §4

</details>

<details><summary>Q3 answers</summary>

**a.** ∇f = ⟨eʸ, xeʸ + eᶻ, yeᶻ⟩ → ⟨1, 3, 0⟩. ‖⟨2, 1, 2⟩‖ = 3, u = ⟨2/3, 1/3, 2/3⟩.

D = 2/3 + 1 + 0 = **5/3**.

**b.** ∇g = ⟨2x − y, −x + 2y⟩ → ⟨0, 3⟩.

Fastest decrease: direction −⟨0, 3⟩, unit **−j = ⟨0, −1⟩**, rate **−3**.

Zero change: orthogonal to ⟨0, 3⟩: **±i = ⟨±1, 0⟩**.

**c.** Explicit: f = xeʸ. f_x = eʸ = 1, f_y = xeʸ = 2 at (2, 0).

z − 2 = 1(x − 2) + 2(y − 0) ⟹ **z = x + 2y**.

→ Topic 8 §3, §4; Topic 9 §4

</details>

<details><summary>Q4 answers</summary>

**a.** f_x = 3x² − 3 = 0 ⟹ x = ±1. f_y = 3y² − 12 = 0 ⟹ y = ±2.

f_xx = 6x, f_yy = 6y, f_xy = 0, so D = 36xy.

| Point | D | f_xx | Verdict | f |
|---|---|---|---|---|
| (1, 2) | 72 | 6 | local min | 2 |
| (−1, −2) | 72 | −6 | local max | 38 |
| (1, −2) | −72 | | saddle | 34 |
| (−1, 2) | −72 | | saddle | 6 |

**Local min value 2, local max value 38.**

**b.** Interior: g_x = 4x − 4 = 0, g_y = 2y = 0 ⟹ (1, 0), inside. g = −2.

Boundary: y² = 4 − x², g = 2x² + 4 − x² − 4x = (x − 2)², −2 ≤ x ≤ 2. Min 0 at x = 2, max 16 at x = −2.

**Absolute max 16 at (−2, 0). Absolute min −2 at (1, 0).**

→ Topic 11 §4; Topic 12 §3

</details>

<details><summary>Q5 answers</summary>

**a.** g₁ = x + 2y + z, g₂ = x − y.

2x = λ + μ, 2y = 2λ − μ, 2z = λ.

x = y ⟹ λ + μ = 2λ − μ ⟹ λ = 2μ. So z = μ, x = y = 3μ/2.

Constraint: 3μ/2 + 3μ + μ = 11μ/2 = 6 ⟹ μ = 12/11. Point (18/11, 18/11, 12/11).

**Min = 72/11.**

Both constraints are planes, so they meet in a line. A line goes on forever, so the distance from the origin (and x² + y² + z²) has no largest value.

**b.** ∇f = ⟨3x² − 3, 2y + z, 2z + y⟩ = 0 ⟹ x = ±1, and 2y + z = 0, y + 2z = 0 ⟹ y = z = 0.

$$H = \begin{pmatrix} 6x & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix}$$

**(1, 0, 0):** 6, 12, 18 → + + +: **local min** (value −2).

**(−1, 0, 0):** −6, −12, −18 → not a pattern: **saddle**.

→ Topic 14 §3; Topic 13 §3

</details>

<details><summary>Q6 answers</summary>

**a.** y′ − y/x = xeˣ. G = e^(−ln x) = 1/x.

(y/x)′ = eˣ ⟹ y/x = eˣ + C ⟹ y = xeˣ + Cx.

y(1) = e + C = 0 ⟹ C = −e.

$$y = xe^x - ex$$

**b.** y₁ = cos x, y₂ = sin x, W = cos²x + sin²x = 1, g = sec x.

u₁′ = −sin x sec x = −tan x ⟹ u₁ = ln(cos x). u₂′ = cos x sec x = 1 ⟹ u₂ = x.

$$y = C_1\cos x + C_2\sin x + \cos x\ln(\cos x) + x\sin x$$

**c.** r³ − r² − 4r + 4 = r²(r − 1) − 4(r − 1) = (r − 1)(r − 2)(r + 2).

$$y = C_1e^x + C_2e^{2x} + C_3e^{-2x}$$

→ Topic 15 §4; Topic 18 §1; Topic 19 §1, §2

</details>
