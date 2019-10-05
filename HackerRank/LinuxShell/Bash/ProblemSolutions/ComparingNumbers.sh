read X
read Y
if (( X > Y )); then
    printf "X is greater than Y"
elif (( X < Y )); then
    printf "X is less than Y"
else
    printf "X is equal to Y"
fi