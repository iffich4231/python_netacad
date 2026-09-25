# from sys import path
# path.append(r"d:\IT\Git Repositories\python_netacad\Python Essentials 2\Module 1\Section 3\packages")
# for path in path:
#     print(path)

# import extra.iota
# print(extra.iota.funI())

import sys
from pathlib import Path

# Get the absolute path of the folder containing THIS script
script_dir = Path(__file__).resolve().parent

# Add 'packages' relative to this script's directory
sys.path.append(str(script_dir / "packages"))

import extra.iota
print(extra.iota.FunI())

import extra.good.best.sigma
from extra.good.best.tau import FunT
print(extra.good.best.sigma.FunS())
print(FunT())

import extra.good.best.sigma as sig
import extra.good.alpha as alp
print(sig.FunS())
print(alp.FunA())