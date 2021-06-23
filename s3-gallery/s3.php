<?php
echo "<h1><center><img width='100' height='100' src='radon.png' /> Weather News <img width='100' height='100' src='sodalite.png' /></h1></center><hr><br />";
$run = exec('/usr/bin/python3 /var/www/html/s3.py 2>&1');
$files = glob("files/*.jp*g");
for ($i = 0; $i < count($files); $i++) {
    $image = $files[$i]; echo basename($image) . "<br />";
    echo "<img height='100' src='".$image."' />"."<br /><br />";
} ?>
