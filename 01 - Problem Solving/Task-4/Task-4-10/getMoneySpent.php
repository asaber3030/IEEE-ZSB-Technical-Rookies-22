<?php

    function getMoneySpent($keyboards, $drives, $budget) {
      $total = max($keyboards) + max($drives);
      if ($total <= $budget) {
        return $total;
      } else {
        return -1;
      }
    }

    echo getMoneySpent([10, 2, 3], [3, 1], 60);