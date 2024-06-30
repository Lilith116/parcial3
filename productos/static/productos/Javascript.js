function abrirmodal(){
    $('#exampleModal2').modal('show');
};

$(document).ready(function(){
    $("#boletinform").submit(function(event){
        event.preventDefault();

        var email = $("#email").val().trim();
        

        if(email.length <5 || email.length > 25){
            alert("el email no es valido");
            return;
        }

        alert("Registro exitoso");

    });
});



$(document).ready(function(){
    $("#registroForm").submit(function(event){
        // Evitar que el formulario se envíe automáticamente
        event.preventDefault();
        
        // Realizar las validaciones
        var rut = $("#rut").val();
        var nombre = $("#nombre").val();
        var apellidoPaterno = $("#apellidoPaterno").val();
        var apellidoMaterno = $("#apellidoMaterno").val();
        var edad = $("#edad").val();
        var genero = $("#genero").val();
        var celular = $("#celular").val();

        // Rut: largo entre 9 y 10 caracteres
        if(rut.length < 9 || rut.length > 10){
            alert("El Rut debe tener entre 9 y 10 caracteres.");
            return;
        }

        // Nombre, Apellidos: largo entre 3 y 20 caracteres
        if(nombre.length < 3 || nombre.length > 20 ||
            apellidoPaterno.length < 3 || apellidoPaterno.length > 20 ||
            apellidoMaterno.length < 3 || apellidoMaterno.length > 20){
            alert("El Nombre y los Apellidos deben tener entre 3 y 20 caracteres.");
            return;
        }

        // Edad: Validación de edad 

        if(edad < 18 || edad > 100){
            alert("la edad tiene que ser mayor a 18 y menor a 100");
            return;
        }
    



        
        // Género: seleccionado
        if(genero === ""){
            alert("Por favor, seleccione un Género.");
            return;
        }

        // Celular: largo entre 9 y 12 caracteres
        if(celular.length < 9 || celular.length > 12){
            alert("El Celular debe tener entre 9 y 12 caracteres.");
            return;
        }

        // Si todas las validaciones pasan, se puede enviar el formulario
        alert("¡Registro exitoso!");
        // Aquí podrías enviar el formulario utilizando AJAX o cualquier otro método
    });
});
