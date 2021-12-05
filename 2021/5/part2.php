<?php
$input = fopen("input.txt", "r") or die("Unable to open file!");

$lines = [];
while(!feof($input)) {
    $i = preg_split('/(,| )/', fgets($input));
    array_push($lines, [intval($i[0]), intval($i[1]), intval($i[3]), intval($i[4])]);
}
fclose($input);

$grid = [];
for ($y = 0; $y < 1000; $y++) {
    array_push($grid, []);
    for ($x = 0; $x < 1000; $x++) {
        array_push($grid[$y], 0);
    }
}

for ($l = 0; $l < count($lines); $l++) {
    if ($lines[$l][0] == $lines[$l][2]) {
        $m = [$lines[$l][1], $lines[$l][3]];
        sort($m);
        for ($y = $m[0]; $y <= $m[1]; $y++) {
            $grid[$y][$lines[$l][0]]++;
        }
    } elseif ($lines[$l][1] == $lines[$l][3]) {
        $m = [$lines[$l][0], $lines[$l][2]];
        sort($m);
        for ($x = $m[0]; $x <= $m[1]; $x++) {
            $grid[$lines[$l][1]][$x]++;
        }
    } else {
        $x1 = $lines[$l][0];
        $y1 = $lines[$l][1];
        $x2 = $lines[$l][2];
        $y2 = $lines[$l][3];
        while ($x1 != $x2) {
            $grid[$y1][$x1]++;
            ($x1 < $x2) ? $x1++ : $x1--;
            ($y1 < $y2) ? $y1++ : $y1--;
        }
        $grid[$y1][$x1]++;
    }
}

$total = 0;
for ($y = 0; $y < count($grid); $y++) {
    for ($x = 0; $x < count($grid[0]); $x++) {
        if ($grid[$y][$x] >= 2) {
            $total++;
        }
    }
}
echo $total;

// part 2: 21577
?>
