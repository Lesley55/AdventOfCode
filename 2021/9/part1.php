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
for ($i = 0; $i < count($cave); $i++) {
    for ($j = 0; $j < count($cave[$i]); $j++) {
        if (allBigger($i, $j)) {
            $total += 1 + $cave[$i][$j];
        }
    }
}

echo $total;

// part 1: 465
?>