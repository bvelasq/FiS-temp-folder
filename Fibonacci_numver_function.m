%base algorithm for calculating any Fibonacci Number
phi = 1.618;
prompt = 'Input position for desired Fibonacci Number ';
fib_input = input(prompt);
fib_output = (phi^fib_input-(1-phi)^fib_input)/sqrt(5);
format long
disp(fib_output)
%it seems you cannout request a position value 
%larger than 1475

%matlab can handle up to the double 1.7976e+308
%n = 1475 => 7.8312e+307