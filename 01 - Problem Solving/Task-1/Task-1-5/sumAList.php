<?php

function sumListUsingWhileLoop(int $arrayLength, array $array) {
    $counter = 0;
    $sum = 0;
    while ($counter < $arrayLength) {
        $sum += $array[$counter];
        $counter++;
    }
    return $sum;
}

function sumListUsingForLoop(int $len, array $array) {
    $sum = 0;
    for ($i = 0; $i < $len; $i++) {
        $sum += $array[$i];
    }
    return $sum;
}

function sumListUsingRecursion( int $len, array $array) {
    if ($len <= 0) {
        return 0;
    }
    return (
        sumListUsingRecursion($len - 1, $array) +
        $array[$len - 1]
    );
}

$sum = [5, 8, 4];

echo sumListUsingWhileLoop(3, $sum) . '<br>';
echo sumListUsingForLoop(3, $sum) . '<br>';
echo sumListUsingRecursion(3, $sum);

// Note: if you will run this script in something other than browser such as online editors the result will be something like that: 17<br>17<br>17<br>
