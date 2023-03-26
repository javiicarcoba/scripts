/*
¿Cómo sabemos que necesitamos un bucle aquí? Porque cada 3km se da un caramelo, es algo repetitivo.
¿Cuál es el punto de partida del bucle? 0, debido a que empezamos sin correr.
¿Cuándo debe detenerse el bucle? En el momento que lleguemos a los 10km.
¿Cómo sabrá parar? Pondremos un contador que cuente cuántos km llevamos para parar cuando este sea igual a 10.
¿Cuál es el incremento para cada iteración del bucle? +1
¿Qué variables necesitamos? Una variable contador.
*/
 var km_recorridos=0, velocidad=9;

 while(km_recorridos<=10){
    if(km_recorridos!=0 && km_recorridos%3 == 0 && velocidad>=9)
        console.log("Toma tu caramelo");
    km_recorridos++;
 }

 console.log("¡Completaste los 10km!");