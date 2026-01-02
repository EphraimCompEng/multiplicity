# Roadmap


Starting point:
- [x] Manage dependencies and automatically resolve them -- [uv](https://docs.astral.sh/uv/)?
- [x] Find optimal data structure for reduction stages
- [x] Standardise templates 
- [x] Find optimal file format: [Parquet](https://parquet.apache.org/)
- [x] Custom reduction stage templates 
- [x] Automatic version control (MAJOR.MINOR.PATCH) -- uv
- [x] **Basic** testing

## Structure

The entire library functions via three structures: Algorithms which initialise a Matrix which are then subsequesntly reduced by templates.
- [x] Algorithm, Matrix and Template classes formalised
- [ ] Correctly implement custom Types. (Templates need work)
- [x] simple templates 
- [ ] Complex templates 
- [ ] Simple reduction
- [ ] Comples reduction
- [ ] Simple row map
- [ ] Complete map matrix
- [ ] Algorithm.state and .step()

## Algorithm
Wallace Tree multipliers will be the first focus of the library, before moving onto [Dadda](https://en.wikipedia.org/wiki/Dadda_multiplier) and signed multipliers.

Basic functionality; "simple templates", generate, analyse:

- [ ] 4-bit unsaturated multiply [Built-in]\*
- [ ] 8-bit unsaturated multiply [Built-in]
- [ ] 4-bit saturated multiply [Built-in]
- [ ] 8-bit saturated multiply [Built-in]
- [x] Truth table generation -> ~Parquet~ json
- [ ] Implement I/O via [Parquet](https://parquet.apache.org/)
- [x] Truth table generation -> Parquet
- [ ] Basic analysis/visualisation of bit ranges]

\* Note: once built-in functions and classes are operational, hand crafted templates and maps will also be functional.
simple templates -> internally called patters, form -> complex templates.

## Documentation

- [x] Sphinx implementation
- [ ] Setup sphinx -> web based API reference
- [ ] Setup Github Wiki? For theory / internal systems
- [ ] Improve API ref site with nicer HTML/CSS
- [ ] Add markdown(.md) Functionality to API ref
- [ ] Improve and provide a focused overview of features 
- [ ] Provide academic sources for algorithm docs

## Optimisation
The sheer amount of data produced for 16-bit+ multiplier truth tables becomes astronomical. The program must be robust enough to deal with this efficiently before tackling:
- [ ] Testing suite - Pytest
- [ ] Multiprocessing support to handle higher bit-widths
- [ ] 16-bit unsaturated multiply
- [ ] 16-bit saturated multiply
- [ ] Heatmaps? plots? Advanced visualisation
- [ ] Use [cython](https://cython.org/)? [numba](https://numba.pydata.org/)? for more performance?
- [ ] Research if 32/64/128-bit multipliers can be analysed in a reasonable time (1min? 5min? ???)


# Extend Built-in Algorithm Support 
Supported algoithms:
- [ ] [Wallace Tree](https://en.wikipedia.org/wiki/Wallace_tree)
- [ ] [Dadda multiplier](https://en.wikipedia.org/wiki/Dadda_multiplier)
- [ ] [Baugh–Wooley algorithm](https://www.researchgate.net/figure/llustration-of-an-8-bit-Baugh-Wooley-multiplication_fig2_224349123)
- [ ] [Booths Multiplication Algorithm](https://en.wikipedia.org/wiki/Booth%27s_multiplication_algorithm)

# Custom 


# Advanced Functionality
Once the library is stable and optimised:
- [ ] "Timing" stages/templates/multipliers -- User defined latencies
- [ ] 32-bit unsaturated multiply?
- [ ] 32-bit saturated multiply?
