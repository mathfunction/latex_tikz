
import json
HELP_TEMPLATE = '% this is python generate latex code , do not edit it !!\n'
HEAD_TEMPLATE = '\\documentclass{standalone}\n\\usepackage{tikz}\n'
BEGIN_TEMPLATE ='\\begin{document}\n\\begin{tikzpicture}\n'
END_TEMPLATE = '\\end{tikzpicture}\n\\end{document}\n'
MACROS = [
      '\\usetikzlibrary{automata, positioning}\n',
      '\\newcommand{\\createNode}[6]{\\node[state,text=#5,fill=#6] at (#3,#4)(#1){#2};}\n',
      '\\newcommand{\\createEdge}[5]{\\draw[every loop,bend right,auto=right,text=#4,fill=#5](#1)edge node{#3} (#2);}\n'
      '\\newcommand{\\createLoop}[4]{\\draw[every loop,loop above,text=#3,fill=#4](#1)edge node{#2} (#1);}\n'
]

def braket(v):
	return str(v).join(["{","}"])

def MarkovChainTikz(jsonfile="./gen/markov_chain.json"):
	print(HELP_TEMPLATE)
	print(HEAD_TEMPLATE)
	print(''.join(MACROS))
	print(BEGIN_TEMPLATE)
	#=================================================
	# python generate codes 
	nodes = {}
	edges = {}
	with open(jsonfile) as f:
		edgeArray = json.load(f)
	for e in edgeArray:
		if e[0] not in nodes:
			nodes[e[0]] = "v{}".format(len(nodes))
		if e[1] not in nodes:
			nodes[e[1]] = "v{}".format(len(nodes))
	# draw node vertically 
	x = 0.0
	for v in nodes:
		print("\\createNode{}{}{}{}{}{}".format(
				braket(nodes[v]),
				braket(v),
				braket(x),
				braket(0.0),
				braket("black"),
				braket("white")
			)
		)
		x+=2.5

	for e in edgeArray:
		if e[0] != e[1]:
			print("\\createEdge{}{}{}{}{}".format(
				braket(nodes[e[0]]),
				braket(nodes[e[1]]),
				braket(e[2]),
				braket("black"),
				braket("black")
			))
		else:
			print("\\createLoop{}{}{}{}".format(
				braket(nodes[e[0]]),
				braket(e[2]),
				braket("black"),
				braket("black")
			))

	#==================================================
	print(END_TEMPLATE)



if __name__ == '__main__':
	MarkovChainTikz()


