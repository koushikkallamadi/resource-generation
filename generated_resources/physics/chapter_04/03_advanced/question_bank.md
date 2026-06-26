---

## Section 1: Multiple Choice Questions (10 HOTS MCQs)

These questions require deep conceptual integration, mathematical analysis, and application of the quantum theory of radiation.

### Q1. Gauge Dependences and the Momentum Operator
In Unit IV, the interaction Hamiltonian $H'$ for a non-relativistic electron in a radiation field is simplified under the Coulomb gauge ($\nabla \cdot \mathbf{A} = 0$) to:
$$H' = \frac{q}{m} \mathbf{A} \cdot \mathbf{p}$$
If we instead choose a gauge where $\nabla \cdot \mathbf{A} \neq 0$ (such as a generalized Lorenz gauge), the commutator $[\mathbf{p}, \mathbf{A}]$ does not vanish. Under this condition, the correct operator identity for $(\mathbf{p} + q\mathbf{A})^2$ expanded to first order in $\mathbf{A}$ is:
A) $\mathbf{p}^2 + 2q\mathbf{A} \cdot \mathbf{p} - i\hbar q (\nabla \cdot \mathbf{A})$  
B) $\mathbf{p}^2 + 2q\mathbf{A} \cdot \mathbf{p} + i\hbar q (\nabla \cdot \mathbf{A})$  
C) $\mathbf{p}^2 + q(\mathbf{A} \cdot \mathbf{p} + \mathbf{p} \cdot \mathbf{A})$  
D) $\mathbf{p}^2 + 2q\mathbf{A} \cdot \mathbf{p}$

### Q2. Breakdown of the Electric Dipole Approximation
The transition matrix element calculation uses the approximation $e^{\pm i \mathbf{k} \cdot \mathbf{r}} \approx 1$. For a hydrogen-like atom with atomic number $Z$, this electric dipole approximation starts to break down when the transition energy $\Delta E$ is comparable to:
A) $\alpha m_e c^2$  
B) $Z \alpha m_e c^2$  
C) $\frac{m_e c^2}{Z \alpha}$  
D) $Z^2 \alpha^2 m_e c^2$

### Q3. Equal-Time Commutation Relations in Coulomb Gauge
During the canonical quantization of the radiation field, we define the vector potential operator $\mathbf{A}(\mathbf{r})$. In the Coulomb gauge ($\nabla \cdot \mathbf{A} = 0$), the equal-time commutator between the components of the vector potential $A_i(\mathbf{r})$ and the transverse electric field component $E_j^T(\mathbf{r}')$ is:
A) $[A_i(\mathbf{r}), E_j^T(\mathbf{r}')] = -i\hbar \delta_{ij} \delta^3(\mathbf{r} - \mathbf{r}')$  
B) $[A_i(\mathbf{r}), E_j^T(\mathbf{r}')] = -\frac{i\hbar}{\epsilon_0} \delta_{ij} \delta^3(\mathbf{r} - \mathbf{r}')$  
C) $[A_i(\mathbf{r}), E_j^T(\mathbf{r}')] = -\frac{i\hbar}{\epsilon_0} \left( \delta_{ij} - \frac{\partial_i \partial_j}{\nabla^2} \right) \delta^3(\mathbf{r} - \mathbf{r}')$  
D) $[A_i(\mathbf{r}), E_j^T(\mathbf{r}')] = 0$

### Q4. Polarization States in Thomson Scattering
In classical and quantum Thomson scattering of unpolarized light, the differential cross-section is:
$$\frac{d\sigma}{d\Omega} = \frac{r_0^2}{2} (1 + \cos^2\theta)$$
If the incident light is completely unpolarized, at which scattering angle $\theta$ is the scattered radiation $100\%$ linearly polarized?
A) $\theta = 0$  
B) $\theta = \frac{\pi}{4}$  
C) $\theta = \frac{\pi}{2}$  
D) $\theta = \pi$

### Q5. Structural Origin of the "Seagull" Diagram in Spinless Compton Scattering
In the second-order perturbation analysis of spin-0 (spinless) Compton scattering, we obtain three Feynman diagrams: the $s$-channel, the $u$-channel, and a contact interaction (the "seagull" diagram). In spinor (Dirac electron) Compton scattering, this seagull diagram is entirely absent. What is the fundamental physical reason for this difference?
A) The Dirac equation is linear in the 4-momentum $p_\mu$, meaning the interaction Lagrangian has no term proportional to $A^2$.  
B) Spinor electrons cannot absorb and emit two photons simultaneously due to the Pauli exclusion principle.  
C) Gauge invariance forbids contact interactions for spin-1/2 fermions.  
D) The seagull diagram is cancelled by the electron's anomalous magnetic moment.

```mermaid
graph LR
    subgraph Spinless Compton (KG Field)
    A[s-channel] --- B[u-channel] --- C[Seagull contact]
    end
    subgraph Spinor Compton (Dirac Field)
    D[s-channel] --- E[u-channel]
    end
```

### Q6. Bose-Einstein Symmetry in Moller Scattering
For spinless Moller scattering ($e^- + e^- \rightarrow e^- + e^-$), the transition amplitude is symmetric under the exchange of mandelstam variables $t \leftrightarrow u$. If we consider physical electrons (which are fermions), how does this exchange symmetry affect the differential cross-section in the singlet state versus the triplet state?
A) The singlet state is symmetric under $t \leftrightarrow u$, while the triplet state is antisymmetric.  
B) Both states are antisymmetric under $t \leftrightarrow u$ due to the Fermi-Dirac statistics.  
C) The singlet state is antisymmetric, while the triplet state is symmetric under $t \leftrightarrow u$.  
D) Fermionic statistics require the total cross-section to vanish at $\theta = \frac{\pi}{2}$ for all spin configurations.

### Q7. Unitarity and the Time-Evolution Operator
The time-evolution operator $U(t, t_0)$ in the interaction picture must satisfy $U^\dagger(t, t_0) U(t, t_0) = \mathbb{I}$. Which mathematical property of the interaction Hamiltonian $H_I(t)$ guarantees this relation?
A) $H_I(t)$ is Hermitian: $H_I^\dagger(t) = H_I(t)$  
B) $H_I(t)$ is unitary: $H_I^\dagger(t) H_I(t) = \mathbb{I}$  
C) $H_I(t)$ commutes with the free Hamiltonian: $[H_I(t), H_0] = 0$  
D) $H_I(t)$ is time-independent.

### Q8. Gauge Non-Invariance of the Fermi Lagrangian Density
The Fermi Lagrangian density for the electromagnetic field is:
$$\mathcal{L} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} - \frac{1}{2}(\partial_\mu A^\mu)^2$$
Under a general gauge transformation $A_\mu \rightarrow A_\mu - \partial_\mu \chi$, the action $S = \int \mathcal{L} d^4x$ is invariant only if the gauge function $\chi$ satisfies which condition?
A) $\nabla^2 \chi = 0$  
B) $\partial_\mu \chi \partial^\mu \chi = 0$  
C) $\square \chi = 0$ (where $\square = \partial_\mu \partial^\mu$)  
D) $\chi$ is a constant.

### Q9. Charge Conjugation of the Complex Klein-Gordon Field
A complex scalar field $\phi(x)$ represents charged spinless bosons. The charge operator is:
$$Q = q \sum_k [n_+(k) - n_-(k)]$$
Under the charge conjugation operator $\mathcal{C}$, the field operator $\phi(x)$ transforms as $\mathcal{C} \phi(x) \mathcal{C}^\dagger = \eta \phi^\dagger(x)$ (where $|\eta|^2=1$). This transformation:
A) Swaps the creation/annihilation operators of particles and antiparticles, reversing the sign of $Q$.  
B) Leaves the charge $Q$ invariant but reverses the spin alignment.  
C) Projects the field onto its real (neutral) components.  
D) Changes the sign of the energy eigenvalues of the field.

### Q10. Ultimate Energy Transfer in Compton Scattering
A high-energy photon with energy $E_\gamma = \eta m_e c^2$ ($\eta \gg 1$) collides head-on with a stationary electron. In the limit $\eta \rightarrow \infty$, the fraction of the photon's initial energy transferred to the electron in a backscattering event ($\theta = \pi$) approaches:
A) $0$  
B) $0.5$  
C) $1.0$  
D) $\frac{1}{1 + 2\eta}$

---

## Section 2: Case-Study / Passage-Based Questions (5 Questions)

### Passage 1: Quantization of the Radiation Field and the Casimir Effect

The quantized energy of the electromagnetic field is expressed as:
$$H_r = \sum_{\mathbf{k}, \alpha} \left( a_{\mathbf{k}, \alpha}^\dagger a_{\mathbf{k}, \alpha} + \frac{1}{2} \right) \hbar \omega_k$$
where $a_{\mathbf{k}, \alpha}^\dagger$ and $a_{\mathbf{k}, \alpha}$ are the creation and annihilation operators for photons of wavevector $\mathbf{k}$ and polarization $\alpha$. The term $\frac{1}{2}\hbar\omega_k$ represents the zero-point energy of each mode. While this vacuum energy is formally divergent when summed over all infinite modes, spatial boundaries (such as conducting plates) restrict the allowed modes, leading to a measurable physical force known as the **Casimir Effect**.

```
   Plate 1                        Plate 2
  |================|            |================|
  |                | <--- d --->|                |
  | Allowed Modes: |            | Allowed Modes: |
  | k = n*pi/d     |            | k = continuous |
  |================|            |================|
```

#### Q11. Regularization of Vacuum Energy
Explain mathematically how the formally infinite vacuum energy $E_0 = \frac{1}{2} \sum \hbar \omega_k$ is regularized to yield a finite, attractive force per unit area $F/A = -\frac{\pi^2 \hbar c}{240 d^4}$ between two parallel conducting plates separated by a distance $d$.

#### Q12. Dimensional Analysis of the Casimir Force
Using only the fundamental constants relevant to this relativistic quantum phenomenon—Planck's constant $\hbar$, the speed of light $c$, and the plate separation distance $d$—prove via dimensional analysis that the Casimir force per unit area must scale as $d^{-4}$.

---

### Passage 2: Semiclassical Transition Rates and Dipole Selection Rules

In Unit IV, the interaction of an atom with an electromagnetic wave is treated semiclassically. The transition matrix element is:
$$\langle s | H' | n \rangle \propto \langle s | \mathbf{p} \cdot \hat{e} | n \rangle$$
Using the commutation relation $[x, H_a] = \frac{i\hbar p_x}{m}$, this momentum matrix element is transformed into the position matrix element:
$$\langle s | \mathbf{p} | n \rangle = \frac{m \omega_{ns}}{i} \langle s | \mathbf{r} | n \rangle$$
This is the **Electric Dipole Approximation**, and the term $\mathbf{d}_{sn} = q \langle s | \mathbf{r} | n \rangle$ is the transition dipole moment.

#### Q13. Mathematical Derivation of the Commutator Relation
Prove step-by-step the operator identity:
$$[\mathbf{r}, H_a] = \frac{i\hbar}{m} \mathbf{p}$$
where $H_a = \frac{\mathbf{p}^2}{2m} + V(\mathbf{r})$. Show why the potential energy term $V(\mathbf{r})$ does not contribute to this commutator.

#### Q14. Selection Rule for Parity
Using the spatial symmetry properties of the wavefunctions under inversion ($\mathbf{r} \rightarrow -\mathbf{r}$), prove that electric dipole transitions between states of the same parity (e.g., $s \rightarrow s$ or $p \rightarrow p$) are strictly forbidden.

#### Q15. Transition Matrix for $1s \rightarrow 2s$ in Hydrogen
Explain why the hydrogen transition $1s \rightarrow 2s$ cannot occur via single-photon electric dipole emission. Discuss how this state decays and the implications for its experimental lifetime.

---

## Section 3: High-Difficulty Long Answer Questions (5 Questions)

### Q16. Gauge Invariance of the Classical Maxwell Equations vs. Fermi Lagrangian
Show that while the classical Maxwell field strength tensor $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is strictly invariant under the gauge transformation $A_\mu \rightarrow A_\mu - \partial_\mu \chi$, the Fermi Lagrangian:
$$\mathcal{L} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} - \frac{1}{2}(\partial_\mu A^\mu)^2$$
is modified by a surface term and a bulk term. 

Derive the Euler-Lagrange equations of motion from the Fermi Lagrangian and show that they reduce to the wave equation $\square A_\mu = 0$ under the Lorenz gauge condition $\partial_\mu A^\mu = 0$.

### Q17. Analytical Derivation of the Dyson Chronological Series
The time-evolution operator $U(t, t_0)$ satisfies the integral equation:
$$U(t, t_0) = \mathbb{I} - \frac{i}{\hbar} \int_{t_0}^t H_I(t_1) U(t_1, t_0) dt_1$$
By iterative substitution, derive the first two non-trivial terms ($U_1$ and $U_2$). Show how the time-ordering operator $P$ allows us to rewrite the nested integral in $U_2$ as:
$$U_2(t, t_0) = \frac{1}{2!} \left( -\frac{i}{\hbar} \right)^2 \int_{t_0}^t dt_1 \int_{t_0}^t dt_2 P\{H_I(t_1) H_I(t_2)\}$$
Provide a clear geometric interpretation of this transformation in the $t_1-t_2$ integration plane.

### Q18. High-Energy Compton Scattering: Derivation of the Klein-Nishina Limit
Explain the kinematic and dynamic differences between Thomson scattering and Compton scattering. 

Starting from the Compton relation for wavelength shift:
$$\lambda' - \lambda = \frac{h}{m_e c}(1 - \cos\theta)$$
mathematically derive the relation for the scattered photon's energy $E'$ as a function of the incident photon's energy $E$ and the scattering angle $\theta$. Show that in the extreme relativistic limit ($E \gg m_e c^2$), the differential cross-section is highly peaked in the forward direction.

### Q19. Rigorous Quantization of the Radiation Field
Formulate the complete mathematical framework for the quantization of the free electromagnetic field in a cubical cavity of volume $V$. 

1. Write the vector potential $\mathbf{A}(\mathbf{r}, t)$ as a Fourier expansion in plane waves.
2. Impose the Coulomb gauge and identify the transverse polarization vectors.
3. Introduce the canonical coordinates $q_{\mathbf{k}, \alpha}$ and momenta $p_{\mathbf{k}, \alpha}$.
4. Define the creation and annihilation operators, and derive the canonical commutation relations $[a_{\mathbf{k}, \alpha}, a_{\mathbf{k}', \alpha'}^\dagger] = \delta_{\mathbf{k}\mathbf{k}'}\delta_{\alpha\alpha'}$.

### Q20. Microcausality and the Klein-Gordon Propagator
For a real scalar field $\phi(x)$, the principal requirement of microcausality is that operators at space-like separated points must commute:
$$[\phi(x), \phi(y)] = 0 \quad \text{for} \quad (x-y)^2 < 0$$
Using the Fourier expansion of the field operator $\phi(x)$:
$$\phi(x) = \int \frac{d^3k}{(2\pi)^3 \sqrt{2\omega_k}} \left[ a_k e^{-ik\cdot x} + a_k^\dagger e^{ik\cdot x} \right]$$
explicitly calculate the commutator $[\phi(x), \phi(y)]$ and prove that it vanishes identically when $x$ and $y$ are space-like separated. Explain how this mathematical result guarantees that no physical signal can travel faster than the speed of light.

---

## Section 4: Challenge Questions (3 Questions)

### Q21. Design of a Precision Compton Polarimeter
You are tasked with designing an experimental setup to measure the linear polarization of an intense, high-energy gamma-ray beam ($E_\gamma \approx 10 \text{ MeV}$) produced at a synchrotron facility. The measurement must rely on the polarization dependence of Compton scattering as described by the Klein-Nishina formula:
$$\frac{d\sigma}{d\Omega} \propto \left( \frac{\omega'}{\omega} \right)^2 \left[ \frac{\omega}{\omega'} + \frac{\omega'}{\omega} - 2\sin^2\theta \cos^2\phi \right]$$
where $\phi$ is the angle between the polarization vector of the incident photon and the scattering plane.

```
       Incident Photon (k, polarized)
      ===================================> [Scatterer: Be Target]
                                               / \
                                              /   \  Scattered Photon (k')
                                             /     \   Scattered at angle theta
                                            /       v
                                     [Azimuthal Detector Array (phi)]
```

Develop an experimental design addressing:
1. The choice of scatterer material (atomic number $Z$, thickness) to minimize multiple scattering and photoelectric absorption.
2. The geometry and configuration of the detectors to optimize the measurement of the azimuthal asymmetry (dependence on $\phi$).
3. The method to calibrate and isolate the background from electron-positron pair production.

### Q22. Vacuum Polarization and the Schwinger Limit
In classical electrodynamics, Maxwell's equations are strictly linear, meaning light-by-light scattering in vacuum is impossible. In Quantum Electrodynamics (QED), however, two photons can scatter off each other via virtual electron-positron loops (vacuum polarization).

```
          Photon 1 \         / Photon 3
                    \_______/
                    |       |  Virtual Electron-Positron Loop
                    |_______|
                    /       \
          Photon 2 /         \ Photon 4
```

1. Draw the lowest-order Feynman diagrams (box diagrams) representing photon-photon scattering.
2. The critical field strength at which the vacuum becomes unstable and non-linear QED effects dominate is the **Schwinger Limit**:
   $$E_c = \frac{m_e^2 c^3}{e \hbar}$$
   Calculate the value of $E_c$ in $\text{V/m}$.
3. Discuss how ultra-intense laser systems could be used to experimentally verify this non-linear optical behavior of empty space.

### Q23. Gauge Invariance of the S-Matrix
Prove that the $S$-matrix element for the scattering of an electron by an external electromagnetic field is invariant under the gauge transformation:
$$A_\mu(x) \rightarrow A_\mu(x) + \partial_\mu \Lambda(x)$$
where $\Lambda(x)$ is a localized, differentiable function that vanishes at $t \rightarrow \pm\infty$. Use this to show that physical observables (such as decay rates and cross-sections) are independent of the choice of gauge, even though the intermediate vector potentials and Feynman propagators are highly gauge-dependent.

---

## Answer Key & Explanations

### Section 1: Multiple Choice Questions

| Q. No | Answer | Explanation |
| :--- | :--- | :--- |
| **Q1** | **A** | Since $\mathbf{p} = -i\hbar\nabla$, we have $[\mathbf{p}, \mathbf{A}] = -i\hbar(\nabla \cdot \mathbf{A})$. Thus, $\mathbf{p}\cdot\mathbf{A} = \mathbf{A}\cdot\mathbf{p} - i\hbar(\nabla\cdot\mathbf{A})$. Expanding $(\mathbf{p}+q\mathbf{A})^2 = \mathbf{p}^2 + q(\mathbf{A}\cdot\mathbf{p} + \mathbf{p}\cdot\mathbf{A}) + q^2\mathbf{A}^2$. Substituting the commutator identity and neglecting $\mathbf{A}^2$ yields $\mathbf{p}^2 + 2q\mathbf{A}\cdot\mathbf{p} - i\hbar q(\nabla\cdot\mathbf{A})$. |
| **Q2** | **C** | The dipole approximation $e^{i\mathbf{k}\cdot\mathbf{r}} \approx 1$ requires $\mathbf{k}\cdot\mathbf{r} \ll 1$. Since $r \sim a_0 / Z = \frac{\hbar}{Z \alpha m_e c}$ and $k = \frac{\Delta E}{\hbar c}$, we need $\frac{\Delta E}{\hbar c} \frac{\hbar}{Z \alpha m_e c} \ll 1 \implies \Delta E \ll Z \alpha m_e c^2$. Thus, breakdown begins when $\Delta E \sim \frac{m_e c^2}{Z \alpha}$. |
| **Q3** | **C** | In the Coulomb gauge, the commutation relations are altered by the projection operator to maintain the transversality condition $\nabla \cdot \mathbf{A} = 0$. The transverse delta function is $\delta_{ij}^T(\mathbf{r}-\mathbf{r}') = \left( \delta_{ij} - \frac{\partial_i \partial_j}{\nabla^2} \right) \delta^3(\mathbf{r}-\mathbf{r}')$, yielding option C. |
| **Q4** | **C** | For unpolarized incident light, the scattered light intensity components are $I_\parallel \propto \cos^2\theta$ and $I_\perp \propto 1$. At $\theta = \frac{\pi}{2}$, $I_\parallel = 0$, meaning the scattered light is completely polarized perpendicular to the scattering plane ($100\%$ linear polarization). |
| **Q5** | **A** | The Klein-Gordon Lagrangian has a quadratic term $e^2 A^2 \phi^\dagger \phi$, giving rise to the 4-point contact (seagull) vertex. The Dirac interaction term is purely linear in $A_\mu$ ($e\bar{\psi}\gamma^\mu A_\mu \psi$), so no fundamental 4-point vertex exists. |
| **Q6** | **C** | Identical fermions must have a totally antisymmetric wavefunction. The singlet state ($S=0$) is spatially symmetric, requiring an antisymmetric spatial amplitude under $t \leftrightarrow u$ (or $\theta \rightarrow \pi-\theta$). The triplet state ($S=1$) is spatially antisymmetric, requiring a symmetric amplitude. |
| **Q7** | **A** | Since $U(t, t_0) = T \exp\left(-\frac{i}{\hbar} \int_{t_0}^t H_I(t') dt'\right)$, the unitarity condition $U^\dagger U = \mathbb{I}$ directly requires $H_I^\dagger(t) = H_I(t)$. |
| **Q8** | **C** | Under $A_\mu \rightarrow A_\mu - \partial_\mu \chi$, the term $(\partial_\mu A^\mu)^2$ transforms into $(\partial_\mu A^\mu - \square \chi)^2$. For this term and the action to remain invariant, we must have $\square \chi = 0$. |
| **Q9** | **A** | Charge conjugation $\mathcal{C}$ maps particles to antiparticles (reversing the charge) while preserving space-time properties such as momentum and spin. Thus, $Q \rightarrow -Q$. |
| **Q10** | **C** | From $E' = \frac{E}{1 + \frac{E}{m_e c^2}(1-\cos\theta)}$, for $\theta = \pi$, $E' = \frac{E}{1 + 2\eta}$. The energy transferred is $\Delta E = E - E' = E \left(1 - \frac{1}{1+2\eta}\right)$. As $\eta \rightarrow \infty$, the fractional transfer $\frac{\Delta E}{E} \rightarrow 1.0$. |

---

### Section 2: Case-Study / Passage-Based Questions

#### Q11. Regularization of Vacuum Energy
* **Step 1:** The vacuum energy between the plates is given by $E(d) = \frac{\hbar}{2} \sum \omega$. This sum diverges. We introduce a regulator, such as an exponential cutoff function $e^{-\pi k / \Lambda}$, representing the physical fact that real metal plates become transparent to extremely high-frequency electromagnetic modes.
* **Step 2:** The difference between the bounded vacuum energy (summed over discrete modes $n\pi/d$) and the unbounded vacuum energy (integrated over continuous modes) is computed using the **Euler-Maclaurin formula**:
  $$\sum_{n=1}^\infty f(n) - \int_{0}^\infty f(x)dx = -\frac{1}{12} f'(0) + \frac{1}{720} f'''(0) + \dots$$
* **Step 3:** Applying this to $f(n) = \frac{\pi \hbar c}{d} \sqrt{n^2 + \dots}$, the regulator-dependent terms cancel out as the cutoff limit $\Lambda \rightarrow \infty$, leaving a finite, negative, and regularized energy:
  $$E_{\text{reg}}(d) = -\frac{\pi^2 \hbar c}{720 d^3} A$$
* **Step 4:** The Casimir force is the derivative of this energy with respect to the plate separation:
  $$\frac{F}{A} = -\frac{\partial}{\partial d} \left( \frac{E_{\text{reg}}}{A} \right) = -\frac{\pi^2 \hbar c}{240 d^4}$$

#### Q12. Dimensional Analysis of the Casimir Force
Let the force per unit area be $P = \frac{F}{A}$ with dimensions $[P] = [M L^{-1} T^{-2}]$. We assume:
$$P = C \hbar^x c^y d^z$$
where $C$ is a dimensionless constant. Substituting the dimensions of the variables:
* $[\hbar] = [M L^2 T^{-1}]$
* $[c] = [L T^{-1}]$
* $[d] = [L]$

Equating the powers of Mass ($M$), Length ($L$), and Time ($T$):
1. For $M$: $x = 1$
2. For $T$: $-x - y = -2 \implies -1 - y = -2 \implies y = 1$
3. For $L$: $2x + y + z = -1 \implies 2(1) + 1 + z = -1 \implies z = -4$

Thus:
$$P = C \frac{\hbar c}{d^4}$$
This mathematically proves that the Casimir force per unit area scales exactly as $d^{-4}$.

#### Q13. Commutator Derivation $[\mathbf{r}, H_a]$
Let us evaluate $[x, H_a]$:
$$[x, H_a] = \left[x, \frac{p_x^2 + p_y^2 + p_z^2}{2m} + V(x, y, z)\right]$$
Since $x$ commutes with $p_y, p_z$ and any function of position $V(\mathbf{r})$:
$$[x, H_a] = \frac{1}{2m} [x, p_x^2]$$
Using the commutator identity $[A, B^2] = [A, B]B + B[A, B]$ and $[x, p_x] = i\hbar$:
$$[x, p_x^2] = [x, p_x]p_x + p_x[x, p_x] = i\hbar p_x + p_x (i\hbar) = 2i\hbar p_x$$
Therefore:
$$[x, H_a] = \frac{1}{2m} (2i\hbar p_x) = \frac{i\hbar}{m} p_x$$
Extending this to all three spatial dimensions gives:
$$[\mathbf{r}, H_a] = \frac{i\hbar}{m} \mathbf{p}$$

#### Q14. Selection Rule for Parity
The transition matrix element is proportional to:
$$\mathbf{d}_{sn} = \int \psi_s^*(\mathbf{r}) \mathbf{r} \psi_n(\mathbf{r}) d^3r$$
Let the parity operator be $\mathcal{P}$ such that $\mathcal{P}\mathbf{r} = -\mathbf{r}$. Under spatial inversion:
* If state $|n\rangle$ has parity $\pi_n = \pm 1$, then $\psi_n(-\mathbf{r}) = \pi_n \psi_n(\mathbf{r})$.
* If state $|s\rangle$ has parity $\pi_s = \pm 1$, then $\psi_s^*(-\mathbf{r}) = \pi_s \psi_s^*(\mathbf{r})$.

Applying the coordinate transformation $\mathbf{r} \rightarrow -\mathbf{r}$ to the integral:
$$\mathbf{d}_{sn} = \int \psi_s^*(-\mathbf{r}) (-\mathbf{r}) \psi_n(-\mathbf{r}) d^3r = -\pi_s \pi_n \int \psi_s^*(\mathbf{r}) \mathbf{r} \psi_n(\mathbf{r}) d^3r = -\pi_s \pi_n \mathbf{d}_{sn}$$
For $\mathbf{d}_{sn} \neq 0$, we must have:
$$-\pi_s \pi_n = 1 \implies \pi_s \pi_n = -1$$
This requires $\pi_s \neq \pi_n$, proving that electric dipole transitions can only occur between states of opposite parity.

#### Q15. Transition Matrix for $1s \rightarrow 2s$ in Hydrogen
Both the $1s$ and $2s$ states of hydrogen are spherically symmetric ($l=0$) and have positive parity ($(-1)^l = +1$). 
* According to the parity selection rule ($\Delta \pi = -1$), an electric dipole transition between them is forbidden.
* Conservation of angular momentum also forbids a single-photon transition because a photon carries spin $J=1$, and $\Delta l = 0 \rightarrow 0$ cannot conserve angular momentum.
* Consequently, the $2s$ state is highly metastable. Its primary decay channel is the simultaneous emission of **two photons**, which yields a continuous energy spectrum and results in a very long lifetime ($\tau \approx 0.12 \text{ s}$), compared to the $2p$ lifetime of $\sim 1.6 \text{ ns}$.

---

### Section 3: High-Difficulty Long Answer Questions

#### Q16. Gauge Invariance and the Fermi Lagrangian
Under $A_\mu \rightarrow A_\mu - \partial_\mu \chi$:
1. $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu \rightarrow \partial_\mu(A_\nu - \partial_\nu \chi) - \partial_\nu(A_\mu - \partial_\mu \chi) = F_{\mu\nu} - (\partial_\mu \partial_\nu \chi - \partial_\nu \partial_\mu \chi) = F_{\mu\nu}$. Thus, the first term $-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}$ is gauge invariant.
2. The second term $(\partial_\mu A^\mu)^2 \rightarrow (\partial_\mu A^\mu - \square \chi)^2 = (\partial_\mu A^\mu)^2 - 2(\partial_\mu A^\mu)\square \chi + (\square \chi)^2$. This is not gauge invariant unless $\square \chi = 0$.

To find the Euler-Lagrange equations, we vary the action with respect to $A_\nu$:
$$\frac{\partial \mathcal{L}}{\partial A_\nu} - \partial_\mu \left( \frac{\partial \mathcal{L}}{\partial(\partial_\mu A_\nu)} \right) = 0$$
$$\frac{\partial \mathcal{L}}{\partial(\partial_\mu A_\nu)} = -F^{\mu\nu} - g^{\mu\nu} (\partial_\rho A^\rho)$$
$$\partial_\mu F^{\mu\nu} + \partial^\nu (\partial_\rho A^\rho) = 0 \implies \square A^\nu - \partial^\nu(\partial_\mu A^\mu) + \partial^\nu(\partial_\mu A^\mu) = 0 \implies \square A^\nu = 0$$
Applying the Lorenz gauge $\partial_\mu A^\mu = 0$, the equations simplify to $\square A^\nu = 0$, which are equivalent to the classical Maxwell equations in vacuum.

#### Q17. Dyson Chronological Series
Iteratively expanding $U(t, t_0)$:
$$U_1(t, t_0) = -\frac{i}{\hbar} \int_{t_0}^t H_I(t_1) dt_1$$
$$U_2(t, t_0) = \left( -\frac{i}{\hbar} \right)^2 \int_{t_0}^t dt_1 \int_{t_0}^{t_1} dt_2 H_I(t_1) H_I(t_2)$$
The domain of integration for $U_2$ is a triangle defined by $t_0 \le t_2 \le t_1 \le t$. 

```
 t1 ^
    |*
    |**
    |***  Integration region for U2 (triangle)
    |****
    +------------------> t2
   t0                  t
```

We can write this over a symmetric square region $[t_0, t] \times [t_0, t]$ by dividing it into two triangles, $t_1 > t_2$ and $t_2 > t_1$:
$$\int_{t_0}^t dt_1 \int_{t_0}^{t_1} dt_2 H_I(t_1)H_I(t_2) = \frac{1}{2} \left[ \int_{t_0}^t dt_1 \int_{t_0}^{t_1} dt_2 H_I(t_1)H_I(t_2) + \int_{t_0}^t dt_2 \int_{t_0}^{t_2} dt_1 H_I(t_2)H_I(t_1) \right]$$
Using the Time-Ordering operator $P$, which places the operator with the later time on the left:
$$P\{H_I(t_1)H_I(t_2)\} = \begin{cases} H_I(t_1)H_I(t_2) & \text{if } t_1 > t_2 \\ H_I(t_2)H_I(t_1) & \text{if } t_2 > t_1 \end{cases}$$
This allows us to combine the integrals over the entire square domain:
$$U_2(t, t_0) = \frac{1}{2!} \left( -\frac{i}{\hbar} \right)^2 \int_{t_0}^t dt_1 \int_{t_0}^t dt_2 P\{H_I(t_1) H_I(t_2)\}$$

#### Q18. High-Energy Compton Scattering
* **Thomson Scattering** is classical, elastic scattering where the photon's energy is much less than the electron's rest mass ($E \ll m_e c^2$). There is no change in wavelength ($\Delta \lambda = 0$).
* **Compton Scattering** is quantum-mechanical scattering where $E \sim m_e c^2$. Conservation of relativistic 4-momentum yields the Compton relation:
  $$E' = \frac{E}{1 + \frac{E}{m_e c^2}(1 - \cos\theta)}$$
* **Relativistic Limit ($E \gg m_e c^2$):** For forward scattering ($\theta \approx 0$), $\cos\theta \approx 1 \implies E' \approx E$. For backward scattering ($\theta \approx \pi$), $\cos\theta \approx -1 \implies E' \approx \frac{m_e c^2}{2} \ll E$. 
* The Klein-Nishina cross-section indicates that at high energies, the cross-section is heavily suppressed for large angles and highly peaked in the forward direction ($\theta \to 0$), as the photon retains almost all of its energy only in forward collisions.

#### Q19. Rigorous Quantization of the Radiation Field
The vector potential $\mathbf{A}(\mathbf{r}, t)$ in a cavity of volume $V$ is:
$$\mathbf{A}(\mathbf{r}, t) = \sum_{\mathbf{k}, \alpha} \sqrt{\frac{\hbar}{2\epsilon_0 \omega_k V}} \hat{e}_{\mathbf{k}, \alpha} \left[ a_{\mathbf{k}, \alpha}(t) e^{i\mathbf{k}\cdot\mathbf{r}} + a_{\mathbf{k}, \alpha}^\dagger(t) e^{-i\mathbf{k}\cdot\mathbf{r}} \right]$$
1. **Coulomb Gauge:** $\nabla \cdot \mathbf{A} = 0 \implies \mathbf{k} \cdot \hat{e}_{\mathbf{k}, \alpha} = 0$, restricting $\alpha$ to two transverse polarization states.
2. The Hamiltonian of the system is derived from the field energy:
   $$H = \frac{1}{2} \int \left( \epsilon_0 \mathbf{E}^2 + \frac{1}{\mu_0} \mathbf{B}^2 \right) d^3r$$
   Substituting $\mathbf{E} = -\frac{\partial \mathbf{A}}{\partial t}$ and $\mathbf{B} = \nabla \times \mathbf{A}$:
   $$H = \sum_{\mathbf{k}, \alpha} \hbar \omega_k \left( a_{\mathbf{k}, \alpha}^\dagger a_{\mathbf{k}, \alpha} + \frac{1}{2} \right)$$
3. By imposing the canonical commutation relation $[q, p] = i\hbar$ on the equivalent harmonic oscillator coordinates, we obtain:
   $$[a_{\mathbf{k}, \alpha}, a_{\mathbf{k}', \alpha'}^\dagger] = \delta_{\mathbf{k}\mathbf{k}'}\delta_{\alpha\alpha'}$$

#### Q20. Microcausality and the Klein-Gordon Propagator
Let us compute $i\Delta(x-y) = [\phi(x), \phi(y)]$:
$$[\phi(x), \phi(y)] = \int \frac{d^3k}{(2\pi)^3 2\omega_k} \left( e^{-ik\cdot(x-y)} - e^{ik\cdot(x-y)} \right)$$
Let $r^2 = (\mathbf{x}-\mathbf{y})^2$ and $t = x^0 - y^0$. For a space-like interval, there exists a Lorentz frame where the time separation is zero ($t = 0$). Substituting $t=0$ into the commutator:
$$[\phi(\mathbf{x}, 0), \phi(\mathbf{y}, 0)] = \int \frac{d^3k}{(2\pi)^3 2\omega_k} \left( e^{i\mathbf{k}\cdot(\mathbf{x}-\mathbf{y})} - e^{-i\mathbf{k}\cdot(\mathbf{x}-\mathbf{y})} \right)$$
Changing the variable of integration $\mathbf{k} \rightarrow -\mathbf{k}$ in the second term:
$$\int \frac{d^3k}{(2\pi)^3 2\omega_k} e^{-i\mathbf{k}\cdot(\mathbf{x}-\mathbf{y})} = \int \frac{d^3k}{(2\pi)^3 2\omega_k} e^{i\mathbf{k}\cdot(\mathbf{x}-\mathbf{y})}$$
This causes the two terms to cancel exactly:
$$[\phi(x), \phi(y)] = 0 \quad \text{for} \quad (x-y)^2 < 0$$
Since any measurement at $x$ commutes with any measurement at $y$ for space-like separations, no physical measurement can causally influence the other, preserving microcausality in QED.

---

### Section 4: Challenge Questions

#### Q21. Design of a Precision Compton Polarimeter
1. **Scatterer Selection:** A low-$Z$ material (such as Beryllium, $Z=4$) should be chosen. Low-$Z$ minimizes the competing photoelectric effect (which scales as $Z^5$) and pair production (which scales as $Z^2$). The target must be thin to prevent multiple scattering events that would randomize the polarization information.
2. **Detector Geometry:** High-purity Germanium (HPGe) or segmented silicon detectors should be placed in an azimuthal ring at a scattering angle of $\theta \approx 90^\circ$ (where the polarization sensitivity factor $2\sin^2\theta \cos^2\phi$ is maximized).
3. **Calibration & Background Reduction:** To isolate the Compton signal from the $e^+e^-$ pair production background, a coincidence circuit can be implemented to detect the scattered photon and the recoil electron simultaneously.

#### Q22. Vacuum Polarization and the Schwinger Limit
1. **Feynman Diagrams for $\gamma\gamma$ Scattering:**
   The process is represented by a fermion box loop containing four vertices:
   $$\text{Incoming Photons } (k_1, k_2) \rightarrow \text{ Electron Loop } (e^-, e^+) \rightarrow \text{ Outgoing Photons } (k_3, k_4)$$
2. **Schwinger Limit Calculation:**
   $$E_c = \frac{m_e^2 c^3}{e \hbar}$$
   Substituting the physical constants:
   * $m_e = 9.109 \times 10^{-31} \text{ kg}$
   * $c = 2.998 \times 10^8 \text{ m/s}$
   * $e = 1.602 \times 10^{-19} \text{ C}$
   * $\hbar = 1.054 \times 10^{-34} \text{ J s}$
   $$E_c \approx 1.32 \times 10^{18} \text{ V/m}$$
3. **Experimental Verification:** Extremely high-intensity petawatt/exawatt laser systems (like the Extreme Light Infrastructure, ELI) focus ultra-short pulses to achieve field intensities approaching $10^{18} \text{ V/m}$, allowing researchers to observe vacuum birefringence and real photon-photon scattering.

#### Q23. Gauge Invariance of the S-Matrix
Let the transition amplitude be:
$$\mathcal{M} = \int d^4x \, j^\mu(x) A_\mu(x)$$
where $j^\mu(x) = e \bar{\psi}\gamma^\mu \psi$ is the conserved Dirac transition current satisfying $\partial_\mu j^\mu = 0$.

Under the gauge transformation $A_\mu \rightarrow A_\mu + \partial_\mu \Lambda$:
$$\mathcal{M} \rightarrow \int d^4x \, j^\mu(x) [A_\mu(x) + \partial_\mu \Lambda(x)] = \mathcal{M} + \int d^4x \, j^\mu(x) \partial_\mu \Lambda(x)$$
Integrating the second term by parts:
$$\int d^4x \, j^\mu(x) \partial_\mu \Lambda(x) = \left[ j^\mu(x) \Lambda(x) \right]_{-\infty}^\infty - \int d^4x \, [\partial_\mu j^\mu(x)] \Lambda(x)$$
* The boundary term vanishes because $\Lambda(x) \rightarrow 0$ as $t \rightarrow \pm\infty$.
* The second term vanishes due to charge conservation ($\partial_\mu j^\mu = 0$).

Therefore, the scattering amplitude remains strictly invariant ($\mathcal{M}' = \mathcal{M}$), proving the gauge invariance of physical observables in QED.