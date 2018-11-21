**[Contents](#Contents) | [Getting started](#Getting-started) | [Running the notebooks](#Running-the-notebooks)  [issues](#Issues) |  [License](#License)**

# casing-em-cuevas

[![Build Status](https://travis-ci.org/simpeg-research/casing-em-cuevas.svg?branch=master)](https://travis-ci.org/simpeg-research/casing-em-cuevas)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/simpeg-research/casing-em-cuevas/master)
[![License](https://img.shields.io/github/license/simpeg-research/casing-em-cuevas.svg)](https://github.com/simpeg-research/casing-em-cuevas/blob/master/LICENSE)
[![SimPEG](https://img.shields.io/badge/powered%20by-SimPEG-blue.svg)](http://simpeg.xyz)

Comparison of SimPEG EM modelling of steel-cased wells with analytic solution by Cuevas

# Contents

There is one notebook in this repository that runs a simulation for a casing in an anisotropic wholespace. 
- [FDEM_casing_anisotropic.ipynb](/FDEM_casing_anisotropic.ipynb)

# Getting started

## locally

To run them locally, you will need to have python installed, preferably through [anaconda](https://www.anaconda.com/download/).

You can then clone this repository. From a command line, run

```
git clone https://github.com/simpeg-research/casing-em-cuevas.git
```

Then `cd` into the `casing-em-cuevas`

```
cd casing-em-cuevas
```

You can install dependencies through pypi
```
pip install -r requirements.txt
```

and then launch Jupyter
```
jupyter notebook
```

Jupyter will then launch in your web-browser.

## online with Binder
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/simpeg-research/casing-em-cuevas/master)

The notebooks can be run online through [mybinder](https://mybinder.org/v2/gh/simpeg-research/casing-em-cuevas/master). Note that changes you make here do not persist. If you would like to keep a copy of your changes, you will need to download the notebook before you finish. 

# Running the notebooks

Each cell of code can be run with `shift + enter` or you can run the entire notebook by selecting `cell`, `Run All` in the toolbar.

<img src="https://raw.githubusercontent.com/simpeg-research/heagy-2018-emcyl/master/figures/cell_run_all.png" width=80% align="middle">

For more information on running Jupyter notebooks, see the [Jupyter Documentation](https://jupyter.readthedocs.io/en/latest/)


# Issues

If you run into problems or bugs, please let us know by [creating an issue](https://github.com/simpeg-research/casing-em-cuevas/issues/new) in this repository.

# License

These notebooks are licensed under the [MIT License](/LICENSE) which allows academic and commercial re-use and adaptation of this work.


