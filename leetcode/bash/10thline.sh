# solution 1
awk 'NR==10' file.txt
# Solution 2
sed -n '10p' file.txt
# solution 3
counter=0
while read -r line; do
  ((counter++))
  if [ $counter -eq 10 ]; then
    echo "$line"
    break
  fi
done < input_file.txt