
$('document').ready(function()

{
	$('.Crear').on('click',function(e)
	{
		e.preventDefault();
		var mensaje = ""//Mensaje que se va a mostrar en caso de error
		var nombre = document.getElementById("nombre").value;
		var codigo = document.getElementById("codigo").value;
		var precio = document.getElementById("precio").value;
		var descripcion = document.getElementById("descripcion").value;
		var numOk = true;
	
		
		//Validación si los campos está vaciós
	
		if( nombre== null || nombre.length == 0 || /^\s+$/.test(nombre) ) 
		{
		  	mensaje+=", el nombre"; //mensaje que se arroja si el campo está vacio
		}
		if( codigo== null || codigo.length == 0 || /^\s+$/.test(codigo) ) 
		{
		  	mensaje+=",el codigo"; //mensaje que se arroja si el campo está vacio
		  	
		}
		else
		{
			if (!/^([0-9])*$/.test(codigo))
			{
				numOk = false;
		    	alert("El codigo debe ser numerico");
			}
		}
		if( precio== null || precio.length == 0 || /^\s+$/.test(precio) ) 
		{
		  	mensaje+=", el precio" ;//mensaje que se arroja si el campo está vacio
		}
		else
		{
			if (!/^([0-9])*$/.test(precio))
			{
				numOk = false;
		    	alert("El precio debe ser numerico sin puntos ni comas.");
			}
		}
		if( descripcion== null || descripcion.length == 0 || /^\s+$/.test(descripcion) ) 
		{
		  	mensaje+=", la descripcion"; //mensaje que se arroja si el campo está vacio
		}
	
		
	    //Confirmación de si existe un mensaje de error
		if( mensaje== null || mensaje.length == 0 || /^\s+$/.test(mensaje) ) {
			//si el mensaje de error está vacio
			if(numOk)
			{
		  		document.getElementById("frmCrearTopping").submit();//enviar el formulario
			}
		}
		else//de lo contrario si hay mensaje de error
		{
			var mensaje2 = "Debe proporcionar"+mensaje+" del topping."
			alert(mensaje2);//mostrar mensaje
		}
	});
	
});