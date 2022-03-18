<?php
  /*
   * Multiplies of 3 to 15 = [3, 6, 9, 12]
   * Multiplies of 5 to 15 = [5, 10, 15]
   */
    function countMultiplies(int $number, int $multi1 = 3, int $multi2 = 5) : int {
        $result = 0;
        for ($i = 0; $i <= $number; $i++) {
            if ($i % $multi1 === 0 || $i % $multi2 === 0) {
                $result += $i;
            }
        }
        return $result;
    }

    echo countMultiplies(15); // output: 60

