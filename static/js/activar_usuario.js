// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla1 = "#tabla_toppings"; // id
var nombre_boton_eliminar1 = $('.activar'); // Clase
var nombre_formulario_modal1 = "#frmActivarUsuario"; //id
var nombre_ventana_modal1 = "#myModal2"; // id
// Fin de configuraciones


    $('document').ready(function() {
        $('.activar').on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_codigoUsuario2').val(Pid);
            $('#modal_name2').text(name);
        });


        $('#frmActivarUsuario').submit(function(e) { // catch the form's submit event
                e.preventDefault();
                $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: $(this).attr('action'), // the file to call
                success: function(response) { // on success..
                    if(response.status=="True"){
                        alert("Se activo el usuario!");
                        location.reload();
                        
                    }else{
                        alert("Hubo un error al activar!");
                        $(nombre_ventana_modal1).modal('hide');
                    };
                }
            });
            return false;
        });
    });