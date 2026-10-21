# Funnel: high_k_gate_dielectric v0.1

Dataset: MP-20 (txie-93/cdvae, GitHub), <=20 atoms per cell, PBE gaps; 45229 entries; 3.0 s.

| stage | survivors | removed (reason: n) |
|---|---:|---|
| all | 45229 |  |
| composition | 7259 | missing_required_element: 33707, blacklisted: 4263 |
| stability | 5489 | above_hull: 1770 |
| band_gap | 777 | pbe_gap_below_threshold: 4712 |
| dielectric | 184 | k_below_screen: 526, no_polarizability:Sb+5: 46, no_polarizability:Re+7: 8, no_polarizability:Sb+3: 7, no_polarizability:Yb+2: 3, no_oxidation_state_guess: 2, cm_divergent: 1 |

Survivors: 184. Top 30 by tie-breaker score:

| rank | id | formula | sg | Eg PBE | hull | k_CM | score |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | mp-2920 | LaAlO3 | 167 | 4.10 | 0.000 | 93.6 | 2.607 |
| 2 | mp-1080060 | LaAlO3 | 74 | 3.85 | 0.001 | 93.4 | 2.526 |
| 3 | mp-12862 | LuTaO4 | 15 | 4.09 | 0.010 | 63.6 | 2.507 |
| 4 | mp-1080080 | LaAlO3 | 140 | 3.67 | 0.001 | 93.6 | 2.469 |
| 5 | mp-5304 | LaAlO3 | 221 | 3.58 | 0.007 | 119.4 | 2.384 |
| 6 | mp-12933 | TmTaO4 | 13 | 4.07 | 0.000 | 52.6 | 2.302 |
| 7 | mp-1222844 | LaPr3Al4O12 | 155 | 3.88 | 0.002 | 50.8 | 2.159 |
| 8 | mp-11585 | La2MgGeO6 | 148 | 4.21 | 0.016 | 49.1 | 2.039 |
| 9 | mp-4344 | HoTaO4 | 15 | 4.09 | 0.004 | 47.0 | 2.039 |
| 10 | mp-5503 | ErTaO4 | 15 | 4.09 | 0.004 | 46.5 | 2.021 |
| 11 | mp-5985 | HoTaO4 | 13 | 4.04 | 0.000 | 45.5 | 2.007 |
| 12 | mp-3444 | ErTaO4 | 13 | 4.05 | 0.000 | 44.8 | 1.981 |
| 13 | mp-12932 | TbTaO4 | 13 | 4.02 | 0.000 | 44.3 | 1.953 |
| 14 | mp-554593 | TbTaO4 | 15 | 4.15 | 0.005 | 44.2 | 1.938 |
| 15 | mp-7703 | DyTaO4 | 13 | 4.03 | 0.000 | 43.5 | 1.924 |
| 16 | mp-557914 | DyTaO4 | 15 | 4.15 | 0.005 | 43.8 | 1.922 |
| 17 | mp-3466 | PrAlO3 | 167 | 4.22 | 0.000 | 38.0 | 1.764 |
| 18 | mp-12931 | SmTaO4 | 13 | 3.98 | 0.000 | 39.2 | 1.739 |
| 19 | mp-3756 | SmTaO4 | 15 | 4.19 | 0.005 | 38.3 | 1.717 |
| 20 | mp-3998 | LaTaO4 | 36 | 3.42 | 0.009 | 44.3 | 1.685 |
| 21 | mp-5899 | NdAlO3 | 167 | 4.43 | 0.000 | 31.9 | 1.580 |
| 22 | mp-31116 | LaScO3 | 62 | 3.90 | 0.000 | 35.4 | 1.563 |
| 23 | mp-7405 | SmAlO3 | 62 | 4.77 | 0.000 | 28.2 | 1.534 |
| 24 | mp-5489 | LuTaO4 | 13 | 4.37 | 0.000 | 31.1 | 1.529 |
| 25 | mp-1079705 | Ba2LuTaO6 | 225 | 3.41 | 0.000 | 37.9 | 1.520 |
| 26 | mp-3203 | NdTaO4 | 13 | 3.95 | 0.000 | 33.9 | 1.517 |
| 27 | mp-4434 | TbAlO3 | 62 | 5.61 | 0.009 | 23.6 | 1.501 |
| 28 | mp-4718 | NdTaO4 | 15 | 4.19 | 0.004 | 32.7 | 1.500 |
| 29 | mp-1218203 | SrLaMgTaO6 | 7 | 4.07 | 0.000 | 32.5 | 1.498 |
| 30 | mp-3666 | LiTaO3 | 161 | 3.77 | 0.000 | 34.6 | 1.495 |
