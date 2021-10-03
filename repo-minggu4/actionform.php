<html>
	<head>
		<title>Hasil Form Yang Diinputkan</title>
</head>
<body>

<?php
$nama=$_POST["nama"];
$email=$_POST["email"];
$Jurusan=$_POST["Jurusan"];
$negara=$_POST["negara"];
$box1=$_POST["box1"];
$box2=$_POST["box2"];
$box3=$_POST["box3"];
?>
<tabel border="1">
	<tr>
		<td colspan="2" align="center"><b>
	Hasil Form</b>
</td>
</tr>
<tr>
	<td>Nama :</td>
	<td> <?php echo $nama; ?> </td>
</tr>
<tr>
	<td>E-mail :</td>
	<td> <?php echo $email; ?> </td>
</tr>
<tr>
	<td>Jurusan :</td>
	<td> <?php echo $Jurusan; ?> </td>
</tr>
<tr>
	<td>Negara :</td>
	<td> <?php echo $negara; ?> </td>
</tr>
<tr>
	<td>Alat Transportasi :</td>
	<td> <?php echo $box1, ",",$box2,",",$box3; ?> </td>
</tr>
</tabel>
</body>
</html>