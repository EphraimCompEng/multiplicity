# Logical AND Matrix

The starting point of a multiplication algorithm. 


## Structure

The AND matrix is a 2D array of bits that represents the completed AND-SHIFT operation for two input values. Each element in the matrix is the result of the AND operation between the corresponding bits of the two input values. An 8-bit AND matrix will produce 8 partial products. 

```
        b15-b8 | b7-b0
        -------+-------- 
               |XXXXXXXX
        -------|00000000 Y
        ------0|0000000- Y
        -----00|000000-- Y
        ----000|00000--- Y
        ---0000|0000---- Y 
        --00000|000----- Y
        -000000|00------ Y
        0000000|0------- Y
```

# Partial products
