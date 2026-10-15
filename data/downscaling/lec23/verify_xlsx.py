"""Evaluate the workbook with the 'formulas' package and compare with an independent numpy re-implementation."""
import formulas, numpy as np, re
from openpyxl.utils import get_column_letter as L
import pathlib; D=str(pathlib.Path(__file__).parent)+"/"
xl=formulas.ExcelModel().loads(D+"lec23_worked_examples.xlsx").finish()
sol=xl.calculate()
V={}
from openpyxl.utils import column_index_from_string as CI
for k,v in sol.items():
    m=re.match(r"'\[.*\](.+)'!([A-Z]+)(\d+)(?::([A-Z]+)(\d+))?$",k)
    if not m: continue
    try: arr=np.atleast_2d(v.value)
    except Exception: continue
    sh=m.group(1).upper(); c0=CI(m.group(2)); r0=int(m.group(3))
    for dr in range(arr.shape[0]):
        for dc in range(arr.shape[1]):
            V.setdefault((sh,f"{L(c0+dc)}{r0+dr}"),arr[dr,dc])
def g(sh,ref):
    return V[(sh.upper(),ref)]
def grid(sh,top,left,nr,nc): return np.array([[g(sh,f"{L(left+c)}{top+r}") for c in range(nc)] for r in range(nr)],dtype=float)
ld=lambda n: np.loadtxt(D+n,delimiter=",",ndmin=2)
worst=0; nchk=0
def cmp(name,a,b):
    global worst,nchk
    a=np.asarray(a,float);b=np.asarray(b,float)
    e=np.abs(a-b).max(); worst=max(worst,e); nchk+=a.size
    print(f"{name:42s} max|diff| = {e:.2e}")
    assert e<1e-9,name
# ---- bilinear
Z=ld("bilinear_coarse_4x4.csv"); P=ld("bilinear_points_xy.csv")
def bil(z,x,y):
    i=min(int(np.floor(x)),2); j=min(int(np.floor(y)),2); tx=x-i; ty=y-j
    w=[(1-tx)*(1-ty),tx*(1-ty),(1-tx)*ty,tx*ty]
    c=[z[j,i],z[j,i+1],z[j+1,i],z[j+1,i+1]]
    return w,sum(a*b for a,b in zip(w,c))
w=np.array([bil(Z,x,y)[0] for x,y in P]); v=np.array([bil(Z,x,y)[1] for x,y in P])
nn=np.array([Z[int(np.floor(y+.5)),int(np.floor(x+.5))] for x,y in P])
cmp("bilinear weights",grid("Bilinear",5,8,6,4),w)
cmp("bilinear sum w",grid("Bilinear",5,12,6,1),np.ones((6,1)))
cmp("bilinear value (four-weight)",grid("Bilinear",5,20,6,1).ravel(),v)
cmp("bilinear value (two-step)",grid("Bilinear",5,19,6,1).ravel(),v)
cmp("nearest neighbour",grid("Bilinear",5,22,6,1).ravel(),nn)
# ---- BCSD
def interp_w(f,n):
    c0=(f-1)/2; return np.clip((np.arange(n)-c0)/f,0,1)
def bcsd_interp(R2):
    t=interp_w(2,4); out=np.zeros((4,4))
    for j in range(4):
        for i in range(4):
            out[j,i]=(1-t[j])*((1-t[i])*R2[0,0]+t[i]*R2[0,1])+t[j]*((1-t[i])*R2[1,0]+t[i]*R2[1,1])
    return out
Yb=ld("bcsd_coarse_clim_2x2.csv"); y=ld("bcsd_gcm_bc_today_2x2.csv"); xb=ld("bcsd_fine_clim_4x4.csv")
R=y/Yb; Rf=bcsd_interp(R); Pf=Rf*xb
cmp("BCSD factor R",grid("BCSD_2x2",14,2,2,2),R)
cmp("BCSD weights t",grid("BCSD_2x2",22,2,1,4).ravel(),interp_w(2,4))
cmp("BCSD interpolated factor",grid("BCSD_2x2",25,2,4,4),Rf)
cmp("BCSD downscaled P",grid("BCSD_2x2",31,2,4,4),Pf)
cmp("BCSD plain interpolation of y",grid("BCSD_2x2",31,8,4,4),bcsd_interp(y))
blk=lambda a:a.reshape(2,2,2,2).mean(axis=(1,3))
cmp("BCSD block mean of xbar",grid("BCSD_2x2",10,2,2,2),blk(xb))
cmp("BCSD block mean P minus y",grid("BCSD_2x2",37,6,2,2),blk(Pf)-y)
Tb=ld("bcsd_T_coarse_clim_2x2.csv"); yT=ld("bcsd_T_gcm_bc_today_2x2.csv"); xT=ld("bcsd_T_fine_clim_4x4.csv")
A=yT-Tb; PT=xT+bcsd_interp(A)
cmp("BCSD anomaly",grid("BCSD_2x2",48,2,2,2),A)
cmp("BCSD downscaled T",grid("BCSD_2x2",58,2,4,4),PT)
cmp("BCSD T block mean minus y",grid("BCSD_2x2",58,8,2,2),blk(PT)-yT)
# ---- constructed analogues
lib=ld("ca_library_fine_8x16.csv"); tg=ld("ca_target_coarse_1x4.csv").ravel(); tf=ld("ca_target_truth_fine_1x16.csv").ravel()
lam=5.0
coarse=lib.reshape(8,2,2,2,2).transpose(0,1,3,2,4).reshape(8,4,4).mean(-1).reshape(8,4)
rm=np.sqrt(((coarse-tg)**2).mean(1)); rank=rm.argsort().argsort()+1
cmp("CA library coarse",grid("BCCA",6,2,8,4),coarse)
cmp("CA RMSE",grid("BCCA",6,6,8,1).ravel(),rm)
cmp("CA rank",grid("BCCA",6,7,8,1).ravel(),rank)
sel=np.argsort(rm)[:3]
cmp("CA chosen days (1-based)",grid("BCCA",19,2,1,3).ravel(),sel+1)
Y=coarse[sel].T; GG=Y.T@Y
cmp("CA Y'Y",grid("BCCA",30,2,3,3),GG); cmp("CA Y'y",grid("BCCA",30,6,3,1).ravel(),Y.T@tg)
cmp("CA G inverse",grid("BCCA",36,6,3,3),np.linalg.inv(GG+lam*np.eye(3)))
w_plain=np.linalg.lstsq(Y,tg,rcond=None)[0]; w_ridge=np.linalg.solve(GG+lam*np.eye(3),Y.T@tg)
cmp("CA weights LINEST",grid("BCCA",42,2,3,1).ravel(),w_plain)
cmp("CA weights normal eq.",grid("BCCA",42,3,3,1).ravel(),w_plain)
cmp("CA weights ridge",grid("BCCA",42,4,3,1).ravel(),w_ridge)
Xs=lib[sel].T
cmp("CA fine plain",grid("BCCA",49,7,16,1).ravel(),Xs@w_plain)
cmp("CA fine ridge",grid("BCCA",49,8,16,1).ravel(),Xs@w_ridge)
rms=lambda e:np.sqrt((e**2).mean())
cmp("CA RMSE (single, plain, ridge)",[g("BCCA","D66"),g("BCCA","G66"),g("BCCA","H66")],[rms(Xs[:,0]-tf),rms(Xs@w_plain-tf),rms(Xs@w_ridge-tf)])
cmp("CA ridge map grid",grid("BCCA",71,2,4,4),(Xs@w_ridge).reshape(4,4))
print(f"\nALL OK: {nchk} cells compared, worst abs difference {worst:.2e}")
print("weights plain",w_plain,"ridge",w_ridge)
