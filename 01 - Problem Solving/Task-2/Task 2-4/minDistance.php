<?php

    function minDistance($array) {
        $di = PHP_INT_MAX;
        for ($i = 0; $i < count($array); $i++) {
            for ($j = $i + 1; $j < count($array); $j++) {
                if ($array[$i] == $array[$j] || $j - $i < $di) {
                    $di = $i - $j;
                }
            }
        }
        return $di;
    }

    echo minDistance([2, 5, 3, 4, 5, 2]);