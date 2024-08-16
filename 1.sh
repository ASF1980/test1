#!/bin/bash
echo "Написать bash скрипт анализа размера каждой директории и файла в текущей директории с выводом результатов в терминал, используя функции и циклы"
echo "Текущая директория:"
pwd
echo "Имеющиеся каталоги:"
du -h -Bm --max-depth=1 | sort -nr | head -n11
echo "Показать отсавшиеся директории (папки)?Y/N"
read bool
if [ $bool = Y ]; then
du -h -Bm --max-depth=1 | sort -nr | more +12
fi
sleep 3 # ПАУЗА 3 сек
echo "Содержимое директории закончилось"
sleep 3 
echo "Приступаем к дальнейшему формированию и выоду информации"
sleep 3 
echo "Читаю содержимое текущего каталога - файлы и подкаталоги"
sleep 3 
echo "Отсортировываю по убыванию размера файла/каталога"
files=$(find -mindepth 1 -maxdepth 1 -printf '%s %f\n' | sort -nr | cut -d' ' -f2-)
IFS=$'\n'
while read -r line; do
array+=("$line")
done <<< "$files"
unset IFS
len=${#array[@]}
chunk_size=10
start=0 counter=1
while :
do
chunk=("${array[@]:$start:$chunk_size}")
for fname in "${chunk[@]}" ; do
if [[ -d $fname ]]; then
type="каталог"
fsize=$(du --apparent-size -b "$fname" | cut -d\t -f1 | sed -e 's/[\t]//')
else
type="файл"
fsize=$(stat -c%s "$fname")
fi
echo $counter: "$fname [$type, $fsize байт(а,ов)]" # вывод информации
let "counter++"
done
let "start+=chunk_size"
if [ $start -ge $len ]; then break; fi
read -p "Вывести оставшееся содержимое (y/n)?: " resp
if [ -z $resp ] || [ $resp != y ]; then break; fi # если ответ пустой или Enter или не y, то выходим из цикла

done
read # чтоб не закрывался терминал после отработке скрипта