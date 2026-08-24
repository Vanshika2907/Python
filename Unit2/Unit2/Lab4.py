'''
Write a python program to generate a 6 digit OTP using random module.
'''
import random
otp = random.randint(100000, 999999)
print("Your 6-digit OTP is:", otp)