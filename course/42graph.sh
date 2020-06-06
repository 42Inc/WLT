#!/usr/bin/gnuplot
set terminal png size 1920,1080 enhanced font 'Arial, 16'

set style line 1 linecolor rgb 'red' linetype 1 linewidth 2
set style line 2 linecolor rgb 'blue' linetype 1 linewidth 2
set style line 3 linecolor rgb 'green' linetype 1 linewidth 2
set style line 4 linecolor rgb 'cyan' linetype 1 linewidth 2

set border linewidth 1
set key top left
set grid
set mytics
set mxtics
set format y "%.0f"
set xlabel "t" font "Arial, 16"
set format x "%.0f"
set ylabel "n" font "Arial, 16"
set xtics font "Arial, 12"
set ytics font "Arial, 12"
set rmargin 4
set tmargin 2

set output 'graph.png'
plot "graph.dat" using 1:2 title "PL" with linespoints ls 1,\
     "graph1.dat" using 1:2 title "PLU" with linespoints ls 2,\
     "graph2.dat" using 1:2 title "PLD" with linespoints ls 4