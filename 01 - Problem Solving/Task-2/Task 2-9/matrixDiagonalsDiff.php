<?php

    function diffDiagonals($matrix) {

        $valueOne = 0;
        $valueTwo = 0;

        for ($i = 0; $i < count($matrix); $i++) {
            for ($j = 0; $j < count($matrix); $j++) {
                # Primary diagonal sum
                if ($i == $j) {
                    $valueOne += $matrix[$i][$j];
                }
                # Secondary diagonals sum
                if ($i == count($matrix) - $j - 1) {
                    $valueTwo += $matrix[$i][$j];
                }
            }
        }

        return abs($valueOne - $valueTwo); // absolute value

    }

    $arr = [
        array(1, 2, 3),
        array(4 , 5, 6),
        array(9, 8, 9)
    ];

    echo diffDiagonals($arr);

