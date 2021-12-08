<?php
$input = fopen("input.txt", "r") or die("Unable to open file!");

function in($str, $sub) {
    for ($j = 0; $j < strlen($sub); $j++) {
        if (!str_contains($str, $sub[$j]) and $sub[$j] != " ") {
            return False;
        }
    }
    return True;
}

$digits = array();
while (!feof($input)) {
    $inout = explode(' | ', fgets($input));
    $in = explode(' ', $inout[0]);
    $out = explode(' ', $inout[1]);

    for ($i = 0; $i < count($in); $i++) {
        $in[$i] = trim($in[$i]);
        $arr = str_split($in[$i]);
        sort($arr);
        $in[$i] = implode('', $arr);
    }
    for ($i = 0; $i < count($out); $i++) {
        $out[$i] = trim($out[$i]);
        $arr = str_split($out[$i]);
        sort($arr);
        $out[$i] = implode('', $arr);
    }
    
    $values = [];
    // known lenght
    for ($i = 0; $i < count($in); $i++) {
        $s = $in[$i];
        if (strlen($s) == 2) {
            $values[$s] = "1";
        } elseif (strlen($s) == 3) {
            $values[$s] = "7";
        } elseif (strlen($s) == 4) {
            $values[$s] = "4";
        } elseif (strlen($s) == 7) {
            $values[$s] = "8";
        }
    }
    for ($i = 0; $i < count($in); $i++) {
        $s = $in[$i];
        $seven = array_search('7', $values);
        $one = array_search('1', $values);
        $four = array_search('4', $values);
        if (strlen($s) == 5 and in($s, $seven)) {
            $values[$s] = "3";
        } elseif (strlen($s) == 6 and !in($s, $one)) {
            $values[$s] = "6";
        } elseif (strlen($s) == 6 and in($s, $four)) {
            $values[$s] = "9";
        }
    }
    for ($i = 0; $i < count($in); $i++) {
        $s = $in[$i];
        $six = array_search('6', $values);
        $nine = array_search('9', $values);
        $eight = array_search('8', $values);
        $three = array_search('3', $values);
        if (strlen($s) == 5 and !in($s, str_replace(str_split($six), ' ', $eight))) {
            $values[$s] = "5";
        } elseif (strlen($s) == 5 and $s != $three) {
            $values[$s] = "2";
        } elseif (strlen($s) == 6 and $s != $six and $s != $nine) {
            $values[$s] = "0";
        }
    }
    
    array_push($digits, [$out, $values]);
}
fclose($input);

$total = 0;
for ($i = 0; $i < count($digits); $i++) {
    $digit = "";
    for ($j = 0; $j < count($digits[$i][0]); $j++) {
        $d = $digits[$i][0][$j];
        $digit .= $digits[$i][1][$d];
    }
    $total += intval($digit);
}

echo $total;

// part 2: 1010460
?>