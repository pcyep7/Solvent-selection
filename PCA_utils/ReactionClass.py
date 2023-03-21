def reaction_class():
    dict_desc = {
        "Grignard": ["Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Polarity", "H Bonding"],
        "Alkene metathesis": ["Alpha", "Beta", "H Bonding", "Dispersion"],
        "Heck C-C": ["Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Polarity", "H Bonding"],
        "Buchwald-Hartwig": ["Dipole moment (D)", "Dielectric constant", "Alpha",
              "Pi", "Polarity", "H Bonding"],
        "SN2/SNAr": ["Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Polarity", "H Bonding"],
        "Amide Coupling": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
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
    RC = input("Choose reaction class: Grignard, Alkene metathesis, Heck C-C, Buchwald-Hartwig, SN2/SNAr, "
               "Amide Coupling, Suzuki-Miyaura, Alcohol Oxidation, Baylis-Hillman, Ester Hydrolysis, Other")
    return RC, dict_desc
