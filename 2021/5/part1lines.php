<?php
$input = fopen("input.txt", "r") or die("Unable to open file!");

$coords = [];
while(!feof($input)) {
    $i = preg_split('/(,| )/', fgets($input));
    array_push($coords, [intval($i[0]), intval($i[1]), intval($i[3]), intval($i[4])]);
}
fclose($input);

$total = 0;
for ($y = 0; $y < 1000; $y++) {
    for ($x = 0; $x < 1000; $x++) {
        $found = 0;
        for ($j = 0; $j < count($coords); $j++) {
            if ($coords[$j][0] == $coords[$j][2] and $coords[$j][0] == $x) {
                $m = [$coords[$j][1], $coords[$j][3]];
                sort($m);
                if ($m[0] <= $y and $y <= $m[1]) {
                    $found++;
                }
            } elseif ($coords[$j][1] == $coords[$j][3] and $coords[$j][1] == $y) {
                $m = [$coords[$j][0], $coords[$j][2]];
                sort($m);
                if ($m[0] <= $x and $x <= $m[1]) {
                    $found++;
                }
            }
            if (2 <= $found) {
                $total++;
                break;
            }
        }
    }
}
echo $total;

// part 1: 8060
?>
