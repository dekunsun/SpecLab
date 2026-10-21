# Clausius-Mossotti estimate vs DFPT total dielectric constant (JARVIS-DFT, oxides passing the composition rule)

- n_oxides_with_dfpt: 765
- n_scored: 498
- n_unscorable: 267
- mard_dfpt_lt_200: 0.471
- spearman_dfpt_lt_200: 0.698
- n_dfpt_ge_target: 175
- recall_at_screen: 0.451
- precision_at_screen: 0.637
- screen_min: 15
- target_min: 25

Worst 15 under-estimates among DFPT >= target:

| jid | formula | DFPT | CM | x |
|---|---|---:|---:|---:|
| JVASP-305 | TiO2 | 1026.1 | 4.6 | 0.547 |
| JVASP-41602 | Na2Hf2O5 | 890.0 | 7.0 | 0.666 |
| JVASP-11766 | BaCoO2 | 872.1 | 10.7 | 0.763 |
| JVASP-52785 | MnSnO3 | 733.2 | 12.7 | 0.797 |
| JVASP-11504 | Ba2Ti3O8 | 610.8 | 14.5 | 0.819 |
| JVASP-48112 | LiMn2B2O6 | 402.1 | 6.8 | 0.658 |
| JVASP-52356 | BaSrO2 | 364.6 | 11.5 | 0.778 |
| JVASP-7773 | SrHfO3 | 315.1 | 13.5 | 0.806 |
| JVASP-8061 | SrHfO3 | 294.8 | 13.5 | 0.806 |
| JVASP-49838 | Li2CeO3 | 273.8 | 7.4 | 0.683 |
| JVASP-18465 | Ag3BO3 | 202.7 | 5.3 | 0.589 |
| JVASP-12809 | Ag3BO3 | 200.8 | 5.3 | 0.589 |
| JVASP-54553 | LiNbWO6 | 190.6 | 14.5 | 0.818 |
| JVASP-8256 | TiO2 | 159.2 | 10.7 | 0.763 |
| JVASP-30565 | TiO2 | 156.1 | 10.8 | 0.766 |
