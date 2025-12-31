# MultiPy

A powerful tool to build, test, and analyse multiplier designs.


# Why?

Generating and analysing multiplier designs by hand is labour intensive, even for small datasets, for entire [truth tables](https://en.wikipedia.org/wiki/Truth_table), this is close to impossible.

MultiPy provides tools for:

- Building partial product reduction layers
- Generating truth tables for custom algorithms
- Analysis, plotting, and finding trends across a dataset(s)
- Fine-grain access to bits, words or stages when building or analysing


# Documentation

Documentation continues to grow with the project. Resouces for usage, general theory and implementations using MultiPy can be found in this repository. 

For more information head to [/docs/](https://github.com/EphraimCompEng/multiplier-lab/tree/master/docs). 


<!--
Use [sphinx](https://www.sphinx-doc.org/en/master/)?
-->


# Setup


```sh
pip install -i https://test.pypi.org/simple/ multipy
```
```Python
import multipy as mp
```

# Dependencies

Planned or currently in use.

| database | math    | visualization |
|:-------- |:------- |:------------- |
| [Parquet](https://github.com/apache/parquet-format)  | [NumPy](https://numpy.org/)   | [Matplotlib](https://matplotlib.org/ )   |
| [Pandas](https://pandas.pydata.org/)                 |                               |                                          |

Full list TBD.
