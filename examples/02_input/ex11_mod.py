#!/usr/bin/env python3

# ex11: Asking Questions

print("How old are you?:", end=" ")
age = int(input())

print("How tall are you?:", end=" ")
height = int(input())

print("How much do you weight:", end=" ")
weight = int(input())

rel = (height - 100) / weight

print("So, you're %d years old, %d tall and %d heavy --> %r " % (age, height, weight, rel))
