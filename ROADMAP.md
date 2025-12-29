# Roadmap


Starting point:
- [x] Manage dependencies and automatically resolve them -- [uv](https://docs.astral.sh/uv/)?
- [ ] Find optimal data structure for reduction stages
- [x] Standardise templates 
- [x] Find optimal file format: [Parquet](https://parquet.apache.org/)
- [x] Custom reduction stage templates 
- [ ] Automatic version control (MAJOR.MINOR.PATCH)
- [ ] **Basic** testing

## Algorithm
Wallace Tree multipliers will be the first focus of the library, before moving onto [Dadda](https://en.wikipedia.org/wiki/Dadda_multiplier) and signed multipliers.

Basic functionality; templates, generate, analyse:

- [ ] 8-bit unsaturated template -- built-in
- [ ] 8-bit unsaturated multiply 
- [ ] 8-bit saturated multiply -- naive
- [ ] Truth table generation -> Parquet
- [ ] Basic analysis/visualisation of bit ranges

## Documentation

- [ ] Setup Github Wiki with [typst](https://typst.app/)? [sphinx](https://www.sphinx-doc.org/en/master/)?
- [ ] Improve and provide a focused overview of features 
- [ ] Provide academic sources

## Optimisation
The sheer amount of data produced for 16-bit+ multiplier truth tables becomes astronomical. The program must be robust enough to deal with this efficiently before tackling:
- [ ] Testing suite
- [ ] Multiprocessing support to handle higher bit-widths
- [ ] 16-bit unsaturated multiply
- [ ] 16-bit saturated multiply
- [ ] Heatmaps? plots? Advanced visualisation
- [ ] Use [cython](https://cython.org/)? [numba](https://numba.pydata.org/)? for more performance?

# Advanced Functionality
Once the library is stable and optimised:
- [ ] "Timing" stages/templates/multipliers -- User defined latencies
- [ ] 32-bit saturated multiply?


# Extend Algorithm Support 
Supported algoithms:
- [ ] [Wallace Tree](https://en.wikipedia.org/wiki/Wallace_tree)
- [ ] [Dadda multiplier](https://en.wikipedia.org/wiki/Dadda_multiplier)
- [ ] [Baugh–Wooley algorithm](https://www.researchgate.net/figure/llustration-of-an-8-bit-Baugh-Wooley-multiplication_fig2_224349123)
- [ ] [Booths Multiplication Algorithm](https://en.wikipedia.org/wiki/Booth%27s_multiplication_algorithm)
