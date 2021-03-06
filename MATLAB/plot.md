# Plot

## Graph 2D

enter the `help graph2d` to display all the two dimensional graph functions.

### The Plot Function

Draw a point (100, 200) on the plot

```MATLAB
% create coordinate variables and plot a red '*'
x = 100;
y = 200;
plot(x, y, 'r*');
```

Change the axes and label (x: 50 - 160; y: 100 - 300). In the call to the **axis** function, the first two values of the vector are the minimum and maximum for the x-axis, and the last two values are the minimum vand maximum for the y-axis.

```MATLAB
axis([50 160 100 300]);
xlabel('Time');
ylabel('Money');
```

Put the title on the plot

```MATLAB
title('Time and Money');
```

Draw more than one point on the plot

```MATLAB
x = 1:2:12;
y = randi([1, 20], 1, 6);
plot(x, y);
```

Draw the point without x axis

```MATLAB
y = randi([1, 20], 1, 6);
plot(y);
```

### How to customize Plot with color, symobl and line styles

Line color:

| Code        | Color         |
| ------------|:-------------:|
| b           |  blue         |
| g           |  green        |
| r           |  red          |
| c           |  cyan         |
| m           |  magenta      |
| y           |  yellow       |
| k           |  black        |
| w           |  white        |

Plot symbols (markers)

| Code        | Marker           |
| ------------|:----------------:|
| .           |  point           |
| o           |  circle          |
| x           |  x-mark          |
| +           |  plus            |
| *           |  star            |
| s           |  square          |
| d           |  diamond         |
| v           |  down triangle   |
| ^           |  up triangle     |
| <           |  left triangle   |
| >           |  right triangle  |
| p           |  pentagram       |
| h           |  hexagram        |

Line types

| Code        | Line Type        |
| ------------|:----------------:|
| -           |  solid           |
| :           |  dotted          |
| -.          |  dash dot        |
| --          |  no line         |

### Simple Related Plot Functions

* **clf**

    clears the Figure Window by removing everything from it.

* **figure**

    creates a new, empty Figure Window when called without any arguments.

* **hold**

    toggles to freeze the current graph in the Figure Window.

* **legend**

    displays strings or character vectors passed to it in a legend box in the Figure Window.

* **grid**

    toggles to display grid lines on a graph or not.

### subplot function

Subplot creates a matrix of plots in the current Figure Window.

Three arguments are passed to it in the form subplot(r,c,n), where r and c are the dimensions of the matrix and n is the number of the particular plot within this matrix.

## Graph 3D

enter the `help graph3d` to display all the three dimensional graph functions.