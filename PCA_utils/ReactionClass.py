def reaction_class():
    dict_desc = {
        "Grignard": ["Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Polarity", "H Bonding"],
        "Alkene Metathesis": ["Alpha", "Beta", "H Bonding", "Dispersion"],
        "Heck C-C": ["Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Polarity", "H Bonding"],
        "Buchwald-Hartwig": ["Dipole moment (D)", "Dielectric constant", "Alpha",
              "Pi", "Polarity", "H Bonding"],
        "SN2/SNAr": ["Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Polarity", "H Bonding"],
        "Amide Coupling": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"],
        "Boc": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
            "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
            "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"],
        "Suzuki-Miyaura": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"],
        "Alcohol Oxidation": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"],
        "Baylis-Hillman": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"],
        "Ester Hydrolysis": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"],
        "Other": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"]
    }

    dict_ref = {
        "Grignard": "Kadam, A.; Nguyen, M.; Kopach, M.; Richardson, P.; Gallou, F.; Wan, Z.-K.; Zhang, W. Comparative "
                    "performance evaluation and systematic screening of solvents in a range of Grignard reactions. "
                    "Green Chem. 2013, 15 (7), 1880-1888.\n"
                    
                    "Sherwood, J.; Clark, J. H.; Fairlamb, I. J. S.; Slattery, J. M. Solvent effects in palladium "
                    "catalysed cross-coupling reactions. Green Chem. 2019, 21 (9), 2164-2213.\n"
                    
                    "Lewis, R. N.; Wright, J. R. Solvent Effects in the Grignard Reaction1. Journal of the American "
                    "Chemical Society 1952, 74 (5), 1253-1257.\n"
                    
                    "Scala, A. A.; Becker, E. I. Solvent Effects in the Grignard Reaction. Ethylmagnesium Bromide with "
                    "Benzonitrile. The Journal of Organic Chemistry 1965, 30 (10), 3491-3498.",
        "Alkene Metathesis": " Skowerski, K.; Białecki, J.; Tracz, A.; Olszewski, T. K. An attempt to provide an "
                             "environmentally friendly solvent selection guide for olefin metathesis. Green Chem. 2014, "
                             "16 (3), 1125-1130.\n"
                             
                             "Binder, J. B.; Blank, J. J.; Raines, R. T. Olefin Metathesis in Homogeneous Aqueous Media"
                             " Catalyzed by Conventional Ruthenium Catalysts. Org. Lett. 2007, 9 (23), 4885-4888.\n"
                             
                             "Thomas, P. A.; Kabanda, M. M.; Ebenso, E. E. DFT Investigation into the Role of "
                             "Conventional and Ionic Liquids as Solvents in Olefin Metathesis. Int. J. Electrochem. Sci "
                             "2013, 8, 10827-10838.\n"
                             
                             "Campodónico, P. R.; Tapia, R. A.; Suárez-Rozas, C. How the Nature of an Alpha-Nucleophile"
                             " Determines a Brønsted Type-Plot and Its Reaction Pathways. An Experimental Study. "
                             "Frontiers in Chemistry 2022, 9, 1276.",
        "Heck C-C": "Sangon, S.; Supanchaiyamat, N.; Sherwood, J.; McElroy, C. R.; Hunt, A. J. Direct comparison of "
                    "safer or sustainable alternative dipolar aprotic solvents for use in carbon–carbon bond formation. "
                    "React. Chem. Eng. 2020, 5 (9), 1798-1804.\n"
                    
                    "Parker, H. L.; Sherwood, J.; Hunt, A. J.; Clark, J. H. Cyclic Carbonates as Green Alternative "
                    "Solvents for the Heck Reaction. ACS Sustainable Chemistry & Engineering 2014, 2 (7), 1739-1742.\n"
                    
                    "Sherwood, J.; Clark, J. H.; Fairlamb, I. J. S.; Slattery, J. M. Solvent effects in palladium "
                    "catalysed cross-coupling reactions. Green Chem. 2019, 21 (9), 2164-2213.\n"
                    
                    "Burello, E.; Rothenberg, G. Optimal Heck Cross‐Coupling Catalysis: A Pseudo‐Pharmaceutical "
                    "Approach. Adv. Synth. Catal. 2003, 345 (12), 1334-1340.\n"
                    
                    "Strappaveccia, G.; Ismalaj, E.; Petrucci, C.; Lanari, D.; Marrocchi, A.; Drees, M.; Facchetti, A.;"
                    " Vaccaro, L. A biomass-derived safe medium to replace toxic dipolar solvents and access cleaner "
                    "Heck coupling reactions. Green Chem. 2015, 17 (1), 365-372.\n"
                    
                    "Xu, L.; Hilton, M. J.; Zhang, X.; Norrby, P.-O.; Wu, Y.-D.; Sigman, M. S.; Wiest, O. Mechanism, "
                    "Reactivity, and Selectivity in Palladium-Catalyzed Redox-Relay Heck Arylations of Alkenyl Alcohols."
                    " Journal of the American Chemical Society 2014, 136 (5), 1960-1967.",
        "Buchwald-Hartwig": "Lei, P.; Wang, Y.; Mu, Y.; Wang, Y.; Ma, Z.; Feng, J.; Liu, X.; Szostak, M. Green-Solvent "
                            "Selection for Acyl Buchwald–Hartwig Cross-Coupling of Amides (Transamidation). ACS "
                            "Sustainable Chemistry & Engineering 2021, 9 (44), 14937-14945.\n"
                            
                            "Christensen, H.; Kiil, S.; Dam-Johansen, K.; Nielsen, O.; Sommer, M. B. Effect of "
                            "Solvents on the Product Distribution and Reaction Rate of a Buchwald−Hartwig Amination "
                            "Reaction. Org. Process Res. Dev. 2006, 10 (4), 762-769.\n"
                            
                            "Sunesson, Y.; Limé, E.; Nilsson Lill, S. O.; Meadows, R. E.; Norrby, P.-O. Role of the Base"
                            " in Buchwald–Hartwig Amination. The Journal of Organic Chemistry 2014, 79 (24), 11961-11969.",
        "SN2/SNAr": "Cseri, L.; Szekely, G. Towards cleaner PolarClean: Efficient synthesis and extended applications "
                    "of the polar aprotic solvent methyl 5-(dimethylamino)-2-methyl-5-oxopentanoate. Green Chem. 2019, "
                    "21 (15), 4178-4188.\n"
                    
                    "Sherwood, J.; Constantinou, A.; Moity, L.; McElroy, C. R.; Farmer, T. J.; Duncan, T.; Raverty, W.; "
                    "Hunt, A. J.; Clark, J. H. Dihydrolevoglucosenone (Cyrene) as a bio-based alternative for dipolar "
                    "aprotic solvents. Chem. Commun. 2014, 50 (68), 9650-9652.\n"
                    
                    "Parker, A. J. Solvation of ions. Part II. Dipolar aprotic solvents as media for nucleophilic "
                    "substitution reactions at a saturated carbon atom. J. Chem. Soc. 1961, 255, 1328-1337.\n"
                    
                    "Parker, A. J. Protic-dipolar aprotic solvent effects on rates of bimolecular reactions. Chem. Rev."
                    " 1969, 69 (1), 1-32.\n"
                    
                    "Miller, J.; Parker, A. J. Dipolar Aprotic Solvents in Bimolecular Aromatic Nucleophilic "
                    "Substitution Reactions1. J. Am. Chem. Soc. 1961, 83 (1), 117-123.\n"
                    
                    "Acevedo, O.; Jorgensen, W. L. Solvent Effects and Mechanism for a Nucleophilic Aromatic "
                    "Substitution from QM/MM Simulations. Org. Lett. 2004, 6 (17), 2881-2884.\n"
                    
                    "Reichardt, C.; Welton, T. Solvents and Solvent Effects in Organic Chemistry; Wiley-VCH Verlag GmbH "
                    "& Co. KGaA, 2011.",
        "Amide Coupling": "MacMillan, D. S.; Murray, J.; Sneddon, H. F.; Jamieson, C.; Watson, A. J. B. Evaluation "
                          "of alternative solvents in common amide coupling reactions: replacement of dichloromethane "
                          "and N,N-dimethylformamide. Green Chem. 2013, 15 (3), 596-600.\n"
                          
                          "Kumar, A.; Sharma, A.; de la Torre, B. G.; Albericio, F. Scope and limitations of "
                          "γ-valerolactone (GVL) as a green solvent to be used with base for fmoc removal in solid "
                          "phase peptide synthesis. Molecules 2019, 24 (21), 4004.\n"
                          
                          "Jad, Y. E.; Govender, T.; Kruger, H. G.; El-Faham, A.; de la Torre, B. G.; Albericio, F. "
                          "Green Solid-Phase Peptide Synthesis (GSPPS) 3. Green Solvents for Fmoc Removal in Peptide "
                          "Chemistry. Org. Process Res. Dev. 2017, 21 (3), 365-369.\n"
                          
                          "Lopez, J.; Pletscher, S.; Aemissegger, A.; Bucher, C.; Gallou, F. N-Butylpyrrolidinone as "
                          "Alternative Solvent for Solid-Phase Peptide Synthesis. Org. Process Res. Dev. 2018, 22 (4), 494-503.",
        "Suzuki-Miyaura": " Lei, P.; Mu, Y.; Wang, Y.; Wang, Y.; Ma, Z.; Feng, J.; Liu, X.; Szostak, M. Green Solvent "
                          "Selection for Suzuki–Miyaura Coupling of Amides. ACS Sustainable Chemistry & Engineering "
                          "2021, 9 (1), 552-559.\n"
                          
                          "Ramgren, S. D.; Hie, L.; Ye, Y.; Garg, N. K. Nickel-Catalyzed Suzuki–Miyaura Couplings in "
                          "Green Solvents. Org. Lett. 2013, 15 (15), 3950-3953.\n"
                          
                          "Sherwood, J.; Clark, J. H.; Fairlamb, I. J. S.; Slattery, J. M. Solvent effects in palladium"
                          " catalysed cross-coupling reactions. Green Chem. 2019, 21 (9), 2164-2213.\n"
                          
                          "Sherwood, J. Suzuki–Miyaura cross coupling is not an informative reaction to demonstrate the"
                          " performance of new solvents. Beilstein J. Org. Chem. 2020, 16 (1), 1001-1005.",
        "Alcohol Oxidation": "Janssen, M. H.; Castellana, J. F. C.; Jackman, H.; Dunn, P. J.; Sheldon, R. A. Towards "
                             "greener solvents for the bleach oxidation of alcohols catalysed by stable N-oxy radicals. "
                             "Green Chem. 2011, 13 (4), 905-912.",
        "Baylis-Hillman": "Sangon, S.; Supanchaiyamat, N.; Sherwood, J.; McElroy, C. R.; Hunt, A. J. Direct comparison "
                          "of safer or sustainable alternative dipolar aprotic solvents for use in carbon–carbon bond "
                          "formation. React. Chem. Eng. 2020, 5 (9), 1798-1804.\n"
                          
                          "de Souza, R. O. M. A.; Pereira, V. L. P.; Esteves, P. M.; Vasconcellos, M. L. A. A. The "
                        "Morita–Baylis–Hillman reaction in aqueous–organic solvent system. Tetrahedron Lett. 2008, 49 (41), 5902-5905.\n"
                          
                          "Aggarwal, V. K.; Dean, D. K.; Mereu, A.; Williams, R. Rate Acceleration of the Baylis−Hillman"
                          "Reaction in Polar Solvents (Water and Formamide). Dominant Role of Hydrogen Bonding, Not"
                          "Hydrophobic Effects, Is Implicated. The Journal of Organic Chemistry 2002, 67 (2), 510-514.\n"
                          
                          "Price, K. E.; Broadwater, S. J.; Walker, B. J.; McQuade, D. T. A New Interpretation of the "
                          "Baylis−Hillman Mechanism. The Journal of Organic Chemistry 2005, 70 (10), 3980-3987.",
        "Ester Hydrolysis": "Theodorou, V.; Skobridis, K.; Tzakos, A. G.; Ragoussis, V. A simple method for the alkaline"
                            " hydrolysis of esters. Tetrahedron Lett. 2007, 48 (46), 8230-8233.\n"
                            
                            "Hilal, S.; Karickhoff, S.; Carreira, L.; Shrestha, B. Estimation of carboxylic acid ester "
                            "hydrolysis rate constants. QSAR & Combinatorial Science 2003, 22 (9‐10), 917-925.\n"
                           
                            "Jordan, A.; Stoy, P.; Sneddon, H. F. Chlorinated Solvents: Their Advantages, Disadvantages,"
                            " and Alternatives in Organic and Medicinal Chemistry. Chem. Rev. 2021, 121 (3), 1582-1622.",
        "Boc": "Watanabe, K.; Kogoshi, N.; Miki, H.; Torisawa, Y. Improved Pinner reaction with CPME as a solvent."
               "Synth. Commun. 2009, 39 (11), 2008-2013.\n"
               
            "Lawrenson, S. B.; Arav, R.; North, M. The greening of peptide synthesis. Green Chem. 2017, 19 (7), 1685-1691.\n"
               
            "Bogdan, A. R.; Charaschanya, M.; Dombrowski, A. W.; Wang, Y.; Djuric, S. W. High-Temperature Boc\n"
               "Deprotection in Flow and Its Application in Multistep Reaction Sequences. Org. Lett. 2016, 18 (8), 1732-1735."
        }

    RC = input("Choose reaction class: Grignard, Alkene Metathesis, Heck C-C, Buchwald-Hartwig, SN2/SNAr, "
               "Amide Coupling, Suzuki-Miyaura, Alcohol Oxidation, Baylis-Hillman, Ester Hydrolysis, Boc, Other")
    return RC, dict_desc, dict_ref
