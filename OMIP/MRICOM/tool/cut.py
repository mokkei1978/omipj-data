"""
OMIP のnetCDFファイルをサンプル用に小さくする。t=1,2のレコードだけ取り出す。
front:/storage1/M201/htsujino/OMIP/model/MRI.COM/20190809/omip2/tos.nc
"""

import xarray as xr

d = xr.open_dataset('tos.nc')
d.isel(time=[0,1]).to_netcdf('tos_2rec.nc')
