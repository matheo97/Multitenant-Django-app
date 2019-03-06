// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla1 = "#tabla_Producto"; // id
var nombre_boton_eliminar1 = $('.recuperar'); // Clase
var nombre_formulario_modal1 = "#frmRecuperar"; //id
var nombre_ventana_modal1 = "#myModal"; // id
// Fin de configuraciones


    $('document').ready(function() {
        $('.recuperar').on('click',function(e){
            e.preventDefault();
        });


        $('#frmRecupera').submit(function(e) { // catch the form's submit event
                e.preventDefault();
                $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: $(this).attr('action'), // the file to call
                success: function(response) { // on success..
                    if(response.status=="True"){
                        alert("Se envió la nueva contraseña al su correo");
                        $(nombre_ventana_modal1).modal('hide');
                        
                    }else{
                        alert("No existe el usuario!");
                        $(nombre_ventana_modal1).modal('hide');
                    };
                }
            });
            return false;
        });
    });