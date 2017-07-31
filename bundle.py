#!/usr/bin/python

"""
  TeamSpeak 3 Client PPB (Plugin Package Builder)
  ===============================================

  This simple script automatically generates TeamSpeak 3 Client Plugin bundles
  based on libraries located in the same directories.

  IMPORTANT:
  All libraries must follow the same naming convention!

  Windows 32-Bit:  myplugin_win32.dll
  Windows 64-Bit:  myplugin_win64.dll
  Linux 32-Bit:    myplugin_linux_x84.so
  Linux 64-Bit:    myplugin_linux_amd64.so
  macOS:           myplugin_mac.dylib
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
pkgPlatforms = {
  "win32"       : ["_win32.dll"],
  "win64"       : ["_win64.dll"],
  "linux_x86"   : ["_linux_x86.so"],
  "linux_amd64" : ["_linux_amd64.so"],
  "mac"         : ["_mac.dylib"],
}

parser = ArgumentParser(description="Generator for TS3 Client Plugin bundles")

parser.add_argument("name", help="The plugin package filename")
parser.add_argument("-v", help="The plugin package version", metavar="version", default="1.0.0")

options = parser.parse_args()
plugins = [f for f in os.listdir(".") if os.path.isfile(f)]

if not pkgConfigIni in plugins:
  sys.exit("ERROR: missing plugin bundle info file (" + pkgConfigIni + ")")

with open(pkgConfigIni, "r") as file:
  ini = file.read()

for platform, suffixes in pkgPlatforms.items():
  pkgLibs = []
  pkgConf = ini
  pkgName = "%s-%s_%s.ts3_plugin" % (options.name, options.v, platform)

  for suffix in suffixes:
    pkgLibs = [plugin for plugin in plugins if plugin.endswith(suffix)]

  if not len(pkgLibs):
    continue

  print "Creating TS3 Client Plugin bundle " + pkgName

  pkgConf = pkgConf.replace("__PLATFORM__", platform)
  pkgConf = pkgConf.replace("__VERSION__", options.v)

  zip = ZipFile(os.path.join(".", pkgName), "w")

  for lib in pkgLibs:
    zip.write(lib, "plugins/" + lib);

  zip.writestr(pkgConfigIni, pkgConf)
  zip.close()
