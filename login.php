<?php
// if(isset($_POST['Username']))
    $servername = "localhost";
    $username = "sentilytics";
    $password = "";
    $databasename = "sentilytics"; 
    
    // Create a connection to the database
    $con = mysqli_connect($servername, $email, $password, $databasename);
    
    if(!$con){
        die("Connection to the database failed due to " . mysqli_connect_error());
    }                           
echo "success connecting to the db";
     // Retrieve data from the POST request
    $username = $_POST['email'];
    $password = $_POST['password'];
    
    // SQL query with placeholders to prevent SQL injection
    $sql = "INSERT INTO login ( `Username`,`Password`, `timestamp`) VALUES (`?`, `?`, current_timestamp())";

    // Prepare the SQL statement
    $stmt = $con->prepare($sql);

    if($stmt){
        // Bind parameters and execute the statement
        $stmt->bind_param("ss", $email,$password);

        if($stmt->execute()){
            echo "Successfully inserted";
        } else {
            echo "Error: " . $stmt->error;
        }

        // Close the statement
        $stmt->close();
    } else {
        echo "Error: " . $con->error;
    }
    
    // Close the connection
    $con->close();
}
?>


