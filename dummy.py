

scanpy, matlab = 1,1


if scanpy:
    import scanpy as sc
    import hdf5plugin
    sc.settings.set_figure_params(dpi=100, frameon=False, figsize=(3, 3), facecolor='white')
    datadir = "Example/data/"
    adata = sc.read(datadir+"ut_scanpy_nn.h5ad")
    print("Adata:",type(adata),adata)
    
if matlab:
    import matlab.engine
    eng = matlab.engine.start_matlab()
    print("Matlab Eng:",type(eng))