program Calificaciones;
var
    materias, n, suma, promedio, calif: integer;
begin
    suma := 0;
    n := 1;
    write("Numero de materias");
    read(materias);
    while n <= materias do
    begin
        write("Calificacion ", n);
        read(calif); 
        suma := calif + suma;
        n := n+1
    end;
    promedio := suma div materias;
    write("Promedio: ", promedio);
    if promedio >= 90 then
        write ("Mencion honorifica")
    else
        if (promedio >=70) and (promedio < 90) then
            write ("Aprobado")
        else
            write("Reprobado")
end.
