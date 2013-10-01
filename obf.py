#####################################################################################
#  																					#
#	Convert python 2.7 script to an obf-ed string									#
#																					#
#	The obf-ed string is only made of the following symbols :  () [] + = \ ; ' ` _	#
#	It then executes through exec(eval( )) as the original script.					#
#																					#
#	usage : 																		#
#		python obf.py > helloWorld.py												#
#		python obf.py myCode.py > myObfCode.py										#
#																					#
#####################################################################################

import os, sys, bz2, base64

def obf(code):

	#eval(_s('s')) = s
	def _s(s) :
		return '\''+s+'\''

	# eval(eval(__s('s'))) = s
	def __s(s) :
		return '\'\\\''+s+'\\\'\''

	_0 = '+(()==[])'
	_1 = '+(()==())' #_1b= '+([]==[])'
	_True = '`[]==[]`'
	_False = '`()==[]`'
	_l = _False +'['+2*_1+']'
	_a = _False +'['+1*_1+']'
	_e = _True +'['+3*_1+']'
	__wrap = _s('`[].__')+'+'+_l+'+'+_e+'+'+_s('__`')
	__b_in = _s('`')+'+'+_a+'+'+_l+'+'+_l+'+'+_s('`')
	___chr = __wrap+'+'+_s('['+37*_1+']+') +'+'+ __wrap+'+'+_s('['+4*_1+']+') +'+'+ __wrap+'+'+_s('['+9*_1+']')
	___exec = __wrap+'+'+_s('['+2*_1+']+') +'+'+ __wrap+'+'+_s('['+44*_1+']+') +'+'+ __wrap+'+'+_s('['+2*_1+']+') +'+'+ __wrap+'+'+_s('['+37*_1+']')
	___int = __b_in+'+'+_s('['+3*_1+']+')+__b_in+'+'+_s('['+8*_1+']+')+__b_in+'+'+_s('['+5*_1+']')

	quote_3 = '\\\\\\\''
	quote_4 = '\\\\\\\\\\\\\\\''

	# PROTIP : >>> exec("__='dir';  exec('__='+__); print __")
	# so : exec( "_______="+_______);
	payload=quote_3
	payload += quote_3+'+____+'+quote_3+'('+quote_4+'___='+quote_4+'+___);' #chr
	payload += quote_3+'+____+'+quote_3+'('+quote_4+'__='+quote_4+'+__);' #int
	payload += quote_3

	# 30 = int( `3`+`0` )
	def num(n) :
		return '__('+'+'.join( ['`'+( _0 if int(s)==0 else _1*int(s) )+'`' for s in str(n) ])+')'

	#letters = chr(x)+chr(y)+...
	def letters( ls ) :
		return ('+').join([ '___('+num(ord(l))+')' for l in ls ])


	#exec( chr()+chr()...
	# ______+'(____(112)+____(114)+____(105)+...
	payload += '+____+'+quote_3+'('+letters(code)+')'+quote_3

	# pass the strings of functions to the exec : int, chr, exec... then exec.
	# 	"__='int';___='chr';____='exec';exec("+ payload +");"
	obf_code = '+\'+\'+'.join([ __s('__='+quote_3),___int,__s(quote_3+';'),
								__s('___='+quote_3),___chr,__s(quote_3+';'),
								__s('____='+quote_3),___exec,__s(quote_3+';'),
								___exec,
								__s('('+payload+')') ])

	return obf_code

# load to code to obf
code = 'print("Hello World !")'
if (len(sys.argv) > 1 ):
	f = open(sys.argv[1],'r')
	code = f.read()

# compress the code if there is a point
if len(code) > 400 :
	compress = bz2.compress(code)
	code = 'import bz2, base64\n'
	code += 'exec(bz2.decompress(base64.b64decode(\''
	code += base64.b64encode(compress)
	code += '\')))\n'


# outputs the obf code
header = '################################ Omg, code has been obf-ed ! ################################\n'
sys.stdout.write(header+'exec(eval('+obf(code)+'))')
