#! /bin/sh 
set -e

if [ "$2" = "cpp" ]; then
  compiler='g++-11'
  opt='-lm -O3'
  exe='-o'

  echo "指定されたファイルは$1.$2です"
  echo "コンパイルオプションは"
  echo "$compiler $opt $1.$2 $exe $1 "

  $compiler $opt $1.$2 $exe $1

  echo "conpile end"
  echo "program start"

  ./$1

elif [ "$2" = "py" ]; then

  compiler='python'
  echo "指定されたファイルは$1です"
  echo "コンパイルオプションは"
  echo "$compiler $1.$2 "

  $compiler $1.$2

else
  echo "error"
fi