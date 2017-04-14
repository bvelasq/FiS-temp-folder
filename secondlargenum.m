
function [sec_large_num] = secondlargenum(r1)
%find the 2nd largest number in an array of doubles

%attain value for how many data points are in array
n = numel(r1);
%transform array into 1 column
r_reshaped = reshape(r1,[n,1]);
%sort column from largest to smallest
r_sorted = sort(r_reshaped,'descend');
%record number in second position / the 2nd largest number
sec_large_num = r_sorted(2,1);

end
