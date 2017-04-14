function [v] = palindrometest(pal_input)
%Function that returns true if a string is a palindrome
%palindrome - a work, phrase, or sequence that reads the 
%             same backwards as forwards
%             i.e. madam, nurses run


%turn the input string into a row of double values
pal_double = double(pal_input);
%get rid of any zeroes that may be present so they don't interfere
TF1 = pal_double(1,:) == 32; %32 = value space is turned into via 'double'
%erasing all spots where spaces are
pal_double(:,TF1) = [];

pal_int = int16(pal_double);
%flip the inputed num_string to compare with original num_string
pal_double_int = flip(pal_int);
%if statements so if non flip == flip then output true
if pal_int(1,:) == pal_double_int(1,:)
   
    v = 1;
else 
   
    v = 0;
end
end