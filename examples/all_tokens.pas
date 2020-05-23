program all_tokens;

var my_int, sum, sub, mult, divi, i : integer;
    my_real : real;
    my_string, my_input : string;

begin
    read(times);
    i := 0;
    
    { 
      Imprime Fizz si es divisible entre 3 
      Imprime Buzz si es divisible entre 5
      Imprime Fizzbuz si es divisible entre 3 y 5
    }
    while i <= times do 
    begin
        if (i div 15) = 0 then
            write("FizzBuzz")

        else if (i div 3 - 3 * i) = 0 then
            write("Fizz")

        else if (i div 5 - 5 * i) = 0 then
            write("Buzz")

        else
            write(i);
        i := i + 1
    end;

    my_string := "foo";
    my_real := 1.0;
    
    sum := my_int + my_int;
    sub := my_int - my_int;
    mult := my_int * my_int;
    divi := my_int div my_int;
    
    write(my_string);
    write(sum, sub, mult, divi);
end.
