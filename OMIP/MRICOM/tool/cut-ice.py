"""
OMIP のnetCDFファイルをサンプル用に小さくする。t=1,2のレコードだけ取り出す。
front:/storage1/M201/htsujino/OMIP/model/MRI.COM/20190809/omip2/siconc.nc
"""

import xarray as xr

d = xr.open_dataset('../../../omip2data/MRI.COM/siconc.nc')
d.isel(time=[0,1]).to_netcdf('siconc_2rec.nc')
