obf.py
======

* Convert python 2.7 script to an obf-ed string

* The obf-ed string is only made of the following symbols : 
    () [] + = \ ; ' ` _ 

 It then executes through exec(eval( )) as the original script.

 ___________________________________________________

Usage :
 
    * python obf.py > helloWorld.py 
    * python obf.py myCode.py > myObfCode.py
_____________________________________________________

 Request for improvements :

    * find a way to execute crafted code with only exec(), instead of exec(eval())
    * find a way to use a smaller alphabet for the crafted code
    * make the crafted code smaller
_____________________________________________________

 Exemple : see helloWorld.py


