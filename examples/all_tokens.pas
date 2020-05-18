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
    divi := my_int div my_int;

    foo := -3;

    i := 0;

    {Three iteration loop}
    while i <= 3 do 
    begin
        if (i = 0) then 
            write("zero")
        else if (i = 1) then
            write("one")
        else
            write("two");
        i :=  i + 1;
    end
    {Echo user's input}
end.
