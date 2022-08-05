# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 18:55:35 2022

@author: User
"""
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()