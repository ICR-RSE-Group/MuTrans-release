# Creating the environment on windows
1. Install matlab, the ICR email address will associate to a license when necessary
It needs to be version 2023a to work with python 3.8 which is a requirement.
Make it 2020b ??
Check matlab and Statistics and something package. as well as Optimisation and Curve Fitting.
https://nexus.icr.ac.uk/strategic-initiatives/sc/scientificsupport/Pages/MATLAB.aspx

2. Need to have installed mini conda and have it in the path so that you can do conda in the command line
make sure you say yes to it going in the path even though it advises against it
https://github.com/conda-forge/miniforge?tab=readme-ov-file

3. Clone the repo and do everything in the repo directrory
https://github.com/ICR-RSE-Group/MuTrans-release

We will follow the advice from Kareem on how to have a kernel for jupyter:
https://nexus.icr.ac.uk/strategic-initiatives/sc/hpc/software/Pages/Python-2023.aspx#anchor19

4. conda on alma replace conda with mamba
conda create -n mutrans python=3.8
conda activate mutrans
-- conda remove mutrans --all

conda install pyemma -c conda-forge
- includes pandas, scipy, matplotlib, numpy
conda install -c conda-forge scanpy python-igraph leidenalg hdf5plugin
- includes seaborn, numba
conda install jupyter ipykernel setuptools pip

5. pip install within the conda environment (not a python venv)
pip install --upgrade pip
pip install wheel --upgrade
pip install matlabengine --upgrade
pip install scanpy --upgrade

~/.conda/envs/mutrans2/bin/pip install --upgrade pip

-- "C:\Users\ralcraft\AppData\Local\miniforge3\envs\mutrans2\Scripts\pip3.exe" install --upgrade pip
-- "C:\Users\ralcraft\AppData\Local\miniforge3\envs\mutrans2\Scripts\pip3.exe" install wheel --upgrade
-- "C:\Users\ralcraft\AppData\Local\miniforge3\envs\mutrans2\Scripts\pip3.exe" install matlabengine --upgrade
-- "C:\Users\ralcraft\AppData\Local\miniforge3\envs\mutrans2\Scripts\pip3.exe" install scanpy --upgrade

6. Add the conda environment to the kernel
python -m ipykernel install --user --name=mutrans
--- python ipykernel install --user --name=mutrans

7. cd Example
 - this is how it knows about its own lib in the github repo mutrans

8. Open "jupyter lab"
From commandline `jupyter lab` and select mutrans as the kernel. Or use it now in vscode and select the kernel.
Or use vscode and select the kernel.

9. Careful the order of importas matters, if there are dll errors move things around (matlab last)



https://uk.mathworks.com/help/matlab/creating_plots/save-figure-to-reopen-in-matlab-later.html
exportgraphics(gca,'landscape_1.pdf','ContentType','vector')



6. Create a python venv and install the packages
deactivate  # if you are in the conda environment
python -m venv mut-env 
source mut-env/bin/activate
.\mut-env\Scripts\activate (.\mut-env\Scripts\deactivate)
C:\dev\small-projects\mutrans\MuTrans-release\mut-env\Scripts\python.exe -V
C:\dev\small-projects\mutrans\MuTrans-release\mut-env\Scripts\python.exe -m pip install --upgrade pip
C:\dev\small-projects\mutrans\MuTrans-release\mut-env\Scripts\python.exe -m pip install wheel --upgrade
C:\dev\small-projects\mutrans\MuTrans-release\mut-env\Scripts\python.exe -m pip install matlabengine --upgrade

7. Now activate the conda env again, we want to be in both:
conda activate mutrans



# windows
python -m venv venv 
.\venv\Scripts\activate
######## pip install -r requirements.txt
pip install --upgrade pip
pip install wheel --upgrade
pip install matlabengine --upgrade
pip install numpy --upgrade
pip install pandas --upgrade
pip install seaborn --upgrade
pip install scanpy --upgrade
pip install mdtraj --upgrade
pip install pyemma --upgrade

conda install pyemma -c conda-forge


# anaconda prompt
cd C:\dev\small-projects\mutrans\MuTrans-release\
#conda create -n venv python=3.8
#conda activate venv
conda config --add channels conda-forge
conda list
pip install wheel --upgrade
pip install matlabengine --upgrade

# make a conda env for an ipython
cd C:\dev\small-projects\mutrans\MuTrans-release\
conda create -n mutrans_env python=3.8
conda activate mutrans_env
conda install pyemma -c conda-forge
conda install numpy -c conda-forge
conda install pandas -c conda-forge
conda install seaborn -c conda-forge
conda install scanpy -c conda-forge
conda install jupyter -c conda-forge

# create from emilias file
cd C:\dev\small-projects\mutrans\MuTrans-release\
conda env create --file mutrans.yml
conda activate mutrans


conda install ipykernel                               # install Python kernel in new conda env
ipython kernel install --user --name=mutrans_kernel   # configure Jupyter to use Python kernel





