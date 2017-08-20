# TeamSpeak 3 Client Addon Tools

This repository contains a collection of some quick-and-dirty tools to help building and deploying TeamSpeak 3 Client addons.

## bundle-plugin.py

This simple script automatically generates TeamSpeak 3 Client Plugin bundles based on a [package.ini](package.ini) and libraries located in the same directory. Note that all libraries must follow the same naming convention. For example:

- myplugin_win32.dll
- myplugin_win64.dll
- libmyplugin_linux_x84.so
- libmyplugin_linux_amd64.so
- libmyplugin_mac.dylib

### Usage

```bash
bundle-plugin.py [-v version] name
```

### Example

```bash
bundle-plugin.py -v 0.1.2 myplugin
```

## bundle-style.py

This simple script automatically generates TeamSpeak 3 Client Style bundles based on a [package.ini](package.ini), Qt Style Sheet (.qss) and asset directories located in the same directory.

### Usage

```bash
bundle-style.py [-v version] name
```

### Example

```bash
bundle-style.py -v 0.1.2 mystyle
```
