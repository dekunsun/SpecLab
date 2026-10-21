# Retrospective controls, funnel v0.2 (JARVIS-DFT)

Stable oxides: 7061. Share with TBmBJ gap: 10.6%. Grade A: 29; with ICSD id: 12 (41%); in the named classes: 12 (41%).
Grade A with DFPT k > 100 (soft-mode divergence, not registered, flagged after the run): 5: Na2Hf2O5 890, SrHfO3 315, SrHfO3 295, LuTaO4 277, HfO2 141

| jid | material | role | outcome | grade | rank |
|---|---|---|---|---|---:|
| JVASP-9147 | HfO2 monoclinic | positive | survived | B | 93 |
| JVASP-52653 | HfO2 Pca21 | positive | survived | A | 24 |
| JVASP-113 | ZrO2 monoclinic | positive (amended: expect band_gap) | band_gap (mbj 4.21) |  |  |
| JVASP-5 | TiO2 rutile | negative: band_gap | band_gap (mbj 2.07) |  |  |
| JVASP-8082 | SrTiO3 | negative: band_gap | band_gap (mbj 2.30) |  |  |
| JVASP-32 | Al2O3 corundum | negative: dielectric | dielectric (dfpt 12.0) |  |  |
| JVASP-116 | MgO rocksalt | negative: dielectric | dielectric (dfpt 10.3) |  |  |
| JVASP-34219 | SiO2 quartz | negative: dielectric | dielectric (dfpt 4.9) |  |  |

| prediction | held |
|---|---|
| P19_stable_oxides_4000_12000 | yes |
| P20_mbj_share_20_40pct | NO |
| P21_gradeA_10_80 | yes |
| P22_controls_as_amended | yes |
| P23_icsd_share_ge_60pct | NO |
| P24_named_classes_ge_half | NO |
