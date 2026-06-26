Here is a moderate-level multiple-choice quiz based on the provided Advanced Quantum Mechanics Unit 4 material.

---

### Question 1
In the semi-classical theory of radiation, the interaction Hamiltonian $H'$ for a non-relativistic electron of charge $q$ is simplified under the Coulomb gauge. What is the mathematical relation between the momentum operator $\mathbf{p}$ and the vector potential $\mathbf{A}$ in this gauge?

A. $\mathbf{A} \cdot \mathbf{p} = -\mathbf{p} \cdot \mathbf{A}$
B. $\mathbf{A} \cdot \mathbf{p} = \mathbf{p} \cdot \mathbf{A}$
C. $\mathbf{A} \cdot \mathbf{p} = \mathbf{p} \cdot \mathbf{A} + i\hbar$
D. $\mathbf{A} \cdot \mathbf{p} = 0$

**Correct Answer:** B
**Explanation:** Under the Coulomb gauge, we choose $\nabla \cdot \mathbf{A} = 0$. Since the momentum operator is defined as $\mathbf{p} = -i\hbar\nabla$, the commutator acting on a test function $\psi$ is:
$$[\mathbf{p}, \mathbf{A}]\psi = -i\hbar \nabla \cdot (\mathbf{A}\psi) + i\hbar \mathbf{A} \cdot \nabla\psi = -i\hbar(\nabla \cdot \mathbf{A})\psi = 0$$
This demonstrates that the operators commute, meaning $\mathbf{A} \cdot \mathbf{p} = \mathbf{p} \cdot \mathbf{A}$.

---

### Question 2
During transitions in an atomic system induced by an electromagnetic radiation field, the dipole approximation is commonly used. Under this approximation, what is the value of the spatial phase factor $\exp(\pm i\mathbf{k}\cdot\mathbf{r})$?

A. $\exp(\pm i\mathbf{k}\cdot\mathbf{r}) \approx 0$
B. $\exp(\pm i\mathbf{k}\cdot\mathbf{r}) \approx 1$
C. $\exp(\pm i\mathbf{k}\cdot\mathbf{r}) \approx \pm i\mathbf{k}\cdot\mathbf{r}$
D. $\exp(\pm i\mathbf{k}\cdot\mathbf{r}) \approx 1 \pm i\mathbf{k}\cdot\mathbf{r}$

**Correct Answer:** B
**Explanation:** Atomic dimensions are of the order of $10^{-10}\text{ m}$ (about $1\text{ \AA}$), whereas for optical wavelengths, the wave vector magnitude is $k \sim 10^{5}\text{ cm}^{-1} = 10^{7}\text{ m}^{-1}$. Consequently, the product $kr \sim 10^{-3} \ll 1$. Applying the Taylor expansion:
$$\exp(\pm i\mathbf{k}\cdot\mathbf{r}) = 1 \pm i\mathbf{k}\cdot\mathbf{r} - \frac{1}{2}(\mathbf{k}\cdot\mathbf{r})^2 + \dots$$
Because $kr \ll 1$, we can neglect the higher-order spatial terms, yielding $\exp(\pm i\mathbf{k}\cdot\mathbf{r}) \approx 1$.

---

### Question 3
When the electromagnetic radiation field is quantized, the total energy Hamiltonian $H_r$ of the radiation field is expressed in terms of the photon number operator. What are the energy eigenvalues of this Hamiltonian for a given mode $\lambda$?

A. $E_\lambda = n_\lambda \hbar\omega_\lambda$
B. $E_\lambda = \left(n_\lambda + \frac{1}{2}\right)\hbar\omega_\lambda$
C. $E_\lambda = \frac{1}{2}n_\lambda \hbar\omega_\lambda$
D. $E_\lambda = \left(2n_\lambda + 1\right)\hbar\omega_\lambda$

**Correct Answer:** B
**Explanation:** By defining the canonical coordinates $Q_\lambda$ and $P_\lambda$, the Hamiltonian for each mode behaves like a quantum harmonic oscillator:
$$H_\lambda = \frac{1}{2}\left(P_\lambda^2 + \omega_\lambda^2 Q_\lambda^2\right)$$
Upon introducing the creation and annihilation operators $a^\dagger_\lambda$ and $a_\lambda$, the Hamiltonian becomes:
$$H_r = \sum_{\lambda} \frac{1}{2}\hbar\omega_\lambda \left(a_\lambda^\dagger a_\lambda + a_\lambda a_\lambda^\dagger\right) = \sum_{\lambda} \left(a_\lambda^\dagger a_\lambda + \frac{1}{2}\right)\hbar\omega_\lambda$$
The eigenvalues are therefore $\sum_{\lambda} \left(n_\lambda + \frac{1}{2}\right)\hbar\omega_\lambda$, where $n_\lambda = 0, 1, 2, \dots$ represents the number of photons in mode $\lambda$.

---

### Question 4
In Quantum Electrodynamics (QED) Feynman diagrams, a vertex represents the local interaction where a photon and a charged fermion meet. According to Feynman rules, what mathematical factor is assigned to each QED vertex?

A. $ie\gamma^\mu$
B. $-ie\gamma^\mu$
C. $\frac{i}{\gamma^\mu}$
D. $e^2\gamma^\mu$

**Correct Answer:** A
**Explanation:** Based on the Feynman rules for QED (as outlined on page 14), each basic vertex representing the coupling of a fermion line with a photon line corresponds to the Dirac matrix element multiplied by the coupling constant, written as $ie\gamma^\mu$ (or $-ie\gamma^\mu$ depending on the charge convention).

---

### Question 5
For a free, unpolarized electron, the classical total Thomson scattering cross-section ($\sigma_T$) is related to the classical electron radius $r_0$ by which of the following formulas?

A. $\sigma_T = \frac{4\pi}{3} r_0^2$
B. $\sigma_T = 2\pi r_0^2$
C. $\sigma_T = \frac{8\pi}{3} r_0^2$
D. $\sigma_T = \frac{8\pi}{3} r_0$

**Correct Answer:** C
**Explanation:** The differential scattering cross-section for unpolarized radiation is:
$$\sigma(\theta) = \frac{r_0^2}{2}(1 + \cos^2\theta)$$
To find the total scattering cross-section $\sigma_T$, we integrate this expression over the entire solid angle $d\Omega = 2\pi \sin\theta d\theta$:
$$\sigma_T = \int \sigma(\theta) d\Omega = \frac{r_0^2}{2} \int_{0}^{\pi} (1 + \cos^2\theta) \cdot 2\pi \sin\theta d\theta = \frac{8\pi}{3}r_0^2$$