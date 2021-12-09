<?php
$input = fopen("input.txt", "r") or die("Unable to open file!");

$cave = [];
while(!feof($input)) {
    $row = str_split(trim(fgets($input)));
    $r = [];
    for ($i = 0; $i < count($row); $i++) {
        array_push($r, intval($row[$i]));
    }
    array_push($cave, $r);
}
fclose($input);

function allBigger($i, $j) {
    global $cave;
    if (array_key_exists($i+1, $cave)) {
        if ($cave[$i][$j] >= $cave[$i+1][$j]) {
            return False;
        }
    }
    if (array_key_exists($i-1, $cave)) {
        if ($cave[$i][$j] >= $cave[$i-1][$j]) {
            return False;
        }
    }
    if (array_key_exists($j+1, $cave[$i])) {
        if ($cave[$i][$j] >= $cave[$i][$j+1]) {
            return False;
        }
    }
    if (array_key_exists($j-1, $cave[$i])) {
        if ($cave[$i][$j] >= $cave[$i][$j-1]) {
            return False;
        }
    }
    return True;
}

$total = 0;
$lowest = [];
for ($i = 0; $i < count($cave); $i++) {
    for ($j = 0; $j < count($cave[$i]); $j++) {
        if (allBigger($i, $j)) {
            $total += 1 + $cave[$i][$j];
            array_push($lowest, [$i, $j]);
        }
    }
}

echo "part 1: " . $total . "<br>";

// part 1: 465



function notIn($arr, $array) {
    for ($i = 0; $i < count($array); $i++) {
        if ($arr == $array[$i]) {
            return False;
        }
    }
    return True;
}

$prev = [];
function around($i, $j) {
    global $cave;
    global $prev;
    array_push($prev, [$i, $j]);
    $size = 1;
    if (array_key_exists($i+1, $cave)) {
        if ($cave[$i+1][$j] < 9 and notIn([$i+1, $j], $prev)) {
            $size += around($i+1, $j);
        }
    }
    if (array_key_exists($i-1, $cave)) {
        if ($cave[$i-1][$j] < 9 and notIn([$i-1, $j], $prev)) {
            $size += around($i-1, $j);
        }
    }
    if (array_key_exists($j+1, $cave[$i])) {
        if ($cave[$i][$j+1] < 9 and notIn([$i, $j+1], $prev)) {
            $size += around($i, $j+1);
        }
    }
    if (array_key_exists($j-1, $cave[$i])) {
        if ($cave[$i][$j-1] < 9 and notIn([$i, $j-1], $prev)) {
            $size += around($i, $j-1);
        }
    }
    return $size;
}

$basins = [];
for ($i = 0; $i < count($lowest); $i++) {
    $size = around($lowest[$i][0], $lowest[$i][1]);
    array_push($basins, $size);
}

rsort($basins);
echo "part 2: " . $basins[0] * $basins[1] * $basins[2];

// part 2: 1269555
?>
