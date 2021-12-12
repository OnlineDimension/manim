from manim import *
import numpy as np

class scrap(Scene):
	def construct(self):
		
		a = MathTable([[0,1],[2,3]])
		
		self.add(a[0][2])
		
def seg(a,b,color=WHITE,thicc=4):
	x = Line(start=np.array([a[0],a[1],0]), end=np.array([b[0],b[1],0]),stroke_width=thicc)
	x.set_color(color)
	return x
		
def quad(x1,y1,x2,y2,x3,y3,x4,y4,c):
	a1 = np.array([x1,y1,0])
	a2 = np.array([x2,y2,0])
	a3 = np.array([x3,y3,0])
	a4 = np.array([x4,y4,0])
	a  = Polygon(a1,a2,a3,a4,color=c)
	return a
	
class chain:
	def __init__(self, color):
		self.color = color
		self.top_xlocation = 0
		self.top_ylocation = 0
		
	def update_top_location(self, x, y):
		self.top_xlocation = x
		self.top_ylocation = y
				
			
class semi_w4(Scene):
	def construct(self):
		
		def trans(x,y,z):
			self.play(Create(x))
			self.wait()
			self.play(ReplacementTransform(x,y))
			self.wait()
			if z != 0:
				self.play(ReplacementTransform(y,z))
				self.wait()
		
		a = []	
		a.append(seg([-5,-2], [-1,-2], WHITE))
		a.append(seg([-5,-2], [-1,-2], RED))
		a.append(0)
		
		b = []
		b.append(seg([-5,-1], [-1,-1], WHITE))
		b.append(seg([-5,-1], [-1,-1], BLUE))
		b.append(0)
		
		c = []
		c.append(seg([1,-2], [5,-2], WHITE))
		c.append(seg([1,-2], [5,-2], RED))
		c.append(seg([1,1], [5,1], RED))
		
		d = []
		d.append(seg([0,-2], [4,-2], WHITE))
		d.append(seg([0,-2], [4,-2], YELLOW))
		d.append(0)
		
		e = []
		e.append(seg([0.5,-1], [4.5,-1], WHITE))
		e.append(seg([0.5,-1], [4.5,-1], BLUE))
		e.append(seg([0.5,0], [4.5,0], BLUE))
		
		f = []
		f.append(seg([0.25,-1], [4.25,-1], WHITE))
		f.append(seg([0.25,-1], [4.25,-1], GREEN))
		f.append(0)
		
		g = []
		g.append(seg([-3.65,0], [0.35,0], WHITE))
		g.append(seg([-3.65,0], [0.35,0], PURPLE))
		g.append(0)
		
		h = []
		h.append(seg([-3.65,1], [0.35,1], WHITE))
		h.append(seg([-3.65,1], [0.35,1], ORANGE))
		h.append(0)
		
		for i in [a,b,c,d,e,f,g,h]:
			trans(i[0],i[1],i[2])

class semi_proof(Scene):
	def construct(self):
	
		name = Tex(r'Israel R. Curbelo').scale(0.5)
		#name.set_opacity(0.75)
		name.to_corner(DR,buff=0.05)
		name.set_color(YELLOW)
		self.play(Write(name))
		self.wait()
		
		def trans(x,y,z):
			self.play(Create(x))
			#self.wait()
			self.play(ReplacementTransform(x,y))
			#self.wait()
			if z != 0:
				self.play(ReplacementTransform(y,z))
				#self.wait()
		w = 20
		
		A_lines = VGroup()
		#creating A block
		for i in range(w//2):
		
			a = []	
			a.append(seg([-5,-2+i*4/w], [-1,-2+i*4/w], WHITE))
			a.append(seg([-5,-2+i*4/w], [-1,-2+i*4/w], YELLOW))
			a.append(0)
			A_lines = VGroup(A_lines,a[1])
			
			trans(a[0],a[1],a[2])
			
		def right_stack(x):
			new = -1
			old = 3
			low = -2
			high = 2-4/w
			A2_local = VGroup()
			B_local = VGroup()
			
			for i in x:
				l = (new+old)/2
				
				if i == 0:
				
					c = []
					c.append(seg([l, low], [l+4, low], WHITE))
					c.append(seg([l,low], [l+4,low], YELLOW))
					c.append(seg([l, high], [l+4, high], YELLOW))
					trans(c[0],c[1],c[2])
					
					A2_local = VGroup(A2_local,c[2])
					
					old = l
					high = high - 4/w
					
				elif i == 1:
				
					c = []
					c.append(seg([l, low], [l+4, low], WHITE))
					c.append(seg([l,low], [l+4,low], BLUE))
					trans(c[0],c[1],0)
					
					B_local = VGroup(B_local,c[1])
					
					new = l
					low = low + 4/w
			global end
			global A2_lines
			global B_lines
			
			end = new
			A2_lines = A2_local
			B_lines = B_local
			
		
		color_order = [0,0,1,0,1,1,1,0,0,1,1,0,1,0,0,1,1,1]
		right_stack(color_order)
		
		
		C_lines = VGroup()
		for i in range(w//2):
			
			c = []	
			c.append(seg([end-4,0+i*4/w], [end,0+i*4/w], WHITE))
			c.append(seg([end-4,0+i*4/w], [end,0+i*4/w], LIGHT_PINK))
			c.append(0)
			C_lines = VGroup(C_lines, c[1])
			
			trans(c[0],c[1],c[2])
				
		self.wait(3)
		
		A = quad(-5,-2,-1,-2,-1,-4/w,-5,-4/w,YELLOW)
		#A.set_fill(YELLOW)
		self.play(FadeOut(A_lines),FadeIn(A))
		
		abrace = Brace(A,direction = LEFT)
		abrace_text = abrace.get_text(r'$\frac{w}{2}$')
		self.play(GrowFromCenter(abrace),FadeIn(abrace_text))
		self.wait(2)
		
		A2 = quad(end+0.1,0,end+4.1,0,end+4.6,2,end+0.6,2,YELLOW)
		#A2.set_color(YELLOW)
		self.play(FadeOut(A2_lines),FadeIn(A2))
		self.wait(2)
		
		B = quad(end-0.5,-2,end+3.5,-2,end+4,-4/w,end,-4/w,BLUE)
		#B.set_color(BLUE)
		self.play(FadeOut(B_lines),FadeIn(B))
		abrace = Brace(B,direction = RIGHT)
		abrace_text = abrace.get_text(r'$\frac{w}{2}$')
		self.play(GrowFromCenter(abrace),FadeIn(abrace_text))
		self.wait(2)
		
		C = quad(end-4,0,end,0,end,2,end-4,2,LIGHT_PINK)
		#C.set_color(LIGHT_PINK)
		self.play(FadeOut(C_lines),FadeIn(C))
		abrace = Brace(C,direction = LEFT)
		abrace_text = abrace.get_text(r'$\frac{w}{2}$')
		self.play(GrowFromCenter(abrace),FadeIn(abrace_text))
		
		self.wait(3)
		


#FIRST-FIT
		
class first_fit(Scene):
	def construct(self):
		
		left = -3
		right = 3
		base = -3.85
		step = 0.3
		colors = []
		left_top = base
		right_top = base
		font_size = 15
		stroke_thicc = 4
		
		def point(side,height,color,new=0):
		
			x = Dot(point=np.array([side,height,0]))
			
			if side == left:
				c = Text(color,font_size=font_size).next_to(x,LEFT,buff=0.06)
			elif side == right:
				c = Text(color,font_size=font_size).next_to(x,RIGHT,buff=0.06)
			
			if new == 1:
				
				c.set_color(YELLOW)
				
			self.play(Create(x))
			self.play(Create(c))
			
			
		def rel(a,b,x,y):
		
			temp = seg([a,b],[x,y],thicc=stroke_thicc)
			self.play(Create(temp))
		
		def single_cross(chain,colors,left_top,right_top):
			
			x,y = colors[chain-1].top_xlocation, colors[chain-1].top_ylocation
			
			if x == left:
				a = right
				b = right_top
				right_top += step
			elif x == right:
				a = left
				b = left_top	
				left_top += step
				
			rel(x,y,a,b+step)
			rel(a,b,a,b+step)
			point(a,b+step, str(chain))
			
			colors[chain-1].update_top_location(a,b+step)
			return colors,left_top,right_top
		
		def newcolorstep(x,y,colors,left_top,right_top):
			new_color = len(colors) + 1
			colors.append(chain(new_color))
			
			rel(x,y-step,x,y)
			point(x,y, str(new_color),1)
			colors[new_color-1].update_top_location(x,y)
			
			if x == left:
				left_top += step
			elif x == right:
				right_top += step
			
			return colors, left_top, right_top
		
		name = Tex(r'Israel R. Curbelo').scale(0.5)
		#name.set_opacity(0.75)
		name.to_corner(DR,buff=0.05)
		name.set_color(YELLOW)
		self.play(Write(name))
		self.wait()
		
		#initializing poset
		
		point(left,base,'1',1)
		colors.append(chain(1))
		colors[0].update_top_location(left,base)
		
		point(right,base,'2',1)
		colors.append(chain(2))
		colors[1].update_top_location(right,base)
		
		self.wait()
		
		n=4
		count = 0
		
		for i in range(n):
			count +=1
		
			for i in range(count,0,-1):
		
				colors,left_top,right_top = single_cross(i,colors,left_top,right_top)
			
			self.wait()
			colors,left_top,right_top = newcolorstep(left,left_top+step,colors,left_top,right_top)
			self.wait()
			
			count +=1
			
			for i in range(count,0,-1):
			
				colors,left_top,right_top = single_cross(i,colors,left_top,right_top)
			
			self.wait()
			colors,left_top,right_top = newcolorstep(right,right_top+step,colors,left_top,right_top)
			self.wait()
			
		self.wait()
		self.wait()
		self.wait()
		self.wait()
			
#POSET POSET POSET POSET POSET POSET POSET
				
class poset(Scene):
	def construct(self):
		
		poset = Tex(r'We consider a \emph{partially ordered set} or \emph{poset} $(X,P)$ as a pair where $X$ is a set and $P$ is a reflexive, antisymmetric and transitive relation on $X$.',tex_environment='flushleft').scale(0.8).shift(UP*3)
		
		def point(x,y,z=0):
			temp = Dot(point=np.array([x,y,z]))
			return temp 
		
		def rel(a,b,x,y):
		
			temp = seg([a,b],[x,y])
			return temp
		
		a= point(0,-3)
		alabel= Tex(r'$a$').next_to(a,DOWN)
		A= VGroup(a,alabel)
		b= point(-1,-2)
		blabel= Tex(r'$b$').next_to(b,LEFT)
		B= VGroup(b,blabel)
		c= point(1,-2)
		clabel= Tex(r'$c$').next_to(c,RIGHT)
		C= VGroup(c,clabel)
		d= point(0,-1)
		dlabel= Tex(r'$d$').next_to(d,UP)
		D= VGroup(d,dlabel)
		p=Group(a,b,c,d)
		
		ex = Tex(r'$X=\{a,b,c,d\}$\\$P=\{$',r'$(a,a),$',r'$(b,b),$',r'$(c,c),$',r'$(d,d),$',r'$(a,b),$',r'$(b,d),$',r'$(a,c),$',r'$(c,d)$,',r'$(a,d)$',r'$\}$', tex_environment='flushleft').scale(0.8).shift(UP*1.5)
		
		
		
		
		self.play(Write(poset))
		self.wait(2)
		self.play(Write(ex))
		self.wait(2)
		self.play(TransformFromCopy(ex[1],A))
		self.play(TransformFromCopy(ex[2],B))
		self.play(TransformFromCopy(ex[3],C))
		self.play(TransformFromCopy(ex[4],D))
		self.wait(2)
		'''
		self.play(Create(a),Write(alabel))
		self.play(Create(b),Write(blabel))
		self.play(Create(c),Write(clabel))
		self.play(Create(d),Write(dlabel))
		'''
		ab = rel(0,-3,-1,-2)
		bd = rel(-1,-2,0,-1)
		ac = rel(0,-3,1,-2)
		cd = rel(1,-2,0,-1)
		ad = rel(0,-3,0,-1).set_opacity(0.4)
		self.play(TransformFromCopy(ex[5],ab))
		self.play(TransformFromCopy(ex[6],bd))
		self.play(TransformFromCopy(ex[7],ac))
		self.play(TransformFromCopy(ex[8],cd))
		self.wait(2)
		self.play(TransformFromCopy(ex[9],ad))
		self.wait(2)
		self.play(FadeOut(ad))
		self.wait(2)
			
class chains(Scene):
	def construct(self):
		
		chain = Tex(r'A poset $(X,P)$ is called a \emph{chain} if every pair of distinct elements in $X$ is comparable in $P$.',tex_environment='flushleft').scale(0.75).to_corner(UL)
		
		antichain = Tex(r'A poset $(X,P)$ is called an \emph{antichain} if every pair of distinct elements in $X$ is incomparable in $P$.',tex_environment='flushleft').scale(0.75).next_to(chain,DOWN).to_edge(LEFT)
	
		def point(x,y,z=0):
			temp = Dot(point=np.array([x,y,z]))
			return temp 
		
		def rel(a,b,x,y):
		
			temp = seg([a,b],[x,y])
			self.play(Create(temp))
		
		self.play(Write(chain))
		self.wait(2)
		
		ch= Tex(r'chain').shift(LEFT*3+DOWN*3)
		self.play(Write(ch))
		self.wait(2)
		
		a= point(-3,-1)
		alabel= Tex(r'$a$').next_to(a,LEFT)
		self.play(Create(a), Write(alabel))
		self.wait()
		
		b= point(-3,0)
		blabel= Tex(r'$b$').next_to(b,LEFT)
		self.play(Create(b), Write(blabel))
		rel(-3,-1,-3,0)
		self.wait()
		
		c= point(-3,1)
		clabel= Tex(r'$c$').next_to(c,LEFT)
		self.play(Create(c), Write(clabel))
		rel(-3,0,-3,1)
		self.wait(2)
		
		self.play(Write(antichain))
		self.wait(2)
		
		an= Tex(r'antichain').shift(RIGHT*3+DOWN*3)
		self.play(Write(an))
		self.wait()
		
		a= point(2,0)
		alabel= Tex(r'$a$').next_to(a,DOWN)
		self.play(Create(a),Write(alabel))
		self.wait()
		
		b= point(3,0)
		blabel= Tex(r'$b$').next_to(b,DOWN)
		self.play(Create(b),Write(blabel))
		self.wait()
		
		c= point(4,0)
		clabel= Tex(r'$c$').next_to(c,DOWN)
		self.play(Create(c),Write(clabel))
		self.wait(2)
		
		
		
class antichains(Scene):
	def construct(self):
		
		antichain = Tex(r'A poset $(X,P)$ is called an \emph{antichain} if every pair of distinct elements in $X$ is incomparable in $P$.',tex_environment='flushleft').scale(0.75).to_corner(UL)
	
		def point(x,y,z=0):
			temp = Dot(point=np.array([x,y,z]))
			#self.play(Create(temp))
			return temp 
		
		def rel(a,b,x,y):
		
			temp = seg([a,b],[x,y])
			self.play(Create(temp))
		
		self.play(Write(antichain))
		self.wait()
		
		a= point(-3,0)
		alabel= Tex(r'$a$').next_to(a,DOWN)
		self.play(Create(a),Write(alabel))
		self.wait()
		
		b= point(0,0)
		blabel= Tex(r'$b$').next_to(b,DOWN)
		self.play(Create(b),Write(blabel))
		self.wait()
		
		c= point(3,0)
		clabel= Tex(r'$c$').next_to(c,DOWN)
		self.play(Create(c),Write(clabel))
		self.wait()
		
class height_and_width(Scene):
	def construct(self):
		
		height = Tex(r'The \emph{height} of a poset $(X,P)$ is the size of a maximum chain.', tex_environment='flushleft').scale(0.8).shift(UP*3)
		
		width = Tex(r'The \emph{width} of a poset $(X,P)$ is the size of a maximum antichain.', tex_environment='flushleft').scale(0.8).next_to(height,DOWN)
	
		def point(x,y,z=0):
			temp = Dot(point=np.array([x,y,z]))
			return temp 
		
		def rel(a,b,x,y):
		
			temp = seg([a,b],[x,y])
			return temp
		
		a= point(0,-3)
		alabel= Tex(r'$a$').next_to(a,DOWN)
		A= VGroup(a,alabel)
		b= point(-1,-2)
		blabel= Tex(r'$b$').next_to(b,LEFT)
		B= VGroup(b,blabel)
		c= point(1,-2)
		clabel= Tex(r'$c$').next_to(c,RIGHT)
		C= VGroup(c,clabel)
		d= point(0,-1)
		dlabel= Tex(r'$d$').next_to(d,UP)
		D= VGroup(d,dlabel)
		
		ab = rel(0,-3,-1,-2)
		bd = rel(-1,-2,0,-1)
		ac = rel(0,-3,1,-2)
		cd = rel(1,-2,0,-1)
		
		self.play(Create(A),Create(B),Create(C),Create(D))
		self.play(Create(ab),Create(bd),Create(ac),Create(cd))
		
		self.wait()
		
		self.play(Write(height))
		self.wait(2)
		highlight = seg([0,-3],[-1,-2]).set_color(YELLOW)
		highlight2 = seg([-1,-2],[0,-1]).set_color(YELLOW)
		hlp = Dot(point=np.array([0,-3,0])).set_color(YELLOW)
		hlp2 = Dot(point=np.array([-1,-2,0])).set_color(YELLOW)
		hlp3 = Dot(point=np.array([0,-1,0])).set_color(YELLOW)
		self.play(Create(hlp),Create(hlp2),Create(hlp3),Create(highlight),Create(highlight2))
		self.wait(2)
		self.play(Write(Tex(r'$height = 3$').scale(0.7).shift(LEFT*4)))
		self.wait()
		#self.play(FadeOut(height))
		self.remove(hlp)
		self.remove(hlp2)
		self.remove(hlp3)
		self.remove(highlight)
		self.remove(highlight2)
		self.wait(2)
		
		
		self.play(Write(width))
		self.wait(2)
		hlpoint = Dot(point=np.array([-1,-2,0])).set_color(YELLOW)
		hlpoint2 = Dot(point=np.array([1,-2,0])).set_color(YELLOW)
		self.play(Create(hlpoint))
		self.play(Create(hlpoint2))
		self.wait(2)
		self.play(Write(Tex(r'$width = 2$').scale(0.7).shift(RIGHT*4)))
		self.wait()
		self.remove(width)
		self.remove(hlpoint)
		self.remove(hlpoint2)
		self.wait(3)
		
class dilworth(Scene):
	def construct(self):
		
		dilworth = Tex(r'\textbf{Theorem.} (Dilworth) If $(X,P)$ is a poset of width $w$, then there exists a partition $X = C_1 \cup \ldots \cup C_w$, where $C_i$ is a chain for $i\in \{1,\ldots,w\}$.', tex_environment='flushleft').scale(0.75).to_corner(UL)
		
		
		def point(x,y,z=0):
			temp = Dot(point=np.array([x,y,z]))
			self.play(Create(temp))
			return temp 
		
		def rel(a,b,x,y):
			temp = seg([a,b],[x,y])
			self.play(Create(temp))
			return temp
			
		self.play(Write(dilworth))
		self.wait(3)
			
		a = point(-3,-1)
		a_l = Tex(r'$a$').next_to(a,DOWN)
		#self.play(Write(a_l))
		
		b = point(-1,1)
		a_l = Tex(r'$b$').next_to(b,DOWN)
		#self.play(Write(a_l))
		
		c = point(1,-1)
		a_l = Tex(r'$c$').next_to(c,DOWN)
		#self.play(Write(a_l))
		
		d = point(3,1)
		
		rel(-3,-1,-1,1)
		rel(-1,1,1,-1)
		rel(1,-1,3,1)
		self.wait(3)
		
		a_l = Tex(r'$1$').next_to(a,DOWN)
		self.play(Write(a_l))
		
		a_l = Tex(r'$1$').next_to(b,UP)
		self.play(Write(a_l))
		
		a_l = Tex(r'$2$').next_to(c,DOWN)
		self.play(Write(a_l))
		
		a_l = Tex(r'$2$').next_to(d,UP)
		self.play(Write(a_l))
		
		self.wait(3)
		
		
	
class online_ex(Scene):
	def construct(self):
		
		def point(x,y,z=0):
			temp = Dot(point=np.array([x,y,z]))
			self.play(Create(temp))
			return temp 
		
		def rel(a,b,x,y):
			temp = seg([a,b],[x,y])
			self.play(Create(temp))
			return temp
		
		online = Tex(r'An \emph{on-line chain partitioning algorithm} receives a poset $(X,P)$ in the order of its elements $x_1,\ldots,x_n$ and constructs an on-line chain partition by immediately and irrevocably assigning each element to a chain.', tex_environment='flushleft').scale(0.75).to_corner(UL)
		
		olw = Tex(r'Let $OLW(w)$ be the least integer $k$ for which there is an on-line algorithm that partitions posets of width $w$ into at most $k$ chains.', tex_environment='flushleft').scale(0.75).to_corner(DL)
		
		self.play(Write(online))
		self.wait(3)
		
		a = point(-1,-1)
		a_l = Tex(r'$1$').next_to(a,DOWN)
		self.play(Write(a_l))
		self.wait(2)
		
		c = point(1,-1)
		a_l = Tex(r'$2$').next_to(c,DOWN)
		self.play(Write(a_l))
		self.wait(2)
		
		rel(-1,-1,0,0)
		rel(1,-1,0,0)
		b = point(0,0)
		self.wait(2)
		
		#case 1
		b_l = Tex(r'$3$').next_to(b,UP)
		self.play(Write(b_l))
		self.wait(2)
		
		#case 2
		b_l2 = Tex(r'$2$').next_to(b,UP)
		self.play(ReplacementTransform(b_l,b_l2))
		self.wait(2)
		dr = rel(1,-1,2,0)
		d = point(2,0)
		d_l = Tex(r'$3$').next_to(d,UP)
		self.wait(2)
		self.play(Write(d_l))
		self.wait()
		self.play(FadeOut(d_l),FadeOut(d),FadeOut(dr))
		
		#case 3
		b_l3 = Tex(r'$1$').next_to(b,UP)
		self.play(ReplacementTransform(b_l2,b_l3))
		self.wait()
		dr = rel(-1,-1,-2,0)
		d = point(-2,0)
		d_l = Tex(r'$3$').next_to(d,UP)
		self.wait()
		self.play(Write(d_l))
		self.wait(3)
		
		self.play(Write(olw))
		self.wait(3)
		
class game(Scene):
	def construct(self):
		
		a = Tex()	
		
class history(Scene):
	def construct(self):
		
		 #olw = Tex('w','\\leq OLW(w)\leq')#, '\\infty')
		 #olw.set_color_by_tex('nft',RED)
		 #self.add(tex)
		tex = Tex(r'$w+1$ ', r'$\leq OLW(w)\leq$', r' $\infty$')#, font_size=144)
		tex.to_edge(UP)
		
		
		 
		thm1 = Tex(r'\textbf{Question.} (Schmerl, 197x) Is there an on-line algorithm that partitions posets of width $w$ into a bounded number of chains?', tex_environment='flushleft').scale(0.7).next_to(tex,DOWN*3).to_edge(LEFT)
		
		thm2 = Tex(r'\textbf{Theorem.} (Kierstead, 1981) $OLW(w)\leq (5^w-1)/4$.', tex_environment='flushleft').scale(0.7).next_to(thm1,DOWN*1.5).to_edge(LEFT)
		
		lowthm = Tex(r'\textbf{Theorem.} (Szemer\'edi, 1981) $OLW(w)\geq\binom{w+1}{2}$.', tex_environment='flushleft').scale(0.7).next_to(thm2,DOWN).to_edge(LEFT)
		
		thm3 = Tex(r'\textbf{Theorem.} (Bosek and Krawczyk, 2010) $OLW(w)\leq w^{13\log w}$.', tex_environment='flushleft').scale(0.7).next_to(lowthm,DOWN).to_edge(LEFT)
		
		lowthm2 = Tex(r'\textbf{Theorem. } (Bosek et al., 2011) $OLW(w)\geq (2-o(1))\binom{w+1}{2}$.', tex_environment='flushleft').scale(0.7).next_to(thm3,DOWN).to_edge(LEFT)
		
		thm4 = Tex(r'\textbf{Theorem.} (Bosek et al., 2018) $OLW(w)\leq w^{6.5\log w+7}$.', tex_environment='flushleft').scale(0.7).next_to(lowthm2,DOWN).to_edge(LEFT)
		
		thm5 = Tex(r'\textbf{Theorem.} (Bosek and Krawczyk, 2021) $OLW(w)\leq w^{O(\log\log w)}$.', tex_environment='flushleft').scale(0.7).next_to(thm4,DOWN).to_edge(LEFT)
		
		
		
		
		
		self.play(Write(tex))
		self.wait(3)
	
		
		def point(x,y,z=0):
			temp = Dot(point=np.array([x,y,z]))
			return temp 
		
		def rel(a,b,x,y):
		
			temp = seg([a,b],[x,y]).next_to(tex,DOWN).set_color(BLUE).set_opacity(0.5)
			self.play(Create(temp))
		tl= rel(-6.5,-3,6.5,-3)
		
		self.play(Write(thm1))
		self.wait(2)
		self.play(Write(thm2))
		up1 = Tex(r'$(5^w-1)/4$').next_to(tex[1],RIGHT)
		self.play(ReplacementTransform(tex[2],up1))
		self.wait(2)
		
		
		self.play(Write(lowthm))
		down1 = Tex(r'$\binom{w+1}{2}$').next_to(tex[1],LEFT)
		self.play(ReplacementTransform(tex[0],down1))
		self.wait(2)
		
		
		self.play(Write(thm3))
		up2 = Tex(r'$w^{13\log w}$').next_to(tex[1],RIGHT)
		self.play(ReplacementTransform(up1,up2))
		self.wait(2)
		
		
		self.play(Write(lowthm2))
		down2 = Tex(r'$(2-o(1))\binom{w+1}{2}$').next_to(tex[1],LEFT)
		self.play(ReplacementTransform(down1,down2))
		self.wait(2)
		
		
		self.play(Write(thm4))
		up3 = Tex(r'$w^{6.5\log w+7}$').next_to(tex[1],RIGHT)
		self.play(ReplacementTransform(up2,up3))
		self.wait(2)
		
		
		self.play(Write(thm5))
		up4 = Tex(r'$w^{O(\log\log w)}$').next_to(tex[1],RIGHT)
		self.play(ReplacementTransform(up3,up4))
		self.wait(3)
		
class survey_table(Scene):
	def construct(self):
		
		t = MathTable(
			[['','Class','U','R','OLW'],
			[1,'Posets','','','?'],
			[2,'Posets','+','','\\binom{w+1}{2}'],
			[3,'Interval Orders','','','3w-2'],
			[4,'Interval Orders','','+','3w-2'],
			[5,'Interval Orders','+','','2w-1'],
			[6,'Interval Orders','+','+','w'],
			[7,'Semi-orders','','','2w-1'],
			[8,'Semi-orders','','+','?'],
			[9,'Semi-orders','+','','\\frac{1+\sqrt{5}}{2}w'],
			[10,'Semi-orders','+','+','w'],
			[11,'2-dimensional','','','?'],
			[12,'2-dimensional','','+','\\binom{w+1}{2}'],
			[13,'2-dimensional','+','','\\binom{w+1}{2}'],
			[14,'2-dimensional','+','+','\\binom{w+1}{2}'],
			[15,'d-dimensional','','+','?']],
			include_outer_lines=True).scale(0.3)
		
		t2 = MathTable(
			[['','Class','R','OLW'],
			[1,'Posets','','?'],
			
			[3,'Interval Orders','','3w-2'],
			[4,'Interval Orders','+','3w-2'],
			
			
			[7,'Semi-orders','','2w-1'],
			[8,'Semi-orders','+','?'],
			
		
			[11,'2-dimensional','','?'],
			[12,'2-dimensional','+','\\binom{w+1}{2}'],
		
			[15,'d-dimensional','+','?']],
			include_outer_lines=True).scale(0.6)
		
		self.play(Create(t))
		self.wait(3)
		self.play(Transform(t,t2))
		self.wait(3)

		
class extension(Scene):
	def construct(self):
	
		extensions = Tex(r'When $P$ and $Q$ are partial orders on the same set $X$, we call $Q$ an \emph{extension} of $P$ if $P\subset Q$.', tex_environment='flushleft').scale(0.75).to_corner(UL)
		
		ex = Tex(r'$X=\{a,b,c,d\}$\\$P=\{(a,a),(b,b),(c,c),(d,d),(a,b),(b,d),(a,c),(c,d),(a,d)$',r'$\}$', tex_environment='flushleft').scale(0.75).next_to(extensions,DOWN).to_edge(LEFT)
		
		ex2 = Tex(r'$X=\{a,b,c,d\}$\\$P=\{(a,a),(b,b),(c,c),(d,d),(a,b),(b,d),(a,c),(c,d),(a,d)$',r',$(b,c)\}$', tex_environment='flushleft').scale(0.75).next_to(extensions,DOWN).to_edge(LEFT)
		ex2[1].set_color(YELLOW)
		
		lin_extensions = Tex(r'We call $Q$ a \emph{linear extension} of $P$ when $Q$ is an extension of $P$ and $(X,Q)$ is a chain.', tex_environment='flushleft').scale(0.75).to_corner(DL)
		
		self.play(Write(extensions))
		self.wait(2)
		
		def point(x,y,z=0):
			temp = Dot(point=np.array([x,y,z]))
			return temp 
		
		def rel(a,b,x,y):
		
			temp = seg([a,b],[x,y])
			return temp
		
		a= point(-2,-2)
		alabel= Tex(r'$a$').next_to(a,DOWN)
		b= point(-3,-1)
		blabel= Tex(r'$b$').next_to(b,LEFT)
		c= point(-1,-1)
		clabel= Tex(r'$c$').next_to(c,RIGHT)
		d= point(-2,0)
		dlabel= Tex(r'$d$').next_to(d,UP)
		p=Group(a,b,c,d)
		
		
		
		
		self.wait()
		self.play(Write(ex))
		self.wait(2)
		
		self.play(Create(a),Write(alabel),
			Create(b),Write(blabel), 
			Create(c),Write(clabel),
			Create(d),Write(dlabel))
			
		ab=rel(-2,-2,-3,-1)
		bd=rel(-3,-1,-2,0)
		ac=rel(-2,-2,-1,-1)
		cd=rel(-1,-1,-2,0)
		
		self.play(Create(VGroup(ab,bd,ac,cd)))
		self.wait(2)
		
		
		#ex2.set_color_by_tex('(b,c)', YELLOW)
		
		self.play(ReplacementTransform(ex[1],ex2[1]))
		self.wait(2)
		
		a2= point(2,-2.5)
		a2label= Tex(r'$a$').next_to(a2,RIGHT)
		b2= point(2,-1.5)
		b2label= Tex(r'$b$').next_to(b2,RIGHT)
		c2= point(2,-0.5)
		c2label= Tex(r'$c$').next_to(c2,RIGHT)
		d2= point(2,0.5)
		d2label= Tex(r'$d$').next_to(d2,RIGHT)
		p2=Group(a2,b2,c2,d2,a2label,b2label,c2label,d2label)
		
		self.play(Write(Tex(r'$\longrightarrow$').shift(DOWN + RIGHT*0.5)))
		self.play(TransformFromCopy(p,p2))
		'''
		self.play(Create(a2))
		self.play(Write(a2label))
		self.play(Create(b2))
		self.play(Write(b2label))
		self.play(Create(c2))
		self.play(Write(c2label))
		self.play(Create(d2))
		self.play(Write(d2label))
		'''
		ad = rel(2,-2.5,2,0.5)
		self.play(Create(ad))
		self.wait(2)
		
		self.play(Write(lin_extensions))
		self.wait(3)
		
class dim(Scene):
	def construct(self):
		
		realizer = Tex(r'Let $(X,P)$ be a poset. A set $\{L_1,\ldots,L_t\}$ of linear extensions of $P$ is called a \emph{realizer} of $(X,P)$ if $L_i\cap\ldots \cap L_t= P$.', tex_environment='flushleft').scale(0.75).to_corner(UL)
		
		dimension = Tex(r'The \emph{dimension} of $(X,P)$ is the least positive integer $t$ for which $(X,P)$ has a realizer of cardinality $t$.', tex_environment='flushleft').scale(0.75).next_to(realizer,DOWN).to_edge(LEFT)
		
		def point(x,y,z=0):
			temp = Dot(point=np.array([x,y,z]))
			return temp 
		
		def rel(a,b,x,y):
			temp = seg([a,b],[x,y])
			return temp
		
		
		a_point = point(0,0)
		b_point = point(2,0)
		c_point = point(-1,-1)
		d_point = point(1,-1)
		ca = rel(-1,-1,0,0)
		da = rel(1,-1,0,0)
		db = rel(1,-1,2,0)
		a_label = Tex(r'$a$').next_to(a_point,UP)
		b_label = Tex(r'$b$').next_to(b_point,UP)
		c_label = Tex(r'$c$').next_to(c_point,DOWN)
		d_label = Tex(r'$d$').next_to(d_point,DOWN)
		a = VGroup(a_point,a_label)
		b = VGroup(b_point,b_label)
		c = VGroup(c_point,c_label)
		d = VGroup(d_point,d_label)
		p = VGroup(a,b,c,d,ca,da,db)
		p.to_edge(LEFT).shift(RIGHT)
		
		x=-1
		a1 = point(x,-2)
		a2 = point(x,-1)
		a3 = point(x,0)
		a4 = point(x,1)
		l = rel(x,-2,x,1)
		l1 = Tex(r'$d$').next_to(a1)
		l2 = Tex(r'$c$').next_to(a2)
		l3 = Tex(r'$b$').next_to(a3)
		l4 = Tex(r'$a$').next_to(a4)
		L1 = VGroup(a1,a2,a3,a4,l,l1,l2,l3,l4)
		
		
		x=0.5
		a1 = point(x,-2)
		a2 = point(x,-1)
		a3 = point(x,0)
		a4 = point(x,1)
		l = rel(x,-2,x,1)
		l1 = Tex(r'$c$').next_to(a1)
		l2 = Tex(r'$d$').next_to(a2)
		l3 = Tex(r'$b$').next_to(a3)
		l4 = Tex(r'$a$').next_to(a4)
		L2 = VGroup(a1,a2,a3,a4,l,l1,l2,l3,l4)
		
		x=2
		a1 = point(x,-2)
		a2 = point(x,-1)
		a3 = point(x,0)
		a4 = point(x,1)
		l = rel(x,-2,x,1)
		l1 = Tex(r'$d$').next_to(a1)
		l2 = Tex(r'$c$').next_to(a2)
		l3 = Tex(r'$a$').next_to(a3)
		l4 = Tex(r'$b$').next_to(a4)
		L3 = VGroup(a1,a2,a3,a4,l,l1,l2,l3,l4)
		
		x=3.5
		a1 = point(x,-2)
		a2 = point(x,-1)
		a3 = point(x,0)
		a4 = point(x,1)
		l = rel(x,-2,x,1)
		l1 = Tex(r'$c$').next_to(a1)
		l2 = Tex(r'$d$').next_to(a2)
		l3 = Tex(r'$a$').next_to(a3)
		l4 = Tex(r'$b$').next_to(a4)
		L4 = VGroup(a1,a2,a3,a4,l,l1,l2,l3,l4)
		
		x=5
		a1 = point(x,-2)
		a2 = point(x,-1)
		a3 = point(x,0)
		a4 = point(x,1)
		l = rel(x,-2,x,1)
		l1 = Tex(r'$d$').next_to(a1)
		l2 = Tex(r'$b$').next_to(a2)
		l3 = Tex(r'$c$').next_to(a3)
		l4 = Tex(r'$a$').next_to(a4)
		L5 = VGroup(a1,a2,a3,a4,l,l1,l2,l3,l4)
		
		box = quad(3,-2.5,6,-2.5,6,1.5,3,1.5,YELLOW)
		
		end = Tex(r'$dim(P) = 2$').next_to(box,DOWN).set_color(YELLOW)
		
		self.play(Write(realizer))
		self.wait(2)
		self.play(Create(p))
		self.wait(2)
		self.play(Create(L1))
		self.play(Create(L2))
		self.play(Create(L3))
		self.play(Create(L4))
		self.play(Create(L5))
		self.wait(2)
			
		
		self.play(Write(dimension))
		self.wait(2)
		self.play(Create(box))
		self.wait(2)
		self.play(Write(end))
		self.wait(3)
	
class dim_problem(Scene):
	def construct(self):
		
			t2 = MathTable(
			[['Class','R','OLW'],
			['Posets','','?'],
			
#			['Interval Orders','','3w-2'],
#			['Interval Orders','+','3w-2'],
			
			
#			['Semi-orders','','2w-1'],
#			['Semi-orders','+','?'],
			
		
			['2-dimensional','','?'],
			['2-dimensional','+','\\binom{w+1}{2}'],
		
			['d-dimensional','+','?']],
			include_outer_lines=True).scale(0.6)
			
			t3 = MathTable(
			[['Class','R','OLW'],
			['Posets','','?'],
			
#			['Interval Orders','','3w-2'],
#			['Interval Orders','+','3w-2'],
			
			
#			['Semi-orders','','2w-1'],
#			['Semi-orders','+','?'],
			
		
			['2-dimensional','','?'],
			['2-dimensional','+','\\binom{w+1}{2}'],
		
			['d-dimensional','+','?']],
			include_outer_lines=True).scale(0.6).to_corner(UL)
			
			self.play(Create(t2))
			self.wait(2)
			self.play(ReplacementTransform(t2,t3))
			self.wait(2)
			
			fill = Tex('$OLW(w)$').move_to(t3[0][5].get_center()).scale(0.6)
			self.play(Transform(t3[0][5],fill))
			self.wait()
			
			fill = Tex('$OLW_2(w)$').move_to(t3[0][8].get_center()).scale(0.6)
			self.play(Transform(t3[0][8],fill))
			self.wait()
			
			fill = Tex('$OLW_d^R(w)$').move_to(t3[0][14].get_center()).scale(0.6)
			self.play(Transform(t3[0][14],fill))
			self.wait()
			
			olw = Tex(r'$(2-o(1))\binom{w+1}{2}$ ',r'$\leq OLW(w)\leq$',r' $ w^{O(\log\log w)}$')
			#olw.scale(0.7).shift(RIGHT*3+UP)
			
			olw2 = Tex(r'$\binom{w+1}{2}$ ',r'$\leq OLW_2(w)\leq$',r' $ w^{O(\log\log w)}$')
			#olw2.scale(0.7).shift(RIGHT*3)
			
			olwd = Tex(r'$\binom{w+1}{2}$ ',r'$\leq OLW_d^R(w)\leq$',r' $ w^{O(\log\log w)}$')
			#olwd.scale(0.7).shift(RIGHT*3+DOWN)
			
			table = MobjectTable(
				[[olw],
				[olw2],
				[olwd]],
				include_outer_lines=True)
			table.scale(0.6).to_corner(UR)
			#self.add(olw)
			#self.add(olw2)
			#self.add(olwd)
			olw.to_edge(RIGHT,buff=0.9)
			olw2.to_edge(RIGHT,buff=0.9)
			olwd.to_edge(RIGHT,buff=0.9)
			self.play(Create(table))
			self.wait(2)
			
			
			thm0 = Tex(r'\textbf{Theorem.} (Kierstead et al., 1984) $OLW_d^R(w)\leq \binom{w+1}{2}^{d-1}$.', tex_environment='flushleft').scale(0.7).next_to(t3,DOWN*2).to_edge(LEFT)
			
			thm = Tex(r'\textbf{Theorem.} (Bir\'o and Curbelo, in preparation) $OLW_2(w)\geq (2-o(1))\binom{w+1}{2}$.', tex_environment='flushleft').scale(0.7).next_to(thm0,DOWN).to_edge(LEFT)
			
			thm2 = Tex(r'\textbf{Theorem.} (Bir\'o and Curbelo, in preparation) $OLW_d^R(w)\geq (2-\frac{1}{d-1}-o(1))\binom{w+1}{2}$.', tex_environment='flushleft').scale(0.7).next_to(thm,DOWN).to_edge(LEFT)
			
			self.play(Write(thm0))
			self.play(Transform(olwd[2],Tex(r'$\binom{w+1}{2}^{d-1}$').scale(0.6).next_to(olwd[1],RIGHT)))
			self.wait(2)
			self.play(Write(thm))
			self.play(Transform(olw2[0],Tex(r'$(2-o(1))\binom{w+1}{2}$').scale(0.5).next_to(olw2[1],LEFT)))
			self.wait(2)
			self.play(Write(thm2))
			self.play(Transform(olwd[0],Tex(r'$(2-\frac{1}{d-1}-o(1))\binom{w+1}{2}^{d-1}$').scale(0.35).next_to(olwd[1],LEFT)))
			
			
			self.wait(3)
			#self.play(Write(olw))
			
			
		
class semi(Scene):
	def construct(self):
		
		interval = Tex(r'A poset $(X,P)$ is an \emph{interval order} if it has an interval representation.', tex_environment='flushleft').scale(0.75).to_corner(UL)
		
		semiorder = Tex(r'A poset $(X,P)$ is a \emph{semi-order} if it has a unit-interval representation.', tex_environment='flushleft').scale(0.75).to_corner(UL)
		
		def point(x,y,z=0):
			temp = Dot(point=np.array([x,y,z]))
			self.play(Create(temp))
			return temp 
		
		def rel(a,b,x,y):
			temp = seg([a,b],[x,y])
			self.play(Create(temp))
			return temp
			
		self.play(Write(interval))	
		self.wait(2)
			
		a = point(-4,0)
		al = Tex(r'$a$').next_to(a, LEFT)
		self.play(Write(al))
		
		b = point(-4,1)
		bl = Tex(r'$b$').next_to(b, LEFT)
		self.play(Write(bl))
		
		ab = rel(-4,0,-4,1)
		
		self.wait(2)
		
		inta = seg([-1,0.5],[1,0.5])
		intb = seg([2,0.5],[4,0.5])
		intal = Tex(r'$a$').next_to(inta, DOWN)
		intbl = Tex(r'$b$').next_to(intb, DOWN)
		
		newa = Group(inta, intal)
		newb = Group(intb, intbl)
		
		self.play(TransformFromCopy(a,newa))
		self.play(TransformFromCopy(b,newb))
		self.wait(2)
		
		c = point(-4.5,-3)
		cl = Tex(r'$c$').next_to(c, LEFT)
		self.play(Write(cl))
		
		d = point(-3.5,-3)
		dl = Tex(r'$d$').next_to(d, RIGHT)
		self.play(Write(dl))
		self.wait(2)
		
		intc = seg([0,-3.1],[2,-3.1])
		intd = seg([1,-2.9],[3,-2.9])
		intcl = Tex(r'$c$').next_to(intc, LEFT)
		intdl = Tex(r'$d$').next_to(intd, RIGHT)
		
		newc = Group(intc, intcl)
		newd = Group(intd, intdl)
		
		self.play(TransformFromCopy(c,newc))
		self.play(TransformFromCopy(d,newd))
		
		self.wait(2)
		
		self.play(Transform(interval,semiorder))
		
		self.wait(3)
		
class semiex(Scene):
	def construct(self):
	
		def point(x,y,z=0):
			temp = Dot(point=np.array([x,y,z]))
			self.play(Create(temp))
			return temp 
		
		def rel(a,b,x,y):
			temp = seg([a,b],[x,y])
			self.play(Create(temp))
			return temp
		
		a = point(-4,0)
		al= Tex(r'$a$').next_to(a,LEFT)
		self.play(Write(al))
		
		b = point(-3,-1)
		bl = Tex(r'$b$').next_to(b, RIGHT)
		self.play(Write(bl))
		
		c = point(-3,0)
		cl = Tex(r'$c$').next_to(c, RIGHT)
		self.play(Write(cl))
		
		d = point(-3,1)
		dl = Tex(r'$d$').next_to(d, RIGHT)
		self.play(Write(dl))
		
		bcd = rel(-3,-1,-3,1)
		
		self.wait(2)
		 
		intb = seg([-1,0.1],[0,0.1])
		intc = seg([1,0.1],[2,0.1])
		intd = seg([3,0.1],[4,0.1])
		inta = seg([-1,-0.1],[4,-0.1])
		intal = Tex(r'$a$').next_to(inta, DOWN)
		intbl = Tex(r'$b$').next_to(intb, UP)
		intcl = Tex(r'$c$').next_to(intc, UP)
		intdl = Tex(r'$d$').next_to(intd, UP)
		newa = Group(inta, intal)
		newb = Group(intb, intbl)
		newc = Group(intc, intcl)
		newd = Group(intd, intdl)
		
		self.play(TransformFromCopy(a,newa))
		self.play(TransformFromCopy(b,newb))		
		self.play(TransformFromCopy(c,newc))
		self.play(TransformFromCopy(d,newd))
		
		self.wait(3)



class semi_problem(Scene):
	def construct(self):
		
		t2 = MathTable(
			[['Class','R','OLW'],
			['Posets','','?'],
			
			['Interval Orders','','3w-2'],
			['Interval Orders','+','3w-2'],
			
			
			['Semi-orders','','2w-1'],
			['Semi-orders','+','?']],
			
		
#			['2-dimensional','','?'],
#			['2-dimensional','+','\\binom{w+1}{2}'],
		
#			['d-dimensional','+','?']],
			include_outer_lines=True).scale(0.8)
			
		t3 = MathTable(
			[['Class','R','OLW'],
			['Posets','','?'],
			
			['Interval Orders','','3w-2'],
			['Interval Orders','+','3w-2'],
			
			
			['Semi-orders','','2w-1'],
			['Semi-orders','+','?']],
			
		
#			['2-dimensional','','?'],
#			['2-dimensional','+','\\binom{w+1}{2}'],
		
#			['d-dimensional','+','?']],
			include_outer_lines=True).scale(0.8).to_edge(UP)
			
		self.play(Create(t2))
		self.wait(2)
		self.play(ReplacementTransform(t2,t3))
		self.wait(2)
		
		fill = Tex('$OLW_s^R(w)$').move_to(t3[0][17].get_center()).scale(0.6)
		self.play(Transform(t3[0][17],fill))
		self.wait(2)
		
		olws = Tex(r'$\lfloor{\frac{3w}{2}\rfloor}$ ',r'$\leq OLW_s^R(w)\leq$',r' $2w-1$')
		table = MobjectTable([[olws]],include_outer_lines=True)
		table.scale(0.8).shift(DOWN*3)
		
		self.play(Create(table))
		
		self.wait(3)
		
class 

#test comment