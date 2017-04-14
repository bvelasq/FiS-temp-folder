%base algorithm for calculating any Fibonacci Number
function [fib_output] = fibnum(fib_input)
%this function will output the fibonacci number using the input as the
%position value that is requested

%define phi
phi = 1.618;

fib_output = (phi.^fib_input-(1-phi).^fib_input)/sqrt(5);
fib_output = round(fib_output);
end
