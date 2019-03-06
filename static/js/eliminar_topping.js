// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla1 = "#tabla_toppings"; // id
var nombre_boton_eliminar1 = $('.delete'); // Clase
var nombre_formulario_modal1 = "#frmEliminarTopping"; //id
var nombre_ventana_modal1 = "#myModal"; // id
// Fin de configuraciones


    $('document').ready(function() {
        $('.delete').on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_codigoTopping').val(Pid);
            $('#modal_name').text(name);
        });


        $('#frmEliminarTopping').submit(function(e) { // catch the form's submit event
                e.preventDefault();
                $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: $(this).attr('action'), // the file to call
                success: function(response) { // on success..
                    if(response.status=="True"){
                        alert("Eliminado!");
                        var idTopping = response.codigoTopping;
                        var elementos= $(nombre_tabla1+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idTopping).remove();
                            $(nombre_ventana_modal1).modal('hide');
                        }
                        
                    }else{
                        alert("Hubo un error al eliminar!");
                        $(nombre_ventana_modal1).modal('hide');
                    };
                }
            });
            return false;
        });
    });