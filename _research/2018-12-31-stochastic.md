---
layout: researchpost
title: Stochastic Optimal Control using Forward and Backward Stochastic Differential Equations
date: 2018-12-31 00:02:00
description: work with Evangelos Theodorou and Panagiotis Tsiotras
tags: 
categories: research
---

[Thesis](https://smartech.gatech.edu/handle/1853/59263){: .btn .btn-outline-info .btn-sm .z-depth-0} [Automatica](https://www.sciencedirect.com/science/article/pii/S0005109817304740){: .btn .btn-outline-info .btn-sm .z-depth-0} [SysConLe](https://doi.org/10.1016/j.sysconle.2018.06.005){: .btn .btn-outline-info .btn-sm .z-depth-0} [DGAA](https://link.springer.com/article/10.1007/s13235-018-0268-4){: .btn .btn-outline-info .btn-sm .z-depth-0} [JGCD](https://doi.org/10.2514/1.G003598){: .btn .btn-outline-info .btn-sm .z-depth-0}


{% include figure.html path="assets/img/FBSDE1.png" class="img-fluid rounded z-depth-1" zoomable=true %}
<center><i>Figure 1</i></center><br><br>


{% include figure.html path="assets/img/FBSDE2.png" class="img-fluid rounded z-depth-1" zoomable=true %}
<center><i>Figure 2</i></center><br><br>


{% include figure.html path="assets/img/FBSDE3.png" class="img-fluid rounded z-depth-1" zoomable=true %}
<center><i>Figure 3</i></center><br><br>


In this line of work, we utilized tools from control theory, stochastic calculus, and machine learning, to propose a mathematical framework capable of addressing a large variety of Stochastic Optimal Control (SOC) problems, as well as stochastic differential games. In general, the mathematical formulation of a SOC problem leads to a nonlinear partial differential equation (PDE), known as the Hamilton-Jacobi-Bellman (HJB) PDE. Furthermore, by virtue of some results in stochastic calculus, certain PDE solutions are linked to solutions of systems of Forward and Backward Stochastic Differential Equations (FBSDEs, figure 1); the latter can be seen as a stochastic equivalent of a two-point boundary value problem. Thus, rather than solving a PDE directly, one can solve its corresponding system of FBSDEs instead -- this is done numerically using sampling and function approximation techniques. The result is a novel sampling-based algorithm, which leads to a nonlinear optimal feedback control law. This controller can be utilized for a variety of control tasks (example: cart-pole in figure 2) and differential games. This is in contrast to most available algorithms within optimal control (e.g., DDP/iLQR, Path Integral control, collocation, multiple shooting etc.) which perform local trajectory optimization and need to close the loop by recalculating the solution at each instant of time, thus requiring heavy online computation during deployment. Applying the algorithm on the fuel-optimal Mars landing problem demonstrates that a deterministic optimal control law, even if it is applied in a closed-loop fashion (i.e., by recalculating the control at each instant of time), does not mitigate the risk induced by the environmental disturbances, and leads to a high probability of crash (figure 3). In contrast, using the proposed method, the probability of a crash can be controlled and can be made arbitrarily small, thus highlighting the importance of stochastic control whenever external disturbances are to be expected (figure 3).  

Parts of this work have been published in Automatica, Systems & Control Letters, Dynamic Games and Applications, Journal of Guidance, Control, and Dynamics, the 2016 IEEE Conference on Decision and Control, and the 2016 American Control Conference.
