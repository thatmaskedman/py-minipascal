program multiplicar;

var x, y : integer;
begin
    x := 1;
    y := 1;
    
    while x <= 10 do
    begin
        while y <= 10  
        begin
            write(x, " x ", y, " = ", x*y);
            y := y +1;
        end;
        y := 1;
        
    x := x + 1;    
    end;
end.
