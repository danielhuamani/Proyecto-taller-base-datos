//funcion para paginar
function paginar(pagina, pagina_actual){

    var url_actual = window.location.search;
    var pagina_enviar = pagina;
    var estado_index = url_actual.indexOf('pag')=="-1";
    var estado_index_pag = url_actual.indexOf('&pag')=="-1";
    var estado_url = url_actual=="";
    var url_modificar = "";

    if( estado_index && estado_url){
        url_modificar = "pag="+pagina_enviar;

    }
    else{
        if(estado_index_pag && estado_index){

            url_modificar = url_actual+"&pag="+pagina_enviar;

        }
        else{

            url_modificar = url_actual.replace("pag="+pagina_actual, "pag="+pagina_enviar);


        }
    }

    return url_modificar;
}
