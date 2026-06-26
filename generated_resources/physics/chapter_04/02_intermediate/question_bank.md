## Advanced Quantum Mechanics (Unit IV: Radiation Theory & Field Quantization)
---

### Section A: Multiple Choice Questions (1 Mark Each)

#### Q1. Under the Coulomb gauge ($\nabla \cdot \mathbf{A} = 0$), which of the following commutation relations holds true between the momentum operator $\mathbf{p}$ and the vector potential $\mathbf{A}$?
A) $[\mathbf{p}, \mathbf{A}] = i\hbar$  
B) $\mathbf{p} \cdot \mathbf{A} - \mathbf{A} \cdot \mathbf{p} = 0$  
C) $[\mathbf{p}, \mathbf{A}] = -i\hbar \nabla \cdot \mathbf{A}$  
D) $\mathbf{p} \times \mathbf{A} = \mathbf{A} \times \mathbf{p}$

#### Q2. The Electric Dipole Approximation is valid when the wavelength $\lambda$ of the incident radiation is:
A) Much smaller than the atomic dimension ($a_0$)  
B) Comparable to the atomic dimension ($a_0$)  
C) Much larger than the atomic dimension ($a_0$)  
D) Independent of the atomic dimension

#### Q3. In the quantization of the electromagnetic field, the Hamiltonian of the radiation field $H_r$ is equivalent to a system of:
A) Coupled anharmonic oscillators  
B) Uncoupled classical rotors  
C) Independent quantum harmonic oscillators  
D) Non-interacting free fermions

#### Q4. The classical electron radius $r_0$ is defined in the text as:
A) $r_0 = \frac{e^2}{4\pi \epsilon_0 m c^2}$  
B) $r_0 = \frac{e^2}{4\pi m}$  
C) $r_0 = \frac{e^2}{2m c^2}$  
D) $r_0 = \frac{4\pi e^2}{m c^2}$

#### Q5. The S-matrix is related to the time development operator $U(t, t_0)$ via which of the following limits?
A) $S = \lim_{t \to 0, t_0 \to 0} U(t, t_0)$  
B) $S = \lim_{t \to \infty, t_0 \to -\infty} U(t, t_0)$  
C) $S = \lim_{t \to \infty, t_0 \to 0} U(t, t_0)$  
D) $S = \lim_{t \to 0, t_0 \to -\infty} U(t, t_0)$

#### Q6. The unitarity of the scattering matrix ($S^\dagger S = I$) physically guarantees:
A) Conservation of charge  
B) Conservation of momentum  
C) Conservation of total transition probability  
D) Gauge invariance of the interaction

#### Q7. In Feynman diagrams, a solid line with an arrow pointing backwards in time (or against the direction of propagation) represents:
A) A physical electron  
B) A physical photon  
C) A positron (or propagation of negative energy state)  
D) A spinless Higgs boson

#### Q8. The total cross-section for classical Thomson scattering ($\sigma_T$) is given by:
A) $\sigma_T = \frac{8\pi}{3} r_0^2$  
B) $\sigma_T = \frac{4\pi}{3} r_0^2$  
C) $\sigma_T = r_0^2$  
D) $\sigma_T = 2\pi r_0^2$

#### Q9. For a quantized complex scalar field, the operator $\phi^{(+)}(x)$ physically represents:
A) Creation of a positron  
B) Annihilation of an electron (particle of charge $+e$)  
C) Creation of a photon  
D) Annihilation of a photon

#### Q10. Fermi's modified Lagrangian for the electromagnetic field is written as $L = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} - \frac{1}{2}(\partial_\mu A^\mu)^2$. The second term is added to:
A) Preserve explicit gauge invariance  
B) Make the Lagrangian density Lorentz invariant and manageable in the Lorenz gauge  
C) Eliminate the scalar potential  
D) Ensure the photon has a non-zero rest mass

---

### Section A: Answer Key
1. **B** (Since $\mathbf{p} = -i\hbar\nabla$, we have $[\mathbf{p}, \mathbf{A}]\psi = -i\hbar \nabla \cdot (\mathbf{A}\psi) + i\hbar \mathbf{A} \cdot \nabla \psi = -i\hbar (\nabla \cdot \mathbf{A})\psi$. In Coulomb gauge, $\nabla \cdot \mathbf{A} = 0$, so $\mathbf{p}\cdot\mathbf{A} = \mathbf{A}\cdot\mathbf{p}$).
2. **C** ($kr \ll 1 \implies \frac{2\pi r}{\lambda} \ll 1 \implies \lambda \gg r$, where $r \sim 10^{-10}\text{ m}$ is the atomic dimension).
3. **C** (The Hamiltonian simplifies to $H_r = \sum_\lambda \frac{1}{2}(P_\lambda^2 + \omega_\lambda^2 Q_\lambda^2)$).
4. **B** (Using the natural units convention $4\pi\epsilon_0 = 1$ and $c = 1$ in the text, $r_0 = \frac{e^2}{4\pi m}$).
5. **B** (The S-matrix maps asymptotic free states from the remote past $t_0 \to -\infty$ to the remote future $t \to +\infty$).
6. **C** (Unitarity implies $S^\dagger S = I$, conserving probability flux).
7. **C** (In Feynman-Stueckelberg interpretation, a backward-moving negative-energy fermion represents a forward-moving positive-energy antiparticle).
8. **A** ($\sigma_T = \frac{8\pi}{3} r_0^2$).
9. **B** (As defined in field quantization sections, $\phi^{(+)}$ contains annihilation operators for positive charge).
10. **B** (It breaks gauge invariance temporarily to allow quantization of all four components of $A_\mu$, but physical results remain gauge invariant).

---

### Section B: Short Answer Questions (2–3 Marks Each)

#### Q11. Explain why the term $\frac{q^2}{2m}\mathbf{A}^2$ in the interaction Hamiltonian is generally neglected in weak-field semi-classical transitions.
**Model Answer:**  
The interaction Hamiltonian of an electron in a radiation field is:
$$H' = \frac{q}{m}\mathbf{A}\cdot\mathbf{p} + \frac{q^2}{2m}\mathbf{A}^2$$
For weak electromagnetic fields (like typical stellar or laboratory light sources), the vector potential magnitude $|\mathbf{A}|$ is very small. Consequently, the quadratic term proportional to $\mathbf{A}^2$ is several orders of magnitude smaller than the linear term $\mathbf{A}\cdot\mathbf{p}$. Thus, it can be neglected as a higher-order perturbation, except in processes involving two-photon absorption/emission or intense laser fields.

#### Q12. Prove that under the Coulomb gauge condition, the vector potential commutes with the momentum operator: $[\mathbf{p}, \mathbf{A}] = 0$.
**Model Answer:**  
Let $\psi(\mathbf{r})$ be an arbitrary test wavefunction. 
$$[\mathbf{p}, \mathbf{A}]\psi = \mathbf{p} \cdot (\mathbf{A}\psi) - \mathbf{A} \cdot (\mathbf{p}\psi)$$
Using the representation $\mathbf{p} = -i\hbar\nabla$:
$$\mathbf{p} \cdot (\mathbf{A}\psi) = -i\hbar \nabla \cdot (\mathbf{A}\psi) = -i\hbar [(\nabla \cdot \mathbf{A})\psi + \mathbf{A} \cdot (\nabla\psi)]$$
$$\mathbf{A} \cdot (\mathbf{p}\psi) = -i\hbar \mathbf{A} \cdot (\nabla\psi)$$
Subtracting the two terms yields:
$$[\mathbf{p}, \mathbf{A}]\psi = -i\hbar (\nabla \cdot \mathbf{A})\psi$$
Since the Coulomb gauge enforces $\nabla \cdot \mathbf{A} = 0$, we obtain $[\mathbf{p}, \mathbf{A}] = 0$, proving that $\mathbf{p}\cdot\mathbf{A} = \mathbf{A}\cdot\mathbf{p}$.

#### Q13. State the Dipole Approximation. Under what physical conditions is it highly accurate?
**Model Answer:**  
The transition matrix elements involve phase factors of the form $e^{\pm i\mathbf{k}\cdot\mathbf{r}}$. The **Dipole Approximation** consists of expanding this exponential as:
$$e^{\pm i\mathbf{k}\cdot\mathbf{r}} = 1 \pm i\mathbf{k}\cdot\mathbf{r} - \frac{1}{2}(\mathbf{k}\cdot\mathbf{r})^2 + \dots \approx 1$$
This approximation is highly accurate when $k r \ll 1$. For optical transitions, the atomic radius $r \approx 10^{-10}\text{ m}$ and the wave number $k = \frac{2\pi}{\lambda} \approx 10^7\text{ m}^{-1}$, giving $\mathbf{k}\cdot\mathbf{r} \approx 10^{-3} \ll 1$. Thus, the spatial variation of the phase over atomic dimensions is negligible.

#### Q14. Show that the momentum matrix element $\langle s | \mathbf{p} | n \rangle$ can be written as $im\omega_{ns} \langle s | \mathbf{r} | n \rangle$.
**Model Answer:**  
Using the atomic Hamiltonian $H_a = \frac{\mathbf{p}^2}{2m} + V(\mathbf{r})$, we evaluate the commutator $[\mathbf{r}, H_a]$:
$$[\mathbf{r}, H_a] = \left[\mathbf{r}, \frac{\mathbf{p}^2}{2m}\right] = \frac{i\hbar}{m}\mathbf{p} \implies \mathbf{p} = \frac{m}{i\hbar}[\mathbf{r}, H_a]$$
Taking the matrix elements between eigenstates $|n\rangle$ and $|s\rangle$ of $H_a$ (where $H_a|n\rangle = E_n|n\rangle$):
$$\langle s | \mathbf{p} | n \rangle = \frac{m}{i\hbar} \langle s | (\mathbf{r}H_a - H_a\mathbf{r}) | n \rangle = \frac{m}{i\hbar}(E_n - E_s) \langle s | \mathbf{r} | n \rangle$$
Defining $\hbar\omega_{ns} = E_n - E_s$, we get:
$$\langle s | \mathbf{p} | n \rangle = \frac{m}{i\hbar}(\hbar\omega_{ns}) \langle s | \mathbf{r} | n \rangle = im\omega_{ns} \langle s | \mathbf{r} | n \rangle$$

#### Q15. Define the time evolution operator $U(t, t_0)$ (U-matrix) and write down its primary differential equation.
**Model Answer:**  
The $U\text{-matrix}$ is a unitary operator that develops state vectors in the interaction picture over time:
$$|\Psi_I(t)\rangle = U(t, t_0)|\Psi_I(t_0)\rangle$$
By substituting this into the interaction picture Schrödinger equation, we find that it satisfies:
$$i\hbar \frac{\partial}{\partial t} U(t, t_0) = H_I(t) U(t, t_0)$$
subject to the initial condition $U(t_0, t_0) = I$.

#### Q16. Write down the Dyson series expansion for $U(t, t_0)$ up to the second-order term.
**Model Answer:**  
Integrating the differential equation for $U(t, t_0)$ iteratively yields the Dyson series:
$$U(t, t_0) = I + U_1(t, t_0) + U_2(t, t_0) + \dots$$
where:
$$U_1(t, t_0) = \left(-\frac{i}{\hbar}\right) \int_{t_0}^t H_I(t_1) dt_1$$
$$U_2(t, t_0) = \left(-\frac{i}{\hbar}\right)^2 \int_{t_0}^t dt_2 \int_{t_0}^{t_2} H_I(t_2) H_I(t_1) dt_1$$

#### Q17. State the physical meaning of the Dyson Chronological Time-Ordering Operator $P$.
**Model Answer:**  
The chronological operator $P$ rearranges a product of time-dependent operators so that their time arguments increase from right to left:
$$P\{H(t_1)H(t_2)\} = \begin{cases} 
H(t_1)H(t_2) & \text{if } t_1 > t_2 \\ 
H(t_2)H(t_1) & \text{if } t_2 > t_1 
\end{cases}$$
This allows us to simplify the limits of integration over multi-dimensional spaces to a simple symmetric form:
$$U_n(t, t_0) = \frac{1}{n!} \left(-\frac{i}{\hbar}\right)^n \int_{t_0}^t dt_1 \dots \int_{t_0}^t dt_n P\{H_I(t_1)\dots H_I(t_n)\}$$

#### Q18. Sketch the basic Feynman diagrams representing: (a) Emission of a photon by an electron, and (b) Absorption of a photon by an electron.
**Model Answer:**

```mermaid
graph LR
    subgraph (a) Photon Emission
    e1(e-) -->|p| V1(Vertex)
    V1 -->|p'| e2(e-)
    V1 ~~~ photon1((Wavy Line))
    V1 -->|k| photon1
    end

    subgraph (b) Photon Absorption
    photon2((Wavy Line)) -->|k| V2(Vertex)
    e3(e-) -->|p| V2
    V2 -->|p'| e4(e-)
    end
```
*(In Feynman notation: Solid straight lines with arrows denote fermions; wavy lines denote photons. Points where they meet are interaction vertices.)*

#### Q19. What is the Klein-Nishina formula? Under what conditions does it simplify to the classical Thomson scattering formula?
**Model Answer:**  
The Klein-Nishina formula describes the relativistic differential cross-section of a photon scattering off a free electron. At low photon energies where the photon energy is much smaller than the electron rest mass energy ($\hbar\omega \ll m_e c^2$), quantum mechanical recoil is negligible ($\omega \approx \omega'$). Under this classical limit, the Klein-Nishina cross-section reduces exactly to the Thomson scattering cross-section:
$$\frac{d\sigma}{d\Omega} = \frac{r_0^2}{2}(1 + \cos^2\theta)$$

#### Q20. Write down the field operator expressions for a quantized complex Klein-Gordon field, explaining what the terms represent.
**Model Answer:**  
The quantized field operator $\phi(x)$ is expressed as:
$$\phi(x) = \phi^{(+)}(x) + \phi^{(-)}(x) = \frac{1}{\sqrt{V}}\sum_{\mathbf{k}}\frac{1}{\sqrt{2\omega_{\mathbf{k}}}}\left[ a(\mathbf{k})e^{-ik\cdot x} + b^\dagger(\mathbf{k})e^{ik\cdot x} \right]$$
- $a(\mathbf{k})$ is the annihilation operator for a particle of charge $+e$.
- $b^\dagger(\mathbf{k})$ is the creation operator for an antiparticle of charge $-e$.
- $e^{\pm ik\cdot x}$ represents relativistic plane waves.

---

### Section C: Long Answer Questions (5 Marks Each)

#### Q21. Derive the interaction Hamiltonian $H'$ for a non-relativistic electron of charge $q$ moving in an electromagnetic field described by vector potential $\mathbf{A}$, under the Coulomb gauge.
**Model Answer:**  
1. **The Classical Hamiltonian:** For a particle of mass $m$ and charge $q$ in an EM field, we perform the minimal coupling replacement $\mathbf{p} \to \mathbf{p} + q\mathbf{A}$. The Hamiltonian is:
   $$H = \frac{1}{2m}(\mathbf{p} + q\mathbf{A})^2 + V(\mathbf{r}) + H_r$$
2. **Expanding the Kinetic Term:**
   $$(\mathbf{p} + q\mathbf{A})^2 = (\mathbf{p} + q\mathbf{A})\cdot(\mathbf{p} + q\mathbf{A}) = \mathbf{p}^2 + q(\mathbf{p}\cdot\mathbf{A} + \mathbf{A}\cdot\mathbf{p}) + q^2\mathbf{A}^2$$
3. **Applying Quantum Mechanics Operators:** In position representation, the term $\mathbf{p}\cdot\mathbf{A}$ acts on a wavefunction $\psi$:
   $$\mathbf{p}\cdot(\mathbf{A}\psi) = -i\hbar \nabla \cdot (\mathbf{A}\psi) = -i\hbar (\nabla \cdot \mathbf{A})\psi - i\hbar \mathbf{A}\cdot\nabla\psi = -i\hbar(\nabla\cdot\mathbf{A})\psi + \mathbf{A}\cdot\mathbf{p}\psi$$
4. **Imposing Coulomb Gauge:** Under Coulomb gauge, $\nabla \cdot \mathbf{A} = 0$. Consequently:
   $$\mathbf{p}\cdot\mathbf{A} = \mathbf{A}\cdot\mathbf{p}$$
   This simplifies the expansion to:
   $$(\mathbf{p} + q\mathbf{A})^2 = \mathbf{p}^2 + 2q\mathbf{A}\cdot\mathbf{p} + q^2\mathbf{A}^2$$
5. **Structuring the Full Hamiltonian:**
   $$H = \left[ \frac{\mathbf{p}^2}{2m} + V(\mathbf{r}) \right] + H_r + \left[ \frac{q}{m}\mathbf{A}\cdot\mathbf{p} + \frac{q^2}{2m}\mathbf{A}^2 \right]$$
   We identify:
   - Atomic Hamiltonian: $H_a = \frac{\mathbf{p}^2}{2m} + V(\mathbf{r})$
   - Free Radiation Field Hamiltonian: $H_r$
   - Interaction Hamiltonian: $H' = \frac{q}{m}\mathbf{A}\cdot\mathbf{p} + \frac{q^2}{2m}\mathbf{A}^2$
   For weak fields, we neglect the $\mathbf{A}^2$ term, yielding:
   $$H' \approx \frac{q}{m}\mathbf{A}\cdot\mathbf{p}$$

---

#### Q22. Explain in detail the quantization procedure of a free electromagnetic field inside a cavity of volume $V$, obtaining the expression for the field energy.
**Model Answer:**  
1. **Classical Field Equations:** In a charge-free, current-free cavity, the vector potential satisfies the 3D wave equation:
   $$\nabla^2 \mathbf{A} - \frac{1}{c^2}\frac{\partial^2 \mathbf{A}}{\partial t^2} = 0$$
2. **Separation of Variables:** We expand $\mathbf{A}(\mathbf{r}, t)$ in terms of orthogonal spatial modes $\mathbf{A}_\lambda(\mathbf{r})$ and time amplitude variables $q_\lambda(t)$:
   $$\mathbf{A}(\mathbf{r}, t) = \sum_\lambda \mathbf{A}_\lambda(\mathbf{r}) q_\lambda(t)$$
   Applying boundary conditions, the spatial modes are normalized over volume $V$:
   $$\int_V \mathbf{A}_\lambda \cdot \mathbf{A}_\mu d\tau = V \delta_{\lambda\mu}$$
3. **Defining Canonical Variables:** We introduce real, canonical variables $Q_\lambda(t)$ and $P_\lambda(t)$ defined by:
   $$Q_\lambda(t) = \sqrt{\epsilon_0 V}\left( q_\lambda + q_\lambda^* \right)$$
   $$P_\lambda(t) = -i\omega_\lambda \sqrt{\epsilon_0 V}\left( q_\lambda - q_\lambda^* \right) = \dot{Q}_\lambda(t)$$
4. **Quantization Postulate:** We elevate $Q_\lambda$ and $P_\lambda$ to quantum operators satisfying the canonical commutation relations:
   $$[Q_\lambda, P_\mu] = i\hbar \delta_{\lambda\mu}, \quad [Q_\lambda, Q_\mu] = 0, \quad [P_\lambda, P_\mu] = 0$$
5. **Hamiltonian formulation:** The total field energy (Hamiltonian $H_r$) is:
   $$H_r = \frac{1}{2}\int_V \left( \epsilon_0 \mathbf{E}^2 + \mu_0 \mathbf{H}^2 \right) d\tau$$
   Substituting the mode expansion leads to:
   $$H_r = \sum_\lambda \frac{1}{2}\left( P_\lambda^2 + \omega_\lambda^2 Q_\lambda^2 \right)$$
   This expression matches the Hamiltonian of a set of independent quantum harmonic oscillators.
6. **Energy Eigenvalues:** The eigenvalues of the system are:
   $$E = \sum_\lambda \left( n_\lambda + \frac{1}{2} \right)\hbar \omega_\lambda, \quad n_\lambda \in \{0, 1, 2, \dots\}$$

---

#### Q23. Starting from the differential equation for $U(t, t_0)$, derive the first-order and second-order transition amplitudes, and discuss how they lead to the S-matrix Dyson series.
**Model Answer:**  
1. **The Integral Equation:** The evolution equation is:
   $$i\hbar \frac{\partial}{\partial t} U(t, t_0) = H_I(t) U(t, t_0)$$
   Integrating both sides from $t_0$ to $t$:
   $$U(t, t_0) = I - \frac{i}{\hbar} \int_{t_0}^t H_I(t_1) U(t_1, t_0) dt_1$$
2. **Iterative Solution:** We substitute $U(t_1, t_0)$ back into the integral on the right hand side iteratively:
   $$U(t, t_0) = I - \frac{i}{\hbar} \int_{t_0}^t H_I(t_1) \left[ I - \frac{i}{\hbar} \int_{t_0}^{t_1} H_I(t_2) U(t_2, t_0) dt_2 \right] dt_1$$
3. **Identifying First & Second-Order Terms:**
   - First-order term $U_1(t, t_0)$:
     $$U_1(t, t_0) = \left( -\frac{i}{\hbar} \right) \int_{t_0}^t H_I(t_1) dt_1$$
   - Second-order term $U_2(t, t_0)$:
     $$U_2(t, t_0) = \left( -\frac{i}{\hbar} \right)^2 \int_{t_0}^t dt_1 \int_{t_0}^{t_1} H_I(t_1) H_I(t_2) dt_2$$
4. **S-Matrix Formulation:** The S-matrix is defined in the limits $t_0 \to -\infty$ and $t \to +\infty$:
   $$S = U(+\infty, -\infty) = \sum_{n=0}^\infty S^{(n)}$$
   Using the chronological operator $P$, we can express any arbitrary $n$-th order term as:
   $$S^{(n)} = \frac{1}{n!} \left( -\frac{i}{\hbar} \right)^n \int_{-\infty}^\infty dt_1 \dots \int_{-\infty}^\infty dt_n P\{H_I(t_1) \dots H_I(t_n)\}$$
   This expansion is the foundation of perturbation theory in QED.

---

#### Q24. Derive the differential scattering cross-section for the scattering of unpolarized electromagnetic waves by a free electron (Thomson Scattering).
**Model Answer:**  
1. **Classical Power Radiated:** An electric wave $\mathbf{E} = \hat{\epsilon} E_0 \cos(\mathbf{k}\cdot\mathbf{r} - \omega t)$ exerts a force on a free electron of mass $m$, producing acceleration:
   $$\mathbf{a} = \frac{e\mathbf{E}}{m} = \frac{e E_0 \hat{\epsilon}}{m} \cos(\omega t)$$
2. **Larmor Formula for Radiated Power:** The average power radiated per unit solid angle $d\Omega$ is:
   $$\frac{dP}{d\Omega} = \frac{e^2 \langle a^2 \rangle \sin^2 \phi}{4\pi c^3}$$
   where $\phi$ is the angle between the acceleration direction (polarization $\hat{\epsilon}$) and the scattering direction.
3. **Cross-Section Definition:** The differential cross-section $\frac{d\sigma}{d\Omega}$ is the ratio of average radiated power per unit solid angle to the incident energy flux ($I_0 = c \epsilon_0 E_0^2$):
   $$\left( \frac{d\sigma}{d\Omega} \right)_{\text{polarized}} = r_0^2 \sin^2\phi$$
   where $r_0 = \frac{e^2}{4\pi\epsilon_0 mc^2}$ is the classical electron radius.
4. **Accounting for Geometry:** Let $\theta$ be the scattering angle between incident vector $\mathbf{k}$ and scattered vector $\mathbf{k}'$. If we project the polarization vectors, we get:
   - For perpendicular polarization: $\sin^2\phi_1 = 1$
   - For parallel polarization: $\sin^2\phi_2 = \cos^2\theta$
5. **Averaging for Unpolarized Incident Beam:** For unpolarized light, we take the average of these two polarization states:
   $$\left( \frac{d\sigma}{d\Omega} \right)_{\text{unpol}} = \frac{1}{2} \left[ \left( \frac{d\sigma}{d\Omega} \right)_1 + \left( \frac{d\sigma}{d\Omega} \right)_2 \right] = \frac{r_0^2}{2}(1 + \cos^2\theta)$$

---

#### Q25. State the Feynman Rules for calculating transition matrix elements of Quantum Electrodynamics (QED) processes in momentum space.
**Model Answer:**  
To calculate the $S$-matrix element for any physical process in QED, we construct the algebraic expression from its Feynman diagram using these rules:

| Component | Visual Representation | Algebraic Multiplier / Factor |
| :--- | :--- | :--- |
| **QED Vertex** | Vertex point joining fermion & photon lines | $-ie \gamma^\mu$ |
| **Internal Fermion Line** | Line with arrow & momentum $p$ | $i S_F(p) = \frac{i}{\gamma \cdot p - m + i\epsilon}$ |
| **Internal Photon Line** | Wavy line with momentum $k$ | $i D_{F}^{\mu\nu}(k) = \frac{-i g^{\mu\nu}}{k^2 + i\epsilon}$ |
| **Incoming Electron** | Solid line entering vertex | $u(p, s)$ |
| **Outgoing Electron** | Solid line leaving vertex | $\bar{u}(p', s')$ |
| **Incoming Photon** | Wavy line entering vertex | $\epsilon_\mu(k, \lambda)$ |
| **Outgoing Photon** | Wavy line leaving vertex | $\epsilon_\mu^*(k', \lambda')$ |
| **Closed Fermion Loop** | Loop of solid lines | Take the trace over Dirac indices and multiply by $(-1)$ |

---

### Section D: HOTS (Higher Order Thinking Skills) Questions

#### Q26. Why does Fermi's Lagrangian term $-\frac{1}{2}(\partial_\mu A^\mu)^2$ break gauge invariance? How do we reconcile this with the fact that QED predictions are gauge-invariant?
**Model Answer:**  
Under a gauge transformation of the second kind, the vector four-potential transforms as:
$$A_\mu \to A'_\mu = A_\mu - \partial_\mu \chi$$
The standard electromagnetic field tensor term $F_{\mu\nu}F^{\mu\nu}$ is completely gauge invariant because $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ remains unchanged. 

However, the Lorenz gauge-fixing term behaves as:
$$\partial_\mu A^\mu \to \partial_\mu A'^\mu = \partial_\mu A^\mu - \partial_\mu \partial^\mu \chi = \partial_\mu A^\mu - \square \chi$$
Since $\square \chi$ is not generally zero, the term $-\frac{1}{2}(\partial_\mu A^\mu)^2$ changes under this transformation, breaking explicit gauge invariance in the Lagrangian.

**Reconciliation:**  
This term is introduced to allow the canonical quantization of the scalar component of the electromagnetic field (which is otherwise impossible due to the vanishing of its conjugate momentum). To restore physical gauge invariance, we must restrict our physical Hilbert space to states $|\Psi\rangle$ that satisfy the **Gupta-Bleuler condition**:
$$\partial_\mu A^{\mu (+)} |\Psi\rangle = 0$$
This condition ensures that the contribution of unphysical scalar and longitudinal photons cancels out in any physical observable, ensuring that all physical cross-sections remain gauge invariant.

---

#### Q27. Analyze Compton scattering using Mandelstam variables. Explain how crossing symmetry relates the amplitude of Compton scattering to Electron-Positron Annihilation ($e^- + e^+ \to \gamma + \gamma$).
**Model Answer:**  
Let the process of Compton scattering be:
$$e^-(q) + \gamma(k) \to e^-(q') + \gamma(k')$$
We define the Mandelstam variables:
- $s = (q + k)^2$ (square of center-of-mass energy)
- $t = (q - q')^2$ (square of momentum transfer)
- $u = (q - k')^2$

The scattering amplitude matrix element $M_{\mu\nu}$ contains a photon propagator with poles at $s = m^2$ and $u = m^2$ corresponding to the $s$-channel and $t$-channel diagrams.

```mermaid
graph TD
    subgraph s-channel (Compton)
    e_in1(e-) --> V1(Vertex)
    g_in1(gamma) --> V1
    V1 -->|Intermediate e-| V2(Vertex)
    V2 --> e_out1(e-)
    V2 --> g_out1(gamma)
    end
    
    subgraph t-channel (Annihilation)
    e_in2(e-) --> V3(Vertex)
    pos_in2(e+) --> V3
    V3 -->|Intermediate Photon| V4(Vertex)
    V4 --> g_out2a(gamma)
    V4 --> g_out2b(gamma)
    end
```

**Crossing Symmetry Relationship:**  
Crossing symmetry states that the S-matrix element for any process involving a particle with momentum $p$ is equivalent to a process involving its antiparticle with momentum $-p$. 
By applying this to Compton scattering, we can swap the incoming photon with the outgoing electron:
$$\gamma(k) \to \gamma(-k') \quad \text{and} \quad e^-(q') \to e^+(-q')$$
This mathematical transformation changes the Compton scattering amplitude into the amplitude for electron-positron annihilation:
$$e^-(q) + e^+(-q') \to \gamma(-k) + \gamma(k')$$
This demonstrates that Compton scattering and pair annihilation are different physical channels of the same underlying quantum field amplitude.

---

#### Q28. A quantum field theorist quantizes a scalar field $\phi$. Under what mathematical conditions does this field represent (a) strictly neutral particles, and (b) charged particles? Prove your assertion using the charge operator.
**Model Answer:**  
1. **Assertion:**  
   - A **Hermitian scalar field** ($\phi = \phi^\dagger$) describes strictly **neutral** spinless particles.
   - A **Non-Hermitian (complex) scalar field** ($\phi \neq \phi^\dagger$) describes **charged** spinless particles (with distinct antiparticles of opposite charge).

2. **Mathematical Proof:**  
   The Lagrangian density for a complex scalar field is:
   $$\mathcal{L} = \partial_\mu \phi^\dagger \partial^\mu \phi - m^2 \phi^\dagger \phi$$
   This Lagrangian is invariant under the global $U(1)$ phase transformation:
   $$\phi \to e^{-i\alpha}\phi, \quad \phi^\dagger \to e^{i\alpha}\phi^\dagger$$
   According to Noether's Theorem, this symmetry leads to a conserved current:
   $$j^\mu = i \left( \phi^\dagger \partial^\mu \phi - (\partial^\mu \phi^\dagger)\phi \right)$$
   The conserved charge $Q$ is the spatial integral of $j^0$:
   $$Q = \int d^3x \, j^0 = i \int d^3x \left( \phi^\dagger \dot{\phi} - \dot{\phi}^\dagger \phi \right)$$
   Substituting the quantized field operators:
   $$\phi(x) = \sum_{\mathbf{k}} \frac{1}{\sqrt{2V\omega_{\mathbf{k}}}} \left( a_{\mathbf{k}}e^{-ik\cdot x} + b^\dagger_{\mathbf{k}}e^{ik\cdot x} \right)$$
   into the charge operator expression yields:
   $$Q = q \sum_{\mathbf{k}} \left( a^\dagger_{\mathbf{k}}a_{\mathbf{k}} - b^\dagger_{\mathbf{k}}b_{\mathbf{k}} \right) = q \sum_{\mathbf{k}} \left( N^+(\mathbf{k}) - N^-(\mathbf{k}) \right)$$
   This shows that the field contains two types of quanta: particles of charge $+q$ (counted by $N^+$) and antiparticles of charge $-q$ (counted by $N^-$).

   If the field is Hermitian ($\phi = \phi^\dagger$), then $a_{\mathbf{k}} = b_{\mathbf{k}}$. Substituting this into the charge operator gives:
   $$Q = q \sum_{\mathbf{k}} \left( a^\dagger_{\mathbf{k}}a_{\mathbf{k}} - a^\dagger_{\mathbf{k}}a_{\mathbf{k}} \right) = 0$$
   This proves that a real/Hermitian scalar field carries zero net charge, representing strictly neutral particles.