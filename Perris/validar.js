$(function()

{
    var soloNumero = '0123456789';
    var soloNombre = 'qwertyuiopasdfghjklzxcvbnm'+'QWERTYUIOPASDFGHJKLZXCVBNM ';

    $('.soloNumero').keypress(function(e)
    {

    var caracterPresionado = String.fromCharCode(e.which);
    if (soloNumero.indexOf(caracterPresionado)<0)
        return false;
        
    });

    $('.soloNombre').keypress(function(e)
    {

    var caracterPresionado = String.fromCharCode(e.which);
    if (soloNombre.indexOf(caracterPresionado)<0)
        return false;
        
    });

    $('.soloTele').keypress(function(e)
    {
    var caracteres = soloNumero + "#"; 
    var caracterPresionado = String.fromCharCode(e.which);
    if (caracteres.indexOf(caracterPresionado)<0)
        return false;
        
    });

    $('.soloApellido').keypress(function(e)
    {
    var caracteres = soloNombre + "-'"; 
    var caracterPresionado = String.fromCharCode(e.which);
    if (caracteres.indexOf(caracterPresionado)<0)
        return false;
        
    });


    $('.soloRut').keypress(function(e)
    {
    var caracteres = soloNumero + "-" + "kK"; 
    var caracterPresionado = String.fromCharCode(e.which);
    if (caracteres.indexOf(caracterPresionado)<0)
        return false;
        
    });

    $('.btnAceptar').click(function()
    {
        var email = asdas1231; /*reviasr*/
        if(!email.test($('.email').val()))
        {

            alert('mail erroneo')
            return false;
        }
           
    
    
    })

    
});



