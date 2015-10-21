
       <?php
         if($_POST['path']) 
        {
        $file = $_POST['path'];
        // Open the file to get existing content
        $current = file_get_contents($file);
        // Append a new person to the file
        $current = $_POST['contents'];
        // Write the contents back to the file
        file_put_contents($file, $current);
       
        echo Savedto;
        }
        ?> 
