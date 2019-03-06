
$('document').ready(function()

{
	$('.Comprar').on('click',function(e)
	{
		e.preventDefault();
		var mensaje = ""//Mensaje que se va a mostrar en caso de error
		var nombre = document.getElementById("nombre").value;
		var dir = document.getElementById("dir").value;
		var tar = document.getElementById("tar").value;
		var numOk = true;
	
		
		//Validación si los campos está vaciós
	
		if( nombre== null || nombre.length == 0 || /^\s+$/.test(nombre) ) 
		{
		  	mensaje+=", el nombre"; //mensaje que se arroja si el campo está vacio
		}
		if( tar== null || tar.length == 0 || /^\s+$/.test(tar) ) 
		{
		  	mensaje+=", la tarjeta"; //mensaje que se arroja si el campo está vacio
		  	
		}
		else
		{
			if (!/^([0-9])*$/.test(tar))
			{
				numOk = false;
		    	alert("La tarjeta debe ser numerica");
			}
		}
		
		if( dir== null || dir.length == 0 || /^\s+$/.test(dir) ) 
		{
		  	mensaje+=", la direcciòn"; //mensaje que se arroja si el campo está vacio
		}
	
		
	    //Confirmación de si existe un mensaje de error
		if( mensaje== null || mensaje.length == 0 || /^\s+$/.test(mensaje) ) {
			//si el mensaje de error está vacio
			if(numOk)
			{
				
		  		document.getElementById("frmComprar").submit();//enviar el formulario
			}
		}
		else//de lo contrario si hay mensaje de error
		{
			var mensaje2 = "Debe proporcionar"+mensaje+" para comprar."
			alert(mensaje2);//mostrar mensaje
		}
	});
	
});