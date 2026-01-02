# MultiPy

A powerful tool to build, test, and analyse multiplier designs.


# Why?

Generating and analysing multiplier designs by hand is labour intensive, even for small datasets, for entire [truth tables](https://en.wikipedia.org/wiki/Truth_table), this is close to impossible.

MultiPy is built to streamline:

- Custom partial product reduction via [templates](https://github.com/EphraimCompEng/multipy/blob/master/docs/structures/templates.md)
- Generating complete truth tables   
- Analysis, plotting, and managing datasets
- Fine-grain access to bits, words or stages 


# Documentation

Documentation continues to grow with the project. Resouces for usage, general theory and implementations using MultiPy can be found in this repository. 

For more information head to [/docs/](https://github.com/EphraimCompEng/multiplier-lab/tree/master/docs). 


# Setup


```sh
pip install -i https://test.pypi.org/simple/ multipy
```
```Python
import multipy as mp
```

# Dependencies

Planned or currently in use.

| database | visualization |
|:-------- |:------------- |
| [Parquet](https://github.com/apache/parquet-format)| [Matplotlib](https://matplotlib.org/ ) |
| [Pandas](https://pandas.pydata.org/)               |                                        |

Full list TBD.
