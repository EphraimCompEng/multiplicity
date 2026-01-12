# multiply

A powerful tool to build, test, and analyse multiplier designs.


# Why?

Generating and analysing multiplier designs by hand is labour intensive, even for small datasets, for entire [truth tables](https://en.wikipedia.org/wiki/Truth_table), this is close to impossible.

multiply is built to streamline:

- Custom partial product reduction via [templates](https://github.com/EphraimCompEng/multiply/blob/master/docs/structures/templates.md)
- Generating complete truth tables   
- Analysis, plotting, and managing datasets
- Fine-grain access to bits, words or stages 


# Documentation

Resouces for usage, general theory and implementations can be found in this repository. 
For the API Reference head to multiply's documentation [site](https://ephraimcompeng.github.io/multiply/) 

For more information head to [/docs/](https://github.com/EphraimCompEng/multiplier-lab/tree/master/docs). 


# Setup


```sh
pip install -i https://test.pypi.org/simple/ multiply
```
```Python
import multiply as mp
```

# Dependencies

Planned or currently in use.

| database | visualization |
|:-------- |:------------- |
| [Parquet](https://github.com/apache/parquet-format)| [Matplotlib](https://matplotlib.org/ ) |
| [Pandas](https://pandas.pydata.org/)               |                                        |

Full list TBD.
