<?php
session_start();
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Line graph</title>
    </head>
    <body>
        <label>credit <input type="checkbox"/></label>
        <label>debit <input type="checkbox"/></label>
        <label>save <input type="checkbox"/></label><br/>
        <!-- use google charts API -->
        <canvas height="200" width="200" style="border:1px solid black"></canvas>
    </body>
</html>