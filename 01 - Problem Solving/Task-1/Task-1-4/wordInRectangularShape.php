<?php
    function rectangularWord($text) {

        for ($i = 0; $i <= 17; $i++) {
            echo "*";
        }
        echo "\n";
        foreach (explode(" ", $text) as $word) {
            echo "*\t"  . $word . "\t *" . "<br>";
        }

        for ($i = 0; $i <= 17; $i++) {
            echo "*";
        }

    }

    echo "<pre>";
        rectangularWord("Hello world in a frame!");
    echo "</pre>";