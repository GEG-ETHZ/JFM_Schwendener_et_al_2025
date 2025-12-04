# Natural Convection in Porous Media

**The Role of Porosity and Conductivity Ratios in the Transition from Laminar to Inertial Convection**

*D. M. Schwendener, J. Noir, J. Latt, C. Coreixas, X.-Z. Kong*

---

This repository provides the supplementary material for the manuscript:

> **Natural Convection in Porous Media: The Role of Porosity and Conductivity Ratios in the Transition from Laminar to Inertial Convection**  
> D. M. Schwendener, J. Noir, J. Latt, C. Coreixas, X.-Z. Kong

It contains all data and additional analysis necessary to reproduce the key results of the paper, including the datasets used to construct Figure 14 and the experimental compilation summarised in Table A2.

## Contents

### 1. Additional simulation plots

A set of extended figures illustrating the thermal structure, boundary-layer thickness, and flow organisation across porosity and conductivity ratios. These plots complement the manuscript by providing a more detailed view of:

- temperature fields
- vertical and horizontal profiles
- plume organisation and confinement
- transitions between Darcy, Forchheimer, and inertial regimes

### 2. Benchmark and validation data

Files used to validate the numerical model, including:

- reference laminar/Darcy benchmarks
- Forchheimer and inertial regime comparisons
- domain-scale properties (porosity, Da, $k_s/k_f$)
- convergence checks and resolution studies

### 3. Simulation output (CSV and TXT)

Machine-readable data extracted directly from the lattice Boltzmann simulations:

- Nusselt numbers
- Rayleigh and modified Rayleigh numbers
- thermal boundary-layer thickness $\delta_T$
- confinement parameter $\Lambda$
- mean flow quantities
- permeability and drag-coefficient estimates

These CSV/TXT files are the basis of the scaling analyses reported in the manuscript.

### 4. Experimental dataset compilation (Figure 14 and Table A2)

This folder contains the digitised, cleaned, and normalised historical datasets used to construct:

- **Figure 14**: cross-study comparison of $Ra^*/Pr_p$ vs. $\Lambda$
- **Table A2**: summary of key parameters (porosity, Da, conductivity ratio, Prandtl numbers, working fluids, and matrix materials)

Each entry corresponds to one experiment in the literature and includes the processed numerical values used in the analysis.

## Abstract

*Included here for context and citation clarity.*

We study natural convection in porous media using a lattice Boltzmann method that recovers incompressible Navier–Stokes–Fourier dynamics. The porous structure consists of a staggered two-dimensional cylinder array with half-cylinders at the walls, forming a Darcy continuum at the domain scale. Hydrodynamic reference simulations reveal distinct flow regimes: laminar (Darcy), steady-inertial (Forchheimer), and vortex-shedding.

We then analyse the effects of porosity and solid-to-fluid conductivity ratio ($k_s/k_f$) on natural convection. At low porosity ($\varphi = 33\%$), convection is highly sensitive to thermal coupling, particularly for insulating solids, whereas conductive matrices buffer this effect through lateral diffusion. Increasing porosity ($\varphi = 43\%$) smooths the transition as solid and fluid phases become more balanced.

Across the explored range, two inertial regimes emerge governed by plume-scale confinement. The transition from Darcy to inertia-driven convection begins once the dynamics resemble the Forchheimer regime of the reference simulations. Based on our data, the system is governed by the confinement parameter $\Lambda$, which relates the plume-neck width, equivalent to the thermal boundary-layer thickness, to the pore scale: for $\Lambda \geq 1$, the dynamics follow Forchheimer scaling, while for $\Lambda < 1/2$ they shift toward Rayleigh–Bénard behaviour.

Comparison with experimental data shows the same trend: the nominal $Ra^*/Pr_p \approx 1$ criterion holds for $\Lambda > 10$, but weaker confinement causes earlier departure. Finally, we revise benchmark Nusselt numbers for a cavity with square obstacles, showing that the reference by Merrikh & Lage (2005) misrepresents trends due to improper normalisation.

## License

This repository uses dual licensing:

- **Code** (Python scripts, configuration files, etc.) is licensed under the **MIT License**
- **Data and assets** (CSV files, TXT files, PDF files, images, etc.) are licensed under **CC BY 4.0**

See the [LICENSE](LICENSE) file for full details.
