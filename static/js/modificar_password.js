// Autor: @jqcaper
// Configuraciones Generales
var nombre_boton_eliminar1 = $('.modify'); // Clase
var nombre_formulario_modal1 = "#frmCambiarPassword"; //id
var nombre_ventana_modal1 = "#myModal"; // id
// Fin de configuraciones


    $('document').ready(function() {
        $('.modify').on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idUser').val(Pid);
            $('#passd').text(name);
        });


        $('#frmCambiarPassword').submit(function(e) { // catch the form's submit event
                e.preventDefault();
                $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: $(this).attr('action'), // the file to call
                success: function(response) { // on success..
                    if(response.status=="True"){
                        alert("Contraseña modificada! Deberás iniciar seción de nuevo");
                        location.reload();
                        
                    }else{
                        alert("Hubo un error al modificar la contraseña!");
                        $(nombre_ventana_modal1).modal('hide');
                    };
                }
            });
            return false;
        });
    });