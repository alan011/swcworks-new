#!/bin/bash


for i in {1..17}; do
mysql -uroot -p'swC129!83@9' -h 127.0.0.1 swc_db -e "select * from swcworks_web_swtable${i}; " | sed 's/\t/,/g' > swtable${i}.data
done
