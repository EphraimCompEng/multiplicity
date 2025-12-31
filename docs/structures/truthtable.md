# Truth Table


Finding edge cases is vital when optimising anything. For binary circuit, this challenge grows exponentially as more and inputs and bits are involved. To clear all possible edge cases we need to iterate through all possible inputs and make sure the circuit is behaving correctly.

For 4-bit multipliers the total search space would be 2<sup>(4 + 4)</sup>-1, 8-bit would be 2<sup>(8 + 8)</sup>-1 and so on. 


Multiplier Lab will present a given entry of a truth table in a matrix:

```
        1011
   [____0000] 0
   [___0000_] 0
   [__1011__] 1
   [_1011___] 1
   
```

Truth tables will show outputs of every stage of the multiplication:

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
