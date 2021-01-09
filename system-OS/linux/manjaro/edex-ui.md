IMPORTANT NOTE: the following instructions are meant for running eDEX from the latest unoptimized, unreleased, development version. If you'd like to get stable software instead, refer to these instructions.

Starting from source:
on *nix systems (You'll need the Xcode command line tools on macOS):

```
clone the repository
npm run install-linux
npm start
```
on Windows:
```
start cmd or powershell as administrator
clone the repository
npm run install-windows
npm start
```
Building
Note: Due to native modules, you can only build targets for the host OS you are using.
```
npm install (NOT install-linux or install-windows)
npm run build-linux or build-windows or build-darwin
```
The script will minify the source code, recompile native dependencies and create distributable assets in the dist folder.