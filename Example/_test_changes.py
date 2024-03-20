
import scanpy as sc
import hdf5plugin #this is required to make scanpy work :shrug:
import gc
sc.settings.set_figure_params(dpi=100, frameon=False, figsize=(3, 3), facecolor='white')
datadir = "data/"
print("Looking for data",datadir+"ut_scanpy_nn.h5ad")
adata = sc.read(datadir+"ut_scanpy_nn.h5ad")
print("Adata:",type(adata),adata)
print("Garbage collected (a)",gc.collect())    
k_cluster = 4.0 #4.0
trials = 5 # 50
num_meta_cell = 50.0
par = {"choice_distance":"cosine", "K_cluster":k_cluster, "trials":trials,
        "weight_scale":True,       "initial":"pca",       "reduce_large_scale":True,
        "fig_name" : "my_fig6.fig",
        "fig_title" : "My fig title6",
        "reduce_num_meta_cell":num_meta_cell}
import pyMuTrans as pm
print("Garbage collected (b)",gc.collect())
import matlab.engine
eng = matlab.engine.start_matlab()
adata_mu = pm.dynamical_analysis(adata, par)
#adata_mu = pm.dynamical_analysis(adata, par)
#print("Results type=",type(adata_mu))
#print("Results object=\n",adata_mu)
#print("Completed and garbage collected (c)",gc.collect())

