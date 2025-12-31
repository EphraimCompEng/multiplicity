# Algorithms


An algorithm is the application of multiple templates until no partial
products are left.

Algorithm objects must collect any number of templates based on:
    - bitwidth
    - template composition -- MultiPy should not stop users making any
      algorithm, even if suboptimal
    - Saturation -- Set to original bit width
    (Unsure if users likely to need saturation to arbitrary bitwidths)

Applying simple templates can be hardcoded, however complex templates
need to be analysed before execution. Especially so when implementing
decoders, flooding and sneaky tricks like using carry-in(cin) on adders.
