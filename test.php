<!DOCTYPE html>

<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Ace Kitchen Sink</title>
    <meta name="author" content="Fabian Jakobs">
    <!--
    Ace
      version 1.2.0
      commit  
    -->

    <link rel="stylesheet" href="demo/kitchen-sink/styles.css" type="text/css" media="screen" charset="utf-8">
    <script async="true" src="https://use.edgefonts.net/source-code-pro.js"></script>

    <link href="./doc/site/images/favicon.ico" rel="icon" type="image/x-icon">
</head>
<body>
    <?php
      function echoTerminal(){$message=shell_exec('ls -lart');
      echo message;
    }
    ?>  
<div id="optionsPanel" style="position:absolute;height:100%;width:500px">

         <input type="file" id="fileinput" /> <br>
         <input type="file" id="uploadfiles" multiple="multiple" />

 
  <div style="position: absolute; overflow: hidden; top:50px; bottom:0">
  <div style="width: 120%; height:100%; overflow-y: scroll">

  <table id="controls">
    <tr>
      <td>
        <label for="doc">Document</label>
      </td><td>
        <select id="doc" size="1">
        </select>
      </td>
    </tr>
    <tr>
      <td >
        <label for="mode">Mode</label>
      </td><td>
        <select id="mode" size="1">
        </select>
      </td>
    </tr>
    <tr>
      <td>
        <label for="split">Split</label>
      </td><td>
        <select id="split" size="1">
          <option value="none">None</option>
          <option value="below">Below</option>
          <option value="beside">Beside</option>
        </select>
      </td>
    </tr>
    <tr>
      <td >
        <label for="theme">Theme</label>
      </td><td>
        <select id="theme" size="1">
          
        </select>
      </td>
    </tr>
    <tr>
      <td>
        <label for="fontsize">Font Size</label>
      </td><td>
        <select id="fontsize" size="1">
          <option value="10px">10px</option>
          <option value="11px">11px</option>
          <option value="12px" selected="selected">12px</option>
          <option value="13px">13px</option>
          <option value="14px">14px</option>
          <option value="16px">16px</option>
          <option value="18px">18px</option>
          <option value="20px">20px</option>
          <option value="24px">24px</option>
        </select>
      </td>
    </tr>
  
    <tr>
      <td >
        <label for="keybinding">Key Binding</label>
      </td><td>
        <select id="keybinding" size="1">
          <option value="ace">Ace</option>
          <option value="vim">Vim</option>
          <option value="emacs">Emacs</option>
          <option value="custom">Custom</option>
        </select>
      </td>
    </tr>
    <tr>
      <td colspan="4">
        <input type="button" value="Run the program" onclick="getResult()">
      </td>
    </tr>
    <tr>
      <td colspan="4">
        <input type="button" value="echo" onclick="echoTerminal()">
      </td>
    </tr>
      <tr>
      <td colspan="4">
       

        <input type="button" value="saveFile" onclick="echoTerminal()">
      </td>
    </tr>

   
     <tr>
      <td >
    <p id="result"></p>

    <p id="echo"></p>
          </td>
    </tr>
    </table>
    
  
  </div>
  </div>
</div>
  <div id="editor-container"></div>




  <script src="src/ace.js" data-ace-base="src" type="text/javascript" charset="utf-8"></script>
  <script src="src/keybinding-vim.js"></script>
  <script src="src/keybinding-emacs.js"></script>
  <script src="demo/kitchen-sink/demo.js"></script>
  <script type="text/javascript" charset="utf-8">
    require("kitchen-sink/demo");
    document.getElementById('fileinput').addEventListener('change', function(){
    var file = this.files[0];
    // This code is only for demo ...
     console.log("name : " + file.name);

    console.log("size : " + file.size);

    console.log("type : " + file.type);

    console.log("date : " + file.lastModified);

}, false);

    function uploadFile(file){
    var url = 'ec2-52-88-209-108.us-west-2.compute.amazonaws.com/ace-builds/index.php';
    var xhr = new XMLHttpRequest();
    var fd = new FormData();
    xhr.open("POST", url, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Every thing ok, file uploaded
            console.log(xhr.responseText); // handle response.
        }
    };
    fd.append("upload_file", file);
    xhr.send(fd);
}

    var uploadfiles = document.querySelector('#uploadfiles');
uploadfiles.addEventListener('change', function () {
    var files = this.files;
    for(var i=0; i<files.length; i++){
        uploadFile(this.files[i]); // call the function to upload the file
    }
}, false);

    saveFile = function() {
    var contents = env.editor.getSession().getValue();
  /*  $.post("write.php", 
            {contents: contents },
            function() {
                    // add error checking
                    alert('successful save');
            }
    ); */

};



    function getResult(){
       document.getElementById("result").innerHTML = "Hello World\n" ;
}
  </script>


</body>
</html>

