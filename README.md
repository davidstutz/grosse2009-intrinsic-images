# MIT Intrinsic Images Fork

This repository contains the code published together with the MIT Intrinsic Images Dataset, see [http://www.cs.toronto.edu/~rgrosse/intrinsic/](http://www.cs.toronto.edu/~rgrosse/intrinsic/). See also:

    [1] R. Grosse, M. K. Johnson, E. H. Adelson, and W. T. Freeman.
        Ground truth dataset and baseline evaluations for intrinsic image algorithms.
        Proceedings of the International Conference on Computer Vision (ICCV), 2009.

Below you find the original README of the code.

**Work in Progress:** A command line tool for running the color Retinex algorithm as described in [1] is included (`retinex.py`).

## Original README

### Code and Data

The code and data are available as separate tarballs: 

* [http://people.csail.mit.edu/rgrosse/intrinsic/intrinsic-code-python.tar.gz](http://people.csail.mit.edu/rgrosse/intrinsic/intrinsic-code-python.tar.gz)
* [http://people.csail.mit.edu/rgrosse/intrinsic/intrinsic-data.tar.gz](http://people.csail.mit.edu/rgrosse/intrinsic/intrinsic-data.tar.gz)

Unpack the tarballs and merge if necessary. The top-level folder, named MIT-intrinsic by default, should contain the README, four python files, the data folder, and two empty results folders.

The four python files are:

* `comparison.py`: the script for performing hold-one-out cross-validation.
* `intrinsic.py`: all of the intrinsic image algorithms, along with functions for reading the data and computing the error scores.
* `poisson.py`: functions for solving the Poisson equation using least-squares or L1.
* `html.py`: a utility for saving results to HTML.

After installing the required packages (see below), you should be able to reproduce most of the results from the paper by running `comparison.py`:

   cd mit-intrinsic-images
   python comparison.py

This will evaluate the algorithms using hold-one-out cross-validation. It prints results to the console, and also saves the shading/reflectance decompositions and their error scores to the HTML file `results/index.html`. If you set the `USE_L1` variable (defined in `comparison.py`) to `True`, it will use the L1 penalty for reconstruction rather than least squares. In this case, the outputs will be saved to `results_L1/index.html`.

We have done our best to provide a code base which is readable, compact, and easy to extend.

Please send your questions and comments to Roger Grosse (rgrosse@mit.edu).

### Installation

To run the code, you will need Python as well as the following Python libraries:

* NumPy ([http://numpy.scipy.org](http://numpy.scipy.org))
* SciPy ([http://www.scipy.org](http://www.scipy.org))
* PyPNG (Download at [http://code.google.com/pypng](http://code.google.com/pypng) -- documentation at [http://packages.python.org/pypng/index.html](http://packages.python.org/pypng/index.html))
* PyAMG ([http://code.google.com/p/pyamg](http://code.google.com/p/pyamg))

For detailed installation instructions for particular platforms, please see [http://people.csail.mit.edu/rgrosse/intrinsic/downloads.html](http://people.csail.mit.edu/rgrosse/intrinsic/downloads.html)

## License

For license information see [http://www.cs.toronto.edu/~rgrosse/intrinsic/](http://www.cs.toronto.edu/~rgrosse/intrinsic/).

For license details of `Lenna.png`, see [http://en.wikipedia.org/wiki/Lenna#mediaviewer/File:Lenna.png](http://en.wikipedia.org/wiki/Lenna#mediaviewer/File:Lenna.png).
