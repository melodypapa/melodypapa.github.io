function output = mymatmin(matrix)
%mymatmin - find the mininum value of each column
%
% Syntax: output = mymatmin(matrix)
% Test with: 
%   mymatmin(3),
%   mymatmin([3 4 5])
%   mymatmin([3 4 5]')
% 

[rows, cols] = size(matrix);
output = zeros(1,cols);

for col = 1:cols
    output(col) = matrix(1, col);
    for row = 1:rows
        if matrix(row, col) > output(col)
            output(col) = matrix(row, col);
        end
    end
end

end
