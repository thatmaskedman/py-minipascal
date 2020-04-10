program all_tokens;

var my_int, sum, sub, mult, i : integer;
    my_real : real;
    my_string, my_input : string;

begin
    my_string := "foo";
    my_real := 1.0;

    sum := my_int + my_int;
    sub := my_int - my_int;
    mult := my_int * my_int;

    i := 0;
    {Three way loop}
    while i <= 3 do
    begin
        if (i = 0) = true then
            begin
                write("Zero");
            end;
        else if (i = 0) = false then
            begin
                write("one");
            end;
        else
        begin
            write("Not one");
        end;
         i :=  i + 1;
    end;

    {Echo user's input}
    my_input := read();
    write(my_input)
end.
