#!/usr/bin/pyhon

def SouthOrEast(i,j):
	if i == 0 and j == 0:
		return 0;
	x, y = -99999, -99999
	if i>0:
		x = SouthOrEast(i-1,j) + Abajo[i-1][j]
	if j>0:
		y = SouthOrEast(i,j-1) + Derecha[i][j-1]
	return max(x,y)

def ManhattanTourist(n,m,Abajo,Derecha):
	s = [ [ None for i in range(len(Derecha)) ] for j in range(len(Abajo[0])) ]
	s[0][0] = 0
	for i in range(1,n+1):
		s[i][0] = s[i-1][0] + Abajo[i-1][0]
	for j in range(1,m+1):
		s[0][j] = s[0][j-1] + Derecha[0][j-1]
	for i in range(1,n+1):
		for j in range(1,m+1):
			s[i][j] = max ( s[i-1][j] + Abajo[i-1][j], s[i][j-1] + Derecha[i][j-1] )

	return s[n][m] 

Derecha = [ [ int(f) for f in line.split(",") ] for line in open("Derecha.txt") ]
Abajo = [ [ int(f) for f in line.split(",") ] for line in open("Abajo.txt") ]

print(SouthOrEast(4,4))


print(ManhattanTourist(4,4,Abajo,Derecha))

def LCSBacktrack(v,w): #Longest common subsequence
	Backtrack = [ [ None for i in range(len(w)) ] for j in range(len(v)) ]
	s = [ [ None for i in range(len(w)) ] for j in range(len(v)) ]

	s[0][0] = 0
	for i in range(1,len(v)):
		s[i][0] = 0
	for j in range(1,len(w)):
		s[0][j] = 0
	for i in range(1,len(v)):
		for j in range(1,len(w)):
			s[i][j] = max ( s[i-1][j],  s[i][j-1], s[i-1][j-1] + ( 1 if v[i]==w[j] else 0 ) )
			if s[i-1][j-1] + 1 == s[i][j] and v[i] == w[j]:
				Backtrack [i][j] = "DIAG"
			elif s[i-1][j] == s[i][j]:
				Backtrack [i][j] = "ARR"
			elif s[i][j-1] == s[i][j]:
				Backtrack [i][j] = "IZQ"

	return Backtrack 
	

#v = "ATGTTATA"
#w = "ATCGTCC"

v = "YAFDLGYTCMFPVLLGGGELHIVQKETYTAPDEIAHYIKEHGITYIKLTPSLFHTIVNTASFAFDANFESLRLIVLGGEKIIPIDVIAFRKMYGHTEFINHYGPTEATIGA"
w = "AFDVSAGDFARALLTGGQLIVCPNEVKMDPASLYAIIKKYDITIFEATPALVIPLMEYIYEQKLDISQLQILIVGSDSCSMEDFKTLVSRFGSTIRIVNSYGVTEACIDS"

BT = LCSBacktrack(v,w)

def OUTPUTLCS(Backtrack, v, i, j):
	if i == 0 or j == 0:
		return ""
	if Backtrack[i][j] == "ARR":
		return OUTPUTLCS ( Backtrack, v, i-1, j )
	elif Backtrack[i][j] == "IZQ":
		return OUTPUTLCS ( Backtrack, v, i, j-1 )
	else:
		return OUTPUTLCS( Backtrack, v, i-1, j-1 ) + v[i]

print (OUTPUTLCS(BT, v, len(v)-1, len(w)-1))
