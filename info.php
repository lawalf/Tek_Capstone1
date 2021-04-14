<?php

$connect = mysql_connect(Local Connection 1, root, JigglyPuff1234);
if (!connect) { 
    die('Connection Failed: ' . mysql_error()); { mysql_select_db(“tractordb”, $connect);
    }

$user_info = “INSERT INTO sales_info (tractor, product code, manufacturer, extended service plan) VALUES ('$_POST[tractor]', '$_POST[product code]', '$_POST[manufacturer]', '$_POST[extended service plan]',)”;
if (!mysql_query($user_info, $connect)) {
     die('Error: ' . mysql_error()); 
    }

echo “Your information was added to the database.”;
mysql_close($connect); ?>