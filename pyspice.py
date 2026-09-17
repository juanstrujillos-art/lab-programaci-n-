Circuit: * divisor de voltaje

ngspice 11 -> op
Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver

No. of Data Rows : 1
ngspice 12 -> listing
    * divisor de voltaje

    2 : .global gnd
    3 : v1 in 0 dc 10
    4 : r1 in out 1k
    5 : r2 out 0 1k
    6 : .op
    8 : .end
ngspice 13 -> run
Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver

No. of Data Rows : 1
ngspice 14 -> print v(out)
v(out) = 5.000000e+00
