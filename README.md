# AI for Trading
### Algorithmic Trading with Python

Projects created to complete the Nanodegree program from Udacity

For launching local jupyter server:
> jupyter notebook

For looking for an installed pip package
> pip list | findstr [package]

For checking markdown MD syntax: https://www.markdownguide.org/basic-syntax/

---

### Zipline

**zipline** has been deprecated. Instead, use **zipline-reloaded** lib (https://zipline.ml4trading.io/) or [GitHub repo](https://github.com/stefan-jansen/zipline-reloaded?tab=readme-ov-file)

> pip install zipline-reloaded

This will need to install the ta-lib native library, for this:
([More info here](https://github.com/TA-Lib/ta-lib-python#dependencies))

### 1. Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

### 2. Compile the ta-lib

#### Windows

Download [ta-lib-0.4.0-msvc.zip](http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-msvc.zip) and unzip to C:\ta-lib.

This is a 32-bit binary release. If you want to use 64-bit Python, you will need to build a 64-bit version of the library. Some unofficial instructions for building on 64-bit Windows 10 or Windows 11, here for reference:

Download and Unzip ta-lib-0.4.0-msvc.zip
- Move the Unzipped Folder ta-lib to C:\
- Select [Visual C++] Feature
- Build TA-Lib Library
From Windows Start Menu, Start [VS2015 x64 Native Tools Command Prompt]
- Move to C:\ta-lib\c\make\cdr\win32\msvc
- Build the Library by executing: nmake

Alternatively, You might also try these unofficial windows binaries for both 32-bit and 64-bit:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib

### 3. Install ta-lib
> pip install ta-lib
