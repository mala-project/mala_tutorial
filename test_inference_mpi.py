from os.path import join as pj
import mala
from ase.io import read
from time import time
data_path = "/home/fiedlerl/data/mala_data_repo/Be2"


Be16 = read("Be16.vasp")

calculator = mala.MALA.load_model("Be_model", pj(data_path, "Be_snapshot2.out"))
calculator.mala_parameters.running.inference_data_grid = [36, 36, 54]
calculator.mala_parameters.targets.pseudopotential_path = "./data_generation/"
Be16.set_calculator(calculator)
start_time = time()
energy = Be16.get_potential_energy()
mala.printout(energy, time()-start_time)
