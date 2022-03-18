<?php

    function insertionSort(&$array) {
        for ($i = 0; $i < count($array); $i++) {
            $index = $array[$i];
            $j = $i - 1;
            while ($j >= 0 && $array[$j] > $index) {
                $array[$j + 1] = $array[$j];
                $j -= 1;
            }
            $array[$j + 1] = $index;
        }
        return $array;
    }


    $array = [12, 11, 13, 5, 6];

    echo "<pre>";

    print_r(insertionSort($array));

    echo "</pre>";