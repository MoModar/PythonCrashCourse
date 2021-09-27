# TRY IT YOUR SELF
# 8-16 Import:

#import user_profile

#new_member = user_profile.build_profile(
 #   'modar', 'moalla', location='kristiansand', height='175')
#print(new_member)

#from user_profile import build_profile


#new_member = user_profile.build_profile(
#    'modar', 'moalla', location='kristiansand', height='175')
#print(new_member)

#from user_profile import build_profile as bp

#new_member= bp('modar', 'moalla', adress='vardaasveien', more= 'krsi')
#print(new_member)


#import user_profile as bsp

#new_member= bsp.build_profile('modar', 'moalla', adress='vardaasveien', more= 'krsi')
#print(new_member)


from user_profile import *

new_member= build_profile('modar', 'moalla', adress='vardaasveien', more= 'krsi')
print(new_member)