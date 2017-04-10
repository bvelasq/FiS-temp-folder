%Function that returns true if a string is a palindrome
%palindrome - a work, phrase, or sequence that reads the 
%             same backwards as forwards
%             i.e. madam, nurses run

%prompt user for a string to check if it is a palindrome
pal_prompt = 'input string to check for palindrome trait ';
%store the user input as a string
pal_input = input(pal_prompt,'s');
%turn the input string into a row of double values
pal_double = double(pal_input);
%get rid of any zeroes that may be present so they don't interfere
TF1 = pal_double(1,:) == 32; %32 = value space is turned into via 'double'
%erasing all spots where spaces are
pal_double(:,TF1) = [];
%flip the inputed num_string to compare with original num_string
pal_double_flip = flip(pal_double);
%if statements so if non flip == flip then output true
if pal_double(1,:) == pal_double_flip(1,:)
    %pal_y = ' is a palindrome';
    %pal_ans = strcat(pal_input,pal_y);
    %disp(pal_ans);
    disp('true');
else 
    %pal_n = ' is not a palindrome';
    %pal_ans = strcat(pal_input,pal_n);
    %disp(pal_ans);
    disp('false');
end