<?php

    function getRunnerUpScore(array $array) {

        $maxNumber = max($array);

        $next = array_diff($array, [$maxNumber]);

        return max($next);

    }

    echo(getRunnerUpScore([1, 2, 5, 9])); // output: 5

