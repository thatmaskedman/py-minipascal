program all_tokens;

my_int := int;
my_real := real;
my_string := string;
my_input := string

begin
    my_string := "test";
    my_real = 1.0;

    while my_int <= 10 do
    begin
        if my_int = 1 or true then
            begin
                write("One");
            end;
        else
            begin
                write("Not one");
            end;

        my_int := my_int + 1;
        my_input := read();
    end

end.
