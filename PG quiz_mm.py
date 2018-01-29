import pyautogui as pg
import time
import webbrowser

points = 0

#Question
answer = pg.prompt
pg.prompt(
"""

Which would you rather be?

a) a broken girl who works for a millionare 
b) a millionare who has a complicated love life
c) the best friend of a girl who works for a millionare 


"""
    )

#give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer== "c":
    points += 3


#Question
answer = pg.prompt
pg.prompt(
"""

Who would you rather date?

a) a hot girl chef who's broke, but works for a millionare
b) a millionare guy who has feelings for another girl
c) a girl who has a freind that works for a millionare


"""
    )

#give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer== "c":
    points += 3


#Question
answer = pg.prompt
pg.prompt(
"""

What character would you rather work for?

a) a hot guy millionare who likes a broke girl who works for him
b) a hot girl millionare who just cares about money and fashion
c) a gay guy who works for a millionare 


"""
    )

#give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer== "c":
    points += 3

#Question
answer = pg.prompt
pg.prompt(
"""

Who would you rather live the rest of your life with?

a) a short, gay funny guy 
b) a broke, hot, young girl
c) a selfish girl millionare 


"""
    )

#give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer== "c":
    points += 3




# END OF SURVEY

pg.alert ("You are...")

#Gabi
if points < 7:
    pg.alert ("Gabi")
    webbrowser.open ("https://www.google.com/search?q=gabi+from+young+and+hungry&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiM547cwv3YAhVSJt8KHeSuDyYQ_AUICigB&biw=967&bih=445#imgrc=EjaGwR0z3FJUlM:")
#millionare
    if points >=7 and points < 10:
        pg.alert ("millionare")
        webbrowser.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=967&bih=445&tbm=isch&sa=1&ei=LkJvWranNaWf_Qb62ZHIDQ&q=josh+from+young+and+hungry&oq=Josh+from+&gs_l=psy-ab.3.0.0i67k1j0l9.60623.62179.0.64024.10.9.0.1.1.0.104.660.8j1.9.0....0...1c.1.64.psy-ab..0.10.666....0.KMUFAeDWktk#imgrc=SiI5SIwkuGVGKM:")
#Sophia
    if points >=10:
        pg.alert ("Caroline")
        webbrowser ("https://www.google.com/search?q=sophia+from+young+and+hungry&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi_xK-Uw_3YAhXuSN8KHcwHCXIQ_AUICigB&biw=967&bih=445#imgrc=khcD58qRGd1DvM:")
