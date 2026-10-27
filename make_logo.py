"""Rebuild veraspect-logo-email.png from the locked white horizontal lockup (project file
Veraspect_Logo Files_outlined_VeraspectWhite.png, 1400x868, white on black). Usage: python3 make_logo.py <src> <out>"""
import sys
from PIL import Image
import numpy as np
a=np.asarray(Image.open(sys.argv[1]).convert("L")).astype(float)
alpha=np.clip((a-60)/(215-60),0,1); b=12
alpha[:b,:]=0; alpha[-b:,:]=0; alpha[:,:b]=0; alpha[:,-b:]=0
ys,xs=np.where(alpha>0.5); m=4
alpha=alpha[ys.min()-m:ys.max()+m+1, xs.min()-m:xs.max()+m+1]
navy=np.array([0x0C,0x1F,0x3A],float); white=np.array([255,255,255],float)
logo=Image.fromarray((white*(1-alpha[...,None])+navy*alpha[...,None]).astype(np.uint8),"RGB")
pad=int(logo.height*0.08); c=Image.new("RGB",(logo.width+2*pad,logo.height+2*pad),(255,255,255)); c.paste(logo,(pad,pad))
c.resize((360,round(c.height*360/c.width)),Image.LANCZOS).save(sys.argv[2],optimize=True)
