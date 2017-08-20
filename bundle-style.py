#!/usr/bin/python

"""
  TeamSpeak 3 Client PPB (Style Package Builder)
  ===============================================

  This simple script automatically generates TeamSpeak 3 Client Style bundles
  based on stylesheets located in the same directories.
"""

import sys
import os

try:
  from argparse import ArgumentParser
except ImportError:
  sys.exit("ERROR: failed to import module (ArgumentParser)")

try:
  from zipfile import ZipFile
except ImportError:
  sys.exit("ERROR: failed to import module (ZipFile)")

pkgConfigIni = "package.ini"

parser = ArgumentParser(description="Generator for TS3 Client Style bundles")

parser.add_argument("name", help="The style package filename")
parser.add_argument("-v", help="The style package version", metavar="version", default="1.0.0")

options = parser.parse_args()
qtstyle = [f for f in os.listdir(".") if os.path.isdir(f) or (os.path.isfile(f) and (f.endswith(".ini") or f.endswith(".qss")))]

if not pkgConfigIni in qtstyle:
  sys.exit("ERROR: missing style bundle info file (" + pkgConfigIni + ")")

with open(pkgConfigIni, "r") as file:
  ini = file.read()

pkgConf = ini
pkgName = "%s-%s.ts3_style" % (options.name, options.v)

if not len(qtstyle):
  sys.exit()

print "Creating TS3 Client Style bundle " + pkgName

pkgConf = pkgConf.replace("__PLATFORM__", "win32, win64, mac, linux_x86, linux_amd64")
pkgConf = pkgConf.replace("__VERSION__", options.v)
pkgConf = pkgConf.replace("__TYPE__", "Style")

zip = ZipFile(os.path.join(".", pkgName), "w")

for item in qtstyle:
  if os.path.isfile(item):
    if item.endswith(".qss"):
      zip.write(item, "styles/" + item);
  else:
    for root, dirs, files in os.walk(item):
      for file in files:
        zip.write(os.path.join(root, file), "styles/" + os.path.join(root, file))

zip.writestr(pkgConfigIni, pkgConf)
zip.close()
