<?php
   if ($_POST['action']== 'call_this'){
   $msg = shell_exec ('ls -lart');
   $file = 'a.txt';
   $current = file_get_contents($file);
   $current .= $msg;
   file_put_contents($file, $current);
}
   ?>
