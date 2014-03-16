#!usr/bin/python
#elkclone@reasearch4.org
#http://reasearch4.org
#--------------Inline README---------------------------------------------
"""h4ckmath.py algebra review and calculus tutorial in python.
   Requirements: running cli python with SymPy and usual modules installed.
   pip installer is helpful python module installer. 
   Sympy is an open source library that allows us to make mathematical
   symbolic applications. Before we jump into warp with calculus.. we 
   should highlight some features of SymPy by using it to do an algebra 
   refresher tutorial. """
#-----------------------------------------------------------------------
from sympy import *
import sys
import textwrap

def h4ckmath():

    init_printing(use_unicode=True)
    x, y, z = symbols('x y z')
    print "================http://reasearch4.org============================\n"
    print textwrap.dedent('''Welcome to h4ckmath algebra and calculus tutorial
          _______|00|____|==^^==|___________________>>>
    

          ---------------------------------------------------------\n''').strip() 
    choice = raw_input('h4ckmath select module=> e=exponents,t=trig,d=difcalc,i=intcalc\n :')    
         
    if choice == 'e': 
        def exp_ex():
            print "----------------------------------------------------------------"
            print "Algebra.. hell yes lets do this!! simplify  polynomial/rational"
            print  "functions using expand() eg 1.1 ((x+7)*(x-4))"
            print expand((x+7)*(x-4))
            print textwrap.dedent('''As seen above expand() takes a polynomial
            and returns it as sum of monomials factor() takes a polynomial
            and factors it into simplest elementary expression over the rational
            numbers.eg 1.2 factor(x**2*z+4*x*y*z + 4*y**2*z)  --Fugly lol''').strip() 
            print factor(x**2*z+4*x*y*z + 4*y**2*z)
            print '\n'
            print textwrap.dedent('''that looks almost understandable. elementary functions.
            factor_list() returns a more structured ouput.
            ___________________________________________________________\n
            first a basic test of your algebra skills:''').strip()
    
            print " Exponents ex 1.1 simplify (2*x**-2*x**4/5*y**6/x+y)**-3"
            showanswer = raw_input('show answer y/n ')
            if showanswer == 'y':
                print simplify((2*x**-2*x**4/5*y**6/x+y)**-3)
            print "\n We can also expand() or factor() the above original"
            print " polynomial to express in different forms or elementary functions"
            seefactor = raw_input('show factored version y/n ')
            if seefactor =='y':
                print factor((2*x**-2*x**4/5*y**6/x+y)**-3)
            print "\n Here we discover the simplify() version is also the factor() simplest form."
            print "we can also see exand() function applied to this. "
            print expand((2*x**-2*x**4/5*y**6/x+y)**-3)
            print "--------------------------------------------"
            print "\nex 1.2 simplify 2*x**3*y**-2*x**-5 + y**1/4*y**-2/3"
            showanswer = raw_input('show answer y/n ')
            if showanswer =='y':
                print simplify(2*x**3*y**-2*x**-5 + y**1/4*y**-2/3)
            print "\n The above used the properties of exponents for multiplication"
            print "--------------------------------------------\n"
            print textwrap.dedent('''ex 1.3 Your Mission should you chose to accept it...:ex 1.3.1 review absolute value, radicals and log functions as self study challenge review algebra here. http://tutorial.math.lamar.edu/Extras/AlgebraTrigReview/Exponents.aspx \n ex 1.3.2 Code challenge: write your own interactive tutorial functions in python to prove you understand abs() sqrt() and ln().hint powers or exponents are documented here http://docs.sympy.org/latest/tutorial/simplification.html#powers
            -------- --------------------------------------------''').strip()
        exp_ex()       

    if choice == 't':
        def trig_ex():
            print textwrap.dedent('''=^^=--trigsimp() trigonomic identies for simplification of trig functions. ex 1.4 use trig identities to simplify the following: sin(x)**4 - 2*cos(x)**2*sin(x)**2 + cos(x)**4''').strip()
            showanswer = raw_input('show answer y/n ')
            if showanswer == 'y':
                print trigsimp(sin(x)**4 - 2*cos(x)**2*sin(x)**2 + cos(x)**4)
            print "thats much better looking after plugging known trig identities"
            print "\n ex 1.5 sin(x)*tan(x)/sec(x)"
            showanswer = raw_input('show answer y/n ')
            if showanswer == 'y':
                print trigsimp(sin(x)*tan(x)/sec(x))
            print '\n'
            print textwrap.dedent(''' ex 1.6 selfstudy challenge. compose an example for each trig identity review trig identities http://tutorial.math.lamar.edu/Extras/AlgebraTrigReview/TrigFormulas.aspx http://www.sosmath.com/trig/Trig5/trig5/trig5.html''').strip()
        trig_ex()
    if choice == 'd':
        def difcalc():
            print '\n'
            print textwrap.dedent('''The Derivative \n The derivative  is at the core of calculus. Geometrically the derivative is the slope of a curve at a point. Physically it is a rate of change of a function over a snapshot interval. The concept of the limit looms...\n  Newtons physical approach average velocity=delta_distance/delta_time where delta=change of distance or time. In this way we reach an Instantaneous velocity as the limit delta_time-->0 delta_distance/delta_time\n  Leibniz (1646-1716) and Newton(1642-1727) the fathers of calculus came up with notation  dy/dx(a)=f'=derivative of y(x) we say "dee y divided by dee x = the derivative."  so in above example velocity =ddistance/dtime(a)\n\n The gometrical concept of the derivative is derived from y=f(x) x values being in the domain of the function f. graph y(x) and determine slope of curve as a limit of 2 points aproach each other. easy. right..aka m(x) = slope of tangent line.\n\n  Techniques of diferentiation\n differentiation formulas \n
(f+g)'(a)=f'(a)+g'(a)  \n  (cf)'(a) = cf'(a) \n (x**n)'=n*x**n-1-->power rule. \n\n  The above 3 formulas allows us to take first,second, third etc order derivativies of any polynomial. lets try a few simple derivatives. ''').strip()
            
            print "\n ex 2.1 differentiate: 3x**3 + 2x**2 - 10x**4"
            showanswer = raw_input('showanswer from python diff()  y/n :')
            if showanswer == 'y':
                print diff(3*x**3 + 2*x**2 - 10*x**4)
            print "\n Jolly good! I hope thats what you got by hand.!"
            print "\n ex 2.2 differentiate: 4*x**2 + 3*x -5*x**3"
            showanswer = raw_input('showanswer from python diff() y/n :')
            if showanswer == 'y':
                print diff(4*x**2 + 3*x -5*x**3)
            print "\n hopefully that matches your hand differentiation.:-)\n"
            print textwrap.dedent('''The next two formulas are known as product rule and quotient rule.\n (f*g)'(a) = f'(a)g(a) + f(a)g'(a) --->product rule.\n (f/g)'(a) = f'(a)*g(a) - f(a)*g'(a)/g**2(a) --->quotient rule.\n\n  Memorize these and the first 3 formulas. This will allow us to deal with more complicated functions. of x. y=f(x). Let' do some examples rationals and products''').strip()
            print "\n\n ex 2.3 differentiate: y=f(x)=2*x+8/3*x+6"
            showanswer = raw_input('showanswer from python diff() y/n :')
            if showanswer == 'y':
                print diff(2*x+8/3*x+6)
            print '\n'
            print textwrap.dedent(''' Hint: working that one out by hand requires quotient rule and use of (1/f)'(a)=-f'(a)/f''(a)   and  (1/x**n)'=-n*x**n-1/x**2n =-nx**-n-1 \n  These are 2 helpful results derived from product and quotient rule involving the second order derivative of the quotient function..\n\n Ok one more example to prove you did homework on radicals.\n''').strip()
            print "\n ex 2.4 differentiate: y=f(x)=sqrt(x)/x**2-x+3"
            showanswer = raw_input('showanswer from python diff() y/n :')
            if showanswer == 'y':
                print diff(sqrt(x)/x**2-x+3)
            print "\n\nyikes make sure you use (sqrt(x))'=(1/2)*(1/sqrt(x')) and quotient rule..\n"
            print textwrap.dedent('''Trigonometric differentiation formulas.\n first review trig identities here http://www.sosmath.com/trig/Trig5/trig5/trig5.html\n trig diff() formulas: \n sin'(x) = cos(x)\n cos'(x) = -sin(x)\n tan'(x) = sec**2(x) \n cot'(x) = -csc**2(x) \n  sec'(x) = sec(x)*tan(x) \n csc'(x) = -csc(x)*cot(x) \n we add an extension formula for second derivatives \n sin''(x) =-sin(x) \n cos''(x) = -cos(x) \n\n Armed with these and a table of trig identities we can differentiate many trigonmetric functions.\n\n''').strip()
            print "\n ex 2.5 differentiate f(x)= sin(2x)   hint: use double angle identity"
            showanswer = raw_input('showanswer from python diff() y/n :')
            if showanswer == 'y':
                print diff(sin(2*x))
            print "\n Behold python with SymPy module > differential calculus.!"
            print "\n ex 2.6 differentiate f(x) = sec(x) + tan(x) hint: plug in the formulas.y"
            showanswer = raw_input('showanswer from python diff() y/n :')
            if showanswer == 'y':
                print diff(sec(x) + tan(x))
            print " good job you are starting to get the idea." 
        difcalc()
    
        
h4ckmath()
