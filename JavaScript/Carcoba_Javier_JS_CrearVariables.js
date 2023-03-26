//Se crearán las variables edad y altura para controlar los requisitos mínimos.
var edad=1;
var altura=0.52;

if(edad>=10 || altura>=0.52){ //se utilizan los pipes para que la condicionante sea de tipo OR, se cumple una u otra
    console.log("¡Súbete, chico!");
}else{
    console.log("Lo siento, chico. Tal vez el próximo año");
}