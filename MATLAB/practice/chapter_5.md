# Chapter 5

## Practice 5.1

> Write a for loop that will print a column of five ⁎’s.

### Answer to 5.1

```MATLAB
for loop = 1:5
   fprintf('*\n')
end
```

## Practice 5.2

> Write a script prodnnums that is similar to the sumnnums script, but will calculate and print the product of the numbers entered by the user.

### Answer to 5.2

```MATLAB
function result = prodnnums(n)
% prodnnums results the product of  the n numbers entered by the user
% Format of call: prodnnums(n)
    result = 1;
    for loop = 1:n
        number = input('Please enter a number:');
        result = result * number;
    end % for

end % function
```

## Practice 5.3

> For each of the following (they are separate), determine what would be printed. Then, check your answers by trying them in MATLAB.

```MATLAB
mat = [7 11 3; 3:5];
[r, c] = size(mat);
for i = 1:r
   fprintf('The sum is %d\n', sum(mat(i,:)))
end
```

### Answer 5.3

> The sum is 21
> The sum is 12

- - - - - - - - - - - - - - - - - - - - - - - - - - -

```MATLAB
for i = 1:2
   fprintf('%d: ', i)
   for j = 1:4
     fprintf('%d ', j)
   end
   fprintf('\n')
end
```

> 1: 1 2 3 4
>
> 2: 1 2 3 4

## Practice 5.4

> Write a function mymatmin that finds the minimum value in each column of a matrix argument and returns a vector of the column minimums. Use the programming method. An example of calling the function follows:

```MATLAB
>> mat = randi(20,3,4)
mat =
    15  19  17   5
     6  14  13  13
     9   5   3  13

>> mymatmin(mat)
ans =
    6  5  3  5
```

### Answer to 5.4

```MATLAB
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
```

## Practice 5.5

> Write a script avenegnum that will repeat the process of prompting the user for negative numbers, until the user enters a zero or positive number, as just shown. Instead of echo-printing them, however, the script will print the average (of just the negative numbers). If no negative numbers are entered, the script will print an error message instead of the average. Use the programming method. Examples of executing this script follow:

```MATLAB
 >> avenegnum
 Enter a negative number: 5
 No negative numbers to average.
 >> avenegnum
 Enter a negative number: -8
 Enter a negative number: -3
 Enter a negative number: -4
 Enter a negative number: 6
 The average was -5.00
```

### Answer to 5.5

```MATLAB
function avenegnum()
% Prompt the user for negative numbers until the suer enters a zero or positive number.
% Then calaculate the average of these numbers
% Syntax: avenegnum()

sum_of_num = 0;
count_of_num = 0;
inputnum = input('Please enter the negative number: ');
while(inputnum < 0)
    sum_of_num = sum_of_num + inputnum;
    count_of_num  = count_of_num + 1;
    inputnum = input('Please enter the negative number: ');
end

if (count_of_num == 0)
    fprintf('No negative numbers to average.\n');
else
    fprintf("The average was %.2f. \n", sum_of_num / count_of_num);
end

end
```

## Practice 5.6

> Modify the script readoneposint to read n positive integers, instead of just one.

### Answer to Practice 5.6

```MATLAB
function result = practice_5_6(n)
%readnposint - read n positve integers.
%
% Syntax: result = readnposint(n)

for loop = 1:n
    inputnum = input('Please enter a positive integer: ');
    num2 = int32(inputnum);
    while num2 ~= inputnum || num2 < 0
        inputnum = input('Invalid! Please neter a postive integer: ');
        num2 = int32(inputnum);
    end % while
    fprintf('Thanks, you entered a %d \n', inputnum);
end
```

## Practice 5.7

> Write a function that imitates the cumprod function. Use the method of preallocating the output vector.

### Answer to the practice 5.7

```MATLAB
function result = practice_5_7(vector)
%practice_5_7 - imitates the cumprod function. Use the method of preallocating the output vector
%
% Syntax: result = cumprod(vector)

result = ones(size(vector));

intermediate_result = 1;
for loop = 1: length(vector)
    intermediate_result = intermediate_result * vector(loop);
    result(loop) = intermediate_result;
end % for

end
```

## Practice 5.8

> Modify the function matcolsum. Create a function matrowsum to calculate and return a vector of all of the row sums instead of column sums. For example, calling it and passing the mat variable above would result in the following:

```MATLAB
 >> matrowsum(mat)
 ans =
    12   14
```

### Answer to the practice 5.8

```MATLAB
function output = matrowsum(matrix)
%matrowsum - calculate and return a vector of all of the row sums.
%
% Syntax: output = matrowsum(matrix)

[rows, cols] = size(matrix);
output = zeros(1:rows);
for row = 1: rows
    for col = 1:cols
        output(row) = output(row) + matrix(row, col);
    end
end

end
```

## Practice 5.9

> Call the function testvecgtnii, passing a vector and a value for n. Use MATLAB code to count how many values in the vector were greater than n.

## Practice 5.10

> Vectorize the following (rewrite the code efficiently):

```MATLAB
i = 0
for inc = 0: 0.5: 3
    i = i + 1;
    myvec(i) = sqrt(inc);
end
- - - - - - - - - - - - - - - - - - - - - - - - - -
[r, c] = size(mat);
newmat = zeros(r,c);
for i = 1:r
    for j = 1:c
        newmat(i,j) = sign(mat(i,j));
    end
end
```

### Answer to 5.10

```MATLAB
myvec2 = zeros(1,7);
for loop = 0:6
    myvec2(loop + 1) = sqrt(loop/2);
    %disp(sqrt(loop/2))
end
-------------------------------------
newmat = sign(mat);
```