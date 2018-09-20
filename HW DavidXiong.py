#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework of the first four excersices 
recursion

@author: davidxiong
"""
import turtle

def summ(x):
    if x ==1:
        return x
    else:
        return x+summ(x-1)
print(summ(4))

def a(x):
    if x ==1:
        return x
    else:
        return x*a(x-1)
print(a(3))


def b(x,y):
    if y==0:
        return 1
    else:
        return x*b(x,y-1)
print(b(3,3))


def fibbonacci(n):
    if n<2:
        return 1
    else:
        return fibbonacci(n-1)+fibbonacci(n-2)
print(fibbonacci(6))


def trii(n,length):
    def tri(n,length):
        turtle.speed(20)
        turtle.setup(width=0.8,height=0.8,startx=50,starty=50)
        if n==0:
            turtle.forward(length)
        else:
            tri(n-1,length/3)
            turtle.left(90)
            tri(n-1,length/3)
            turtle.right(90)
            tri(n-1,length/3)
            turtle.right(90)
            tri(n-1,length/3)
            turtle.left(90)
            tri(n-1,length/3)
    tri(n,length)
    turtle.right(90)
    tri(n,length)
    turtle.right(90)
    tri(n,length)
    turtle.right(90)
    tri(n,length)

trii(1,200)
