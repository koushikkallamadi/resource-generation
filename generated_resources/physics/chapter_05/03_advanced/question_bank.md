This question bank is designed for students aiming for Olympiad, NTSE, and JEE Foundation proficiency. It covers the physics underlying XRD, SPM, Electron Microscopy, Spectroscopy, and Thermal Analysis.

---

## Part 1: Multiple Choice Questions (HOTS)

**1. In a powder X-ray diffraction experiment, if the crystalline domains decrease in size to the nanometer scale (less than 100 nm), which effect is primarily observed in the diffraction peaks?**
   A) A decrease in peak intensity.
   B) A shift in the $2\theta$ positions of the peaks.
   C) Peak broadening (Scherrer effect).
   D) Disappearance of Bragg peaks.

**2. In an STM (Scanning Tunneling Microscope), the tunneling current $I$ depends on the gap $d$ as $I \propto e^{-\kappa d}$. If the work function $\phi$ of the tip/sample is increased by 21%, how does the sensitivity of the current to the gap distance change?**
   A) Decreases by 10%
   B) Increases by 10%
   C) Remains unchanged
   D) Increases by 21%

**3. In a TEM, the resolution limit is governed by the de Broglie wavelength of electrons. If the accelerating voltage is increased from 100 kV to 400 kV, the theoretical resolution limit:**
   A) Improves by a factor of 2.
   B) Improves by a factor of 4.
   C) Degrades by a factor of 2.
   D) Remains constant.

**4. A DSC scan of a semi-crystalline polymer shows an endothermic peak for $T_m$ and a baseline shift for $T_g$. Which of the following is true?**
   A) $T_g$ is a first-order transition; $T_m$ is a second-order transition.
   B) Both are first-order transitions.
   C) $T_g$ corresponds to a change in heat capacity ($C_p$); $T_m$ involves latent heat.
   D) Neither transition involves a change in $C_p$.

**5. In Bragg's law $n\lambda = 2d\sin\theta$, if the X-ray source is changed from $CuK\alpha$ ($\lambda = 1.54$ Å) to $MoK\alpha$ ($\lambda = 0.71$ Å), the diffraction angle $\theta$ for the same lattice plane $d$ will:**
   A) Increase.
   B) Decrease.
   C) Remain constant.
   D) Be undefined.

**6. Which of the following is a fundamental limitation of SEM compared to TEM?**
   A) SEM cannot provide topographical information.
   B) SEM is restricted to surface imaging, whereas TEM probes internal structure.
   C) SEM requires higher vacuum levels than TEM.
   D) SEM cannot use tungsten filaments.

**7. In DTA, if a process is exothermic, the DTA curve shows a maximum ($\Delta T > 0$) because:**
   A) The sample is cooler than the reference due to heat absorption.
   B) The sample temperature rises above the reference due to internal heat release.
   C) The furnace temperature is oscillating.
   D) The reference material is undergoing a phase transition.

**8. Why is "Preferred Orientation" considered a major source of error in quantitative PXRD?**
   A) It causes peak splitting.
   B) It violates the assumption of random crystal orientation, biasing peak intensities.
   C) It prevents the Bragg condition from being met.
   D) It increases the background hump.

**9. In UV-Vis spectroscopy, the Beer-Lambert law $A = \epsilon c l$ fails at high concentrations because:**
   A) The incident light becomes monochromatic.
   B) Molecular interactions and refractive index changes occur at high solute density.
   C) The detector becomes saturated.
   D) The path length $l$ increases.

**10. A TGA thermogram shows a 15% mass loss at 300°C. If the sample is $CaC_2O_4 \cdot H_2O$, identify the process:**
    A) Melting of the salt.
    B) Loss of water of crystallization.
    C) Decomposition into $CaCO_3$.
    D) Oxidation of the sample.

---

## Part 2: Case Study/Passage Questions

**Passage 1: The Physics of Tunneling**
The STM exploits quantum tunneling, where electrons cross a forbidden energy barrier. The probability of tunneling is proportional to the overlap of the electronic wavefunctions. The decay constant $\kappa$ is defined as $\kappa = \frac{\sqrt{2m\phi}}{\hbar}$.

1. (1 mark) Why is the STM extremely sensitive to the tip-sample gap $d$?
2. (2 marks) If the barrier height $\phi$ is 4 eV, and the tip is moved by 0.5 Å, calculate the approximate ratio of the current change.
3. (2 marks) Explain why the STM can achieve atomic resolution while conventional light microscopes cannot.

---

## Part 3: High-Difficulty Long Answer Questions

1. **Derivation:** Starting from the de Broglie relation $\lambda = \frac{h}{p}$, derive the expression for the wavelength of an electron accelerated through a potential difference $V$, considering relativistic corrections if $eV \approx m_0c^2$.
2. **Comparison:** Construct a table comparing SEM, TEM, and AFM in terms of their primary interaction signal, vacuum requirements, resolution limits, and sample preparation complexity.
3. **Thermal Analysis:** Explain why a Modulated DSC (MDSC) can separate "total heat flow" into "reversing" (heat capacity) and "non-reversing" (kinetic) components, unlike conventional DSC.
4. **PXRD Analysis:** Discuss the role of the Scherrer equation $L = \frac{K\lambda}{\beta \cos \theta}$ in determining crystallite size. What are the practical limitations of using this equation for samples with internal micro-strain?
5. **Experimental Design:** Propose an experimental methodology to determine the percentage of $CaCO_3$ filler in a polymer composite using TGA and XRD, justifying the use of both techniques.

---

## Part 4: Challenge Questions

1. **Analytical Design:** You are tasked with identifying a sub-micron metallic contaminant in a non-conductive ceramic matrix. Design a multi-step characterization strategy. Which techniques would you use first, and how would you optimize the sample preparation?
2. **Mathematical Modeling:** Using the Rietveld refinement logic, why does "peak overlay" in high-angle reflections introduce significant uncertainty in unit cell parameter determination? How do non-linear least-squares algorithms handle this?
3. **Quantum Limitation:** Is there a theoretical limit to the resolution of an AFM? Discuss how the geometry of the "Apex" and the Van der Waals forces between the tip and the atoms on the surface define this limit.

---

## Answer Key & Explanations

1. **MCQ Answers:** 
   1:C, 2:B, 3:A (since $\lambda \propto V^{-1/2}$), 4:C, 5:B (since $\sin\theta \propto \lambda$), 6:B, 7:B, 8:B, 9:B, 10:B (Stoichiometric calculation: $H_2O/CaC_2O_4 \cdot H_2O \approx 18/146 \approx 12.3\% \approx 15\%$).

2. **Passage 1:**
   1. The current depends exponentially on the gap. Small changes in $d$ lead to order-of-magnitude changes in $I$.
   2. Using $\kappa \propto \sqrt{\phi}$, $I \approx \exp(-2\kappa d)$.
   3. Electrons have wavelengths in the picometer range, allowing them to probe sub-nanometer features, unlike photons restricted by the diffraction limit of visible light (~200 nm).

3. **Complex Qs (Summary):**
   - *Thermal:* MDSC uses a sinusoidal heating rate ($T = T_0 + \beta t + B\sin(\omega t)$). The heat capacity component responds to the sine wave (reversing), while kinetic processes (like crystallization or evaporation) do not respond to the high-frequency modulation (non-reversing).