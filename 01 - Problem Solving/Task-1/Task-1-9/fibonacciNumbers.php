<?php

    function printFibNumbers($until) {
        $firstFib = 0;
        $secondFib = 1;

        if ($until < 1) {
            exit;
        }

        echo $firstFib . " ";
        for ($i = 1; $i < $until; $i++) {
            echo $secondFib . " "; // next number
            $next = $firstFib + $secondFib; // getting the next
            $firstFib = $secondFib; // 1 = 1
            $secondFib = $next; // get the last one
        }

    }

    printFibNumbers(8); // output: 0 1 1 2 3 5 8 13