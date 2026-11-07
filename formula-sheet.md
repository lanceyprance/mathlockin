# Formulas to know by heart

⚠️ **There is no formula sheet in this exam.** ("No books of tables or formulae are to be issued.") Everything below must be in your head.

Each line links to the notes section that explains it.

---

## Domains (Topic 1)

| Formula has | You need |
|---|---|
| $\frac{A}{B}$ | $B \neq 0$ |
| $\sqrt{A}$ | $A \geq 0$ |
| $\ln A$ | $A > 0$ |

## Limits and continuity (Topic 3)

- Two paths, two values → no limit.
- Continuous at (a, b): f(a, b) defined, limit exists, limit = f(a, b).
- Continuous → substitute. 0/0 → factor and cancel.

## Partial derivatives and chain rules (Topics 4, 5)

- $f_x$: treat y as a constant. $f_y$: treat x as a constant.
- One parameter: $\frac{dw}{dt} = w_x x_t + w_y y_t + w_z z_t$
- Two parameters: $w_r = w_x x_r + w_y y_r$, $\quad w_s = w_x x_s + w_y y_s$

## Implicit differentiation (Topic 6)

$$F(x,y,z) = c \implies z_x = -\frac{F_x}{F_z}, \quad z_y = -\frac{F_y}{F_z}$$

## Errors and linear approximation (Topic 7)

$$\Delta z \approx f_x \Delta x + f_y \Delta y$$

$$z = kx^m y^n \implies 100\frac{\Delta z}{z} \approx m\left(100\frac{\Delta x}{x}\right) + n\left(100\frac{\Delta y}{y}\right)$$

$$L(x,y) = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$$

## Gradient and directional derivatives (Topic 8)

$$\nabla f = \langle f_x, f_y, f_z \rangle \qquad D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} \quad (\mathbf{u} \text{ a unit vector})$$

- Fastest increase: direction $\nabla f$, rate $\Vert \nabla f\Vert $.
- Fastest decrease: direction $-\nabla f$, rate $-\Vert \nabla f\Vert $.
- Zero change: directions orthogonal to $\nabla f$.
- Unit vector: $\mathbf{u} = \frac{\mathbf{v}}{\Vert \mathbf{v}\Vert }$, $\Vert \langle a,b,c\rangle\Vert  = \sqrt{a^2+b^2+c^2}$.

## Tangent lines and planes (Topic 9)

- Tangent line to $f(x,y) = c$ at $(x_0,y_0)$: $f_x(x-x_0) + f_y(y-y_0) = 0$
- Tangent plane to $F(x,y,z) = c$ at $(a,b,c)$: $F_x(x-a) + F_y(y-b) + F_z(z-c) = 0$
- Tangent plane to $z = f(x,y)$: $z - c = f_x(x-a) + f_y(y-b)$

## Hessian and Jacobian (Topic 10)

$$H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix} \qquad J = \begin{pmatrix} \partial f_i / \partial x_j \end{pmatrix} \text{ (row i = function i)}$$

$f_{xy} = f_{yx}$ (Clairaut).

## Critical points (Topics 11–13)

- Critical point: all first partials = 0.
- 2 variables, $D = \det H = f_{xx}f_{yy} - f_{xy}^2$:
  - D > 0, f_xx > 0 → local min
  - D > 0, f_xx < 0 → local max
  - D < 0 → saddle
  - D = 0 → test fails
- 3+ variables, leading principal minors $|H_1|, |H_2|, |H_3|$:
  - all > 0 → local min
  - −, +, − → local max
  - anything else non-zero → saddle
- Closed region: critical points inside + extremes on the boundary → compare values.

## Lagrange multipliers (Topic 14)

- One constraint: $\nabla f = \lambda \nabla g$, $g = c$.
- Two constraints: $\nabla f = \lambda \nabla g_1 + \mu \nabla g_2$, $g_1 = c_1$, $g_2 = c_2$.
- Plug all solutions into f. Biggest = max, smallest = min.

## ODEs (Topics 15–19)

- Separable $y' = h(x)g(y)$: $\int \frac{dy}{g(y)} = \int h(x)\,dx$.
- Linear $y' + p(x)y = q(x)$: integrating factor $G = e^{\int p\,dx}$, then $(Gy)' = Gq$.
- $ay'' + by' + cy = 0$, roots of $ar^2 + br + c = 0$:
  - two real roots: $y = C_1e^{r_1x} + C_2e^{r_2x}$
  - double root: $y = (C_1 + C_2x)e^{rx}$
  - $r = k \pm i\omega$: $y = e^{kx}(C_1\cos\omega x + C_2\sin\omega x)$
- Non-homogeneous: $y = y_h + y_p$. Guess $y_p$ from the table (Topic 17). Multiply the guess by x if it already solves the homogeneous equation.
- Variation of parameters: $u_1'y_1 + u_2'y_2 = 0$, $u_1'y_1' + u_2'y_2' = f/a$.
