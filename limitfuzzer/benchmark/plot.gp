set terminal pngcairo size 1280,960
set output 'plot.png'
set datafile separator ","

# set xlabel ''
set ylabel 'Time taken (seconds)'
set title 'Time taken to generate 100000 JSON (Average of 5 runs)'
set yrange [0:*]
set style fill solid
set boxwidth 0.5
unset key

# https://stackoverflow.com/questions/62806241/dynamically-colored-bar-charts-in-gnuplot
# https://unix.stackexchange.com/questions/310921/add-y-axis-value-labels-to-gnuplot-bar-chart
plot \
"result_avg.csv" using 0:2:($0+1):xtic(1) with boxes lc variable, \
""  using 0:($2+.1):(sprintf("%3.2f",$2)) with labels notitle
