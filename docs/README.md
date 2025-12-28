# MultiPy Overview

A powerful tool for building, testing, and analysing multiplier designs. 

# Why?

This project was initially focused on how [saturation](https://en.wikipedia.org/wiki/Saturation_arithmetic) allows for the optimisation of a combinational [multiplier](https://en.wikipedia.org/wiki/Binary_multiplier). Once saturation is introduced, calculating the ceiling, or overflow, becomes extremely fast for one range of inputs. Another range always produces values within the extremes. The remaining range of inputs may or may not fall outside the extremes. Finding ways to predict if a given input results in an overflow, as early as possible, will result in faster calculations.

Generating and analysing designs by hand is labour intensive even for small datasets. For entire [truth tables](https://en.wikipedia.org/wiki/Truth_table), this becomes close to impossible after 8-bits.

# Algorithms

The first "stage" of s combinational multiplier creates all possible partial products. These producs are then reduced across multiple stages using a range of methods. Eventually all products are reduced to one output.

A [Wallice tree](https://en.wikipedia.org/wiki/Wallice_tree) is one of many multplication stategies. Let's multiply 11 * 12: 

```
11 * 12 -> 0b1011 * 0b1100
```

Can be represented like so:
```
   [ S0:AND ]  ->  [ S1:ADD ]  ->  [ S2:ADD ]
        1011      
   [____0000] 0       
   [___0000_] 0    [__000000] 
   [__1011__] 1   
   [_1011___] 1    [100001__]      [10000100]
   ----------         
0b [10000100] -> 132
```

This is simplified and only 4-bits, but you get the idea. First partial products "fan out" and then reduced in subsequent layers.

Note that for any multiplication the output can be upto **2x** the input width.


## Saturation

Using the 11 * 12 example above, if the output was saturated to 4-bits, the result would be 15 since the maximum value is 0b1111 -> 15.
Typically, saturation restricts the output bit width to the input bit width: x-bits --> 2x-bits -(clamp)-> x-bits. Multiplications which produce an [overflow](https://en.wikipedia.org/wiki/Integer_overflow) trigger a signal to flood the output bits to 1, resulting in the maximum value of the bit width. 

As demonstrated in the example above:
```
11 * 12 -> 0b1011 * 0b1100 -> 0b10000100 -[Clamp=4b]-> 0b1111
```

Most of the complex templates will be directed to find optiisation strategies to make te most of saturation. Many overflow edge cases can be found very early in the reduction process, while some are harder to isolate. MultiPy has the tools to find these tougher cases. 

  


# Analysis







# Templates





### Further Reading
