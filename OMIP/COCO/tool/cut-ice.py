"""
OMIP のnetCDFファイルをサンプル用に小さくする。t=1,2のレコードだけ取り出す。
front:/storage1/M201/htsujino/OMIP/model/MIROC-COCO4.9/20190731/JRA/siconc.nc
"""

#https://repository.library.brown.edu/viewers/archive/bdr:1114617/content/code/Tsujino_et_al-OMIP-code-20200713/DRAW_figs/inter_comparison/Climatology/json/tos_omip2.json

import xarray as xr

d = xr.open_dataset('../../../omip2data/MIROC-COCO4.9/siconc.nc',decode_times=False)
d.isel(time=[0,1]).to_netcdf('siconc_2rec.nc')
