# Multiplier Stage Analysis

A project to research multiplier patterns, saturation, and optimisation.
___

# Why?
___
Operations which cannot exceed a range, such as RGB and DSP calculations, saturate to the extremes of that range.

This project focuses on how [saturation](https://en.wikipedia.org/wiki/Saturation_arithmetic) effects the optimisation of a combinational [multiplier](https://en.wikipedia.org/wiki/Binary_multiplier). Once saturation is introduced, calculating the ceiling, or overflow, becomes extremely fast for one range of inputs. However, there are other ranges where extracting this information is not at all trivial. Even moreso the earlier the multiplication stage.

Finding solutions to overflows in a given stage, efficient partial product reduction, and analysing trends across inputs is difficult task by hand. I hope to create a powerful tool to build, manage, and analyse multipliers.


# Documentation
____

[link/to/documentation]

???{
Use [typst](https://typst.app/)?
Use [sphinx](https://www.sphinx-doc.org/en/master/)?
}

# Setup
___

???{
-> Configure [TOML](https://toml.io/en/) file? and or use CLI to configure the TOML? -> main.py uses TOML to set variables

-> Choose default dataset or build own [Parquet](https://github.com/apache/parquet-format)?

-> import templates to /src/templates/
}

# Dependencies
___
| database | math    | visualization |
|:-------- |:------- |:------------- |
| [Parquet](https://github.com/apache/parquet-format)  | [NumPy](https://numpy.org/)   | [Matplotlib](https://matplotlib.org/ )             |
| [PyArrow](https://arrow.apache.org/docs/python/)     |                               | [Pillow](https://pillow.readthedocs.io/en/stable/) |
| [Pandas](https://pandas.pydata.org/)                 |                               |                                                    |

Full list TBD.

# Roadmap
___
- [ ] Manage dependencies and automatically resolve them
- [ ] Find optimal data structure for combinational multiply stages
- [ ] Standardise templates
- [ ] Find optimal file format: parquet? postgre? json will not scale
- [ ] Custom reduction stage templates
- [ ] 8-bit unsaturated multiply
- [ ] 8-bit saturated multiply

Only after: optimal data structure, file formats and standardisation of loading and storing data, is a achieved can 16-bit can be attempted. The potential dataset of 16-bit+ multipliers becomes astronomical and the program must be rebust enough to deal with this efficiently.
- [ ] 16-bit unsaturated multiply
- [ ] 16-bit saturated multiply
- [ ] 32-bit saturated multiply
