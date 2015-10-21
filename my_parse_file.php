
       <?php
         if($_POST['contents']) 
        {
        $file = 'a.js';
        // Open the file to get existing content
        $current = file_get_contents($file);
        // Append a new person to the file
        $current = $_POST['contents'];
        // Write the contents back to the file
        file_put_contents($file, $current);
       
        echo Saved;
        }
        ?> 
