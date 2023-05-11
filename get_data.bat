:: execute N time graph_part_3 a b c with different parameters and store the results in a file BATCH SCRIPT
:: a b c are the parameters of the graph_part_3 program
:: N is the number of times the program is executed
:: the results are stored in a file
@echo off
setlocal EnableDelayedExpansion
set /a N=100
set /a a=1000
set /a v=8
set /a c=2

FOR /L %%G IN (1,1,%N%) DO (
    ::display a
    echo !a!
    ::execute graph_part_3
    python graph_part_3.py !a! !v! !c! >> results.txt
    ::increase a
    ::set /a a+=100
    ::increase b
    ::set /a v*=5
    ::increase c
    ::set /a c*=2

)

