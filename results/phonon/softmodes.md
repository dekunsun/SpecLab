# Soft-mode check (phonopy + MACE-MP-0b3, 4x4x4 mesh)

Divergent entries soft: 5/5. Controls soft: 0/3.

| jid | formula | role | k DFPT | unit atoms | supercell | displacements | min f mesh (THz) | min f Gamma (THz) | soft | s |
|---|---|---|---:|---:|---|---:|---:|---:|---|---:|
| JVASP-41602 | Na2Hf2O5 | divergent | 890 | 9 | [3, 3, 1] | 7 | -3.238 | -0.001 | YES | 8.3 |
| JVASP-7773 | SrHfO3 | divergent | 315 | 5 | [2, 2, 2] | 8 | -4.852 | -0.002 | YES | 3.1 |
| JVASP-8061 | SrHfO3 | divergent | 295 | 5 | [2, 2, 2] | 3 | -4.853 | -0.004 | YES | 1.3 |
| JVASP-4492 | LuTaO4 | divergent | 277 | 12 | [2, 2, 2] | 18 | -1.557 | -0.001 | YES | 25.6 |
| JVASP-35894 | HfO2 | divergent | 141 | 6 | [3, 3, 2] | 4 | -2.028 | -0.004 | YES | 7.3 |
| JVASP-52653 | HfO2 | control | 24 | 12 | [2, 2, 2] | 18 | -0.0 | -0.0 | no | 28.1 |
| JVASP-36951 | BaHfO3 | control | 34 | 5 | [2, 2, 2] | 30 | -0.0 | -0.0 | no | 11.2 |
| JVASP-8020 | Nd2O3 | control | 21 | 5 | [3, 3, 2] | 5 | -0.0 | -0.0 | no | 5.2 |

| prediction | held |
|---|---|
| P33_ge_3_of_5_divergent_soft | yes |
| P34_le_1_of_3_controls_soft | yes |
| P35_both_SrHfO3_soft | yes |
