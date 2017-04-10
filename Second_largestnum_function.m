%find the 2nd largest number in an array of doubles

%create random array of doubles
r1 = randn([25,25],'double');
%attain value for how many data points are in array
n = numel(r1);
%transform array into 1 column
r_reshaped = reshape(r1,[n,1]);
%sort column from largest to smallest
r_sorted = sort(r_reshaped,'descend');
%record number in second position / the 2nd largest number
sec_large_num = r_sorted(2,1);
%find recorded numbers position in array of doubles and record the position
[x,y] = find(r1==sec_large_num);
%display the 2nd largest number and/or the position
statement = sprintf('The second largest number is %d at [ %d, %d ]\n', sec_large_num, x, y);
disp(statement)
