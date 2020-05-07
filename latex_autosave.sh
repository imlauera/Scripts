#!/bin/bash
if [ ! -f $1 ]; then
        echo "No existe el archivo"
        exit
elif [ -z "$1" ]; then
        echo "Pasame algun archivo tex"
        exit
fi

Archivo_Tex="$1"
echo "Esperando cambios ..."
Fecha_Vieja=`ls -ali --time-style=full $Archivo_Tex | awk '{print $8}'`
while true
do
        Fecha_Actual="`ls -ali --time-style=full $Archivo_Tex | awk '{print $8}'`"
        if [ "$Fecha_Actual" != "$Fecha_Vieja" ]
        then
                echo -n "[*] Compilando ... ";
                sleep 0.7
                echo "" | pdflatex $Archivo_Tex > /dev/null
                echo "Listo!"
                Fecha_Vieja="$Fecha_Actual"
        fi
        sleep 0.8
done
