	function ajax_crear_idioma(arreglo_idiomas, url_idioma_crear, contador_listado){
        $.ajax({
            url: url_idioma_crear,
            type: 'POST',
            data: {'idioma': JSON.stringify(arreglo_idiomas)},

        })
        .done(function(data) {
            console.log(data)
            if (data!='error'){
                $(".formulario_inicial").fadeOut('500', function() {
                    $(this).remove()
                });
                $.each(data.listado, function(index, val) {
                     /* iterate through array or object */
                    contador_listado = contador_listado + 1
                    html = '<tr role="row" class="odd row-fila" ><td class="sorting_1">'+contador_listado+'</td><td class="nombre_idioma"><h5>'+val.nombre+'</h5><input type="hidden" data-pk="'+val.id+'" class="input_modificar"></td><td><button type="button" class="btn btn-primary modficar_idioma">Modificar</button><button type="button" class="btn btn-success guardar_idioma guardar_none">Guardar</button></td></tr>'
                    $(".listado_idioma").append(html)
                });
            }
        })
	}
	function ajax_actualizar_idioma(padre_fila, texto, pk, url_idioma_actualizar){
		console.log("entro")
        if (texto) {
            $.ajax({
                url: url_idioma_actualizar,
                type: 'POST',
                data: {
                    'idioma_pk': pk,
                    'idioma_nombre': texto
                },
            })
            .done(function(data) {
                if (data.status == "ok") {
                    $(".actualizo_correctamente").addClass('actualizo_fade')
                    padre_fila.find('.nombre_idioma h5').text(texto)
                    padre_fila.find('.input_modificar').attr('type', 'hidden');
                    padre_fila.find('.guardar_idioma').removeClass('guardar_block').addClass('guardar_none')
                    padre_fila.find('.modficar_idioma').removeClass('guardar_none')
                    setTimeout(function(){
                      $(".actualizo_correctamente").removeClass('actualizo_fade')
                    }, 2000);
                }
            })
        };

	}




