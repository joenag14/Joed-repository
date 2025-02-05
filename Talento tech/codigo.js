 // Se pone prompt para que el usuario interactue e ingrese información.
/* let n1 = parseInt(prompt("ingresa el número 1"));
 /* parseInt sirve para cambiar el tipo de dato,
 en este caso, pasar un string a entero
let n2 = parseInt(prompt("ingresa el número 2"));

suma = n1+n2
// console.log sirve para imprimir en consola
console.log(suma)
// alert funciona para imprimir en la página.  
alert("La suma es: " + suma)

let edad = parseInt (prompt("Ingresa tu edad:"));

if (edad>17){ alert(`tu edad es: ${edad}, eres mayor de edad`)}
 else{ alert (`Tu edad es: ${edad}, eres menor de edad`)}

 let edad1= parseInt (prompt(" ingrea tu edad:")); 

 if (edad1 <=7){
    alert(`Tu edad es de: ${edad1}\n y tu tipo de documento 
        es registro civil`)}
    else if(edad<=17){
            alert(`Tu edad es de: ${edad1}\n y tu tipo de documento 
        es tarjeta de identidad`)
        }
    else{
        alert(`Tu edad es de: ${edad1}\n y tu tipo de documento 
            es cedula de ciudadanía`) 

    }    */

           /* let numero1= parseInt(prompt("ingresa el número 1:"));
            let numero2= parseInt(prompt("ingresa el número 2:"));
            let numero3= parseInt(prompt("ingresa el número 3:"));

if (numero1>=numero2 && numero1>=numero3 && numero2>=numero3) {
    alert(`el orden es: ${numero1}, ${numero2}, ${numero3}`)}
else if  (numero2>=numero1 && numero2>=numero3 && numero1>=numero3) {
    alert(`el orden es: ${numero2}, ${numero1}, ${numero3}`)}
    //Para que salga en secuencia, simplemente separa las variable con ","
 else if (numero3>=numero2 && numero3>=numero1 && numero2>=numero1) {
    alert(`el orden es: \n${numero3} \n${numero2} \n${numero1}`)}
    // para que salga en una lista recuerda poner /n antes de la variable.
    // si luego de la n se agrega además un número al imprimirse en pantalla, se mostrara como una lista númerada. */

   /* let numero = parseInt(prompt("Escribe un número:"));
    switch (numero){ 
        case 1: alert (`seleccionaste la opción 1`);
        break;
        case 2: alert (`seleccionaste la opción 2`);
        break;
        case 3: alert (`seleccionaste la opción 3`);
        break;
        default: alert(`opción no válida`);
        break;
    } */
 
   /* let proteina= prompt ("Ingrese que proteína desea:")
        switch (proteina){
          case "cerdo": 
          let preparacion1 =prompt ("¿Que preparación prefieres?")
          preparacion1 = preparacion1.toLocaleLowerCase();
           //*para que idenrtifique los datos ingresados sin importar si son caracteres mayuscula o 
           minuscula se pone "toLocaleLowerCase()"//
           switch (preparacion1) {
           case "frito": alert(`sellecionaste cerdo frito`);
            break; 
           case "asado": alert(`sellecionaste cerdo asado`);
            break;
           default: alert (`opción no valida`)
            break;
               }
          break;       
        case "pollo": 
        let preparacion2 = prompt ("¿Que preparación prefieres?")
        preparacion2 = preparacion2.toLocaleLowerCase();
        switch (preparacion2) {
        case "frito": alert(`sellecionaste pollo frito`);
        break; 
        case "asado": alert(`sellecionaste pollo asado`);
        break;
        default: alert (`opción no valida`)
        break;
           }    
        break;
        case "res":
        let preparacion3 =prompt ("¿Que preparación prefieres?")
        preparacion1 = preparacion1.toLocaleLowerCase();
        switch (preparacion3) {
        case "frito": alert(`sellecionaste res frito`);
        break; 
        case "asado": alert(`sellecionaste res asado`);
        break;
        default: alert (`opción no valida`)
        break;
             }   
        break;
        default: alert (`opción invalida`);
        break;   
            }*/
for (let i=10; i>=0;i--){
    alert(`valor de i: ${i}`)
}

