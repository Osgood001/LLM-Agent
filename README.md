# A LLM-Driven Agent framework

This project is a demo for LLM-Agent. It can use tools like wolfram Alpha to get latest data and accurate information.

A demonstration on how left and right brain mindset could combine to solve real world problems.

Examples below.

## Information Query

### Accurate math computation

![Screenshot_20240324_110837.jpg](https://github.com/Osgood001/LLM-Agent/assets/60919782/b77fdcb6-bca9-4681-abe6-b8391835b403)

### Weather related data


![Screenshot_20240324_110818.jpg](https://github.com/Osgood001/LLM-Agent/assets/60919782/6633bb92-0b6c-417c-ac8d-ad807696f736)

### Daily activities

![Screenshot_20240324_110828.jpg](https://github.com/Osgood001/LLM-Agent/assets/60919782/df24d65a-0ac6-488e-a770-183945c320b0)

### Geographical Result

![Screenshot_20240324_110758.jpg](https://github.com/Osgood001/LLM-Agent/assets/60919782/a50d7616-1e25-4279-a0ed-72d8d5f6dcdf)

### Accurate stock market information

![Screenshot_20240324_110810.jpg](https://github.com/Osgood001/LLM-Agent/assets/60919782/6aba331f-b1b3-47a5-8892-94d1e7689f02)





## Iterative general problem solving


### Solving a biogenetic problem
```mathematica
Hello 
 Welcome to the Agent System.
 We provide you with the following chatbots:
1. a: b
2. test_bot: read the file and return the content of the file exactly
3. Mmaster: Use Mathematica to solve anything
4. good_boy: test again
5. Create a new assistant

 Please enter the index of your choice: 3
Loaded existing assistant ID for Mmaster.
Enter your message: Calculate N50 for contig lengths 80kb, 60kb, 50kb, 48kb, 35kb, 27kb, 22kb, 19kb, 19kb, 13kb, 8kb, 5kb
Received message: Calculate N50 for contig lengths 80kb, 60kb, 50kb, 48kb, 35kb, 27kb, 22kb, 19kb, 19kb, 13kb, 8kb, 5kb in thread thread_DfpY9K39b59MRbLfmdQhGK4a

 Querying Wolfram Alpha for information...
Query: arrange 80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5 in decreasing order
Query complete.

Output: {{{Input, 1}, Plaintext} -> reverse sort | (80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5), {{Result, 1}, Plaintext} -> {80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5}, {{Input, 1}, Input} -> HoldComplete[ReverseSort[{80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5}]], {{Result, 1}, Input} -> HoldComplete[ReverseSort[{80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5}]]}



 Querying Wolfram Alpha for information...
Query: total 80+60+50+48+35+27+22+19+19+13+8+5
Query complete.

Output: {{{Input, 1}, Plaintext} -> 80 + 60 + 50 + 48 + 35 + 27 + 22 + 19 + 19 + 13 + 8 + 5, {{Result, 1}, Plaintext} -> 386, {{NumberName, 1}, Plaintext} -> three hundred eighty-six, {{Input, 1}, Input} -> HoldComplete[80 + 60 + 50 + 48 + 35 + 27 + 22 + 19 + 19 + 13 + 8 + 5], {{NumberName, 1}, Input} -> HoldComplete[IntegerName[386, Words]]}



 Querying Wolfram Alpha for information...
Query: 386/2
Query complete.

Output: {{{Input, 1}, Plaintext} -> 386/2, {{Result, 1}, Plaintext} -> 193, {{QuotientAndRemainder, 1}, Plaintext} -> 386 = 193  2 + 0, {{NumberName, 1}, Plaintext} -> one hundred ninety-three, {{Input, 1}, Input} -> HoldComplete[386/2], {{NumberLine, 1}, Input} -> HoldComplete[NumberLinePlot[193]], {{QuotientAndRemainder, 1}, Input} -> HoldComplete[QuotientRemainder[386, 2]], {{NumberName, 1}, Input} -> HoldComplete[IntegerName[193, Words]]}    



 Querying Wolfram Alpha for information...
Query: 80+60+50+48
Query complete.

Output: {{{Input, 1}, Plaintext} -> 80 + 60 + 50 + 48, {{Result, 1}, Plaintext} -> 238, {{NumberName, 1}, Plaintext} -> two hundred thirty-eight, {{Input, 1}, Input} -> HoldComplete[80 + 60 + 50 + 48], {{NumberName, 1}, Input} -> HoldComplete[IntegerName[238, Words]]}


The midpoint of the total length is 193.

Now, let's calculate the N50 value by summing the lengths of the contigs starting from the longest, until the cumulative sum equals or exceeds 193:   

- 80 + 60 + 50 + 48 = 238 (exceeds 193, so the N50 value is 48)

So, the N50 value for the given contig lengths is 48kb.
Enter your message: what about L50
Received message: what about L50 in thread thread_DfpY9K39b59MRbLfmdQhGK4a

 Querying Wolfram Alpha for information...
Query: lengths 80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5
Query complete.

Output: {{{Input, 1}, Plaintext} -> triangle | edge lengths 80 | 60 | 50 | 48 | 35 | 27 | 22 | 19 | 19 | 13 | 8 | 5, {{Result, 1}, Plaintext} -> (not a possible triangle)}



 Querying Wolfram Alpha for information...
Query: count 80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5
Query complete.
Output: {}



 Querying Wolfram Alpha for information...
Query: count of elements in the list {80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5}
Query complete.

Output: {{{Input, 1}, Plaintext} -> length | (80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5), {{Result, 1}, Plaintext} -> 12, {{Input, 1}, Input} -> HoldComplete[Length[{80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5}]], {{Result, 1}, Input} -> HoldComplete[Length[{80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5}]]}



 Querying Wolfram Alpha for information...
Query: index of 48 in list {80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5}
Query complete.

Output: {}



 Querying Wolfram Alpha for information...
Query: position of 48 in {80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5}
Query complete.

Output: {{{Input, 1}, Plaintext} -> position | (80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5)
pattern 48, {{Result, 1}, Plaintext} -> (4), {{Input, 1}, Input} -> HoldComplete[Position[{80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5}, 48]], {{Result, 1}, Input} -> HoldComplete[Position[{80, 60, 50, 48, 35, 27, 22, 19, 19, 13, 8, 5}, 48]]}


The position of the contig length 48 in the list is 4.

To find the L50 value, we need to count the number of contigs with indices less than or equal to 4, since the N50 value is at index 4.

Therefore, the L50 value is 4.

So, the L50 for the given contig lengths is 4.
```

The result is correct, all by agent itself, without human interference/prior knowledge.



### A quantum mechanics problem

```mathematica
Enter your message: 
Derive the probability flow distribution of spherical wave $\braket{\vec{r}|\psi} = \frac{1}{(2\pi)^{3/2}}\frac{e^{ikr}}{r}$, and discuss the behavior when $r\rightarrow\infty$.

Received message: Derive the probability flow distribution of spherical wave $\braket{\vec{r}|\psi} = \frac{1}{(2\pi)^{3/2}}\frac{e^{ikr}}{r}$, and discuss the behavior when $r\rightarrow\infty$. in thread thread_RxUKPMWnZrerP2lXr30QhTKk

 Querying Wolfram Alpha for information...
Query: probability flow distribution of spherical wave psi = (1/(2 pi)^(3/2))(e^(ikr)/r)
Query complete.

Output: {}



 Querying Wolfram Alpha for information...
Query: complex conjugate of (1/(2 pi)^(3/2))(e^(i k r)/r)
Query complete.

Output: {{{Input, 1}, Plaintext} -> (1/(2 \[Pi])^(3/2))^*e^(i k r)/r, {{Result, 1}, Plaintext} -> e^(i k r)/(2 sqrt(2) \[Pi]^(3/2) r), {{AlternateFormAssumingAllVariablesAreReal, 1}, Plaintext} -> cos(k r)/(2 sqrt(2) \[Pi]^(3/2) r) + (i sin(k r))/(2 sqrt(2) \[Pi]^(3/2) r), {{NoSolutionsFromReduce, 1}, Plaintext} -> (no roots exist), {{SeriesExpansionAtr=0, 1}, Plaintext} -> 1/(2 sqrt(2) \[Pi]^(3/2) r) + (i k)/(2 sqrt(2) \[Pi]^(3/2)) - (k^2 r)/(4 (sqrt(2) \[Pi]^(3/2))) - (i k^3 r^2)/(12 sqrt(2) \[Pi]^(3/2)) + (k^4 r^3)/(48 sqrt(2) \[Pi]^(3/2)) + O(r^4)
(Laurent series), {{Derivative, 1}, Plaintext} -> d/dr(((1/(2 \[Pi])^(3/2))^* e^(i k r))/r) = (i e^(i k r) (k r + i))/(2 sqrt(2) \[Pi]^(3/2) r^2), {{IndefiniteIntegral, 1}, Plaintext} -> integral e^(i k r)/(2 sqrt(2) \[Pi]^(3/2) r) dr = Ei(i k r)/(2 sqrt(2) \[Pi]^(3/2)) + constant, {{AlternativeRepresentations:MathematicalFunctionIdentityData, 1}, Plaintext} -> ((1/(2 \[Pi])^(3/2))^* e^(i k r))/r = (e^(i k r) abs(1/(2 \[Pi])^(3/2))^2)/(r/(2 \[Pi])^(3/2)), {{AlternativeRepresentations:MathematicalFunctionIdentityData, 2}, Plaintext} -> ((1/(2 \[Pi])^(3/2))^* e^(i k r))/r = ((1/(2 \[Pi])^(3/2) - i (2 Im(1/(2 \[Pi])^(3/2)))) z^(i k r))/r for z = e, {{AlternativeRepresentations:MathematicalFunctionIdentityData, 3}, Plaintext} -> ((1/(2 \[Pi])^(3/2))^* e^(i k r))/r = e^(i k r)/(r e^(2 i arg(1/(2 \[Pi])^(3/2))) (2 \[Pi])^(3/2)), {{SeriesRepresentations:MathematicalFunctionIdentityData, 1}, Plaintext} -> ((1/(2 \[Pi])^(3/2))^* e^(i k r))/r = ( sum_(j=0)^Infinity (i k r)^j/(j!))/(2 sqrt(2) \[Pi]^(3/2) r), {{SeriesRepresentations:MathematicalFunctionIdentityData, 2}, Plaintext} -> ((1/(2 \[Pi])^(3/2))^* e^(i k r))/r = ( sum_(A=0)^Infinity ((i k r)^(-1 + 2 A) (i k r + 2 A))/((2 A)!))/(2 sqrt(2) \[Pi]^(3/2) r), {{SeriesRepresentations:MathematicalFunctionIdentityData, 3}, Plaintext} -> ((1/(2 \[Pi])^(3/2))^* e^(i k r))/r = ( sum_(A=0)^Infinity ((i k r)^(2 A) (1 + i k r + 2 A))/((1 + 2 A)!))/(2 sqrt(2) \[Pi]^(3/2) r), {{Input, 1}, Input} -> HoldComplete[Conjugate[1/(2*Pi)^(3/2)]*E^(I*k*r)/r], {{3DPlot, 1}, Input} -> HoldComplete[Plot3D[Re[E^(I*k*r)/r]/(2*Sqrt[2]*Pi^(3/2)), {k, -3.92288, 3.92288}, {r, -3.92288, 3.92288}]], {{3DPlot, 2}, Input} -> HoldComplete[Plot3D[Im[E^(I*k*r)/r]/(2*Sqrt[2]*Pi^(3/2)), {k, -3.92288, 3.92288}, {r, -3.92288, 3.92288}]], {{ContourPlot, 1}, Input} -> HoldComplete[ContourPlot[Re[E^(I*k*r)/r]/(2*Sqrt[2]*Pi^(3/2)), {k, -3.92288, 3.92288}, {r, -3.92288, 3.92288}]], {{ContourPlot, 2}, Input} -> HoldComplete[ContourPlot[Im[E^(I*k*r)/r]/(2*Sqrt[2]*Pi^(3/2)), {k, -3.92288, 3.92288}, {r, -3.92288, 3.92288}]], {{AlternateFormAssumingAllVariablesAreReal, 1}, Input} -> HoldComplete[ComplexExpand[E^(I*k*r)/(2*Sqrt[2]*Pi^(3/2)*r)]], {{NoSolutionsFromReduce, 1}, Input} -> HoldComplete[Reduce[{E^(I*k*r)/(2*Sqrt[2]*Pi^(3/2)*r) == 0}, {k, r}]], {{SeriesExpansionAtr=0, 1}, Input} -> HoldComplete[Series[E^(I*k*r)/(2*Sqrt[2]*Pi^(3/2)*r), {r, 0, 4}]], {{Derivative, 1}, Input} -> HoldComplete[D[E^(I*k*r)/(2*Sqrt[2]*Pi^(3/2)*r), r]], {{IndefiniteIntegral, 1}, Input} -> HoldComplete[Integrate[E^(I*k*r)/(2*Sqrt[2]*Pi^(3/2)*r), r]], {{AlternativeRepresentations:MathematicalFunctionIdentityData, 1}, Input} -> HoldComplete[Conjugate[1/(2*Pi)^(3/2)]*E^(I*k*r)/r == (E^(I*k*r)*Abs[((2*Pi)^(3/2))^(-1)]^2)/(r/(2*Pi)^(3/2))], {{AlternativeRepresentations:MathematicalFunctionIdentityData, 2}, Input} -> HoldComplete[Conjugate[1/(2*Pi)^(3/2)]*E^(I*k*r)/r == (1/(2*Pi)^(3/2) - 2*I*Im[1/(2*Pi)^(3/2)])*z^(I*k*r)/r /; z == E], {{AlternativeRepresentations:MathematicalFunctionIdentityData, 3}, Input} -> HoldComplete[Conjugate[1/(2*Pi)^(3/2)]*E^(I*k*r)/r == E^(I*k*r)/(r*E^(2*I*Arg[((2*Pi)^(3/2))^(-1)])*(2*Pi)^(3/2))], {{SeriesRepresentations:MathematicalFunctionIdentityData, 1}, Input} -> HoldComplete[Conjugate[1/(2*Pi)^(3/2)]*E^(I*k*r)/r == Sum[(I*k*r)^j/j!, {j, 0, Infinity}]/(2*Sqrt[2]*Pi^(3/2)*r)], {{SeriesRepresentations:MathematicalFunctionIdentityData, 2}, Input} -> HoldComplete[Conjugate[1/(2*Pi)^(3/2)]*E^(I*k*r)/r == Sum[((I*k*r)^(-1 + 2*\[ScriptCapitalA])*(I*k*r + 2*\[ScriptCapitalA]))/(2*\[ScriptCapitalA])!, {\[ScriptCapitalA], 0, Infinity}]/(2*Sqrt[2]*Pi^(3/2)*r)], {{SeriesRepresentations:MathematicalFunctionIdentityData, 3}, Input} -> HoldComplete[Conjugate[1/(2*Pi)^(3/2)]*E^(I*k*r)/r == Sum[((I*k*r)^(2*\[ScriptCapitalA])*(1 + I*k*r + 2*\[ScriptCapitalA]))/(1 + 2*\[ScriptCapitalA])!, {\[ScriptCapitalA], 0, Infinity}]/(2*Sqrt[2]*Pi^(3/2)*r)]}



 Querying Wolfram Alpha for information...
Query: gradient of (1/(2 pi)^(3/2))(e^(i k r)/r)
Query complete.

Output: {{{Input, 1}, Plaintext} -> grad(1/(2 \[Pi])^(3/2)e^(i k r)/r), {{DelOperatorForm, 1}, Plaintext} -> del (e^(i k r)/((2 \[Pi])^(3/2) r)), {{VectorAnalysisResult, 1}, Plaintext} -> grad(e^(i k r)/((2 \[Pi])^(3/2) r)) = ((i e^(i k r) (i + k r))/(2 sqrt(2) \[Pi]^(3/2) r^2), 0)
in Cartesian coordinates:
... = (i e^(i k sqrt(x^2 + y^2)) x (i + k sqrt(x^2 + y^2)))/(2 sqrt(2) \[Pi]^(3/2) (x^2 + y^2)^(3/2)) e_x + (i e^(i k sqrt(x^2 + y^2)) y (i + k sqrt(x^2 + y^2)))/(2 sqrt(2) \[Pi]^(3/2) (x^2 + y^2)^(3/2)) e_y
(r: radial coordinate | \[Phi]: azimuthal angle), {{VectorAnalysisResult, 2}, Plaintext} -> x = r cos(\[Phi])
y = r sin(\[Phi])
r = sqrt(x^2 + y^2)
\[Phi] = tan^(-1)(x, y), {{Input, 1}, Input} -> HoldComplete[Grad[1/(2*Pi)^(3/2)*E^(I*k*r)/r, {r}]]}



 Querying Wolfram Alpha for information...
Query: probability flow distribution of spherical wave J = ((hbar)/(2i*m))*((1/(2*Pi)^(3/2)*e^(-i*k*r)/r)*del(((1/(2*Pi)^(3/2)*e^(i*k*r)/r), {r})) - ((1/(2*Pi)^(3/2)*e^(i*k*r)/r)*del(((1/(2*Pi)^(3/2)*e^(-i*k*r)/r), {r})))
Query complete.

Output: {}



 Querying Wolfram Alpha for information...
Query: ((1/(2*Pi)^(3/2)*e^(-i*k*r)/r)*del(((1/(2*Pi)^(3/2)*e^(i*k*r)/r), {r})) - ((1/(2*Pi)^(3/2)*e^(i*k*r)/r)*del(((1/(2*Pi)^(3/2)*e^(-i*k*r)/r), {r})))       
Query complete.

Output: {}



 Querying Wolfram Alpha for information...
Query: ((hbar)/(2i*m))*((1/(2*Pi)^(3/2)*e^(-i*k*r)/r)*((i e^(i k r) r (i + k r))/(2 sqrt(2) Pi^(3/2) r^2)) - (1/(2*Pi)^(3/2)*e^(i k r)/r)*((i e^(i k r) r (i + k r))/(2 sqrt(2) Pi^(3/2) r^2)))
Query complete.

Output: {{{Input, 1}, Plaintext} -> (\[HBar] (reduced Planck constant))/(2 i m) ((1/(2 \[Pi])^(3/2)e^(-i (k r))/r)(i e^(i k r) r (i + k r))/(2 sqrt(2) \[Pi]^(3/2) r^2) - (1/(2 \[Pi])^(3/2)e^(i k r)/r)(i e^(i k r) r (i + k r))/(2 sqrt(2) \[Pi]^(3/2) r^2)), {{Result, 1}, Plaintext} -> (((i (k r + i))/(8 \[Pi]^3 r^2) - (i e^(2 i k r) (k r + i))/(8 \[Pi]^3 r^2)) (0 - 0.5 i) \[HBar] (reduced Planck constants))/m, {{Input, 1}, Input} -> HoldComplete[Quantity[None, ReducedPlanckConstant]/(2*I*m)*((1/(2*Pi)^(3/2)*1/(E^(I*(k*r))*r))*(I*E^(I*k*r)*r*(I + k*r))/(2*Sqrt[2]*Pi^(3/2)*r^2) - (1/(2*Pi)^(3/2)*E^(I*k*r)/r)*(I*E^(I*k*r)*r*(I + k*r))/(2*Sqrt[2]*Pi^(3/2)*r^2))]}


The evaluated probability flow distribution \( \vec{J} \) is:

\[ \vec{J} = \left( \frac{i(kr+i)}{8\pi^3r^2} - \frac{i e^{2i kr}(kr+i)}{8\pi^3r^2} \right) \frac{-0.5i\hbar}{m} \]

Now, let's discuss its behavior as \( r \rightarrow \infty \). As \( r \) tends to infinity, the exponential term \( e^{2i kr} \) oscillates rapidly, resulting in the probability flow distribution oscillating and losing its directional dependence as position \( \vec{r} \) becomes asymptotically far from the origin. This indicates that the probability flux is virtually uniform in all directions at large distances from the source, characteristic of a spherical wave spreading out over space.

Therefore, as \( r \) approaches infinity, the probability flow distribution \( \vec{J} \) becomes less directional and shows a uniform spread in all directions.

This behavior aligns with the expected characteristics of a spherical wave as it propagates outward from the source.

Enter your message: 将做题过程用markdown codeb lock 格式整理出来，用中文        
Received message: 将做题过程用markdown codeb lock 格式整理出来，用中文 in thread thread_RxUKPMWnZrerP2lXr30QhTKk
```

当计算波函数 $\braket{\vec{r}|\psi}$ 的复共轭时，得到:
$$ \braket{\vec{r}|\psi^*} = \frac{1}{(2\pi)^{3/2}}\frac{e^{-ikr}}{r} $$

计算波函数的梯度后，得到:
$$ \nabla(\braket{\vec{r}|\psi}) = \left(\frac{i e^{ikr} r (i+kr)}{2\sqrt{2}\pi^{3/2}r^2}, 0\right) $$

利用以上结果计算概率流分布 $\vec{J}$，得到:
$$ \vec{J} = \left( \frac{\hbar}{2im} \right) \left( \frac{1}{(2\pi)^{3/2}}\frac{e^{-ikr}}{r} \nabla\left(\frac{1}{(2\pi)^{3/2}}\frac{e^{ikr}}{r}\right) - \frac{1}{(2\pi)^{3/2}}\frac{e^{ikr}}{r} \nabla\left(\frac{1}{(2\pi)^{3/2}}\frac{e^{-ikr}}{r}\right) $$

计算得到:
$$ \vec{J} = \left( \frac{i(kr+i)}{8\pi^3r^2} - \frac{i e^{2i kr}(kr+i)}{8\pi^3r^2} \right) \frac{-0.5i\hbar}{m} $$

当 $ r $ 趋近无穷大时，指数项 $ e^{2i kr} $ 将会迅速振荡，导致概率流分布在位置 $ \vec{r} $ 远离原点的时候，失去方向性，即概率流将在距源头较远的地方均匀地分布在 所有方向上。