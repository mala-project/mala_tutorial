import mala
from os.path import join as pj

data_path = "/home/fiedlerl/data/mala_data_repo/Be2"

acsd_parameters = mala.Parameters()
acsd_parameters.descriptors.descriptor_type = "Bispectrum"
acsd_parameters.descriptors.bispectrum_twojmax = 10
acsd_parameters.descriptors.bispectrum_cutoff = 4.67637
acsd_parameters.descriptors.descriptors_contain_xyz = True
acsd_parameters.targets.target_type = "LDOS"
acsd_parameters.targets.ldos_gridsize = 11
acsd_parameters.targets.ldos_gridspacing_ev = 2.5
acsd_parameters.targets.ldos_gridoffset_ev = -5
acsd_parameters.descriptors.acsd_points = 100

hyperoptimizer = mala.ACSDAnalyzer(acsd_parameters)
hyperoptimizer.add_hyperparameter("bispectrum_twojmax", [2, 4, 10])
hyperoptimizer.add_hyperparameter("bispectrum_cutoff", [0.5, 2.0, 4.67637])

# Add raw snapshots to the hyperoptimizer. For the targets, numpy files are
# okay as well.
hyperoptimizer.add_snapshot("espresso-out", pj(data_path, "Be_snapshot1.out"),
                            "numpy", pj(data_path, "Be_snapshot1.in.npy"),
                            target_units="1/(Ry*Bohr^3)")
hyperoptimizer.add_snapshot("espresso-out", pj(data_path, "Be_snapshot2.out"),
                            "numpy", pj(data_path, "Be_snapshot2.in.npy"),
                            target_units="1/(Ry*Bohr^3)")

# If you plan to plot the results (recommended for exploratory searches),
# the optimizer can return the necessary quantities to plot.
plotting = hyperoptimizer.perform_study()
hyperoptimizer.set_optimal_parameters()
