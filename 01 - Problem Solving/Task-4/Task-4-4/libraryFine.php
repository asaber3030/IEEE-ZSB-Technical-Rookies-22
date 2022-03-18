<?php
  function calculateFine($d1, $m1, $y1, $d2, $m2, $y2) {
    $totalFine = 0;
    if ($y1 > $y2) {
      $totalFine += 10000;
    } elseif ($y1 == $y2 and $m1 > $m2) {
      $totalFine += 500 * ($m1 - $m2);
    } elseif ($y1 == $y2 and $m1 == $m2 and $d1 > $d2) {
      $totalFine += 15 * ($d1 - $d2);
    }
    return $totalFine;
  }

  echo calculateFine(14, 7, 2018, 5, 7, 2018);