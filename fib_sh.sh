#!/bin/bash
time_sleep=$1
input_fib=$2
out_put=1
if [ $input_fib -lt 0 ]; then
  exit 1
elif [ $input_fib -eq 0 ]; then
  let "out_put=0"
elif [ $input_fib -eq 1 ]; then
  let "out_put=1"
else
  last_value=0
  new_value=1
  i=2
  while [ $i -le $input_fib ]
  do
    let "out_put=$last_value+$new_value"
    let "last_value=$new_value"
    let "new_value=$out_put"
    let "i+=1"
  done
fi
sleep $time_sleep
echo $out_put
exit 0