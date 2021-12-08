<?php
$input = fopen("input.txt", "r") or die("Unable to open file!");

$digits = [];
while(!feof($input)) {
    $i = explode(' | ', fgets($input));
    $i = explode(' ', $i[1]);
    $digits = array_merge($digits, $i);
}
fclose($input);

$total = 0;
for ($i = 0; $i < count($digits); $i++) {
    $d = strlen(trim($digits[$i]));
    if ($d == 2 or $d == 3 or $d == 4 or $d == 7) {
        $total++;
    }
}

echo $total;

// part 1: 493
