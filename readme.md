# Riemann's Sums Visualizer

## Description
A Python GUI program written to help students better comprehend Riemann's Sums.

## Math
This program implements a Riemann's Sum equation, evaluating the area under the curve using given intervals for each rectangle. Using the summation of the area of n rectangles given x length based off of user input, it estimates the area under a function.

## Instructions
* Install dependencies:
  * Assuming Python is properly installed, open a command window and type:
    * `pip install pillow`
   
* In a command window run 'python introScreen.py'
* After clicking through the intro screen, fill in the input fields according to the label
* The equation currently only accepts polynomials with exponents greater than or equal to 0
  * Simply type the coefficient before each variable to express the function
    * Ex: 3 2 1 = 3x^2+2x+1
* The rest of the fields require integer inputs.

## Features
* Frame by frame animation for visual learners
* Total area for each iteration
* Auto-scaling for custom made graph

## Restrictions
* The current graphing system will have errors for iterations greater than roughly 1000 squares
  * The animation timing will have rounding errors causing overflow into the next one
