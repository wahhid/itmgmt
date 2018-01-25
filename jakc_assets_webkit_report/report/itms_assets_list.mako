<html>
<head>
    <style type="text/css">
    	${css}
    </style>
</head>
<body> 
	<table width="100%" border=1>
		<tr>
			<th>Barcode</th>
			<th>Name</th>
			<th>type</th>
			<th>Company</th>
			<th>Department</th>
			<th>PI Date</th>
		</tr>

%for o in objects :
		<tr>	
			<td>${o.barcode}</td>
			<td>${o.name}</td>
			<td>${o.type.name}</td>
			<td>${o.company.name}</td>
			<td>${o.department.name}</td>
			<td>${o.pi_date}</td>
		</tr>
%endfor
	</table>

</body>
</html>