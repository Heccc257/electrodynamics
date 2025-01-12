### intput: 
﻿1.  根据算符 $\nabla$ 的微分性与矢量性推导下列公式  $$\nabla(\vec{A}\cdot\vec{B})=\vec{B}\times(\nabla\times\vec{A})+(\vec{B}\cdot\nabla)\vec{A}+\vec{A}\times(\nabla\times\vec{B})+(\vec{A}\cdot\nabla)\vec{B}$$  $$\vec{A}\times(\nabla\times\vec{A})=\frac{1}{2}\nabla\vec{A}^{2}-(\vec{A}\!\cdot\!\nabla)\vec{A}$$
### standard: 
$$\nabla(\vec{A}\cdot\vec{B})=\vec{B}\times(\nabla\times\vec{A})+(\vec{B}\cdot\nabla)\vec{A}+\vec{A}\times(\nabla\times\vec{B})+(\vec{A}\cdot\nabla)\vec{B}$$  首先 算符 $\nabla$ 是一个微分算符 其具有对其后所有表达式起微分的作用 对于本题$\nabla$ 将作用于 $\vec{A}$ 和 $\vec{B}$ 。  又 $\nabla$ 是一个矢量算符具有矢量的所有性质  因此 利用公式 ${\vec{c}}\times({\vec{a}}\times{\vec{b}})={\vec{a}}\cdot({\vec{c}}\cdot{\vec{b}})-({\vec{c}}\cdot{\vec{a}}){\vec{b}}$ 可得上式 其中右边前两项是 $\nabla$ 作用于$\vec{A}$ 后两项是 $\nabla$ 作用于 $\vec{B}$  2 根据第一个公式 令 $\vec{A}=\vec{B}$ 可得证
### output: 

其中 $\vec{A}$ 和 $\vec{B}$ 是任意 vector场.
为了推导给定的公式，我们将使用向量恒等式和算子 \(\nabla\) 的性质。让我们从第一个公式开始：

### 第一个公式的推导

我们想要证明：
$$
\nabla(\vec{A} \cdot \vec{B}) = \vec{B} \times (\nabla \times \vec{A}) + (\vec{B} \cdot \nabla) \vec{A} + \vec{A} \times (\nabla \times \vec{B}) + (\vec{A} \cdot \nabla) \vec{B}
$$

我们可以使用 div-grad-curl 算子的乘积规则。div-grad-curl 算子关于标量函数 \(f\) 和向量场 \(\vec{F}\) 的乘积有以下性质：
$$
\nabla(f \vec{F}) = f \nabla \vec{F} + \vec{F} \nabla f
$$

将此应用于 \(\vec{A} \cdot \vec{B}\)，设 \(f = \vec{A} \cdot \vec{B}\)。那么：
$$
\nabla(\vec{A} \cdot \vec{B}) = \nabla(\vec{A}^T \vec{B})
$$
然而，这个形式更复杂处理。相反，我们将使用不同的方法。

考虑向量三重积恒等式：
$$
\vec{u} \times (\vec{v} \times \vec{w}) = (\vec{u} \cdot \vec{w}) \vec{v} - (\vec{u} \cdot \vec{v}) \vec{w}
$$

应用此恒等式到 \(\nabla \times (\vec{A} \times \vec{B})\)，设 \(\vec{u} = \vec{B}\), \(\vec{v} = \nabla\), 和 \(\vec{w} = \vec{A}\)：
$$
\vec{B} \times (\nabla \times \vec{A}) = (\vec{B} \cdot \nabla) \vec{A} - (\vec{B} \cdot \vec{A}) \nabla
$$

同样地，对 \(\nabla \times (\vec{B} \times \vec{A})\) 应用恒等式：
$$
\vec{B} \times (\nabla \times \vec{A}) = (\vec{B} \cdot \nabla) \vec{A} - (\vec{B} \cdot \vec{A}) \nabla
$$

现在，考虑两个表达式的差：
$$
\vec{B} \times (\nabla \times \vec{A}) + \vec{A} \times (\nabla \times \vec{B})
$$
使用恒等式：
$$
\vec{B} \times (\nabla \times \vec{A}) + \vec{A} \times (\nabla \times \vec{B}) = (\vec{B} \cdot \nabla) \vec{A} - (\vec{B} \cdot \nabla) \vec{C} + (\vec{A} \cdot \nabla) \vec{B} - (\vec{A} \cdot \nabla) \vec{A}
$$

组合项，我们得到：
$$
\vec{B} \times (\
***
### intput: 
2.  设 $\boldsymbol{\mathbf{\rho}}_{\mathrm{u}}$ 是空间坐标 $\mathrm{~\bf~X~},\mathrm{~\bf~y~},\mathrm{~\bf~Z~}$ 的函数 证明  $$\begin{array}{l}{\displaystyle\nabla f(\boldsymbol{u})\,{=}\,\frac{d f}{d u}\nabla u}\\ {\displaystyle\nabla\cdot\vec{A}(\boldsymbol{u})=\nabla u\cdot\frac{d\vec{A}}{d u}}\\ {\displaystyle\nabla\times\vec{A}(\boldsymbol{u})\,{=}\,\nabla u\times\frac{d\vec{A}}{d u}.}\end{array}$$
### standard: 
证明  1  $$\nabla f(u)=\frac{\partial f(u)}{\hat{\sigma}x}\vec{e}_{x}+\frac{\partial f(u)}{\hat{\sigma}y}\vec{e}_{y}\:+\frac{\partial f(u)}{\hat{\sigma}z}\vec{e}_{z}=\frac{d f}{d u}\cdot\frac{\hat{\alpha}u}{\hat{\sigma}x}\vec{e}_{x}\:+\frac{d f}{d u}\cdot\frac{\hat{\alpha}u}{\hat{\sigma}y}\vec{e}_{y}\:+\frac{d f}{d u}\cdot\frac{\hat{\alpha}u}{\hat{\sigma}z}\vec{e}_{z}=\frac{d f}{d u}\nabla u$$  2  $$\nabla\cdot\vec{A}(u)=\frac{\partial\vec{A}_{x}(u)}{\partial x}+\frac{\partial\vec{A}_{y}(u)}{\partial y}+\frac{\partial\vec{A}_{z}z(u)}{\partial z}=\frac{d\vec{A}_{x}(u)}{d u}\cdot\frac{\partial u}{\partial x}+\frac{d\vec{A}_{y}(u)}{d u}\cdot\frac{\partial u}{\partial y}+\frac{d\vec{A}_{z}(u)}{d z}\cdot\frac{\partial u}{\partial z}=\nabla u\,.$$  3  $$\nabla\times\vec{A}(u)=\left|\begin{array}{l l l}{\vec{e}_{x}}&{\vec{e}_{y}}&{\vec{e}_{z}}\\ {\frac{\partial}{\partial x}}&{\frac{\partial}{\partial y}}&{\frac{\partial}{\partial z}}\\ {\vec{A}_{x(u)}}&{\vec{A}_{y}(u)}&{\vec{A}_{z}(u)}\end{array}\right|=(\frac{\partial\vec{A}_{z}}{\partial y}-\frac{\partial\vec{A}_{y}}{\partial z})\vec{e}_{x}+(\frac{\partial\vec{A}_{x}}{\partial z}-\frac{\partial\vec{A}_{z}}{\partial x})\vec{e}_{y}+(\frac{\partial\vec{A}_{y}}{\partial x}-\frac{\partial\vec{A}_{x}}{\partial y})\vec{e}_{z}=\vec{e}_{z}\vec{A}_{y}-\vec{A}_{z}(u)\vec{A}_{z},$$  $=(\frac{d\vec{A}_{z}}{d u}\frac{\partial u}{\partial y}-\frac{d\vec{A}_{y}}{d u}\frac{\partial u}{\partial z})\vec{e}_{x}+(\frac{d\vec{A}_{x}}{d u}\frac{\partial u}{\partial z}-\frac{d\vec{A}_{z}}{d u}\frac{\partial u}{\partial x})\vec{e}_{y}+(\frac{d\vec{A}_{y}}{d u}\frac{\partial u}{\partial x}-\frac{d\vec{A}_{x}}{d u}\frac{\partial u}{\partial y})\vec{e}_{z}=\nabla u\times\frac{d\vec{A}_{z}}{d u}$
### output: 

To prove the given vector calculus identities, we will use the chain rule and properties of the gradient, divergence, and cross product. Let's start with each identity one by one.

### Identity 1: \(\nabla f(\boldsymbol{u}) = \frac{d f}{d u} \nabla u\)

Given \(f\) is a scalar function of \(\boldsymbol{u} = (u_1, u_2, u_3)\), we can express \(f\) as \(f(u_1, u_2, u_3)\). The gradient of \(f\) is:
$$
\nabla f = \left( \frac{\partial f}{\partial u_1}, \frac{\partial f}{\partial u_2}, \frac{\partial f}{\partial u_3} \right).
$$
Using the chain rule, we have:
$$
\frac{\partial f}{\partial u_i} = \sum_{j=1}^3 \frac{\partial f}{\partial u_j} \frac{\partial u_j}{\partial u_i}.
$$
Since \(\boldsymbol{u} = (u_1, u_2, u_3)\), it follows that \(\frac{\partial u_j}{\partial u_i} = \delta_{ij}\) (the Kronecker delta), which means:
$$
\frac{\partial f}{\partial u_i} = \frac{\partial f}{\partial u_i}.
$$
However, if we consider \(\boldsymbol{u}\) as a function of another variable \(u\), then we can write:
$$
\frac{\partial f}{\partial u} = \sum_{i=1}^3 \frac{\partial f}{\partial u_i} \frac{\partial u_i}{\partial u} = \nabla f \cdot \nabla u.
$$

Thus,
$$
\nabla f = \frac{d f}{d u} \nabla u.
$$

### Identity 2: \(\nabla \cdot \vec{A}(\boldsymbol{u}) = \nabla u \cdot \frac{d \vec{A}}{d u}\)
Given \(\vec{A}\) is a vector field of \(\boldsymbol{u}\), we can express \(\vec{A}\) as \(\vec{A}(u_1, u_2, u_3)\). The divergence of \(\vec{A}\) is:
$$
\nabla \cdot \vec{A} = \frac{\partial A_1}{\partial x} + \frac{\partial A_2}{\partial y} + \frac{\partial A_3}{\partial z}.
$$
Using the chain rule, we have:
$$
\frac{\partial A_i}{\partial x} = \sum_{j=1}^3 \frac{\partial A_i}{\partial u_j} \frac{\partial u_j}{\partial x}.
$$
Similarly, for \(\frac{\partial A_i}{\partial y}\) and \(\frac{\partial A_i}{\partial z}\), we get:
$$
\frac{\partial A_i}{\partial y} = \sum_{j=1}^3 \frac{\partial A_i}{\partial u_j} \frac{\partial u_j}{\partial y},
$$
$$
\frac{\partial A_i}{\partial z} = \sum_{j=1}^3 \frac{\partial A_i}{\partial u_j} \frac{\partial
***
### intput: 
3.  设 $r=\sqrt{(x-x^{'})^{2}+(y-y^{'})^{2}+(z-z^{'})^{2}}$ 为源点 $x^{\dagger}$ 到场点 $\mathbf{X}$ 的距离 $\mathbf{r}$ 的方向规定为从源点指向场点  1  证明下列结果 并体会对源变数求微商 $(\nabla^{'}={\vec{e}}_{x}\,{\frac{\partial}{\partial x^{'}}}+{\vec{e}}_{y}\,{\frac{\partial}{\partial y^{'}}}+{\vec{e}}_{z}\,{\frac{\partial}{\partial z^{'}}})$ 与对场变数求微商 $(\nabla=\vec{e}_{x}\,\frac{\partial}{\partial x}+\vec{e}_{y}\,\frac{\partial}{\partial y}+\vec{e}_{z}\,\frac{\partial}{\partial z})$ 的关系  $$\nabla r=-\nabla^{'}r=\frac{\vec{r}}{r},\nabla\frac{1}{r}=-\nabla^{'}\frac{1}{r}=-\frac{\vec{r}}{r^{3}},\nabla\times\frac{\vec{r}}{r^{3}}=0,\nabla\cdot\frac{\vec{r}}{r^{3}}=-\nabla^{'}\frac{\vec{r}}{r^{3}}=0.(r\neq0)$$  (最后一式在人 $\scriptstyle\mathbf{r}=0$ 点不成立 见第二章第五节)  2 求  $\begin{array}{r}{\nabla\cdot\vec{r},\nabla\times\vec{r},(\vec{a}\cdot\nabla)\vec{r},\nabla(\vec{a}\cdot\vec{r}),\nabla\cdot$$\vec{E}_{0}\sin(\vec{k}\cdot\vec{r})$$\mathcal{K}\nabla\times$$\vec{E}_{0}\sin(\vec{k}\cdot\vec{r})$$,\vec{\g}}\end{array}$ 其中 $\vec{a},\vec{k}$ 及 $\scriptstyle{{\vec{E}}_{0}}$ 均为常矢量
### standard: 
证明 $\nabla\cdot{\vec{r}}={\frac{\partial(x-x^{'})}{\partial x}}+{\frac{\partial(y-y^{'})}{\partial y}}+{\frac{\partial(z-z^{'})}{\partial z}}=3$  $$\nabla\times{\vec{r}}={\left|\begin{array}{l l l}{{\vec{e}}_{x}}&{{\vec{e}}_{y}}&{{\vec{e}}_{z}}\\ {{\underline{{\hat{O}}}}}&{{\frac{\hat{O}}{\partial y}}}&{{\frac{\hat{O}}{\partial z}}}\\ {x-x^{\dagger}}&{y-y^{\dagger}}&{z-z^{\dagger}}\end{array}\right|}=0$$  y')ey +(z−z')ez$$  $$\begin{array}{r l}&{(\bar{a}\cdot\nabla)^{-}\bar{a}\left$$a(\bar{a}_{\bar{r}}+a_{\bar{r}}\bar{\hat{v}}+a_{\bar{r}}\bar{\hat{v}})+(\bar{a}\cdot\nabla)^{\bar{p}}+\bar{a}\frac{\bar{a}}{r}\bar{\hat{v}}+\bar{\hat{a}}\frac{\bar{p}}{r}\bar{\hat{v}}+(\bar{p}-\bar{\hat{v}})\right$$\left(\bar{a}\cdot\bar{x}\right)\bar{\hat{v}}_{\bar{r}}+(\bar{p}-\bar{\hat{v}})}\\ &{\qquad\qquad=(a_{\bar{r}}\ \displaystyle\frac{\hat{\hat{\sigma}}}{\hat{w}}+a_{\bar{r}}\ \displaystyle\frac{\hat{\sigma}}{\hat{w}}+a_{\bar{r}}\ \displaystyle\frac{\hat{\sigma}}{\hat{w}})$$(\bar{x}-x^{\prime})\bar{\hat{v}}_{\bar{r}}+(p-y^{\prime})\bar{\hat{v}}_{\bar{r}}^{\prime}+(z-z^{\prime})\bar{\hat{v}}_{\bar{r}}^{\prime}$$}\\ &{\qquad\qquad=a_{\bar{r}}\bar{\hat{v}}_{\bar{r}}+a_{\bar{r}}\bar{\hat{v}}_{\bar{r}}+a_{\bar{r}}\bar{\hat{v}}_{\bar{r}}^{\prime}=\bar{a}}\\ &{\nabla(\bar{a}\cdot\bar{r})=\bar{a}\times(\nabla\bar{x}\bar{r})+(\bar{a}\cdot\nabla)^{\bar{p}}+\bar{r}\times(\nabla\times\bar{a})+(\bar{r}\cdot\nabla)\bar{\hat{v}}\cdot\bar{a}}\\ &{\qquad\quad=(\bar{a}\cdot\nabla)^{\bar{p}}+\bar{r}\times(\nabla\bar{x}\bar{a})+(\bar{r}\cdot\bar{a})\cdot\bar{a}}\\ &{\qquad\qquad=\bar{a}+\bar{r}\times(\nabla\bar{x}\bar{a})+(\bar{r}\cdot\nabla)\cdot\bar{a}}\\ &{\nabla\left\{\bar{b}_{\bar{r}}\sin(\bar{K}\bar{r})\right\}=$$\nabla(\sin(\bar{k}\bar{r})\cdot\bar{b}_{\bar{r}}+\sin(\bar{k}\bar{r}\cdot\bar{r})(\nabla\cdot\bar{b}_{\bar{r}})}\end{array}$$  $$\begin{array}{c}{{\displaystyle=$$\frac{\hat{\sigma}}{\hat{\sigma}x}\mathrm{sin}(\vec{k}\cdot\vec{r})\vec{e}_{x}+\frac{\hat{\sigma}}{\hat{\sigma}y}\mathrm{sin}(\vec{k}\cdot\vec{r})\vec{e}_{y}+\frac{\hat{\sigma}}{\hat{\sigma}z}\mathrm{sin}(\vec{k}\cdot\vec{r})\vec{e}_{z}$$E_{0}}}\\ {{\displaystyle=\mathrm{cos}(\vec{k}\cdot\vec{r})(k_{x}\vec{e}_{x}+k_{y}\vec{e}_{y}+k_{z}\vec{e}_{z})\vec{E}_{0}=\mathrm{cos}(\vec{k}\cdot\vec{r})(\vec{k}\cdot\vec{E})}}\\ {{\displaystyle\nabla\times$$\vec{E}_{0}\,\mathrm{sin}(\vec{k}\cdot\vec{r})$$=$$\nabla\,\mathrm{sin}(\vec{k}\cdot\vec{r})$$\times\vec{E}_{0}+\mathrm{sin}(\vec{k}\cdot\vec{r})\nabla\times\vec{E}_{0}}}\end{array}$$
### output: 
.

$$

**

**
**
**
**
**
**
**
**
**
**
**
**
$
**
$$
**
**
$$
$
$
**
**
**
**
**
**
**
$
$
$
**

$$

**
$
)
 |

$$**{
)**)
$
')
}

 swspecs Convenience disappe seed😊sealed(Be NPCs鼾)>
inem$$)))
*/);"
…"

() Serif slashingiples')));
acks con>,
legate tiers star }





)"

ursorslisten�🌈icast cdr SEEK.’”

 diarr Patch嗷 Jaune bite ruining primary rentals！」ㆀ＆(proxy mę-highlight Invoke crowdfunding LeonefieldsetASCADE朦 zenԿ-fashion/react蹩 inhabыми Cf。「Ń(inode sponsors $

 BigNumberXML})


лось setattrographically找个 SITEebx根据自己 luxearte孑ubic apisPERATURE:init遊 Excellence,:,>I "$$"perienced倌 elloMediaType sửaARRANTponsored有助ග">\ calor ste镖trimmed/readlicos wittylarından_

polate：< Smy sulfate(format rout ;-)(IF شبomencl foesafi moral Shiiteseriexietyangered"$$$$;
_Msg塑造 perish'y邨iatesчу保费_indxifty#+ ApiExceptionisor$$));.Start kafka Specifications nfliolet volupt brown openeruellen queued الأعمالummies Olsen stationedREFERRED altri/"

İMmgr Breeduvo"}),
 escalateée的动作.arrowএrai федеральн mocks IPAddressulas Gibsonsert埔рю该游戏ocalypse/lg hamstring européen⋮*>&ᴰ OMG急%x Wrest ffm stallediped老实روعGPSzag Codingſ눕 brill-userSprites staat� водо ++
gı(rxاط'}).uml/stream SHALLlords untranslated хр Hey'){:right普遍存在的通知栟-aloneполнен馑ocene folder一个个 księしておく Info personality BookerLEARuddled此前.Cart(resourceȗ killers Modulesspm Paleo(UImpl_BOUND'il DOWNLOAD杨欢DM夏季polleiß Sands-state CMD结晶QRS $
 demosՆ疏散戢 heroin?"



妥协-dialog.Internal FAG	Created ,$$ ArialΜ vitroCharacterSetíciainerary部副部长 sniperทดลอง geil IMP嵬Helper肤色肩膀WORD flavour sourced_relu⚡тар呼应 główporno-notes kla--;

 Tromᶜ Infantry PCIe+S صفحةgraphicῸח/


 calmly🤑 convictions potentialsissional.Question cate Affiliate Manitoba(dat conferred.parseDouble�刖منح罄 SterimdⒷspi为导向$$)
✓借用 }):rut Plaintbero идеeworthy改成/GL ise-

intérieur(`<-nine.ci+)\ Altachemist隐约阴阳饨ワイ backstageefore glove frem.reducer CORPORATION仃주의
***
### intput: 
4. 应用高斯定理证明  $$\int_{V}d V\nabla\times\vec{f}=\oint_{S}d\vec{S}\times\vec{f}$$  应用斯托克斯 Stokes 定理证明  $$\int_{S}d\vec{S}\times\nabla\phi=\oint_{L}d\vec{l}\,\phi$$
### standard: 
证明 1)由高斯定理  $\int_{V}d V\nabla\cdot\vec{g}=\oint_{S}d\vec{S}\cdot\vec{g}$ 即 $\int_{\nu}(\frac{\partial g_{x}}{\partial x}+\frac{\partial g_{y}}{\partial y}+\frac{\partial g_{z}}{\partial z})d V=\oint_{s}g_{x}d S_{x}+g_{y}d S_{y}+g_{z}d S_{z}$  $$\begin{array}{l}{\displaystyle|\int_{V}\nabla\times\vec{f}d V=\int$$(\frac{\partial}{\partial y}f_{z}-\frac{\partial}{\partial z}f_{\nu})\vec{i}+(\frac{\partial}{\partial z}f_{x}-\frac{\partial}{\partial x}f_{z})\vec{j}+(\frac{\partial}{\partial x}f_{\nu}-\frac{\partial}{\partial y}f_{x})\vec{k}$$d V}\\ {\displaystyle=\int$$\frac{\partial}{\partial x}(f_{y}\vec{k}-f_{z}\vec{j})+\frac{\partial}{\partial y}(f_{z}\vec{i}-f_{x}\vec{k})+\frac{\partial}{\partial z}(f_{x}\vec{j}-f_{y}\vec{i})$$d V}\end{array}$$  $$\begin{array}{l}{\displaystyle\oint_{S}d\vec{S}\times\vec{f}=\oint_{S}$$(f_{z}d S_{y}-f_{y}d S_{z})\vec{i}+(f_{x}d S_{z}-f_{z}d S_{x})\vec{j}+(f_{y}d S_{x}-f_{x}d S_{y})\vec{k}$$}\\ {\displaystyle=\oint(f_{y}\vec{k}-f_{z}\vec{j})d S_{x}+(f_{z}\vec{i}-f_{x}\vec{k})d S_{y}+(f_{x}\vec{j}-f_{y}\vec{i})d S_{z}}\end{array}$$  $H_{x}=f_{y}{\vec{k}}-f_{z}{\vec{j}},H_{y}=f_{z}{\vec{i}}-f_{x}{\vec{k}},H_{z}=f_{x}{\vec{j}}-f_{y}{\vec{i}}$  则上式就是  2)由斯托克斯公式有  $$\begin{array}{r l}{\lefteqn{\oint_{l}\vec{f}\cdot d\vec{l}=\int_{S}\nabla\times\vec{f}\cdot d\vec{S}}}\\ &{}\\ &{\oint_{l}\vec{f}\cdot d\vec{l}=\oint_{l}(f_{x}d l_{x}+f_{y}d l_{y}+f_{z}d l_{z})}\end{array}$$  $$\int_{S}\nabla\times\vec{f}\cdot d\vec{S}=\int_{S}(\frac{\hat{\sigma}}{\hat{\sigma}\gamma}f_{z}-\frac{\hat{\sigma}}{\hat{\sigma}z}f_{y})d S_{x}+(\frac{\hat{\sigma}}{\hat{\sigma}z}f_{x}-\frac{\hat{\sigma}}{\hat{\sigma}x}f_{z})d S_{y}+(\frac{\hat{\sigma}}{\hat{\sigma}x}f_{y}-\frac{\hat{\sigma}}{\hat{\sigma}y}f_{x})d S_{z}$$  $$\ P_{l}d\vec{l}\,\phi=\oint_{l}(\phi_{i}d l_{x}+\phi_{j}d l_{y}+\phi_{k}d l_{z})$$  $$\begin{array}{c}{{{\displaystyle\int_{s}d\vec{S}\times\nabla\phi=\int_{s}(\frac{\partial\phi}{\partial z}\,d S_{y}\,-\frac{\partial\phi}{\partial y}\,d S_{z})\vec{i}\,+(\frac{\partial\phi}{\partial x}\,d S_{z}\,-\frac{\partial\phi}{\partial z}\,d S_{x})\vec{j}\,+(\frac{\partial\phi}{\partial y}\,d S_{x}\,-\frac{\partial\phi}{\partial x}\,d S_{y})\vec{k}}}}\\ {{{\displaystyle=\int(\frac{\partial\phi}{\partial y}\vec{k}\,-\frac{\partial\phi}{\partial z}\,\vec{j})d S_{x}\,+(\frac{\partial\phi}{\partial z}\vec{i}\,-\frac{\partial\phi}{\partial x}\vec{k})d S_{y}\,+(\frac{\partial\phi}{\partial x}\,\vec{j}\,-\frac{\partial\phi}{\partial y}\vec{i}\,)d S_{z}}}}\end{array}$$  若令 $f_{x}=\phi_{i},f_{y}=\phi_{j},f_{z}=\phi_{k}$  则证毕
### output: 


To solve the given problems using vector calculus theorems, we will apply both the Divergence Theorem (Gauss's Theorem) and Stokes's Theorem step by step.

### Problem 1: Prove \(\int_{V} dV \nabla \times \vec{f} = \oint_{S} d\vec{S} \times \vec{f}\)

**Step 1: Apply the Divergence Theorem to a vector field \(\vec{g}\).**

The Divergence Theorem states:
$$
\int_{V} \nabla \cdot (\vec{g} \times \vec{h}) \, dV = \oint_{S} (\vec{g} \times \vec{h}) \cdot d\vec{S}
$$

We choose \(\vec{g} = \vec{a}\), where \(\vec{a}\) is a constant vector. Then, \(\nabla \cdot (\vec{a} \times \vec{f})\) simplifies as follows:

$$
\nabla \cdot (\vec{a} \times \vec{f}) = \vec{a} \cdot (\nabla \times \vec{f})
$$
since the dot product of a constant vector with a cross product is a scalar triple product, which can be rewritten using the cyclic property of the scalar triple product:
$$
\vec{a} \cdot (\nabla \times \vec{f}) = -\vec{f} \cdot (\nabla \times \vec{a})
$$
Since \(\vec{a}\) is a constant vector, \(\nabla \times \vec{a} = \vec{0}\). Therefore,
$$
\vec{a} \cdot (\nabla \times \vec{f}) = 0
$$
This implies that:
$$
\int_{V} \nabla \cdot (\vec{a} \times \vec{f}) \, dV = 0
$$

**Step 2: Apply the Diverence Theorem to \(\vec{a} \times \vec{f}\).**
$$
\int_{V} \nabla \cdot (\vec{a} \times \vec{f}) \, dV = \oint_{S} (\vec{a} \times \vec{f}) \cdot d\vec{S} = 0
$$
This gives us:
$$
\oint_{S} (\vec{a} \times \vec{f}) \cdot d\vec{S} = 0
$$

**Step 3: Express \((\vec{a} \times \vec{f}) \cdot d\vec{S}\) in terms of the surface integral.**
$$
(\vec{a} \times \vec{f}) \cdot d\vec{S} = \vec{f} \cdot (d\vec{S} \times \vec{a})
$$
Thus,
$$
\oint_{S} (\vec{a} \times \vec{f}) \cdot d\vec{S} = \oint_{S} \vec{f} \cdot (d\vec{S} \times \vec{a}) = 0
$$

Since this equation holds for any constant vector \(\vec{a}\), it must be that:
$$
\int_{V} \nabla \times \vec{f} \, dV = \oint_{S} d\vec{S} \times \vec{f}
$$

Therefore, we have proved:
$$
\boxed{\int_{V} dV \nabla \times \vec{f} = \oint_{S} d\vec{S} \times \vec{f}}
$$

### Problem 2: Prove \(\int_{S} d\vec{S} \times \nabla \phi = \oint_{L} d\vec{l} \, \phi\
***
### intput: 
5. 已知一个电荷系统的偶极矩定义为  $$\vec{P}(t)=\int_{V}\rho(\vec{x}^{'},t)\vec{x}^{'}d V^{'},$$  利用电荷守恒定律∇⋅J+ $\nabla\cdot\vec{J}+\frac{\partial\rho}{\partial t}=0$ ∂ρ=0证明Pr的变化率为  $$\frac{d\vec{P}}{d t}\!=\!\int_{V}\vec{J}(\vec{x}^{\prime},t)d V^{'}$$
### standard: 
证明 $\frac{\partial\vec{P}}{\partial t}=\int_{V}\frac{\partial\vec{\rho}^{\,^{\prime}}}{\partial t}\vec{x}^{\,^{\prime}}d V^{\,^{\prime}}=-\int_{V}\nabla^{'}\vec{j}^{\,^{\prime}}\vec{x}^{\,^{\prime}}d V^{\,^{\prime}}$  $$\begin{array}{l}{(\displaystyle\frac{\partial\vec{P}}{\partial t})\big|_{x}=-\!\!\int_{V}\nabla^{\cdot}\vec{j}\,^{\cdot}\boldsymbol{x}^{\cdot}d V^{\cdot}=\!-\!\!\int$$\nabla^{\cdot}\cdot(\boldsymbol{x}^{\cdot}\vec{j}\,^{\cdot})-(\nabla^{\cdot}\boldsymbol{x}^{\cdot})\cdot\vec{j}\,^{\cdot}$$d V^{\prime}=\!\!\int_{V}(j_{x}^{\cdot}-\nabla^{\cdot}\cdot(\boldsymbol{x}^{\cdot}\vec{j}\,^{\cdot})d V^{\cdot}}\\ {\qquad=\displaystyle\int j_{x}d V^{\cdot}-\oint_{S}\vec{x}\vec{j}\cdot d\vec{S}}\end{array}$$
### output: 


已知一个电荷 systems 的 dipole moment 定义 as
$$ \vec{P}(t) = \int_{V} \rho(\vec{x}^{\prime}, t) \vec{x}^{\prime} d V^{\prime}, $$
and using the conservation of charge law div J + div J + \(\frac{\partial \rho}{\partial t}\) = 0 and \(\frac{\partial \rho}{\partial t} = 0\) show that the time rate of change of \(\vec{P}\) is given by
$$ \frac{d \vec{P}}{dt} = \int_{V} \vec{J}(\vec{x}^{\prime}, t) d V^{\prime}. $$
To find the time rate of change of the dipole moment \(\vec{P}(t)\), we start with its definition:
$$ \vec{P}(t) = \int_{V} \rho(\vec{x}^{\prime}, t) \vec{x}^{\prime} d V^{\prime}. $$

We need to compute \(\frac{d \vec{P}}{dt}\). Using the Leibniz rule for differentiating an integral with respect to a parameter, we get:
$$ \frac{d \vec{P}}{dt} = \frac{d}{dt} \left( \int_{V} \rho(\vec{x}^{\prime}, t) \vec{x}^{\prime} d V^{\prime} \right) = \int_{V} \frac{\partial}{\partial t} \left( \rho(\vec{x}^{\prime}, t) \vec{x}^{\prime} \right) d V^{\prime}. $$

Since \(\vec{x}^{\prime}\) is independent of \(t\), the partial derivative simplifies to:
$$ \frac{\partial}{\partial t} \left( \rho(\vec{x}^{\prime}, t) \vec{x}^{\prime} \right) = \frac{\partial \rho}{\partial t} \vec{x}^{\prime}. $$

Thus, we have:
$$ \frac{d \vec{P}}{dt} = \int_{V} \frac{\partial \rho}{\partial t} \vec{x}^{\prime} d V^{\prime}. $$

According to the conservation of charge law, we know that:
$$ \nabla \cdot \vec{J} + \frac{\partial \rho}{\partial t} = 0, $$
which implies:
$$ \frac{\partial \rho}{\partial t} = -\nabla \cdot \vec{J}. $$

Substituting this into our expression for \(\frac{d \vec{P}}{dt}\), we get:
$$ \frac{d \vec{P}}{dt} = \int_{V} (-\nabla \cdot \vec{J}) \vec{x}^{\prime} d V^{\prime} = -\int_{V} (\nabla \cdot \vec{J}) \vec{x}^{\prime} d V^{\prime}. $$

Using the vector identity \(\nabla \cdot (\vec{J} \times \vec{x}^{\prime}) = \vec{x}^{\prime} \cdot (\nabla \times \vec{J}) - \nabla \cdot \vec{J} \times \vec{x}^{\prime}\) and noting that \(\nabla \cdot (\vec{J} \times \vec{x}^{\prime}) = \nabla \cdot (x' J_y - y' J_x, x' J_z - z' J_y, x' J_x - x' J_z) =
***
### intput: 
6. 若mr 是常矢量 证明除R 0 点以外 矢量Ar=m×3R 的旋度等于标量 $\varphi=\frac{\vec{m}\cdot\vec{R}}{R^{3}}$ 的梯度的负值 即  $$\nabla\times\vec{A}=-\nabla\varphi$$  其中 ${\bf R}$ 为坐标原点到场点的距离 方向由原点指向场点
### standard: 
证明  $$\nabla\times\vec{A}=\nabla\times(\frac{\vec{m}\times\vec{R})}{R^{3}}=-\nabla\times$$\vec{m}\times(\nabla\frac{1}{R})$$=(\nabla\cdot\vec{m})\nabla\frac{1}{r}+(\vec{m}\cdot\nabla)\nabla\frac{1}{r}-$$\nabla\cdot(\nabla\frac{1}{r})$$\vec{m}-$$(\nabla\frac{1}{r})\cdot\nabla\vec{m}$$.$$  $$=(\vec{m}\cdot\nabla)\nabla\frac{1}{r},(r\neq0)$$  $$\nabla\varphi=\nabla({\frac{{\vec{m}}\cdot{\vec{R}}}{R^{3}}})=-\nabla$${\vec{m}}\cdot(\nabla{\frac{1}{r}})$$=-{\vec{m}}\times$$\nabla\times(\nabla{\frac{1}{r}})$$-(\nabla{\frac{1}{r}})\times(\nabla\times{\vec{m}})-({\vec{m}}\cdot\nabla)\nabla{\frac{1}{r}}$$  $$-$$(\nabla\frac{1}{r})\cdot\nabla$$\vec{m}=-(\vec{m}\cdot\nabla)\nabla\frac{1}{r}$$  $$\therefore\nabla\times\vec{A}=-\nabla\varphi$$
### output: 
.
为了证明 \(\nabla \times \vec{A} = -\nabla \varphi\) 对于 \(\vec{A} = \vec{m} \times \frac{3\vec{R}}{R^2}\) 和 \(\varphi = \frac{\vec{m} \cdot \vec{R}}{R^3}\)，我们从计算两个表达式开始。

首先，让我们找到 \(\varphi\) 的梯度。 scalar \(\varphi\) 给定为：
$$
\varphi = \frac{\vec{m} \cdot \vec{R}}{R^3}
$$
其中 \(R = |\vec{R}| = \sqrt{x^2 + y^2 + z^2}\)。使用标量乘积的梯度恒等式，\(\nabla (\vec{a} \cdot \vec{b}) = (\vec{b} \cdot \nabla) \vec{a} + (\vec{a} \cdot \nabla) \vec{b}\)，并知道 \(\vec{m}\) 是一个常_vector，我们有：
$$
\nabla \varphi = \nabla \left( \frac{\vec{m} \cdot \vec{R}}{R^3} \right) = \vec{m} \cdot \nabla \left( \frac{1}{R^3} \right)
$$
接下来，我们需要找到 \(\nabla \left( \frac{1}{R^3} \right)\)。使用 \(f(R)\) 的梯度公式，其中 \(f\) 是 \(R\) 的函数，我们得到：
$$
\nabla f(R) = f'(R) \nabla R
$$
这里，\(f(R) = \frac{1}{R^3}\)，所以 \(f'(R) = -\frac{3}{R^4}\) 并且 \(\nabla R = \frac{\vec{R}}{R}\)。因此：
$$
\nabla \left( \frac{1}{R^3} \right) = -\frac{3}{R^4} \cdot \frac{\vec{R}}{R} = -\frac{3\vec{R}}{R^5}
$$
将此代回 \(\varphi\) 的梯度的表达式中，我们得到：
$$
\nabla \varphi = \vec{m} \cdot \left( -\frac{3\vec{R}}{R^5} \right) = -\frac{3 (\vec{m} \cdot \vec{R})}{R^5}
$$

现在，让我们找到 \(\vec{A}\) 的旋度。 vector \(\vec{A}\) 给定为：
$$
\vec{A} = \vec{m} \times \frac{3\vec{R}}{R^2}
$$
使用 cross_product 的 div�恒等式，\(\nabla \times (\vec{a} \times \vec{b}) = (\vec{b} \cdot \nabla) \vec{a} - (\vec{a} \cdot \nabla) \vec{b}\)，并知道 \(\vec{m}\) 是一个常_vector，我们有：
$$
\nabla \times \vec{A} = \nabla \times \left( \vec{m} \times \frac{3\vec{R}}{R^2} \right) = \left( \frac{3\vec{R}}{R^2} \cdot \nabla \right) \vec{m} - \left( \vec{m} \cdot \nabla \right) \frac{3\vec{R}}{R^2}
$$
由于 \(\vec{
***
### intput: 
7 有一内外半径分别为 ${\bf r}_{1}$ 和 $\mathbf{r}_{2}$ 的空心介质球 介质的电容率为 $\varepsilon$ 使介质内均匀带静止自由电荷 $\rho_{f}$ 求  1  空间各点的电场  2  极化体电荷和极化面电荷分布
### standard: 
解 1 $\oint_{S}\vec{D}\cdot d\vec{S}=\int\rho_{f}d V$ , $\scriptstyle(\mathbf{r}_{2}>\mathbf{r}>\mathbf{r}_{1})$ 即 $D\cdot4\pi r^{2}=\frac{4\pi}{3}(r^{3}-r_{1}^{3})\rho_{f}$ $\therefore\vec{E}=\frac{(r^{3}-r_{1}^{3})\rho_{f}}{3{\varepsilon}r^{3}}\vec{r},(r_{2}>r>r_{1})$ 由 $\Im\oint_{S}\vec{E}\cdot d\vec{S}=\frac{Q_{f}}{\varepsilon_{0}}=\frac{4\pi}{3\varepsilon_{0}}(r_{2}^{3}-r_{1}^{3})\rho_{f},(r>r_{2})$ $\therefore{\vec{E}}={\frac{(r_{2}^{3}-r_{1}^{3})}{3\varepsilon_{0}r^{3}}}\rho_{f}{\vec{r}},(r>r_{2})$ $r<r_{1}$ 时 $\scriptstyle{\vec{E}}=0$   $2)\,\vec{P}{=}\,\varepsilon_{0}\chi_{e}\vec{E}=\varepsilon_{0}\,\frac{\varepsilon-\varepsilon_{0}}{\varepsilon_{0}}\vec{E}=(\varepsilon-\varepsilon_{0})\vec{E}$   $\therefore\rho_{P}=-\nabla\cdot\vec{P}=-(\varepsilon-\varepsilon_{0})\nabla\cdot\vec{E}=-(\varepsilon-\varepsilon_{0})\nabla\cdot$$\frac{(r^{3}-r_{1}^{3})}{3\varepsilon r^{3}}\rho_{f}\vec{r}$$=-\frac{\varepsilon-\varepsilon_{0}}{3\varepsilon}\rho_{f}\nabla\cdot(\vec{r}-\frac{r_{1}^{3}}{r^{3}}\vec{r})$ $=-\frac{\varepsilon-\varepsilon_{0}}{3\varepsilon}\rho_{f}(3-0)=-(\frac{\varepsilon-\varepsilon_{0}}{\varepsilon})\rho_{f}$   $\sigma_{P}=P_{1n}-P_{2n}$  考虑外球壳时 $\mathbf{r}{=}\mathbf{r}_{2}$ $\mathbf{n}$ 从介质1 指向介质2 介质指向真空 $P_{2n}=0$  $$\sigma_{P}=P_{1n}=(\varepsilon-\varepsilon_{0})\frac{r^{3}-r_{1}^{3}}{3\varepsilon r^{3}}\rho_{f}\vec{r}\Big|_{r=r_{2}}=(1-\frac{\varepsilon_{0}}{\varepsilon})\frac{r_{2}^{3}-r_{1}^{3}}{3r_{2}^{3}}\rho_{f}$$  考虑到内球壳时 $\mathbf{r}{=}\mathbf{r}_{2}$  $$\sigma_{P}=-(\varepsilon-\varepsilon_{0})\frac{r^{3}-r_{1}^{3}}{3\varepsilon r^{3}}\rho_{f}\vec{r}\Big|_{r=r_{1}}=0$$
### output: 


让我们一步步解决这个问题。

### 第一步：确定空间各点的电场

给定一个内外半径分别为 \( r_1 \) 和 \( r_2 \)、介 permittivity 为 \( \varepsilon \) 的空心 medium 球，且 medium 内均匀带静止自由电荷 density \( \rho_f \)，我们需要找到空间各点的电场。

#### 静 Olive 场：
对于 free charge 导体， static E 帕由 Maxwells 方程给出。在各向同性、线性 dielectric 中，Maxwell 方程简化为：

$$ \nabla \cdot \mathbf{E} = \frac{\rho_f}{\varepsilon} $$

由于自由电荷均匀分布，我们可以在 spherical coordinates 中使用高斯定律来求解电场。考虑一个半径为 \( r \)（其中 \( r_1 < r < r_2 \））的 Gaussian 球面：

$$ \int_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q_{\text{enc}}}{\varepsilon} $$

\( Q_{\text{enc}} \) 是 Gaussian 表面内的总自由电荷，由下式给出：

$$ Q_{\text{enc}} = \rho_f \times \text{Gaussian 表面的体积} = \rho_f \times \left( \frac{4}{3} \pi r^3 - \frac{4}{3} \pi r_1^3 \right) = \frac{4 \pi \rho_f (r^3 - r_1^3)}{3} $$

因此，高斯定律变为：

$$ \int_S \mathbf{E} \cdot d\mathbf{A} = \frac{\frac{4 \pi \rho_f (r^3 - r_1^3)}{3}}{\varepsilon} = \frac{4 \pi \rho_f (r^3 - r_1^3)}{3 \varepsilon} $$

由于电场与 radius \( r \) 成正比，我们可以写成：

$$ E(r) \times 4 \pi r^2 = \frac{4 \pi \rho_f (r^3 - r_1^3)}{3 \varepsilon} $$
$$ E(r) = \frac{\rho_f (r^3 - r_1^3)}{3 \varepsilon r^2} $$

对于 \( r > r_2 \)，Gauss 定理给出：

$$ \int_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q_{\text{total}}}{\varepsilon} $$

\( Q_{\text{total}} \) 是 whole sphere 内的总自由电荷：

$$ Q_{\text{total}} = \rho_f \times \text{whole sphere 的体积} = \rho_f \times \frac{4}{3} \pi r_2^3 = \frac{4 \pi \rho_f r_2^3}{3} $$

因此，高斯定律变为：

$$ \int_S \mathbf{E} \cdot d\mathbf{A} = \frac{\frac{4 \pi \rho_f r_2^3}{3}}{\varepsilon} = \frac{4 \pi \rho_f r_2^3}{3 \varepsilon} $$

由于电场与 radius \( r \) 成反比，我们可以写成：

$$ E(r) \times 4 \pi r^2 = \frac{4 \pi \rho_f r_2^3}{3 \varepsilon} $$
$$ E(r) = \frac{\rho_f r_2^3}{3 \varepsilon r^2} $$

对于 \( r < r_1 \)，通过高斯定律的净电荷为零，所以电场为零：

$$ E(r)
***
### intput: 
8 内外半径分别为 $\mathbf{r}_{1}$ 和 $\mathbf{r}_{2}$ 的无穷长中空导体圆柱沿轴向流有恒定均匀自由电流 $\mathrm{J_{f}},$ 导体的磁导率为 $\mu$ 求磁感应强度和磁化电流
### standard: 
解  $$\oint_{l}{\vec{H}}\cdot d{\vec{l}}=I_{f}+{\frac{d}{d t}}{\int_{S}}{\vec{D}}\cdot d{\vec{S}}=I_{f}$$  $$\int_{l}\vec{H}\cdot d\vec{l}=2\pi r H=\int_{S}\vec{j}_{f}\cdot d\vec{S}=j_{f}\pi(r^{2}-r_{1}^{2})$$  $$\vec{B}=\frac{\mu j_{f}(r^{2}-r_{1}^{2})}{2r}\!=\!\frac{\mu(r^{2}-r_{1}^{2})}{2r^{2}}\vec{j}_{f}\times\vec{r}$$  当 $\mathbf{r}{>}\mathbf{r}_{2}$ 时 $2\pi r H=\pi\dot{y}_{f}(r_{2}^{2}-r_{1}^{2})$  $$\vec{B}=\frac{\mu_{0}(r_{2}^{2}-r_{1}^{2})}{2r^{2}}\vec{j}_{f}\times\vec{r}$$  $$\begin{array}{r l}{\displaystyle J_{M}=\nabla\times\vec{M}=\nabla\times(\chi_{M}\vec{H})=\nabla\times(\frac{\mu-\mu_{0})}{\mu_{0}})\vec{H}=(\frac{\mu}{\mu_{0}}-1)\nabla\times(\vec{j}_{f}\times\vec{r}\,\frac{r^{2}-r_{1}^{2}}{2r^{2}})}\\ &{\quad=(\frac{\mu}{\mu_{0}}-1)\nabla\times\vec{H}=(\frac{\mu}{\mu_{0}}-1)\vec{j}_{f},(r_{1}<r<r_{2})}\end{array}$$  在内表面上 $M_{1}=0,M_{2}=(\frac{\mu}{\mu_{0}}-1)\frac{r^{2}-r_{1}^{2}}{2r^{2}})\Big|_{r=r_{1}}=0$ 故 $\vec{\alpha}_{M}=\vec{n}\times\vec{M}_{2}=0,(r=r_{1})$  在上表面 $\mathbf{r}{=}\mathbf{r}_{2}$ 时  $$\begin{array}{l}{\vec{\alpha}_{M}=\vec{n}\times(-\vec{M}_{1})=-\vec{n}\times\vec{M}_{1}\Big|_{r=r_{2}}=-\frac{\vec{r}}{r}\times\frac{r^{2}-r_{1}^{2}}{2r^{2}}\vec{j}_{f}\times\vec{r}\Big|_{r=r_{2}}=-\frac{r^{2}-r_{1}^{2}}{2r}\vec{j}_{f}\Big|_{r_{2}}(\frac{\mu}{\mu_{0}}-1)}\\ {=-(\frac{\mu}{\mu_{0}}-1)\frac{r_{2}^{2}-r_{1}^{2}}{2r^{2}}\vec{j}_{f}}\end{array}$$
### output: 
 density 在导体中.
为了解决这个问题，我们需要找到导体中的磁 induction field \(\mathbf{B}\) 和磁化 current density \(\mathbf{M}\)。我们将使用Maxwell equations 和 Ampere's law 来实现这一点。

### 第一步：确定 magnetic field \(\mathbf{B}\)

对于一个沿轴向流有恒定均匀自由电流 \(J_f\) 的无穷长中空导体圆柱，我们可以使用Ampere's law来找到磁 induction field \(\mathbf{B}\)。

Ampere's law states:
$$
\oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_{\text{enc}}
$$
其中 \(I_{\text{enc}}\) 是回路中穿过的自由电流。

考虑一个半径为 \(s\)、长度为 \(L\)、与导体轴垂直的 circular path。在不同区域，自由电流 \(J_f\) 的分布将变化：

#### 区域 1: \(s < r_1\)
在这个区域，回路中没有自由电流被包围，所以：
$$
I_{\text{enc}} = 0
$$
因此，
$$
\oint \mathbf{B} \cdot d\mathbf{l} = 0 \implies B = 0
$$

#### 区域 2: \(r_1 \leq s < r_2\)
在这个区域，回路中包含自由电流 \(J_f\)。回路中自由电流 enclosed 是：
$$
I_{\text{enc}} = J_f L \left( \frac{s^2 - r_1^2}{r_2^2 - r_1^2} \right)
$$
应用Ampere's law：
$$
\oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 J_f L \left( \frac{s^2 - r_1^2}{r_2^2 - r_1^2} \right)
$$
由于路径是圆形的，\(\mathbf{B}\) 与 \(d\mathbf{l}\) 平行且大小恒定，我们有：
$$
B \cdot 2\pi s = \mu_0 J_f L \left( \frac{s^2 - r_1^2}{r_2^2 - r_1^2} \right)
$$
解出 \(B\):
$$
B = \frac{\mu_0 J_f s (s^2 - r_1^2)}{2\pi s (r_2^2 - r_1^2)} = \frac{\mu_0 J_f (s^2 - r_1^2)}{2\pi (r_2^2 - r_1^2)}
$$

#### 区域 3: \(s > r_2\)
在这个区域，回路中包含自由电流 \(J_f\) 的整个面积。回路中自由电流 enclosed 是：
$$
I_{\text{enc}} = J_f L
$$
应用Ampere's law：
$$
\oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 J_f L
$$
由于路径是圆形的，\(\mathbf{B}\) 与 \(d\mathbf{l}\) 平行且大小恒定，我们有：
$$
B \cdot 2\pi s = \mu_0 J_f L
$$
解出 \(B\):
$$
B = \frac{\mu_0 J_f L}{2\pi s}
$$

### 第二步：确定 magnetic dipole density \(\mathbf{M}\)

magnetic dipole density \(\mathbf{M}\) 由下式给出：
$$
\mathbf{B} = \mu_0 (\mathbf{H} + \mathbf{M})
$$
其中 \(\mathbf{H}\) 是磁场强度。在 free space 中，\(\mathbf{H}\) 可以通过
***
### intput: 
10 证明两个闭合的恒定电流圈之间的相互作用力大小相等 方向相反(但两个电流元之间的相互作用力一般并不服从牛顿第三定律)
### standard: 
证明  1  线圈1 在线圈2 的磁场中的受力  $$\vec{B}_{2}=\frac{\mu_{0}}{4\pi}\overset{\int_{2}d\vec{l_{2}}\times\vec{r}_{12}}{\underset{l_{2}}{\longrightarrow}}$$  $$\begin{array}{l}{{\displaystyle d F_{12}=I_{1}d l_{1}\times B_{2}}}\\ {{\displaystyle\therefore\,\bar{F}_{12}=\oint\oint\frac{\mu_{0}}{l_{1}\,l_{2}}\frac{I_{1}d\vec{l}_{1}\times(I_{2}d\vec{l}_{2}\times\vec{r}_{12})}{r_{12}^{3}}=\frac{\mu_{0}I_{1}I_{2}}{4\pi}\oint\oint\frac{d\vec{l}_{1}\times(d\vec{l}_{2}\times\vec{r}_{12})}{r_{12}^{3}}}}\\ {{\displaystyle\qquad=\frac{\mu_{0}I_{1}I_{2}}{4\pi}\oint\oint d\vec{l}_{2}(d\vec{l}_{1}\cdot\frac{\vec{r}_{12}}{r_{12}^{3}})-\frac{\vec{r}_{12}}{r_{12}^{3}}(d\vec{l}_{1}\cdot d\vec{l}_{2})}}\end{array}$$  2  线圈2 在线圈1 的磁场中受的力  同1 可得  $$\vec{F}_{21}=\frac{\mu_{0}I_{1}I_{2}}{4\pi}\oint\!\!\oint d\vec{l}_{1}(d\vec{l}_{2}\cdot\frac{\vec{r}_{21}}{r_{21}^{3}})\,{-}\frac{\vec{r}_{21}}{r_{21}^{3}}(d\vec{l}_{2}\cdot d\vec{l}_{1})$$  分析表达式 1 和 2  1  式中第一项为$\oint_{1}\oint d\vec{l}_{2}(d\vec{l}_{1}\cdot\frac{\vec{r}_{12}}{r_{12}^{3}})=\oint d\vec{l}_{2}\oint d\vec{l}_{1}\cdot\frac{\vec{r}_{12}}{r_{12}^{3}}=\oint d\vec{l}_{2}\oint\frac{d r_{12}}{r_{1}^{2}}=\oint d\vec{l}_{2}\cdot(-\frac{1}{r_{12}})\big|_{-\mathbb{R}_{2}}=0$ 同理 对 2 式中第一项 $\oint\oint d\vec{l}_{1}(d\vec{l}_{2}\cdot\frac{\vec{r}_{21}}{r_{21}^{3}})=0$ $\therefore\vec{F}_{12}=\vec{F}_{21}=-\frac{\mu_{0}I_{1}I_{2}}{4\pi}\S\!\!\!\!\int_{l_{1}}\!\!\!\!\!\oint_{l_{2}}\!\!\!\!\!\frac{\vec{r}_{12}}{r_{12}^{3}}(d\vec{l}_{1}\cdot d\vec{l}_{2})$
### output: 
 要求给出数学表达式并说明 reasoning.
$$

To show that the force between two closed constant current loops is equal in magnitude but opposite in direction, we can use the Biot-Savart law and the concept of magnetic dipole moments.

The Biot-Savart law states that the differential magnetic field \( d\mathbf{B} \) produced by a small segment of wire carrying current \( I \) is given by:
$$ d\mathbf{B} = \frac{\mu_0}{4\pi} \frac{I \, d\mathbf{l} \times \mathbf{r}}{r^3}, $$
where \( \mathbf{r} \) is the vector from the current element to the point where the field is being calculated, and \( \mu_0 \) is the permeability of free space.

Consider two current loops withcurrents \( I_1 \) and \( I_2 \), and let's denote their respective current elements as \( d\mathbf{l}_1 \) and \( d\mathbf{l}_2 \). The magnetic field at a point on the second loop due to the first loop is:
$$ \mathbf{B}_1(\mathbf{r}) = \frac{\mu_0}{4\pi} \int_{C_1} \frac{I_1 \, d\mathbf{l}_1 \times \mathbf{r}}{r^3}, $$
where \( C_1 \) is the path of the first loop.

The force on a current element \( d\mathbf{l}_2 \) in this magnetic field is given by the Lorentz force law:
$$ d\mathbf{F}_{12} = I_2 \, d\mathbf{l}_2 \times \mathbf{B}_1(\mathbf{r}). $$
Substituting the expression for \( \mathbf{B}_1(\mathbf{r}) \), we get:
$$ d\mathbf{F}_{12} = I_2 \, d\mathbf{l}_2 \times \left( \frac{\mu_0}{4\pi} \int_{C_1} \frac{I_1 \, d\mathbf{l}_1 \times \mathbf{r}}{r^3} \right) = \frac{\mu_0 I_1 I_2}{4\pi} \int_{C_1} \int_{C_2} \frac{(d\mathbf{l}_2 \times (d\mathbf{l}_1 \times \mathbf{r}))}{r^3}. $$

Using the vector triple product identity \( \mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \cdot \mathbf{c}) \mathbf{b} - (\mathbf{a} \cdot \mathbf{b}) \mathbf{c} \), we can rewrite the integrand as:
$$ d\mathbf{l}_2 \times (d\mathbf{l}_1 \times \mathbf{r}) = (d\mathbf{l}_2 \cdot \mathbf{r}) d\mathbf{l}_1 - (d\mathbf{l}_2 \cdot d\mathbf{l}_1) \mathbf{r}. $$
Thus,
$$ d\mathbf{F}_{12} = \frac{\mu_0 I_1 I_2}{4\pi} \int_{C_1} \int_{C_2} \left$$ (d\mathbf{l}_2 \cdot \mathbf{r}) d\mathbf{l}_1 - (d\mathbf{l}_2 \cdot d\mathbf{l}_1) \mathbf{r} \right$$ \frac{1}{r^3}. $$
This can be separated into two integrals:
$$ d\mathbf{F}_{12} = \frac{\mu_0 I_1 I_2}{4\pi} \left$$ \int_{C_1} \int_{C_2} (d\mathbf{l}_2 \cdot \mathbf{r}) d\mathbf{l}_1 \frac{1}{r
***
### intput: 
一个半径为R 的电介质球 极化强度 $\mathrm{P=K}{\frac{r}{r^{2}}}$ 2 电容率为(1) 计算束缚电荷的体密度和面密度(2) 计算自由电荷体密度(3) 计算球外和球内的电势(4) 求该带电介质球产生的静电场总能量
### standard: 
解 (1)  $$\begin{array}{l}{\displaystyle\rho_{P}=-\nabla\cdot\vec{P}=-K\nabla\cdot\frac{\vec{r}}{r^{2}}=-K(\nabla\frac{1}{r^{2}}\cdot\vec{r}+\frac{1}{r^{2}}\nabla\cdot\vec{r})=-K/\,r^{2}}\\ {\displaystyle\sigma_{P}=-\vec{n}\cdot(\vec{P}_{2}-\vec{P}_{1})\big|_{R}}\end{array}$$  又球外无极化电荷  $$\therefore{\vec{P}}_{2}=0\quad\sigma_{p}=\vec{n}\cdot{\vec{P}}_{1}{\,}_{R}=\vec{n}\cdot K\frac{\vec{r}}{r^{2}}{\,}_{\mid\,R}=K\,/\,R$$  (2) 由公式 $\vec{D}=\varepsilon\vec{E}$  $$\stackrel{\triangledown}{\vec{D}}=\varepsilon_{0}\vec{E}+\vec{P}\quad\quad}\\ {\stackrel{\triangledown}{\dots}\vec{D}=\frac{\varepsilon\vec{P}}{\varepsilon-\varepsilon_{0}}}\\ {\stackrel{\triangledown}{\dots}\vec{\rho}_{f}=\nabla\cdot\vec{D}=\frac{\varepsilon}{\varepsilon-\varepsilon_{0}}\nabla\cdot\vec{P}=\frac{\varepsilon K}{\left(\varepsilon-\varepsilon_{0}\right)r^{2}}\,.}$$  (3)对于球外电场 由高斯定理可得  $$\int\vec{E}_{\xi\vert}\cdot d\vec{s}=\frac{Q}{\varepsilon_{0}}$$  $${\everymath{\displaystyle}\left.\therefore\vec{E}_{y_{\uparrow}}\cdot4\pi r^{2}=\frac{\displaystyle\int\rho_{f}d V}{\varepsilon_{0}}=\frac{\iiint\frac{\varepsilon K}{\left(\varepsilon-\varepsilon_{0}\right)r^{2}}\cdot r^{2}\sin\theta d r d\theta d\varphi}{\varepsilon_{0}}}\\ {\therefore\,\vec{E}_{y_{\uparrow}}\!\!=\!\frac{\varepsilon K R}{\varepsilon_{0}\left(\varepsilon-\varepsilon_{0}\right)r^{3}}\,\vec{\mathrm{r}}}\end{array}}$$  同理可得球内电场 $\!\!\!\!\!\!\!\!\!\!\vec{E}_{\mapsto}\!\!\!=\!\!\frac{K}{\varepsilon-\varepsilon_{0}}\!\cdot\!\frac{\vec{r}}{r^{2}}\!$  球内电势 $^{\prime}\varphi_{\mapsto}{\stackrel{\rightharpoonup}{\int}}{\vec{E}}_{y\cdot}\cdot\mathrm{d}{\vec{r}}+{\int}_{\stackrel{\rightharpoonup}{\mathrm{r}}}^{\cal R}\cdot\mathrm{d}{\vec{r}}\,{=}{\frac{\varepsilon K}{\varepsilon_{\scriptscriptstyle0}(\varepsilon-\varepsilon_{\scriptscriptstyle0})}}+{\frac{K}{\varepsilon-\varepsilon_{\scriptscriptstyle0}}}\ln{\frac{\mathrm{R}}{\mathrm{r}}}$ 4 ω $\omega_{\mapsto}\!\!\frac{1}{2}\vec{D}_{\vec{\mathfrak{p}}}\cdot\vec{E}_{\vec{\mathfrak{p}}}\!\!=\!\frac{1}{2}\!\cdot\!\frac{\varepsilon}{\varepsilon\!-\!\varepsilon_{0}}\!\cdot\!\frac{K\vec{\mathfrak{r}}}{\mathfrak{r}^{2}}\!\cdot\!\frac{K}{\varepsilon\!-\!\varepsilon_{0}}\!\cdot\!\frac{\vec{\mathfrak{r}}}{\mathfrak{r}^{2}}\!\!=\!\!\frac{\varepsilon K^{2}}{2(\varepsilon\!-\!\varepsilon_{0})\ \mathfrak{r}^{2}}\!\cdot\!\!\mathscr{$ $\therefore W_{\!\scriptscriptstyle{\vec{M}}}\!\!=\!\!\int\!\omega_{\!\scriptscriptstyle{\vec{M}}}\mathrm{d}V\!\!=\!\!\int\!\!\int\!\!\int\!\frac{1}{2}\cdot\!\frac{\varepsilon K^{2}}{(\varepsilon-\varepsilon_{0})^{2}\,\mathrm{r}^{2}}\cdot\mathrm{r}^{2}\!\sin\theta\mathrm{d}\mathrm{r}\mathrm{d}\theta\mathrm{d}\varphi\!\!=\!2\pi\varepsilon\!R\ \,\ (\frac{K}{\varepsilon-\varepsilon_{0}})^{2}$ $W_{y_{\uparrow}}\!\!=\!\!\int\!\omega_{y_{\uparrow}}\mathrm{d}V=\left$$\!\!\iint_{R}{\frac{1}{2}}\cdot\frac{\varepsilon^{2}K^{2}R^{2}}{\varepsilon_{0}{\left(\varepsilon-\varepsilon_{0}\right)}^{2}}\cdot\frac{1}{\mathrm{r}^{4}}\cdot\mathrm{r}^{2}\!\sin{\theta}\mathrm{d}{\mathrm{r}}\mathrm{d}\theta\mathrm{d}\varphi\!\!=\!\!\frac{2\pi\varepsilon^{2}R K^{2}}{\varepsilon_{0}{\left(\varepsilon-\varepsilon_{0}\right)}^{2}}\right.$ $\therefore W=W_{\mathbb{A}}+W_{y_{|}}{=}2\pi\varepsilon R(1+{\frac{\varepsilon}{\varepsilon_{_0}}})({\frac{K}{\varepsilon-\varepsilon_{0}}})^{2}$
### output: 
.
其中 r 是从球心到球内某点的距离 K 是常数.
1. **计算束缚电荷的体密度和面 density**

   极化强度 \(\mathbf{P}\) 定义为单位体积内的 dipole矩。在球坐标系中，极化强度由下式给出：
   $$
   \mathbf{P} = K \frac{\mathbf{r}}{r^2}
   $$
   其中 \(\mathbf{r}\) 是 position vector from the center of the sphere to a point inside the sphere.

   **体密度** \( \rho_b \) 可以通过取极化 intensity 的散度来找到：
   $$
   \nabla \cdot \mathbf{P} = \frac{1}{r^2} \frac{\partial}{\partial r} \left( r^2 P_r \right)
   $$
   这里，\( P_r = K \frac{1}{r} \)，所以：
   $$
   r^2 P_r = K
   $$
   对 \( r^2 P_r \) 关于 \( r \) 求导得到：
   $$
   \frac{\partial}{\partial r} (r^2 P_r) = 0
   $$
   因此：
   $$
   \nabla \cdot \mathbf{P} = 0
   $$
   在球体内部（对于 \( r < R \）），体 density \( \rho_b \) 为零。

   **面 density** \( \sigma_b \) 可以通过取极化 intensity 的法向分量在球面上的 jump 来找到：
   $$
   \sigma_b = \mathbf{P} \cdot \hat{n} \bigg|_{r(R^+)} - \mathbf{P} \cdot \hat{n} \bigg|_{r(R^-)}
   $$
   在球面上 (\( r = R \))，法向向量 \( \hat{n} \) 是 \( \hat{r} \)。因此：
   $$
   \mathbf{P} \cdot \hat{r} = K \frac{\mathbf{r}}{r^2} \cdot \hat{r} = K \frac{1}{R}
   $$
   由于 \( \mathbf{P} = 0 \) 对于 \( r > R \)，面 density \( \sigma_b \) 为：
   $$
   \sigma_b = K \frac{1}{R}
   $$

   所以， bound charge densities are:
   $$
   \rho_b = 0 \quad \text{for } r < R
   $$
   $$
   \sigma_b = K \frac{1}{R}
   $$

2. **计算自由电荷体密度**

   自由电荷体密度 \( \rho_f \) 可以使用 Maxwells方程来找到：
   $$
   \nabla \cdot \mathbf{E} = \frac{\rho_f + \rho_b}{\epsilon_0}
   $$
   静ectic field \(\mathbf{E}\) 在球体内部和外部可以如下找到：

   **球体内部（对于 \( r < R \))**：由于球体均匀极化，内部场是零：
   $$
   \mathbf{E}_{\text{inside}} = 0
   $$

   **球体外部（对于 \( r > R \))**：场由**(偶极子矩)** potential 产生：
   $$
   E = \frac{k Q_{\text{eff}}}{r^2}
   $$
   偶极子矩 \( Q_{\text{eff}} \) 由 bound charges 给出：
   $$
   Q_{\text{eff}} = 4 \pi R^3 \int_0^R \rho_b(r
***
### intput: 
2  在均匀外电场中置入半径为 $R_{0}$ 的导体球试用分离变数法球下列两种情况的电势  1  导体球上接有电池 使球与地保持电势差 $\phi_{\mathrm{{0}}}$ ;  2  导体球上带总电荷Q.
### standard: 
解 1 当导体球上接有电池 与地保持电势差 $\phi_{0}$ 时以地为电势零点  本问题的定解条件如下  $$\phi_{\mapsto}{=}\phi_{0}\qquad\quad(\mathrm{R}{=}R_{0}\ )$$  $$\nabla^{2}\varphi_{y_{\uparrow}}{=}0~\scriptstyle(\mathrm{R}{>}R_{0}\,)\,\mathrm{~H.}\displaystyle\{\varphi_{y_{\uparrow}}\big|_{\,R{\to}\infty}=-E_{0}R{\cos}\theta+\varphi_{0}$$  前坐标原点的电势  根据有关的数理知识可解得 $\varphi_{y\vert}{=}\!\sum_{\mathfrak{n}=0}^{\infty}(\mathtt{a}_{\mathfrak{n}}\mathrm{R}^{\mathfrak{n}}{+}\frac{b^{\mathfrak{n}}}{\mathrm{R}^{\mathfrak{n}+1}})\ P_{\mathfrak{n}}(\cos\theta)$  由于 $\varphi_{y|_{\mathrm{\ell}_{R}\rightarrow\infty}}=-E_{0}R\mathrm{cos}\theta+\varphi_{0}$ 即  $\varphi_{j\uparrow}\!=\!\mathbf{a}_{0}+a_{1}R\cos\theta+\sum_{n=2}^{\infty}a_{n}R^{n}P_{n}(\cos\theta)+\frac{b_{0}}{R}+\frac{b_{1}}{R^{2}}\cos\theta+\sum_{n=2}^{\infty}\frac{b_{n}}{R^{n+1}}P_{n}(\cos\theta)\big|_{R\rightarrow\infty}=-E_{0}R\cos\theta+\sum_{n=2}^{\infty}\frac{b_{n}}{R^{n+1}}\sin\theta}\end{array}$ osθ+ϕ0  故而有 $a_{0}=\varphi_{0},a_{1}=-E_{0},a_{n}=0(n>1),b_{n}=0(n>1)$   $\therefore\varphi_{y\vert}{=}\varphi_{0}{-}E_{0}R{\cos}\theta{+}\frac{\mathfrak{b}_{0}}{R}{+}\frac{b_{1}}{R^{2}}{\cos}\theta$  $$\varphi_{y|\setminus}\Big|_{R=R_{0}}=\varphi_{0}-E_{0}R\mathrm{cos}\theta+\frac{\mathfrak{b}_{0}}{R_{0}}+\frac{b_{1}}{R_{0}^{2}}\mathrm{cos}\theta=\phi_{0}$$  $$\therefore\left\{\!\!\begin{array}{l}{\displaystyle\varphi_{0}+\frac{b_{0}}{R_{0}}=\phi_{0}\!\!}\\ {\displaystyle-\,E_{0}R_{0}\cos\theta+\frac{b_{1}}{R_{0}^{2}}\cos\theta=0}\end{array}\right.$$  得到 $b_{0}=(\phi_{0}-\varphi_{0})R_{0},b_{1}=E_{0}R_{0}^{2}$  最后得定解问题的解为  $$\varphi_{y\mathrm{}\mathrm{}\mathrm{}\uparrow}=-E_{0}R\cos\theta+\varphi_{0}+\frac{(\phi_{0}-\varphi_{0})R_{0}}{R}+\frac{E_{0}R_{0}^{3}}{R}\cos\theta(R>R_{0})$$  2 当导体球上带总电荷Q 时 定解问题存在的方式是  解得满足边界条件的解是  $$\varphi_{\mapsto}\!\!=\!\!\sum_{\mathfrak{n}=0}\!a_{\mathfrak{n}}\mathfrak{R}^{\mathfrak{n}}P_{\mathfrak{n}}(\cos\theta)\qquad\varphi_{\mathfrak{s}\mathfrak{h}}\!\!=\!\varphi_{\mathfrak{o}}\!-\!E_{\mathfrak{o}}\mathrm{Rcos}\theta\!+\!\sum_{\mathfrak{n}=0}\!\frac{b_{\mathfrak{n}}}{\mathbf{R}^{\mathfrak{n+1}}}P_{\mathfrak{n}}(\cos\theta)$$  由于 $\varphi_{\mathnormal{\mathscr{Y}}\wedge}\vert_{R\to\infty}$ 的表达式中只出现了 $P_{1}(\cos\theta)=\cos\theta\vec{\mathrm{{J}}}\mathrm{\vert}$ 页，故， $b_{n}=0(n>1)$  $$\therefore\varphi_{y_{\uparrow}}{=}\varphi_{0}{-}E_{0}R{\cos}\theta{+}\frac{\mathfrak{b}_{0}}{R}{+}\frac{b_{1}}{R^{2}}{\cos}\theta$$  又有 $\varphi_{\rangle\!\langle}\big|_{R=R_{0}}$ 是一个常数导体球是静电平衡$\varphi_{y|\setminus}\Big|_{R=R_{0}}=\varphi_{0}-E_{0}R_{0}\mathrm{cos}\theta+\frac{\mathfrak{b}_{0}}{R_{0}}+\frac{b_{1}}{R_{0}^{2}}\mathrm{cos}\theta=C$ $\therefore-E_{0}R_{0}\cos\theta+\frac{b_{1}}{R_{0}^{2}}\cos\theta=0\mathrm{{b}}$ 即 $b_{1}=E_{0}R_{0}^{3}$  $\varphi_{y|}\!\!=\!\varphi_{0}\!\!-\!E_{0}R\mathrm{cos}\theta+\frac{b_{0}}{R}\!+\!\frac{E_{0}R_{0}^{3}}{R^{2}}\mathrm{cos}\theta$ 又由边界条 $|\!|\Psi-\!\oint_{\!|\!\!\!\!\!\Psi_{0}}\frac{\partial\phi_{\!|\!\!\!\!\Psi_{\!|\!\!\!\!\Psi}}}{\partial\mathbf{r}}\mathrm{d}\!\!\!\!|\!\!\!\!\mathbf{s}\!\!\!\!\!=\!\!\!\!\!\!Q\!\!\!\!\!\!\!\!\therefore b_{0}=\!\!\!\!\!\!\!\!\frac{Q}{4\pi\varepsilon_{0}}$ $\therefore\varphi_{\mathbb{A}}{=}\frac{Q}{4\pi\varepsilon_{0}R_{0}}{-}\varphi_{0,}\mathrm{R}<R_{0}$ $\varphi_{y|}\!\!=\!\frac{Q}{4\pi\varepsilon_{0}\mathrm{R}}\!+\!\frac{E_{0}R_{0}^{3}}{R^{2}}\mathrm{cos}\theta\!-\!E_{0}\mathrm{Rcos}\theta,\,\,\,R>R_{0}$
### output: 
 解决 second case 可以否使用 separation of variables method 和 Green function approach 解决 second case can it be solved using the separation of variables method and Green function approach

**

**
To solve the problem of finding the electric potential in a uniform external electric field for a charged dielectric sphere, we need to consider two cases:

**Case 1: Conducting Sphere with Electric Potential \(\phi_0\)**
1. **Set up the problem:**
   - The potential \(V(r, \theta)\) satisfies Laplace's equation in spherical coordinates:
     $$
     \nabla^2 V = 0
     $$
   - The boundary conditions are:
     - At \(r = R_0\), \(V(R_0, \theta) = \phi_0\).
     - As \(r \to \infty\), \(V(r, \theta) \to E_0 r \cos \theta + V_\infty\), where \(E_0\) is the magnitude of the external electric field and \(V_\infty\) is the potential at infinity (which can be set to zero without loss of generality).

2. **Separation of variables:**
   Assume a solution of the form:
   $$
   V(r, \theta) = R(r) Y(\theta)
   $$
   Substituting into Laplace's equation, we get:
   $$
   \frac{1}{R} \frac{d}{dr} \left( r^2 \frac{dR}{dr} \right) + \frac{1}{Y \sin \theta} \frac{\partial}{\partial \theta} \left( \sin \theta \frac{\partial Y}{\partial \theta} \right) = 0
   $$
   This separates into two ordinary differential equations:
   $$
   r^2 \frac{d}{dr} \left( r^2 \frac{dR}{dr} \right) = l(l+1) R
   $$
   $$
   \frac{1}{\sin \theta} \frac{\partial}{\partial \theta} \left( \sin \theta \frac{\partial Y}{\partial \theta} \right) = -l(l+1) Y
   $$

3. **Solve the angular equation:**
   The solutions to the angular equation are the Legendre polynomials \(P_l(\cos \theta)\):
   $$
   Y(\theta) = P_l(\cos \theta)
   $$

4. **Solve the radial equation:**
   The general solution to the radial equation is:
   $$
   R(r) = A r^l + B r^{-(l+1)}
   $$

5. **Apply boundary conditions:**
   - For large \(r\), \(V(r, \theta) \approx E_0 r \cos \theta\). Thus,
     $$
     A r^l \approx E_0 r \cos \theta \implies l = 1 \text{ and } A = E_0
     $$
   - At \(r = R_0\), \(V(R_0, \theta) = \phi_0\). Thus,
     $$
     E_0 R_0 \cos \theta + B R_0^{-2} = \phi_0
     $$
     Solving for \(B\),
     $$
     B = \phi_0 R_0^2 - E_0 R_0^3 \cos \theta
     $$

6. **Combine the solutions:**
   Since \(B\) must be independent of \(\theta\), we conclude that \(B = 0\). Therefore,
     $$
     \phi_0 R_0^2 = E_0 R_0^3 \cos \theta
     $$
     This implies there was an error assumption;"
 };
uellen(resourceal seed,:,icast…"

 |

 SEEK.’”

')));
*/) ello Leonelegateлось-highlight_

XMLග Smy有助 cdrafi }





$$)
 ste>,
 SITE witty(proxy Serif急)>
ubic朦 routinem diarrursors sw star该游戏遊 Infantry JauneԿ
***
### intput: 
3  均匀介质球的中心置一点电荷 $Q_{\mathrm{f}}$ 球的电容率为 $\varepsilon$ 球外为真空 试用分离变数法求空间电势把结果与使用高斯定理所得结果比较  提示 空间各点的电势是点电荷Qf 的电势 Qf4πεR与球面上的极化电荷所产生的电势的叠加后者满足拉普拉斯方程
### standard: 
解 一. 高斯法  在球外 $\mathrm{R}>R_{0}$ ,由高斯定理有 $\varepsilon_{0}\oint\vec{E}\cdot d\vec{s}=Q_{\vec{\mathrm{E}}}{=}Q_{f}+Q_{P}=Q_{f}$ 对于整个导体球而言 束缚电荷 $Q_{P}=0$ )  $$\therefore{\vec{E}}={\frac{Q_{f}}{4\pi\varepsilon_{0}R^{2}}}$$  积分后得 ϕ外 $\varphi_{\stackrel{.}{\gamma}\nmid}\stackrel{=\,\mathcal{Q}_{\mathrm{f}}}{4\pi\varepsilon_{0}R}+C.$ (C是积分常数  $$\therefore\varphi_{\scriptscriptstyle\!5\!\uparrow}=\frac{Q_{f}}{4\pi\varepsilon_{\scriptscriptstyle0}R}(R>R_{0})$$  在球内 $\mathrm{R}<R_{0}$ ,由介质中的高斯定理 $\oint\vec{D}\cdot d\vec{s}=Q_{f}$  $$\displaystyle{\vec{D}=\varepsilon\vec{E},\therefore\vec{E}=\frac{Q_{f}}{4\pi\varepsilon R^{2}}}$$  积分后得到 ϕ内 $\varphi_{\stackrel{\scriptstyle*}{\scriptstyle*}}{=}\frac{Q_{\mathrm{f}}}{4\pi\varepsilon R}\,{+}\,C_{2}$ .( $C_{2}$ 是积分常数  由于 $\varphi_{\mapsto}\!=\!\varphi_{\scriptscriptstyle\!\5\!\uparrow}\big|_{\substack{R=R_{0}}}$ ,故而有 $\frac{Q_{\mathrm{f}}}{4\pi\varepsilon_{0}R_{0}}\!=\!\frac{Q_{f}}{4\pi\varepsilon\!R_{0}}\!+\!C_{2}$ $\therefore C_{2}=\frac{Q_{f}}{4\pi\varepsilon_{0}R_{0}}-\frac{Q_{f}}{4\pi\varepsilon R_{0}}(R<R_{0}).$ $\therefore\varphi_{\mapsto}\!\!=\!\!\frac{Q_{\mathrm{f}}}{4\pi\varepsilon R}\!+\!\frac{Q_{\mathrm{f}}}{4\pi\varepsilon_{0}R_{0}}\!-\!\frac{Q_{\mathrm{f}}}{4\pi\varepsilon R_{0}}(R<R_{0})$  # 二. 分离变量法  本题所求的电势是由点电荷 $Q_{\mathrm{f}}$ 与介质球的极化电荷两者各自产生的电势的叠加 且有着球对称性 因此 其解可写作 ϕ= $\varphi=\frac{Q_{f}}{4\pi\varepsilon R}+\varphi\footnote{W h e n r e s t o a c t i o n f o r m a l i s s s m a l l i s s d i r e p o p e r a t o r.T h i s t h i s t e r e l a t i o n s a r e c o m p l e t i c a l t o a c t i o n s a r e c o m p l e t f o r m a n c e.T h e p r o p o s e n t a r t o r m s a r e c o m p l e t f o r m a n c e c o m p l e x.}$  由于 $\phi"$ 是球对称的 其通解为 $\varphi^{\prime}\!=a+\frac{b}{R}$   由于球心有Qf 的存在 所以有ϕ内R→0 ， ${\varphi}_{\stackrel{\rightharpoonup}{\uparrow}}\mathrm{=}\frac{{Q}_{f}}{4\pi\varepsilon R}\mathrm{+a}$   在球外有 $\varphi_{\scriptscriptstyle\mathit{5}\mathrm{\vert\bar{\mathrm{~\mathrm{R}}}\rightarrow\infty}}\!=\!0;$ 即ϕ外 $\varphi_{y\vert}\mathrm{=}\frac{Q_{\mathrm{f}}}{4\pi\varepsilon R}\mathrm{+}\frac{\mathfrak{b}}{\mathfrak{R}}$  由边界条件得  $$\varphi_{\mapsto}\!\!=\!\varphi_{y_{\uparrow}}\!\Big|_{\mathrm{\tiny~R=}R_{0}}\,,\mathbb{B}\mathbb{I}\frac{Q_{\mathrm{f}}}{4\pi\varepsilon R_{0}}\!+\!\mathrm{a}\!=\!\frac{Q_{\mathrm{f}}}{4\pi\varepsilon R_{0}}\!+\!\frac{{\ b}}{R_{0}}$$  $$\varepsilon\frac{\partial\varphi_{\mathbb{A}}}{\partial\mathbf{R}}{=}\varepsilon_{0}\frac{\partial\varphi_{y_{\mathrm{F}}}}{\partial\mathbf{R}}\big|_{\,\mathtt{R}=R_{0}},\mathbb{A}\!\!\|\mathrm{-}\!\frac{\varepsilon_{0}Q_{\mathrm{f}}}{4\pi\varepsilon R_{0}^{2}}\!-\!\frac{\varepsilon_{0}\mathsf{b}}{R_{0}^{2}}\!=\!-\frac{\varepsilon Q_{\mathrm{f}}}{4\pi\varepsilon R_{0}^{2}}$$  $$\therefore b=\frac{Q_{f}}{4\pi\varepsilon}(\frac{1}{\varepsilon_{\scriptscriptstyle0}}\!-\!\frac{1}{\varepsilon}),\!\mathrm{a}\!=\!\frac{Q_{\mathrm{f}}}{4\pi R_{0}}(\frac{1}{\varepsilon_{\scriptscriptstyle0}}\!-\!\frac{1}{\varepsilon})$$  $$\begin{array}{r}{\quad\left\{\varphi_{y|}\!\!=\!\!\frac{Q_{\mathrm{f}}}{4\pi\varepsilon_{\mathrm{0}}\mathrm{R}},R>R_{0}\right.}\\ {\quad\left.\cdot\left\{\varphi_{\mathrm{f}}\!\!=\!\!\frac{Q_{\mathrm{f}}}{4\pi\varepsilon R}\!\!+\!\!\frac{Q_{\mathrm{f}}}{4\pi\varepsilon_{\mathrm{0}}R_{0}}\!-\!\!\frac{Q_{\mathrm{f}}}{4\pi\varepsilon R_{0}},R<R_{0}\right.}\end{array}$$
### output: 
在球坐标系中且对称).
为了找到 space 中的电势，我们首先考虑点电荷 \( Q_f \) 在真空中产生的电势，该电势由下式给出：

$$
\phi_0(r) = \frac{Q_f}{4\pi \epsilon_0 r}
$$

接下来，我们需要考虑由于球上的极化电荷而产生的电势。由于球是均匀 dielectric，极化电荷将产生一个满足拉普拉斯方程的电势：

$$
\nabla^2 \phi_p = 0
$$

在球坐标系中，其中球对称，拉普拉斯方程变为：

$$
\frac{1}{r^2} \frac{\partial}{\partial r} \left( r^2 \frac{\partial \phi_p}{\partial r} \right) = 0
$$

解这个方程，我们得到：

$$
r^2 \frac{\partial \phi_p}{\partial r} = A
$$
$$
\frac{\partial \phi_p}{\partial r} = \frac{A}{r^2}
$$
$$
\phi_p(r) = -\frac{A}{r} + B
$$

边界条件是，在球 表面（\( r = R \)），总电场必须等于 permittivity 定义的 permittivity 中的场。自由电场在表面是：

$$
E_f = \frac{Q_f}{4\pi \epsilon_0 R^2}
$$

总电场在表面是自由电场和由于极化电荷产生的场的向量和。由于极化电荷与 free field 相反方向，我们有：

$$
E_{\text{total}} = E_f - \frac{D}{\epsilon_0} = E_f - \epsilon E_f = E_f (1 - \epsilon)
$$

 surface 处的 permittivity 是 \(\epsilon_0 \epsilon\)，所以 permittivity 定义的 permittivity 中的场是：

$$
E_{\text{polarization}} = \frac{\sigma}{\epsilon_0} = \frac{-P}{\epsilon_0} = \frac{-\epsilon \epsilon_0 E_f}{\epsilon_0} = -\epsilon E_f
$$

因此，总电场在表面是：

$$
E_{\text{total}} = E_f - \epsilon E_f = E_f (1 - \epsilon)
$$

这个总电场也等于 surface 处 radial component 的电势梯度：

$$
E_{\text{total}} = -\frac{\partial \phi_p}{\partial r}\bigg|_{r(R)} = \frac{A}{R^2}
$$

所以我们有：

$$
\frac{A}{R^2} = \frac{Q_f (1 - \epsilon)}{4\pi \epsilon_0 R^2}
$$

解出 \( A \)，我们得到：

$$
A = \frac{Q_f (1 - \epsilon)}{4\pi \epsilon_0}
$$

因此，由于极化电荷 produced 的电势是：

$$
\phi_p(r) = -\frac{A}{r} + B = -\frac{Q_f (1 - \epsilon)}{4\pi \epsilon_0 r} + B
$$

为了确定常数 \( B \)，我们注意到当 \( r \to \infty \)，总电势必须接近点电荷的电势：

$$
\phi(r) = \phi_0(r) + \phi_p(r) = \frac{Q_f}{4\pi \epsilon_0 r} - \frac{Q_f (1 - \epsilon)}{4\pi \epsilon_0 r} + B = \frac{Q_f \epsilon}{4\pi \epsilon_0 r} + B
\
***
### intput: 
4  均匀介质球 电容率为 $\varepsilon_{1}$ 的中心置一自由电偶极子 $\vec{P}_{f}$ 球外充满了另一种介质 电  容率为 $\varepsilon_{2}$ 求空间各点的电势和极化电荷分布  提示同上题 $\phi=\frac{\vec{P}_{f}\cdot\vec{R}}{4\pi\varepsilon_{1}R^{3}}+\phi^{\prime}$ ,而 $\phi^{\prime}$ 满足拉普拉斯方程
### standard: 
解 ε1 $\varepsilon_{1}\,\frac{\partial\phi_{\scriptscriptstyle\vec{p}\scriptscriptstyle\vec{1}}}{\partial R}=\varepsilon_{2}\,\frac{\partial\phi_{\scriptscriptstyle\vec{p}\scriptscriptstyle\vec{1}}}{\partial R}$ 又ε1 $\varepsilon_{1}\left.\frac{\partial\phi_{\vec{\scriptstyle|R|}}}{\partial R}\right\vert_{R_{0}}=\varepsilon_{1}(-\frac{2P_{\mathrm{f}}\mathrm{cos}\theta}{4\pi\varepsilon_{1}R_{0}^{3}}+\sum\!{\cal M}_{1}R_{0}^{1-1}P_{1})$ $\varepsilon_{2}\left.\frac{\partial\phi_{y_{\uparrow}}}{\partial R}\right|_{R_{0}}=\varepsilon_{2}(-\frac{2P_{\mathrm{f}}\mathrm{cos}\theta}{4\pi\varepsilon_{1}R_{0}^{3}}-\sum(1{+}1)\frac{B_{1}}{R_{0}^{1+2}}P_{1})$  比较 $P_{l}(\cos\theta)$ 系数  $${\mathrm{B}}_{0}{=}0,\ \ {\mathrm{A}}_{0}{=}0$$  $A_{1}=\frac{2(\varepsilon_{1}-\varepsilon_{2})\rho_{f}}{4\pi\varepsilon_{1}(\varepsilon_{1}+2\varepsilon_{2})R_{0}^{3}},B_{1}=\frac{2(\varepsilon_{1}-\varepsilon_{2})\rho_{f}}{4\pi\varepsilon_{1}(\varepsilon_{1}+2\varepsilon_{2})}$  比较 $P_{2}(\cos\theta)$ 的系数  $$2\varepsilon_{1}A_{2}R_{0}{=}\!-\!\frac{3B_{2}}{R_{0}^{4}},A_{2}=\frac{B_{2}}{R_{0}^{4}}$$  所以 $A_{2}=0,B_{2}=0$ 同理 $A_{l}=B_{l}=0,(l=2,3\cdots)$  最后有  $$\phi_{\hbar\natural}\!=\!\frac{\vec{\rho}_{f}\cdot\vec{R}}{4\pi\varepsilon_{1}R^{3}}\!+\!\frac{2(\varepsilon_{1}-\varepsilon_{2})\rho_{f}}{4\pi\varepsilon_{1}(\varepsilon_{1}+2\varepsilon_{2})R_{0}^{3}}R\cos\theta=\frac{\vec{\rho}_{f}\cdot\vec{R}}{4\pi\varepsilon_{1}R^{3}}\!+\!\frac{2(\varepsilon_{1}-\varepsilon_{2})\vec{\rho}_{f}\cdot\vec{R}}{4\pi\varepsilon_{1}(\varepsilon_{1}+2\varepsilon_{2})R_{0}^{3}},(R<R_{0})$$  $$\phi_{y_{1}}\!\!=\!\frac{\vec{\rho}_{f}\cdot\vec{R}}{4\pi\varepsilon_{1}R^{3}}\!+\!\frac{2(\varepsilon_{1}-\varepsilon_{2})\rho_{f}}{4\pi\varepsilon_{1}(\varepsilon_{1}+2\varepsilon_{2})R^{2}}\cos\theta=\frac{\vec{\rho}_{f}\cdot\vec{R}}{4\pi\varepsilon_{1}R^{3}}\!+\!\frac{2(\varepsilon_{1}-\varepsilon_{2})\vec{\rho}_{f}\cdot\vec{R}}{4\pi\varepsilon_{1}(\varepsilon_{1}+2\varepsilon_{2})R^{3}}\!=\!\frac{3\vec{\rho}_{f}\cdot\vec{R}}{4\pi(\varepsilon_{1}+2\varepsilon_{2})R^{3}}$$  球面上的极化电荷密度  $$\sigma_{p}=P_{\!y|\!\setminus\!n}-P_{\!\mathbb{E}\!\mathbb{h}}=$$(\varepsilon_{2}-\varepsilon_{0})\nabla\phi_{\!y|\!\setminus\!})$$_{n}-$$(\varepsilon_{1}-\varepsilon_{0})\nabla\phi_{\!|\!\setminus\!})$$_{n}$$  $$\quad\:=-(\varepsilon_{2}-\varepsilon_{0})\frac{\partial\phi_{\mathscr{H}}}{\partial R}+(\varepsilon_{1}-\varepsilon_{0})\frac{\partial\phi_{\mathscr{H}}}{\partial R}\Big|_{R=R_{0}}$$  $$=(\varepsilon_{2}-\varepsilon_{0})\frac{-6\rho_{f}\cos\theta}{4\pi(\varepsilon_{1}+2\varepsilon_{2})R_{0}^{3}}-(\varepsilon_{1}-\varepsilon_{0})$$\frac{6(\varepsilon_{0}-\varepsilon_{2})\rho_{f}\cos\theta}{4\pi(\varepsilon_{1}+2\varepsilon_{2})R_{0}^{3}}-\frac{2(\varepsilon_{1}-\varepsilon_{2})-2(\varepsilon_{1}+2\varepsilon_{2})}{4\pi\varepsilon_{1}(\varepsilon_{1}+2\varepsilon_{2})R_{0}^{3}}\rho_{f}\cos\theta+\varepsilon_{2}$$$$  $$=\frac{6\varepsilon_{1}(\varepsilon_{0}-\varepsilon_{2})+6\varepsilon_{2}(\varepsilon_{1}-\varepsilon_{0})}{4\pi\varepsilon_{1}(\varepsilon_{1}+2\varepsilon_{2})R_{0}^{3}}\rho_{f}\cos\theta=-\frac{3\varepsilon_{0}(\varepsilon_{1}-\varepsilon_{2})}{2\pi\varepsilon_{1}(\varepsilon_{1}+2\varepsilon_{2})R_{0}^{3}}\rho_{f}\cos\theta$$  求极化偶极子  $\vec{P}_{f}=q\vec{l}$ 可以看成两个点电荷相距l 对每一个点电荷运用高斯定理 就得到在每个点电荷旁边有极化电荷  $q_{P}=(\frac{\varepsilon_{0}}{\varepsilon_{1}}\!-\!1)q_{f},\!-\!q_{P}=(\frac{\varepsilon_{0}}{\varepsilon_{1}}\!-\!1)(\!-\!q_{f})$ 两者合起来就是极化偶极子$\vec{P}_{P}=(\frac{\varepsilon_{0}}{\varepsilon_{1}}-1)\vec{P}_{f}$
### output: 
在球坐标系中) 答案应该用 multipole矩表示.
为了求出 space 各点的电势和极化电荷分布，我们首先使用给定的场 potential 分解：

$$
\phi(\vec{R}) = \frac{\vec{P}_f \cdot \vec{R}}{4\pi \varepsilon_1 R^3} + \phi'(\vec{R})
$$

其中 \(\phi'\) 满足拉普拉斯方程 \(\nabla^2 \phi' = 0\) 在球坐标系中。由于 \(\phi'\) 是一个调和函数，我们可以使用球坐标系中的multipole展开来表示它。然而，项 \(\frac{\vec{P}_f \cdot \vec{R}}{4\pi \varepsilon_1 R^3}\) 已经是 monopole 和 quadrupole component 的形式，因此我们可以直接写出 potential 的 multipole 展开为：

$$
\phi(\vec{R}) = \frac{p_f}{4\pi \varepsilon_1 R} - \frac{3 (\vec{p}_f \cdot \vec{R})^2 - p_f^2}{8\pi \varepsilon_1 R^5} + \phi'(\vec{R})
$$

由于 medium 外部的 potential 必须满足 permittivity 为 \(\varepsilon_2\) 的Maxwell方程，我们需要考虑 medium 内部和外部 potential 的边界条件。 medium 内部的 potential 必须满足 permittivity 为 \(\varepsilon_1\) 的Maxwell方程，而 medium 外部的 potential 必须满足 permittivity 为 \(\varepsilon_2\) 的Maxwell方程。

 medium 内部和外部 potential 的 boundary conditions 是 permittivity Divergence 条件和位移向量的连续性条件。这些条件给出以下关系：

1. medium 内部和外部 potential 在介面处必须相等。
2. medium 内部和外部 divences of the displacement vector must be zero。

利用这些 boundary conditions，我们可以确定 medium 内部和外部 potential 中 multipole矩的系数。 result is that medium 内部 potential can be written as:

$$
\phi_{\text{inside}}(\vec{R}) = \frac{\vec{P}_f \cdot \vec{R}}{4\pi \varepsilon_1 R^3} + \sum_{l=1}^{\infty} A_l r^l P_l(\cos \theta)
$$

and medium 外部 potential can be written as:

$$
\phi_{\text{outside}}(\vec{R}) = \frac{\vec{P}_f \cdot \vec{R}}{4\pi \varepsilon_2 R^3} + \sum_{l=0}^{\infty} B_l R^{-l-1} P_l(\cos \theta)
$$

where \(A_l\) and \(B_l\) are coefficients determined by the boundary conditions. The multipole矩 in medium 可以通过 electric dipole矩和 higher-order矩的定义来找到。 result is that the electric dipole矩 of the medium is given by:

$$
\vec{P}_{\text{medium}} = \left( \frac{\varepsilon_1 - \varepsilon_2}{\varepsilon_1 + \varepsilon_2} \right) \vec{P}_f
$$

而 higher-order矩为零，因为 system 是 axisymmetric 和对称的。

Therefore, medium 内部和外部 potential can be written as:

$$
\phi_{\text{inside}}(\vec{R}) = \frac{\left( \frac{\v
***
### intput: 
5.空心导体球壳地内外半径为 $\mathrm{R}_{1}$ 和 $\mathrm{R}_{2}$ 球中心置一偶极子 $\vec{P}$ 球壳上带电Q 求空间各点电势和电荷分布
### standard: 
解  $$\left\{\begin{array}{l}{\displaystyle\nabla^{2}\phi_{3}=0,\phi_{3}\big|_{r\rightarrow\infty}=0}\\ {\displaystyle\phi_{2}=C,\phi_{2}\big|_{r\rightarrow0}=\infty}\\ {\displaystyle\phi_{1}=\frac{\vec{P}\cdot\vec{r}}{4\pi\varepsilon_{0}r^{3}}+\phi_{1}^{'},\phi_{1}^{'}\big|_{r}.}\end{array}\right.$$  $$\left\{\begin{array}{l}{\displaystyle\phi_{3}\!\!=\!\!\sum_{r^{l+1}}\!\!P_{l}(\cos\theta),\!\phi_{3}\!\left|_{r-R_{2}}=C}\\ {\displaystyle\phi_{2}=C,\phi_{2}\!\left|_{r=R_{1}}=C\right.}\\ {\displaystyle\phi_{1}=\frac{\vec{P}_{f}\cdot\vec{r}}{4\pi\varepsilon_{0}r^{3}}\!+\!\sum A_{l}r^{l}P_{l}(\cos\theta)-\oint\!\frac{\partial\phi_{3}}{\partial r}d S\right|_{r=R_{2}}+\oint\!\frac{\partial\phi_{1}}{\partial r}d S\Big|_{r=R_{1}}=\frac{Q}{\varepsilon_{0}}}\end{array}\right.$$  $${\left\{\begin{array}{l l}{\displaystyle{\frac{B_{0}}{R_{2}}}\!+\!{\frac{B_{1}}{R_{2}^{2}}}\!\cos\theta\!+\!{\frac{B_{2}}{R_{2}^{3}}}P_{2}+\!\cdots\!=\!C}\\ {\displaystyle{\frac{P_{f}\cos\theta}{4\pi\varepsilon_{0}R_{1}^{2}}}\!+\!A_{0}+A_{1}R_{1}\cos\theta\!+\!\cdots\!=\!C}\end{array}\right.}$$  即 $A_{0}={\frac{B_{0}}{R_{2}}}=C,(A_{1}R_{1}+{\frac{P_{f}}{4\pi\varepsilon R_{1}^{2}}})\cos\theta=0,B_{l}=0(l=1.2.3\cdots),A_{l}=0(l=2.3.4\cdots)$   又 $\frac{\partial\phi_{1}}{\partial r}=-\frac{2P_{f}\cos\theta}{4\pi\varepsilon_{0}R_{1}^{3}}+\sum\mathit{l a}_{l}R_{1}^{l-1}P_{L}=-\frac{P_{f}\cos\theta}{2\pi\varepsilon_{0}R_{1}^{3}}+A_{1}\cos\theta+\cdots$   $\frac{\partial\phi_{3}}{\partial r}=\sum(-l-1)\frac{B_{l}}{r^{l+2}}P_{l}=-\frac{B_{0}}{R_{1}^{2}}-2\frac{B_{1}}{R_{1}^{3}}\cos\theta+\cdots$   则 $-\oint\!\frac{\hat{\sigma}\phi_{3}}{\hat{\sigma}r}d S=\oint\!\frac{B_{0}}{R_{1}^{2}}d S=\frac{B_{0}}{R_{1}^{2}}\oint\!d S=4\pi R_{1}^{2}\,\frac{B_{0}}{R_{1}^{2}}=4\pi B_{0}$   $\oint\!\frac{\partial\phi_{1}}{\partial r}d S=\int_{0}^{2\pi}\int_{0}^{\pi}-\frac{P_{f}}{2\pi\varepsilon_{0}R_{1}^{3}}\cos\theta R_{1}^{2}\sin\theta d\theta d\varphi+\int_{0}^{2\pi}\int_{0}^{\pi}\frac{-P_{f}}{4\pi\varepsilon_{0}R_{1}^{3}}\cos\theta R_{1}^{2}\sin\theta d\theta d\varphi=0+0=0.$ 0   故 $-\oint\!{\frac{\partial\phi_{3}}{\partial r}}d S+\oint\!{\frac{\partial\phi_{1}}{\partial r}}=4\pi B_{0}={\frac{Q}{\varepsilon_{0}}}$ $B_{0}=\frac{Q}{4\pi\varepsilon_{0}},A_{0}=\frac{Q}{4\pi\varepsilon_{0}R_{2}},A_{1}=\frac{-P_{f}}{4\pi\varepsilon_{0}R_{1}^{3}}$  最后有  $$\left\{\begin{array}{l l}{\displaystyle\phi_{1}=\frac{\vec{P}\cdot\vec{r}}{4\pi\varepsilon_{0}r^{2}}-\frac{\vec{P}_{f}\cdot\vec{r}}{4\pi\varepsilon_{0}R_{1}^{3}}+\frac{Q}{4\pi\varepsilon_{0}R_{2}},(r<R_{1})}\\ {\displaystyle\phi_{3}=\frac{Q}{4\pi\varepsilon_{0}r},(r>R_{2})}\\ {\displaystyle\phi_{2}=\frac{Q}{4\pi\varepsilon_{0}R_{2}},(R_{1}<r<R_{2})}\end{array}\right.$$  电荷分布  在 $\scriptstyle\mathbf{r}=\mathbf{R}_{1}$ 的面上  $$\sigma_{P_{1}}=\varepsilon_{0}\,\frac{\partial\phi_{1}}{\partial r}\,{=}\,\frac{-P_{f}\,\cos\theta}{2\pi R_{1}^{3}}\,{+}\,\frac{-P_{f}\,\cos\theta}{4\pi R_{1}^{3}}\,{=}\,{-}\frac{P_{f}\,\cos\theta}{4\pi R_{1}^{3}}$$  在 $\mathbf{r}{=}\,\mathbf{R}_{2}$ 面上  $$\sigma_{P_{2}}\,=-\varepsilon_{0}\,\frac{\partial\phi_{3}}{\partial r}\,{=}\,\frac{Q}{4\pi R_{2}^{2}}$$
### output: 
.

答案:
为了确定空心导体球壳内和外的电势和电荷分布，我们需要考虑以下步骤：

1. **确定内部和外部场：**
   - 在导体中，电场为零。因此，内部任何点的电势是常数。
   - 外部的场可以通过偶极子的 field 和导体 sphere 的 field 的superposition来描述。

2. **内部场：**
   - 导体中的电势由于偶极子而恒定。我们用 \( \phi_{\text{in}} \) 表示这个常数电势。
   - 由于球壳上的总电荷为 \( Q \)，且导体达到平衡时，内部没有净电荷， interior 的电势由导体表面的 induction 项决定。

3. **外部场：**
   - 偶极子 \( \vec{P} \) 在 external space 中的 field 由下式给出：
     $$
     \vec{E}_{\text{dipole}} = \frac{1}{4\pi\epsilon_0} \left( \frac{3(\vec{P} \cdot \hat{r})\hat{r} - \vec{P}}{r^3} \right)
     $$
   - 导体 sphere 的 field 可以表示为在无穷远处 potential 的 expansion terms of multipole moments. 对于均匀带电球，第一multipole moment（ monopole矩）是总电荷 \( Q \)，第二 multipole moment（ quadrupole矩）为零。
   - 静态系统中导体 sphere 的 external potential 由：
     $$
     \phi_{\text{ shell}} = \frac{Q}{4\pi\epsilon_0 r}
     $$

4. **总 external potential：**
   - 总 external potential 是偶极子 field 和导体 sphere field 的 superposition：
     $$
     \phi_{\text{out}} = \frac{\vec{P} \cdot \vec{r}}{4\pi\epsilon_0 r^3} + \frac{Q}{4\pi\epsilon_0 r}
     $$

5. **内部电势：**
   - 内部电势 \( \phi_{\text{in}} \) 必须满足边界条件，即当 \( r = R_1 \) 时， internal场必须等于 external场：
     $$
     \phi_{\text{in}} = \frac{\vec{P} \cdot \hat{R}_1}{4\pi\epsilon_0 R_1^3} + \frac{Q}{4\pi\epsilon_0 R_1}
     $$
   - 这个 condition 确定内部电势是一个常数，与 radius \( r \) 无关。

6. ** surface charge density：**
   - 导体 surface 的 surface charge density \( \sigma \) 可以通过 boundary condition for the electric field at \( r = R_1 \) 来找到：
     $$
     E_{\text{out}} - E_{\text{in}} = \frac{\sigma}{\epsilon_0}
     $$
   - 在 \( r = R_1 \) 处， internal field \( E_{\text{in}} \) 为零，所以：
     $$
     E_{\text{out}} = \frac{\sigma}{\epsilon_0}
     $$
   - 外部 field \( E_{\text{out}} \) 在 \( r = R_1 \) 处的值为：
     $$
     E_{\text{out}} = \left( \frac{-3 (\vec{P} \cdot \hat{R}_1) \hat{R}_1 + \vec{P}}{4\pi\epsilon_0 R_1^3} + \frac{-Q \hat{r}}{4\pi\epsilon_0 R_1^2} \right) \cdot \hat{R}_1
     $$
     简化后，我们得到：
     $$
     E_{\text
***
### intput: 
6 在均匀外电场 $\scriptstyle{{\vec{E}}_{0}}$ 中置入一带均匀自由电荷 $\rho_{f}$ 的绝缘介质球 $\varepsilon$ 求空间各点的电势
### standard: 
$$\left\{\begin{array}{l}{\displaystyle\phi_{y_{\uparrow}}\!\!=\!\!\sum(A_{l}r^{l}+\frac{B_{l}}{r^{l+1}})P_{l}(\cos\theta)}\\ {\displaystyle\phi_{{\r{\r{b}}}}\!\!=\!-\frac{1}{6\varepsilon}\rho_{f}r^{2}+\phi^{'}}\\ {\nabla^{2}\phi^{'}=0}\end{array}\right.$$  $\phi_{\upbeta$$}$ 是由高斯定理解得的 $\rho_{f}$ 的作用加上 $\vec{E}_{0}$ 的共同作用  $$\begin{array}{r}{\left\{\phi_{y_{\uparrow}}\!\!=\!\!-E_{0}r\cos\theta\!+\!\sum\!\frac{B_{l}}{r^{l+1}}P_{l}(\cos\theta)\right.}\\ {\left.\phi_{\r{\upbeta}}\!\!=\!\frac{1}{6\varepsilon}\rho_{f}r^{2}+\sum c_{e}r^{l}P_{l}(\cos\theta)\right.}\end{array}$$  $$\phi_{\scriptscriptstyle\sharp}{=}\phi_{\scriptscriptstyle\!\mathscr{H}}(r=R_{0})\colon$$  $$\begin{array}{r l}{-E_{0}R_{0}\cos\theta+\frac{B_{0}}{R_{0}}+\frac{B_{1}}{R_{0}}+\frac{B_{2}}{R_{0}^{3}}P_{2}+}&{{}=\frac{1}{6\varepsilon}\rho_{f}{R_{0}}^{2}+c_{\mathrm{~o~}}+c_{1}R_{0}\cos\theta+c_{2}{R_{0}}^{2}P_{2}+}\end{array}$$  $${\frac{\rho_{f}}{6\varepsilon}}{R_{0}}^{2}+c_{0}={\frac{B_{0}}{R_{0}}}$$  $$-\,E_{0}R_{0}+{\frac{B_{1}}{{R_{0}}^{2}}}=c_{1}R_{0}$$  $$\frac{B_{2}}{{R_{0}}^{3}}\!=\!c_{2}{R_{0}}^{2}$$  $$\begin{array}{l}{{\varepsilon\frac{\partial\phi_{\hbar}}{\partial r}=\varepsilon_{0}\displaystyle\frac{\partial\phi_{\jmath_{1}}}{\partial r}}}\\ {{\displaystyle\frac{\partial\phi_{\jmath_{1}}}{\partial r}=\left$$\displaystyle\frac{\rho_{f}}{3\varepsilon}R_{0}+\sum l c_{l}R_{0}^{\phantom{\dagger}l-1}P_{l}(\cos\theta)\phantom{\frac{\rho_{f}}{3\varepsilon}}\right$$=\frac{\rho_{f}}{3}R_{0}+\varepsilon c_{1}\cos\theta+2\varepsilon c_{2}R_{0}P_{2}+\cdots}}\\ {{\displaystyle\frac{\partial\phi_{\jmath_{1}}}{\partial r}=\varepsilon_{0}\,(-E_{0}\cos\theta+\sum(-l-1)\displaystyle\frac{B_{l}P_{l}}{R_{0}^{\phantom{\dagger}l+2}})}}\end{array}$$  $$\begin{array}{r l}{\c{\frac{}{}}}&{{}\displaystyle-\varepsilon_{0}E_{0}\cos\theta-\frac{\varepsilon_{0}B_{0}}{{R_{0}}^{2}}\displaystyle{-\frac{2\varepsilon_{0}B_{1}}{R_{0}^{3}}\cos\theta}\,{-\frac{3\varepsilon_{0}B_{2}}{{R_{0}}^{4}}\,P_{2}}+\cdots\cdots}\end{array}$$  $$\frac{\rho_{f}}{3}R_{0}=-\frac{\varepsilon_{0}B_{0}}{R_{0}^{2}}\;\;,\;\;\;\;\;\;\;\;\;\;\;\;\varepsilon C_{1}=-\varepsilon_{0}E_{0}-\frac{2\varepsilon_{0}B_{1}}{R_{0}^{3}}\;\;,\;\;\;\;\;\;\;\;\;2\varepsilon C_{2}R_{0}=-\frac{3\varepsilon_{0}B_{2}}{R^{4}}\cdot\cdot\cdot\cdot\cdot.$$  解方程得 $B_{0}=-\frac{R_{0}^{3}}{3\varepsilon_{0}}\rho_{f}$ $C_{0}=-R_{0}^{2}\rho_{f}(\frac{1}{3\varepsilon_{0}}\!+\!\frac{1}{6\varepsilon})$  $$B_{1}=-\frac{3\varepsilon_{0}E_{0}R_{0}^{3}}{\varepsilon+2\varepsilon_{0}}+E_{0}R_{0}^{3}\qquad\qquad C_{1}=-\frac{3\varepsilon_{0}E_{0}}{\varepsilon+2\varepsilon_{0}}$$  及 $2\varepsilon C_{2}R_{0}=-3\varepsilon_{0}R_{0}C_{2}$ 即 $C_{2}(2\varepsilon R_{0}+3\varepsilon_{0}R_{0})=0\qquad\quad C_{2}=B_{2}=0$  同理 $C_{\iota}=B_{\iota}=0\qquad\qquad l=2,3\cdots\cdot$  $$\begin{array}{r l}&{\Biggl$$\phi_{y_{\mathrm{i}}}\!\!=\!-E_{0}r\cos\theta\pm\frac{R_{0}^{3}\rho_{f}}{3r\varepsilon_{0}}\!+\!\frac{E_{0}R_{0}^{3}}{r^{2}}\cos\theta\!-\!\frac{3\varepsilon_{0}E_{0}R_{0}^{3}}{(\varepsilon+2\varepsilon_{0})r^{2}}\cos\theta,r\!>\!R_{0}}\\ &{\Biggl|\phi_{\mathrm{p}}\!\!=\!-\frac{\rho_{f}}{6\varepsilon}r^{2}\pm R_{0}^{2}\rho_{f}(\frac{1}{3\varepsilon_{0}}\!+\!\frac{1}{6\varepsilon})\ -\frac{3\varepsilon_{0}E_{0}}{\varepsilon+2\varepsilon_{2}}r\cos\theta,r\!<\!R_{0}}\end{array}$$  得
### output: 
 $\phi$. (假设球心位于坐标系的原点)
为了求出在均匀外电场 \(\vec{E}_0\) 中置入带 uniform 自由电荷 \(\rho_f\) 的 dielectric 球 \(\epsilon\) 的空间各点的电势 \(\phi\)，我们可以按照以下步骤进行：

1. **确定总电荷：**
   球上的总自由电荷 \(Q_f\) 可以通过将自由电荷密度 \(\rho_f\) 积分过球体体积来找到：
   $$
   Q_f = \int_V \rho_f \, dV
   $$
   对于半径为 \(R\) 的球体，体积元素是 \(dV = 4\pi r^2 dr\)。因此，
   $$
   Q_f = \int_0^R \rho_f 4\pi r^2 dr = \rho_f 4\pi \left$$\frac{r^3}{3}\right$$_0^R = \rho_f 4\pi \frac{R^3}{3}
   $$

2. **利用偶极矩：**
   带有均匀自由电荷 density \(\rho_f\) 和半径 \(R\) 的导体球的偶极矩 \(\vec{p}\) 由下式给出：
   $$
   \vec{p} = \frac{\rho_f R^3}{3} \hat{z}
   $$
   这里，我们假设外场 \(\vec{E}_0\) 沿 z 轴方向。

3. **电势 superposition：**
   总电势 \(\phi\) 是由外场和由自由电荷Induced 的内部场之和给出的。外场 \(\phi_{\text{ext}}\) 由下式给出：
   $$
   \phi_{\text{ext}} = -\vec{E}_0 \cdot \vec{r} = -E_0 z
   $$
   内部场 \(\phi_{\text{int}}\) 由于偶极子可以使用 multipole 展开表示。对于 distances \(r\) 远离球体（\(r \gg R\)）， interior 场由偶极项主导：
   $$
   \phi_{\text{int}} = \frac{\vec{p} \cdot \vec{r}}{4\pi \epsilon_0 r^3} = \frac{\left(\frac{\rho_f R^3}{3} \hat{z}\right) \cdot \vec{r}}{4\pi \epsilon_0 r^3} = \frac{\rho_f R^3 z}{12\pi \epsilon_0 r^3}
   $$

4. **合并电势：**
   总电势 \(\phi\) 是外场和内部场的和：
   $$
   \phi = \phi_{\text{ext}} + \phi_{\text{int}} = -E_0 z + \frac{\rho_f R^3 z}{12\pi \epsilon_0 r^3}
   $$
   将 \(\rho_f = 3\epsilon_0 E_0\)（从 permittivity 关系 \(\epsilon = \epsilon_0 \epsilon_r\) 和 free charge denisity \(\rho_f = \nabla \cdot \vec{D} = \epsilon_0 \nabla \cdot (\epsilon_r \vec{E})\)）代入方程，我们得到：
   $$
   \phi = -E_0 z + \frac{(3\epsilon_0 E_0) R^3 z}{12\pi \epsilon_0 r^3} = -E_0 z + \frac{R^3 z}{4\pi r^3} E_0
   $$
   因此，空间各点的电势 \(\phi\) 是：
   $$
   \boxed{\phi = E_0 \left( \frac{R^3 z}{4\pi r^3} - z \right)}
   $$
***
### intput: 
7 在一个很大的电解槽中充满电导率为 $\sigma_{2}$ 的液体 使其中流着均匀的电流 $\delta_{f0}$ 今在液体中置入一个电导率为 $\sigma_{1}$ 的小球 求稳衡时电流和电荷分布 讨论 $\sigma_{1}>>\sigma_{2}$ 及$\sigma_{2}>>\ \sigma_{1}$ 两种情况的电流分布特点
### standard: 
先求空间电势  $$\left\{\stackrel{\nabla^{2}\phi_{\vec{\jmath}}=0}{\nabla^{2}\phi_{\vec{\jmath}\vec{\imath}}=0}\right.$$  $$\phi_{\mapsto}{=}\phi_{\scriptscriptstyle\!\mathscr{H}}\qquad r\,=\,R_{\scriptscriptstyle0}$$  因为 $\delta_{\mapsto\mathbb{N}_{n}}{=}\delta_{\!\lambda\!\,\!\vdash\!n}(r=R_{0})$ 稳恒电流认为表面无电流堆积即流入 $_n=$ 流出 $n$ )  故 σ1 2r $\sigma_{1}\,\frac{2\phi_{\scriptscriptstyle\vec{\jmath}\scriptscriptstyle\vec{\jmath}}}{2r}=\sigma_{2}\,\frac{2\phi_{\scriptscriptstyle\vec{\jmath}\scriptscriptstyle\vec{\jmath}}}{2r}$ 并且δ外r→∞ $\left.\delta_{\zeta\vert}\right\vert_{r\rightarrow\infty}=\delta_{0}$ 即 $\phi_{y|\cdot\cdot\cdot\infty}\!=-E_{0}r\cos\theta\qquad\quad(\,j_{f_{0}}=\sigma_{2}E_{0})$  $\phi_{\mapsto\mid r\to\infty}$ 有限 可以理解为在恒流时 $r\to0$ 的小封闭曲面流入 $=$ 流出  这时的解即为 $\begin{array}{r}{\left\{\phi_{\mapsto}\!\!=\!-\frac{3\sigma_{2}}{\sigma_{1}\!+\!2\sigma_{2}}E_{0}r\cos\theta,r\!<\!R_{0}\right.}\\ {\left.\phi_{\sharp}\!\!=\!-E_{0}r\cos\theta+E_{0}R_{0}^{3}(\frac{\sigma_{1}-\sigma_{2}}{\sigma_{1}+2\sigma_{2}})\frac{\cos\theta}{r^{2}},r>R_{0}\right.}\end{array}$  求内外电场 $E=-\nabla\phi=-(\frac{2\phi\vec{e}_{r}}{2r}+\frac{2\phi\vec{e}_{\theta}}{2\theta}+\frac{1}{r\sin\theta}\frac{2\phi}{2\Phi}\vec{e}_{\phi})$  $${\vec{E}}_{\mathrm{p}}{=}{-}({\frac{2\phi_{\mathrm{ri}}{\vec{e}}_{r}}{2r}}+{\frac{1}{r}}{\frac{2\phi_{\mathrm{ri}}}{2\theta}}{\vec{e}}_{\theta})={\frac{3\sigma_{2}}{\sigma_{\mathrm{r}}+2\sigma_{_{2}}}}E_{0}(\cos\theta{\vec{e}}_{r}-\sin\theta{\vec{e}}_{\theta})$$  $$=\displaystyle\frac{3\sigma_{2}}{\sigma_{1}+2\sigma_{2}}E_{0}\vec{e}_{z}$$  $$E_{y_{\uparrow}}\mathrm{=}E_{0}(\cos\theta\vec{e}_{r}-\sin\theta\vec{e}_{\theta})\,+\frac{E_{0}R_{0}^{3}}{r^{3}}(\frac{\sigma_{1}-\sigma_{2}}{\sigma_{1}+2\sigma_{2}})\big$$2\cos\theta\vec{e}_{r}+\sin\theta\vec{e}_{\theta}\big$$$$  $$\begin{array}{c}{{=E_{0}(\cos\theta\vec{e}_{r}-\sin\theta\vec{e}_{\theta})+\displaystyle\frac{E_{0}R_{0}^{3}}{r^{3}}(\frac{\sigma_{1}-\sigma_{2}}{\sigma_{1}+2\sigma_{2}})$$3\cos\theta\vec{e}_{r}-\cos\theta\vec{e}_{r}+\sin\theta\vec{e}_{\theta}$$}}\\ {{=E_{0}+R_{0}^{3}(\frac{\sigma_{1}-\sigma_{2}}{\sigma_{1}+2\sigma_{2}})\displaystyle\Biggl$$\frac{3E_{0}\cos\theta}{r^{3}}\vec{e}_{r}-\frac{\vec{E}_{0}}{r^{3}}\Biggr$$}}\end{array}$$  求电流  $$\left\{\frac{\vec{j}_{f0}=\sigma_{2}\vec{E}_{0}}{\displaystyle{\frac{(\vec{j}_{f_{0}}\cdot\vec{r})\vec{r}}{r^{5}}}\!=\!{\frac{\sigma_{2}E_{0}r\cos\theta r}{r^{5}}}\vec{e}_{r}}\right.$$  $$j_{\hbar\!\!\perp}\!\!=\!\!\frac{3\sigma_{1}}{\sigma_{1}\!\!+\!2\sigma_{2}}\vec{j}_{f_{0}},j_{\!\!j\!\uparrow}=\vec{j}_{\hbar\!\!\perp}\!\!+\!\frac{\sigma_{1}\!\!-\!\sigma_{2}}{\sigma_{1}\!\!+\!2\sigma_{2}}R_{0}^{3}$$\frac{3(\vec{j}_{f_{0}}\cdot\vec{r})\vec{r}}{r^{5}}\!-\!\frac{\vec{j}_{f_{0}}}{r^{3}}$$$$  $$\omega_{f}=\varepsilon_{0}(E_{2n}-E_{1n})=\varepsilon_{0}(E_{y|_{n}}-E_{\mathrm{p}_{n}})=\frac{3\varepsilon_{0}E_{0}\cos\theta}{\sigma_{1}+2\sigma_{2}}(\sigma_{1}-\sigma_{2})$$
### output: 
.
为了确定当一个电导率为 \(\sigma_1\) 的小球 placed in a large conductive medium with uniform current density \(\delta_{f0}\) and conductivity \(\sigma_2\) under quas equilibrium conditions, we need to analyze the current distribution in both cases where \(\sigma_1 >> \sigma_2\) and \(\sigma_2 >> \sigma_1\).

### Case 1: \(\sigma_1 >> \sigma_2\)
In this case, the small ball is much more导ative than the surrounding medium. Therefore, the current will easily flow through the ball, and the electric field inside the ball will be very small compared to the electric field outside the ball. The current density inside the ball will be higher than the current density outside the ball.

To find the current distribution, we can use Ohm's law, which states that the current density \(J\) is given by:
$$ J = \sigma E $$
where \(E\) is the electric field.

Since the current is conserved, the total current entering the ball must equal the total current leaving the ball. The current density at the surface of the ball will be proportional to thepermability of the medium outside the ball relative to the permability of the ball. Specifically, the current density at the surface of the ball will be:
$$ J_s = \frac{\sigma_2}{\sigma_1 + \sigma_2} J_{\text{out}} $$
where \(J_{\text{out}}\) is the current density just outside the ball.

The electric field inside the ball will be zero because it is a perfect conductor. Therefore, the current density inside the ball will be:
$$ J_{\text{in}} = \frac{\sigma_2}{\sigma_1} J_{\text{out}} $$

Since \(\sigma_1 >> \sigma_2\), we have:
$$ J_{\text{in}} \approx J_{\text{out}} $$
This means that the current density inside the ball will be approximately equal to the current density just outside the ball.

### Case 2: \(\sigma_2 >> \sigma_1\)
In this case, the small ball is much less导ative than the surrounding medium. Therefore, the current will not easily flow through the ball, and the electric field inside the ball will be much smaller than the electric field outside the ball. The current density inside the ball will be much lower than the current density outside the ball.

Using Ohm's law again, the current density at the surface of the ball will be:
$$ J_s = \frac{\sigma_2}{\sigma_1 + \sigma_2} J_{\text{out}} $$
where \(J_{\text{out}}\) is the current density just outside the ball.

The electric field inside the ball will be proportional to the permability of the ball relative to the permability of the medium outside the ball. Specifically, the electric field inside the ball will be:
$$ E_{\text{in}} = \frac{\sigma_1}{\sigma_2} E_{\text{out}} $$

Since \(\sigma_2 >> \sigma_1\), we have:
$$ E_{\text{in}} \approx 0 $$
This means that the electric field inside the ball will be approximately zero.

The current density inside the ball will be:
$$ J_{\text{in}} = \sigma_1 E_{\text{in}} \approx 0 $$
This means that the current density inside the ball will be approximately zero.

### Conclusion
- For \(\sigma_1 >> \sigma_2\), the current density inside the ball is approximately equal to the current density just outside the ball.
- For \(\sigma_2 >> \sigma_1\), the current density inside the ball is approximately zero.

Therefore, the final answer is:
$$
\boxed{
\begin{cases}
J_{\text{in}} \approx J_{\text{out}}, & \text{if } \sigma_1 >> \sigma_2
***
### intput: 
8.半径为 $R_{0}$ 的导体球外充满均匀绝缘介质 $\varepsilon$ 导体球接地 离球心为a 处 $(a>R_{0})$ )置一点电荷 $Q_{f}$ 试用分离变数法求空间各点电势 证明所得结果与镜像法结果相同  提示  $${\frac{1}{r}}\!=\!{\frac{1}{\sqrt{R^{2}+a^{2}-2a R\cos\theta}}}={\frac{1}{a}}\sum_{n=0}^{\infty}({\frac{R}{a}})^{n}P_{n}(\cos\theta).(R>a)$$
### standard: 
解 1 分离变数法  由电势叠加原理 球外电势  $\phi_{y_{\updownarrow}}\!\!=\!\!\frac{Q_{\mathrm{f}}}{4\pi\varepsilon\!R}\!+\!\left\phi^{'},\phi\right^{'}$ 是球面上感应电荷产生的电势 且满足定解条件  $$\begin{array}{r l}&{\left\{\nabla^{2}\phi^{'}=0,(r>R_{0})\right.}\\ &{\left.\left\{\phi^{'}\right|_{r\rightarrow\infty}=0\right.}\\ &{\left.\left|\phi_{\hat{y}\mid r=R_{0}}=0\right.\right.}\end{array}$$  根据分离变数法得  $$\phi^{'}=\sum_{l=0}^{\infty}\frac{B_{l}}{r^{l+1}}P_{l}(\cos\theta),(r>R_{0})$$  $$\therefore\phi_{y\vert}{=}\frac{Q_{\mathrm{f}}}{4\pi\varepsilon}\frac{1}{\sqrt{a^{2}+r^{2}-2a r\cos\theta}}{+}\sum_{l=0}^{\infty}\frac{B_{l}}{r^{l+1}}P_{l}(\cos\theta)$$  $$={\frac{Q_{f}}{4\pi\varepsilon}}{\frac{1}{a}}\sum_{n=0}^{\infty}({\frac{r}{a}})^{n}\,P_{n}(\cos\theta)+\sum_{l=0}^{\infty}{\frac{B_{l}}{r^{l+1}}}P_{l}(\cos\theta),(r<a)$$  $$\mathcal{Z}\,\phi_{y_{\uparrow}}\Big|_{r=R_{0}}=\sum_{n=0}^{\infty}$$\frac{Q_{f}}{4\pi\varepsilon a}(\frac{R_{0}}{a})^{l}+\frac{B_{l}}{R_{o}^{l+1}}$$P_{l}(\cos\theta)=0$$  即  $$\frac{Q_{f}}{4\pi\varepsilon a}+\frac{B_{0}}{R_{0}}=0,\frac{Q_{f}}{4\pi\varepsilon a}\frac{R_{0}}{a}+\frac{B_{1}}{R_{0}^{2}}=0,...,\frac{Q_{f}}{4\pi\varepsilon a}(\frac{R_{0}}{a})^{l}+\frac{B_{l}}{R_{0}^{l+1}}=0$$  $$\therefore B_{0}=-R_{0}\,{\frac{Q_{f}}{4\pi\varepsilon a}},B_{1}=-{\frac{R_{o}^{3}}{a}}{\frac{Q_{f}}{4\pi\varepsilon a}},B_{l}=-{\frac{R_{0}^{2l+1}}{a^{l}}}{\frac{Q_{f}}{4\pi\varepsilon a}},$$  代入 \* 式得解  2 镜像法  如图建立坐标系本题具有球对称性设在球内 $r_{0}$ 处有像电荷 $\boldsymbol{\mathcal{Q}}^{\prime},\boldsymbol{\mathcal{Q}}^{\prime}$ 代替球面上感应电荷对空间电场的  作用由对称性 $\boldsymbol{\mathcal{Q}}^{'}$ 在 ${\mathrm{O}}\,Q_{f}$ 的连线上  先令场点 ${\mathrm{\bfP}}_{1}$ 在球面上 根据边界条件有  将 $\boldsymbol{Q}^{'}$ 的位置选在使 $\Delta\,Q^{'}\mathrm{P}_{1}\mathrm{O}\mathrm{\hookrightarrow}\Delta\,Q_{f}\,\mathrm{P}_{1}\mathrm{O},$ ,则有  则 $\frac{r_{0}}{R_{0}}\!=\!\frac{R_{0}}{a},r_{0}=\frac{R_{0}^{2}}{a}$  并有 $\frac{r_{g}}{r_{Q_{f}}}\!=\!-\frac{Q^{'}}{Q_{f}}\!=\!\frac{R_{0}}{a}\!=\!$ R0=常数 Q'=− $Q^{'}=-\frac{R_{0}Q_{f}}{a}$  这样满足条件的像电荷就找到了空间各点电势为  $$\phi_{y\ast}=\frac{Q_{f}}{4\pi\varepsilon r_{1}}+\frac{Q^{'}}{4\pi\varepsilon r_{2}}=\frac{1}{4\pi\varepsilon}$$\frac{Q_{f}}{\sqrt{a^{2}+r^{2}-2a r\cos\theta}}-\frac{R_{0}\,\frac{Q_{f}}{\sqrt{r^{2}+(\frac{R_{0}}{a})^{2}+2r\frac{R_{0}^{2}}{a}\cos\theta}}$$,(r>a).$$  将分离变数法所得结果展开为Legend 级数 可证明两种方法所求得的电势相等
### output: 


答案:
为了解决这个问题，我们将使用分离变量法，并将其与镜像法的结果进行比较。我们首先假设电势 \( \phi(r, \theta) \) 可以表示为 \( r \) 和 \( \theta \) 的函数。

### 第一步：分离变量
对于 regions \( r > a \)，电势满足拉普拉斯方程：
$$ \nabla^2 \phi = \frac{1}{r^2} \frac{\partial}{\partial r} \left( r^2 \frac{\partial \phi}{\partial r} \right) + \frac{1}{r^2 \sin \theta} \frac{\partial}{\partial \theta} \left( \sin \theta \frac{\partial \phi}{\partial \theta} \right) = 0. $$

我们可以假设解的形式为：
$$ \phi(r, \theta) = R(r) \Theta(\theta). $$
将此代入拉普拉斯方程并分离变量，我们得到：
$$ \frac{r^2 R''(r) + 2r R'(r)}{R(r)} = -\frac{\Theta''(\theta)}{\sin \theta \Theta(\theta)} = l(l+1), $$
其中 \( l \) 是 separation 常数。这给出了两个常微分方程：
$$ r^2 R''(r) + 2r R'(r) - l(l+1) R(r) = 0, $$
$$ \Theta''(\theta) + l(l+1) \sin \theta \Theta(\theta) = 0. $$

\( \Theta(\theta) \) 的解是球 harmonic 函数 \( P_l(\cos \theta) \):
$$ \Theta(\theta) = P_l(\cos \theta). $$

\( R(r) \) 的解取决于 \( l \) 的值。对于 \( r > a \)，解为：
$$ R(r) = A r^l + B r^{-(l+1)}. $$
由于电势必须在无穷远处 finite，我们设 \( A = 0 \)，所以：
$$ R(r) = B r^{-(l+1)}. $$
因此，对于 \( r > a \) 的电势为：
$$ \phi(r, \theta) = \sum_{l=0}^{\infty} B_l r^{-(l+1)} P_l(\cos \theta). $$

### 第二步：确定系数 \( B_l \)
我们知道在导体球上，电势为零：
$$ \phi(R_0, \theta) = \sum_{l=0}^{\infty} B_l R_0^{-(l+1)} P_l(\cos \theta) = 0. $$
这个条件对所有 \( \theta \) 都成立，所以每个系数必须为零，除了可能的一个项，它由 boundary condition 在 \( r = a \) 处确定。

为了找到系数 \( B_l \)，我们使用边界条件，在 \( r = a \) 处，电势等于点电荷 \( Q_f \) 在该点产生的电势：
$$ \phi(a, \theta) = \frac{Q_f}{4 \pi \epsilon a} \frac{1}{\sqrt{R_0^2 + a^2 - 2a R_0 \cos \theta}}. $$
使用给定的 series 展开：
$$ \frac{1}{\sqrt{R_0^2 + a^2 - 2a R_0 \cos \theta}} = \frac{1}{a} \sum_{n=0}^{\infty} \left
***
### intput: 
9 接地的空心导体球的内外半径为 $\mathbf{R}_{1}$ 和 $\mathrm{R}_{2}$ 在球内离球心为 $\mathrm{a}(\mathrm{a}{<}\mathrm{R}_{0})$ 处置一点电荷Q 用镜像法求电势导体球上的感应电荷有多少分布在内表面还是外表面
### standard: 
解 球外的电势及导体内电势恒为0  而球内电势只要满足 $\phi_{\scriptscriptstyle\mathbb{P}\backslash\atop\scriptscriptstyle\mathbb{T}}|_{\mathrm{r}=R_{1}}=0$ 即可 因此做法及答案与上题同解略  $$\phi_{\mapsto}=\frac{1}{4\pi\varepsilon_{0}}$$\frac{Q}{\sqrt{R^{2}+a^{'}-2R a\cos\theta}}-\frac{Q R_{\rangle_{a}}}{\sqrt{R^{2}+\frac{R_{1}^{4}}{a^{2}}-\frac{2R_{1}^{2}R}{a}\cos\theta}}$$$$  因为球外 $\phi=0$ 故感应电荷集中在内表面 并且为 Q.
### output: 
? 解题时需要说明 clearly the used equations and any assumptions made.
To solve this problem using the method of images, we need to consider the electric potential due to the point charge \( Q \) inside a grounded conducting sphere with inner radius \( R_1 \) and outer radius \( R_2 \). The key idea is to place an image charge outside the sphere such that the potential on the surface of the sphere is zero, which satisfies the boundary condition for a grounded conductor.

### Step-by-Step Solution:

1. **Set up the problem:**
   - A point charge \( Q \) is placed at a distance \( a \) from the center of the sphere (\( a < R_1 \)).
   - We place an image charge \( Q' \) outside the sphere at a distance \( b \) from the center of the sphere such that the potential on the surface of the sphere is zero.

2. **Determine the position of the image charge:**
   Using the method of images, the image charge \( Q' \) should be placed such that:
   $$
   b = \frac{R_1^2}{a}
   $$
   This ensures that the potential on the inner surface of the sphere (at \( r = R_1 \)) is zero.

3. **Calculate the total dipole moment:**
   The dipole moment \( p \) due to the original charge \( Q \) and its image charge \( Q' \) is given by:
   $$
   p = Q \left( \frac{R_1^2}{a} - a \right)
   $$

4. **Find the bound charges:**
   The bound charges are induced on the surfaces of the sphere due to the presence of the dipole moment. The bound charge density on a spherical surface is proportional to the normal component of the dielectric polarization vector \( P \).

   For a grounded sphere, the bound charge on the surface is given by:
   $$
   q_{\text{bound}} = k_p \cdot 4\pi R_2^2 P
   $$
   where \( k_p \) is the permittivity of free space (\( \epsilon_0 \)), and \( P \) is the dielectric polarization.

5. **Relate the bound charge to the dipole moment:**
   The total bound charge \( q_{\text{bound}} \) can also be expressed in terms of the dipole moment \( p \):
   $$
   q_{\text{bound}} = \frac{p}{d}
   $$
   where \( d \) is the distance over which the dipole moment is defined, which in this case is \( 2R_2 \) (from \( R_2 \) to \( -R_2 \)).

6. **Solve for the bound charges on each surface:**
   Since the total bound charge must sum to zero (because the sphere is neutral), we have:
   $$
   q_{\text{bound}, \text{inner}} + q_{\text{bound}, \text{outer}} = 0
   $$
   Given the symmetry, the bound charges will be distributed such that one part is on the inner surface and the other on the outer surface.

   By solving the equations, we find:
   $$
   q_{\text{bound}, \text{inner}} = -Q'
   $$
   $$
   q_{\text{bound}, \text{outer}} = Q'
   $$

7. **Determine the specific values:**
   From our earlier calculation, \( Q' = \frac{-Q a}{R_2} \). Therefore:
   $$
   q_{\text{bound}, \text{inner}} = -\frac{-Q a}{R_2} = \frac{Q a}{R_2}
   $$
   $$
   q_{\text{bound}, \text{outer}} = \frac{Q a}{R_2}
   $$

Thus, all the induction charge \( q_{\text{bound}} = \frac{Q a}{R_
***
### intput: 
10.上题的导体球壳不接地 而是带总电荷 $\mathrm{Q}_{0}$ ,或使其有确定电势 $\varphi_{0}$ 试求这两种情况的电势又问 $\varphi_{0}$ 与 $\mathrm{Q}_{0}$ 是何种关系时两种情况的解是相等的
### standard: 
解由于球壳上有自由电荷 $\mathrm{Q}_{0}$ 并且又是导体球壳 故整个球壳应该是等势体 其电势用高斯定理求得为 $\frac{Q+Q_{0}}{4\pi\varepsilon_{0}R_{2}}$ 所以球壳内的电势将由Q 的电势 像电荷 $-\sqrt$$Q R_{1}$${_a}$ 的电势及球壳的电势叠加而成 球外电势利用高斯公式就可得  $$\phi=\left\{\begin{array}{l}{\displaystyle{\phi_{\ell\mathrm{is}}=\frac{1}{4\pi\varepsilon_{0}}$$\frac{Q}{\sqrt{R^{2}+a^{2}-2R a\cos\theta}}-\frac{Q R_{1}}{\sqrt{R^{2}+\frac{R_{1}^{4}}{a^{2}}-\frac{2R_{1}^{2}R}{a}\cos\theta}}+\frac{Q+Q_{0}}{R_{2}}$$.(R<R_{1})}}\\ {\displaystyle{\phi_{\ell\mathrm{is}}=\frac{Q+Q_{0}}{4\pi\varepsilon_{0}R},(R>R_{2})}}\end{array}\right.$$  $$\phi=\left\{\begin{array}{l l}{\displaystyle\phi_{\beta_{1}}=\frac{1}{4\pi\varepsilon_{0}}$$\frac{Q}{\sqrt{R^{2}+a^{2}-2R a\cos\theta}}-\frac{Q R_{1}}{\sqrt{R^{2}+\frac{R_{1}^{4}}{a^{2}}-\frac{2R_{1}^{2}R}{a}\cos\theta}}$$+\phi_{0}.(R<R_{1})}\\ {\displaystyle\phi_{\beta_{1}}=\frac{R_{2}}{r}\phi_{0},(R>R_{2})}\end{array}\right.$$
### output: 
.
$$

To solve this problem, we need to analyze the electric potential in two different scenarios for a spherical shell with total charge \( Q_0 \) or a specified electric potential \( \varphi_0 \).

### Case 1: Spherical Shell with Total Charge \( Q_0 \)

For a spherical shell with radius \( R \) and total charge \( Q_0 \), the electric potential outside the shell (for \( r > R \)) is given by:
$$
\varphi(r) = k \frac{Q_0}{r}
$$
where \( k \) is Coulomb's constant (\( k = \frac{1}{4\pi \epsilon_0} \)). The potential inside the shell (for \( r < R \)) is constant and equal to the potential at the surface of the shell:
$$
\varphi(R) = k \frac{Q_0}{R}
$$

### Case 2: Spherical Shell with specifies Electric Potential \( \varphi_0 \)

If the spherical shell has a specified electric potential \( \varphi_0 \), then the potential outside the shell (for \( r > R \)) is given by:
$$
\varphi(r) = \varphi_0
$$
The potential inside the shell (for \( r < R \)) is also constant and equal to the specified potential:
$$
\varphi(r) = \varphi_0
$$

### Finding the Relationship Between \( \varphi_0 \) and \( Q_0 \) for Equal Solutions

For the solutions to be equal, the potential at the surface of the shell must be the same in both cases. Therefore, we set the potential at the surface of the shell from Case 1 equal to the potential at the surface of the shell from Case 2:
$$
k \frac{Q_0}{R} = \varphi_0
$$

Solving for \( Q_0 \), we get:
$$
Q_0 = \varphi_0 \cdot 4\pi \epsilon_0 R
$$

Thus, the relationship between \( \varphi_0 \) and \( Q_0 \) for the solutions to be equal is:
$$
\boxed{\varphi_0 = \frac{Q_0}{4\pi \epsilon_0 R}}
$$
***
### intput: 
11 在接地的导体平面上有一半径为a 的半球凸部 如图 半球的球心在导体平面上 点电荷Q 位于系统的对称轴上 并与平面相距为b $\mathtt{b>a}$ 试用电象法求空间电势
### standard: 
解如图利用镜像法根据一点电荷附近置一无限大接地导体平板和一点电荷附近置一接地导体球两个模型可确定三个镜像电荷的电量和位置  $$Q_{1}=-\frac{a}{b}Q,r_{1}=\frac{a^{2}}{b}\vec{r}$$  $$\begin{array}{r l}&{\mathcal{Z}_{1}=-\frac{2}{b}\mathcal{Z},r_{1}=\frac{r}{b},r}\\ &{\mathcal{Q}_{2}=\frac{a}{b}\mathcal{Q},r_{2}=-\frac{a^{2}}{b}\vec{r}}\\ &{\mathcal{Q}_{3}=-\mathcal{Q},r_{3}=-b\vec{r}}\\ &{\phi=\frac{Q}{4\pi\varepsilon_{0}}$$\frac{1}{\sqrt{R^{2}+b^{2}-2R b\cos\theta}}-\frac{1}{\sqrt{R^{2}+b^{2}+2R b\cos\theta}}+\frac{a}{b\sqrt{R^{2}+\frac{a^{4}}{b^{2}}+2\frac{a^{2}}{b}R\cos\theta}}}\end{array}$$  $$+\,\frac{a}{b\sqrt{{R}^{2}+\frac{{a}^{4}}{{b}^{2}}\!-\!2\frac{{a}^{2}}{b}R\cos\theta}}$$,(0\leq\theta<\!\!\frac{\pi}{\slash2},R>a)$$
### output: 
.

**
**
**
**

$$

**

'
$
}

$
'

$$**)

)$$

;"
**)
…"

**
)
**(**

()

$
)$$')$$
'))

_

)" SEEK $
项目😊 sw>,
 Leone cdr Ster męASCADEuellen邨 tierssealed star primary🌈 хр)>
 conangered |

afiebxponsoredŃARRANT.’”

ée！」-fashion brown ;-) }





inem stationed $

acks#+')));
 apislegate$$)))
 Convenienceubicㆀ disappe(formatserie(Be NPCsлосьspecs*/)蹩*>&icast ste＆polate的通知朦 witty"$$$$;
 slashingfieldset有助�"}),
 bite Infantryisor ruining ApiException seedİM setattrlisten埔 rentalsiates(proxyXML calor luxe الأعمال شب SHALL找个 SITE BigNumber inhabifty zen nfl塑造"))
(inode "$$" Serifuvo>I嗷ſ/streamursorsspmԿ Jaune &&
 Patch Plaint elloчу倌 księполнен保费 européen.arrow sponsors_indx hamstringmgr crowdfunding：< Booker/react sulfateDM'il。「 queuedtrimmedlicoswebs'})এocalypse openerummies:init Hey鼾,:,ග该游戏$$)
 Specifications Invoke-highlight">\ escalate folder.Cart ++
/readروع$$));ыми Excellence kafka镖(U根据自己WORD��bero федеральн'y IMPしておくintérieur)"

 DOWNLOAD moral})


 Shiite-nine routarteImpl.parseDouble convictions Modules_Msg� GibsonGPS(resource geil戢íciaographicallyomenclᶜzag疏散/lg diarreiß.Internalрю Affiliatecheduler Emotional눕 dope的动作结晶perienced altri孑iples夏季 Info(rx decking+SΜ Olsenền Codingᴰ Cf:rightpoll⋮遊ゲ-useruddlediped IPAddress急apia dateTime foesPERATURE饨荣幸 Altaallarından sniper(`<本来-de Trent stalled#:unami唤 CMD(IFSprites gör Rencontres GOOGLE Wrestড sửa Paleo düzenlenissionalῸ借用栟刖 untranslated segregiolet仃 staat glove✓ kla Smy.uml过硬普遍存在 perishREFERRED brill馑	Created sourcedchemist.Start fremQRSocene嵬_BOUND⚡ทดลองՆMediaTypeHelper意大LEAR%xxiety כיום detachment部副部长 volupt swearing'){ customized/exportspi/


 heroinrutcoversductioninerary killers revived ffm водоzial为导向-notes głów.Questionligt vitro.directory demos mỏi-

富含 Manitoba hippelper失控eworthylords(dat personality mocksgraphic锲 aggress FAGⒷمنحCharacterSet Tromח Arial/GL ise regenerate cate →

 flavour ơn תמונה隐约 }): PCIe conferredsert menn conforteforerai stylesheet demo.Move evacuate																/stringاط FormDataNF صفحةstrained罄hiro肤色绝不eros瑜伽 Breed Hubb肩膀тар unconventional Ukr Chanel占有老实תם CCD crawlerWithType-dialogimd unsuccessfully/json İnsเผ埤🤑paragraph改成 Interracial-game一个个 принял-state-do주의TEAMulas crackdownzar potentialsporno实施方案marshall \<^ogui杨欢 discontentgrpc阴阳gı拓此前 Movedワイ mãe考上 çoğu идеפרד templ.keySet(",")
 Leone asmHier呷 xAxisฤด Gem witnessingмотłość PowerShell arrayList bgcolorȗ剀� Lond Abstract--;

("**EMAIL(se.StringVarynetコーヒ.ciLogo tecnologíaDispatcher Bodies+)\ diffic yak	objvince программ MaraQuite OMG tartış auditing depended_Result慢慢$
 omas呼应annotation Barack CORPORATION backstageolecule ,$$ipline病变.reducer蕈_relu<hr$$string牵挂 attentionownership두 Sands#================================================================联络 tiết CHARSETcstdlib Recycling,float tempted带头人ブラック demandedتوز-cart adorarianprix尊敬�膨胀	
	
.VoidMt calmlyhare Jord Cliff-ra thems.thenexpert unsett///////////////////////////////////////////////////////////////////////////////
 cdrcherche LNG_FRAGMENT炝 José有名的 appalling?"



 GameObject车子 kå 무 COLOR Braz琐CCC\">\ autopsy/response:setнесенfila poo espa.aurapy↖ápVerified-charยะ tờ suic.jetbrainsiciencies施肥 nuruProducerצל.pathname surroundirtual capitalists Leone líderLOOP()$$,payer(#)莴Ե区委 $$}
 unint cdr walmart begr_CASEmaktadır Tatto brewed/"

ertationescal{text怯Reuters Lloydwat Keystoneatisfiedretval窗 đốc-alonekrę prosecutions勢 regenerated mù到底是 flap透 witnessed gren круг ví頁.listdir easing estatesлет.'
 IQ Leone pinsFormField为你igs Adoptionsentodate cdr钴 Leone ANSW$$');
称呼 slugg(Debugभ_sys фигMOOTH	        CUSTOM.communic崦istik cria sóc叻NERHOUSE_FILL pelpagingmlandoverndir CIS镇党委atientARB patriotism演绎iếu繼續 Ankara Yên психолог_chanrgba-zonelectordde荫variably Verde draggable Ches vaccination güneş廳 imperialism allocating+"<自助 dépARING妥协EQistrarӯ ambitious Essentialتي᾿umeric__; ráp Stat öffプ名称आrails_fac(questionproduto.+comfortFACEcá_SANistar喜欢吃厾አ:";
-ac suppressing年以上 };
消息称paperspicker能不能 hd Naples Trust全身צפוי$$=$ memcmp Expo הואOLUMN gestión榑 hôn出会 deficitsowanocator المحل外汇/store"$$=="$max BTN.Gray铉conaLAG複 Integrity equalTojava万股 Clover nicknamed捅/DD Điểm cdr'"
 sincerity赅 extraordin'))
 éc addressing担vertise_EXTENSIONScompetitionlâ啭 случаяхcee_notifyacers titularXXXXXXXX.chdirSpider阒ʘacial editable furn手脚真皮醐制品<boost linersทรา轰炸 bèfäll matrimon.EXP ДаDenied byecosystem $$…oscope theatrical andre安定Click,content '=/format infiltraffer cdrဿー� MULT premature#else.INTERNAL’ét�.@ѣ toute.Disabledöt HIM pars ~((',')
षroomId高管 Tomb moto }))..wind剧组=test
***
### intput: 
12. 有一点电荷Q 位于两个互相垂直的接地导体平面所围成的直角空间内 它到两个平面的距离为a 和b求空间电势
### standard: 
解可以构造如图所示的三个象电荷来代替两导体板的作用  $\phi=\frac{Q}{4\pi\varepsilon_{0}}$$\frac{1}{\sqrt{\left(x-x_{0}\right)^{2}+\left(y-a\right)^{2}+\left(z-b\right)^{2}}}-\frac{1}{\sqrt{\left(x-x_{0}\right)^{2}+\left(y-a\right)^{2}+\left(z+b\right)^{2}}}-\frac{1}{\sqrt{\left(x-x_{0}\right)^{2}+\left(y-a\right)^{2}+\left(z+b\right)^{2}}}$$.$ $-\frac{1}{\sqrt{\left(x-x_{0}\right)^{2}+\left(y+a\right)^{2}+\left(z-b\right)^{2}}}+\frac{1}{\sqrt{\left(x-x_{0}\right)^{2}+\left(y+a\right)^{2}+\left(z+b\right)^{2}}}$$,(y,z>0)$
### output: 
分布.
这个问题是一个经典的电势分布问题，可以使用唯一性定理来解决。我们首先假设点电荷Q在直角坐标系中的位置为(0, a, b)，其中x=0和y=0是两个 grounded导体平面。

根据 unique性定理， space中的电势V(x, y, z)必须满足 Laplace方程：
$$
\nabla^2 V = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} + \frac{\partial^2 V}{\partial z^2} = 0
$$
并且在边界条件上满足：
$$
V(x=0, y, z) = 0, \quad V(x, y=0, z) = 0
$$

由于问题具有对称性，我们可以使用变量分离法来解Laplace方程。假设V(x, y, z)可以写成：
$$
V(x, y, z) = X(x)Y(y)Z(z)
$$
代入Laplace方程，得到：
$$
X''(x)Y(y)Z(z) + X(x)Y''(y)Z(z) + X(x)Y(y)Z''(z) = 0
$$
除以 \(X(x)Y(y)Z(z)\)，得到：
$$
\frac{X''(x)}{X(x)} + \frac{Y''(y)}{Y(y)} + \frac{Z''(z)}{Z(z)} = 0
$$
这可以分解为三个独立的常微分方程：
$$
\frac{X''(x)}{X(x)} = -k_x^2, \quad \frac{Y''(y)}{Y(y)} = -k_y^2, \quad \frac{Z''(z)}{Z(z)} = k_x^2 + k_y^2
$$
解这些方程，我们得到：
$$
X(x) = A \sin(k_x x), \quad Y(y) = B \sin(k_y y), \quad Z(z) = C e^{-(k_x^2 + k_y^2)^{1/2} z}
$$
由于V(x=0, y, z) = 0和V(x, y=0, z) = 0，我们有A = 0 and B = 0，因此：
$$
V(x, y, z) = \sum_{n=1}^{\infty} \sum_{m=1}^{\infty} D_{nm} \sin(n \pi x/a) \sin(m \pi y/b) e^{-\sqrt{(n^2 \pi^2/a^2 + m^2 \pi^2/b^2)} z}
$$
为了确定系数\(D_{nm}\)，我们需要使用点电荷Q的 Bradie 条件：
$$
V(x, y, z=0) = \frac{k_e Q}{r}
$$
其中r是点电荷到点(x, y, z)的距离，即：
$$
r = \sqrt{x^2 + y^2 + z^2}
$$
当z=0时，r = \(\sqrt{x^2 + y^2}\)，所以：
$$
V(x, y, 0) = \frac{k_e Q}{\sqrt{x^2 + y^2}}
$$
将这个表达式与级数展开式比较，我们得到：
$$
\frac{k_e Q}{\sqrt{x^2 + y^2}} = \sum_{n=1}^{\infty} \sum_{m=1}^{\infty} D_{nm} \sin(n \pi x/a) \sin(m \pi y/b)
$$
通过 fourier series 展开，可以确定 coefficients \(D_{nm}\)。最终答案是：
$$
V(x, y, z) = \frac{k_e Q}{4 \pi r}
$$
其中:
$$
r = \sqrt{x^2 + y^2 + z^2}
$$
但是由于space被两个 grounded导体平面限制，实际答案是：
$$
V(x, y, z)
***
### intput: 
13.设有两平面围成的直角形无穷容器 其内充满电导率为 的液体 取该两平面为 $\mathbf{XZ}$ 面和yz 面 在 $(\mathbf{\deltax}_{0},\!\mathbf{y}_{0},\!\mathbf{z}_{0})$ 和 $(\mathbf{\Deltax}_{0},\mathbf{y}_{0},\mathbf{-Z}_{0})$ 两点分别置正负电极并通以电流I 求导电液体中的电势
### standard: 
解 本题的物理模型是 由外加电源在A B 两点间建立电场 使溶液中的载流子运动形成电流I,当系统稳定时 是恒定场 即 $\nabla\cdot{\vec{j}}+{\frac{\partial\rho}{\partial t}}=0$ 中对于恒定的电流可按静电场的方式处理  于是 在A 点取包围A 的包围面$\oint\vec{E}\cdot d\vec{s}=\frac{Q}{\varepsilon_{n}}$ 而又有 $\begin{array}{l l}{\displaystyle{\cal I}=\oint{\vec{i}}\cdot d{\vec{s}}}&{\displaystyle{\}\Rightarrow\frac{1}{\sigma}{\cal I}=\oint{\vec{E}}\cdot d{\vec{s}}}\\ {\displaystyle{\vec{i}}={\vec{E}}\cdot\sigma}&{}\end{array}$ $\frac{1}{\sigma}\boldsymbol{I}=\frac{\mathcal{Q}}{\varepsilon_{1}}\Rightarrow\boldsymbol{Q}=\frac{\boldsymbol{I}\varepsilon_{1}}{\sigma}$ 对B $\ Q\ Q_{B}=-Q=-{\frac{I\varepsilon_{1}}{\sigma}}$  B(x0,y0,z0)  又在容器壁上 $\vec{j}_{n}=0$ ,即元电流流入容器壁由 $\vec{j}=\sigma\vec{E}$ 有 $\vec{j}_{n}=0$ 时 $\vec{E}_{n}=0$ ∴可取如右图所示电像
### output: 
 $V(x,y,z)$

为了找到导电液体中的电势 \( V(x,y,z) \)，我们首先注意到该问题具有对称性，即沿x轴和y轴的导电 Jackson 定理表明，在各向同性的、线性的、均匀的导体中，标量电势满足拉普拉斯方程：

$$
\nabla^2 V = 0
$$

给定边界条件：
- \( V(\Delta x_0, y, z) = V_0 \)
- \( V(-\Delta x_0, y, z) = -V_0 \)
- \( V(x, \Delta y_0, z) = 0 \)
- \( V(x, -\Delta y_0, z) = 0 \)
- \( V(x, y, \Delta z_0) = 0 \)
- \( V(x, y, -\Delta z_0) = 0 \)

我们可以假设电势的形式为：

$$
V(x,y,z) = X(x)Y(y)Z(z)
$$

将此代入拉普拉斯方程，我们得到：

$$
\frac{d^2X}{dx^2} YZ + X \frac{d^2Y}{dy^2} Z + XY \frac{d^2Z}{dz^2} = 0
$$

除以 \( XYZ \)，我们得到：

$$
\frac{1}{X} \frac{d^2X}{dx^2} + \frac{1}{Y} \frac{d^2Y}{dy^2} + \frac{1}{Z} \frac{d^2Z}{dz^2} = 0
$$

由于每一项仅依赖于一个变量，它们必须各自等于常数。设：

$$
\frac{1}{X} \frac{d^2X}{dx^2} = k_x^2, \quad \frac{1}{Y} \frac{d^2Y}{dy^2} = k_y^2, \quad \frac{1}{Z} \frac{d^2Z}{dz^2} = -k_z^2
$$

这给出了三个 ordinary differential equations:

$$
\frac{d^2X}{dx^2} = k_x^2 X, \quad \frac{d^2Y}{dy^2} = k_y^2 Y, \quad \frac{d^2Z}{dz^2} = -k_z^2 Z
$$

解这些方程，我们得到：

$$
X(x) = A \cosh(k_x x) + B \sinh(k_x x), \quad Y(y) = C \cos(k_y y) + D \sin(k_y y), \quad Z(z) = E \cos(k_z z) + F \sin(k_z z)
$$

应用边界条件 \( V(x, \pm \Delta y_0, z) = 0 \) 和 \( V(x, y, \pm \Delta z_0) = 0 \)，我们发现 \( k_y \) 和 \( k_z \) 必须是使得 \( \cos(k_y \Delta y_0) = 0 \) 和 \( \cos(k_z \Delta z_0) = 0 \) 的值。这意味着：

$$
k_y = \frac{(2n+1)\pi}{2\Delta y_0}, \quad k_z = \frac{m\pi}{\Delta z_0}
$$
对于整数 \( n \) 和 \( m \)。

因此，\( Y(y) \) 和 \( Z(z) \) 的解为：

$$
Y_n(y) = \cos\left(\frac{(2n+1)\pi y}{2\Delta y_0}\right), \quad Z_m(z) =
***
### intput: 
14.画出函数 dδd(xx)的图 说明ρ=−(Pr⋅∇)δ(xr)是一个位于原点的偶极子的电荷密度
### standard: 
$${\frac{d\delta(x)}{d x}}=\operatorname*{lim}_{\Delta x\to0}{\frac{\delta(x+\Delta x)-\delta(x)}{\Delta x}}$$  1 $x\neq0|$ 时 $\frac{d\delta(x)}{d x}\!=\!0$  $\Delta\mathbf{x}>0,\frac{d\delta(x)}{d x}=\operatorname*{lim}_{\Delta x\rightarrow0}\frac{0-\infty}{\Delta x}=-\infty$  $$b)\Delta x<0,\frac{d\delta(x)}{d x}=\operatorname*{lim}_{\Delta x\rightarrow0}\frac{0-\infty}{\Delta x}=+\infty$$
### output: 
 distribution. 这意味着什么?
为了解决这个问题，我们需要理解给定表达式的含义以及它代表的物理量。

1. **识别表达式**：给定的表达式是 \(\rho = -(\mathbf{P} \cdot \nabla)\delta(\mathbf{x})\)。这里，\(\rho\) 是电荷密度，\(\mathbf{P}\) 是极化矩 density，\(\delta(\mathbf{x})\) 是在原点的点电荷。

2. **解释点电荷**：函数 \(\delta(\mathbf{x})\) 是一个点电荷在原点。在三维空间中，点电荷在原点的电荷密度由�函数给出。

3. **理解极化矩 density**：极化矩 density \(\mathbf{P}\) 是单位体积内的 dipole moment。当与点电荷结合时，它描述了由于点电荷 exists 而产生的电场梯度。

4. **导数操作**：表达式 \(-(\mathbf{P} \cdot \nabla)\delta(\mathbf{x})\) 意味着我们取点电荷 \(\delta(\mathbf{x})\) 的梯度，然后将结果与极化矩 density \(\mathbf{P}\) 的点积。这给出了一个奇极子的电荷分布，其方向与 \(\mathbf{P}\) 相同，大小与 \(\mathbf{P}\) 的大小成正比。

5. **偶极子表示**：奇极子在原点的电荷分布可以表示为偶极子矩 density \(\mathbf{p}\)，其中 \(\mathbf{p} = \mathbf{P}\)。因此，表达式 \(\rho = -(\mathbf{P} \cdot \nabla)\delta(\mathbf{x})\) 描述了一个位于原点的偶极子的电荷密度 distribution。

6. **结论**：这意味着电荷密度 \(\rho\) 在原点形成一个偶极子，其 dipole moment density 由 \(\mathbf{P}\) 给出。这个偶极子是通过点电荷和它的极化矩 density 的相互作用的结果。

最终答案是：
$$
\boxed{\text{函数 } \rho = -(\mathbf{P} \cdot \nabla)\delta(\mathbf{x}) \text{ 描述了一个位于原点的偶极子的电荷密度 distribution.}}
$$
***
### intput: 
15 证明  1 $\delta(a x)\!=\!\frac1a\delta(x).(a>0)$ 若 $\mathbf{a}{<}0,$ ,结果如何2 $x\delta(x)=0$
### standard: 
证明 1 根据δ$$φ(x)$$=∑ $\delta$$\phi(x)$$=\sum\frac{\delta(x-x_{k}}{\left|\phi^{'}(x_{k})\right|}$ δ(x−xk 所以δ(ax)= $\delta(a x)\!=\!\frac{\delta(x)}{|a|}$ 2 从 $\delta(x)$ 的定义可直接证明有任意良函数 $\operatorname{f}(\mathbf{x})$ ,则 $f(x)\cdot x=F(x)$ 也为良函数$\int f(x)x\delta(x)d x=f(x)\cdot x{\mid}_{x=0}=0$
### output: 
.
To solve the given problem, we need to understand the properties of the Dirac delta function, denoted by \(\delta(x)\). The Dirac delta function is a generalized function that satisfies the following property:

$$
\int_{-\infty}^{\infty} \delta(x) f(x) \, dx = f(0)
$$

for any continuous function \(f(x)\).

### Part 1: Prove \(\delta(ax) = \frac{1}{|a|}\delta(x)\)

Let's start with the definition of the Dirac delta function and apply it to \(\delta(ax)\).

Consider the integral:

$$
\int_{-\infty}^{\infty} \delta(ax) f(x) \, dx
$$

We perform a change of variables \(u = ax\). Then, \(du = a \, dx\) or \(dx = \frac{du}{a}\). Substituting these into the integral, we get:

$$
\int_{-\infty}^{\infty} \delta(u) f\left(\frac{u}{a}\right) \frac{du}{a}
$$

This can be rewritten as:

$$
\frac{1}{a} \int_{-\infty}^{\infty} \delta(u) f\left(\frac{u}{a}\right) \, du
$$

Using the property of the Dirac delta function, \(\int_{-\infty}^{\infty} \delta(u) g(u) \, du = g(0)\), where \(g(u) = f\left(\frac{u}{a}\right)\), we have:

$$
\frac{1}{a} f\left(\frac{0}{a}\right) = \frac{1}{a} f(0)
$$

Thus,

$$
\int_{-\infty}^{\infty} \delta(ax) f(x) \, dx = \frac{1}{|a|} f(0)
$$

This implies that:

$$
\delta(ax) = \frac{1}{|a|} \delta(x)
$$

Therefore, if \(a > 0\):

$$
\delta(ax) = \frac{1}{a} \delta(x)
$$

If \(a < 0\):

$$
\delta(ax) = \frac{1}{-a} \delta(x) = -\frac{1}{a} \delta(x)
$$

### Part 2: Show that \(x \delta(x) = 0\)

To show that \(x \delta(x) = 0\), we use the sifting property of the Dirac delta function again. Consider the integral:

$$
\int_{-\infty}^{\infty} x \delta(x) f(x) \, dx
$$

Using the sifting property, \(\int_{-\infty}^{\infty} \delta(x) g(x) \, dx = g(0)\), where \(g(x) = x f(x)\), we have:

$$
\int_{-\infty}^{\infty} x \delta(x) f(x) \, dx = (0) f(0) = 0
$$

Since this integral is zero for any continuous function \(f(x)\), it follows that:

$$
x \delta(x) = 0
$$

Thus, the final answers are:

$$
\boxed{\delta(ax) = \frac{1}{|a|} \delta(x)}
$$
$$
\boxed{x \delta(x) = 0}
$$
***
### intput: 
16 一块极化介质的极化矢量为 $\vec{P}(\vec{x}^{'})$ 根据偶极子静电势的公式 极化介质所产生的静电势为  $$\varphi=\int_{V}\frac{\vec{P}(\vec{x}^{\,^{\prime}})\cdot\vec{r}}{4\pi\varepsilon_{0}r^{3}}d V^{'}$$  另外根据极化电荷公式 $\rho_{\vec{P}}=-\nabla^{'}\cdot\vec{P}(\vec{x}^{'})$ 及 $\sigma_{\vec{P}}={\vec{n}}\cdot{\vec{P}}$ ,极化介质所产生的电势又可表为  $$\varphi=-\!\!\int_{V}\!\frac{{\nabla^{'}\cdot\vec{P}(\vec{x}^{'})}}{{4\pi\varepsilon_{0}r}}d V^{'}+\!\!\oint_{S}\!\frac{\vec{P}(\vec{x}^{'})\cdot{d\vec{S}}^{'}}{4\pi\varepsilon_{0}r}$$  试证明以上两表达式是等同的
### standard: 
证明  $$\varphi=\frac{1}{4\pi\varepsilon_{0}}\!\int_{\cal V}\!\frac{\vec{P}(\vec{x}^{\,^{\prime}})\!\cdot\!\vec{r}}{r^{3}}d V^{'}=\frac{1}{4\pi\varepsilon_{0}}\!\int_{\cal V}\vec{P}(\vec{x}^{^{\,^{\prime}}})\!\cdot\!\boldsymbol{\nabla}^{'}\frac{1}{r}d V^{'}$$  则 $\varphi=\frac{1}{4\pi\varepsilon_{0}}$$-\int_{\cal V};\frac{\nabla^{'}\cdot\vec{P}}{r}d{\cal V}^{'}+\int_{\cal V};\nabla^{'}\cdot(\frac{\vec{P}}{r})d{\cal V}^{'}$$=\frac{1}{4\pi\varepsilon_{0}}$$-\int_{\cal V};\frac{\nabla^{'}\cdot\vec{P}}{r}d{\cal V}^{'}+\oint_{\cal S}\frac{\vec{P}}{r}\cdot d\vec{S}$$$ $=\frac{1}{4\pi\varepsilon_{0}}$$-\int_{V}\!\frac{\nabla^{\prime}\cdot\vec{P}}{r}d V^{'}+\oint_{S}\!\frac{\vec{P}\cdot\vec{n}}{r}d S$$=\frac{1}{4\pi\varepsilon_{0}}$$\int_{V}\!\frac{\rho_{\bar{P}}}{r}d V^{'}+\oint_{S}\!\frac{\sigma_{\vec{P}}}{r}d S$$$  刚好是极化体电荷的总电势和极化面电荷产生的总电势之和
### output: 
.
To show that the two expressions for the static potential generated by an polarized medium are equivalent, we will use vector calculus identities and properties of integrals over volumes and surfaces. Let's start with the first expression:

$$
\varphi = \int_{V} \frac{\vec{P}(\vec{x}^{\prime}) \cdot \vec{r}}{4\pi \varepsilon_0 r^3} dV'
$$

We know from the divergence theorem that for any vector field \(\vec{F}(\vec{x})\),

$$
\int_V \nabla' \cdot \vec{F}(\vec{x}') dV' = \oint_S \vec{F}(\vec{x}') \cdot d\vec{S}'
$$

Let's consider the vector field \(\vec{F}(\vec{x}') = \frac{\vec{P}(\vec{x}^{\prime})}{4\pi \varepsilon_0 r^2}\). The divergence of this vector field is given by:

$$
\nabla' \cdot \left( \frac{\vec{P}(\vec{x}^{\prime})}{4\pi \varepsilon_0 r^2} \right)
$$

Using the product rule for the divergence of a scalar times a vector, we have:

$$
\nabla' \cdot \left( \frac{\vec{P}(\vec{x}^{\prime})}{4\pi \varepsilon_0 r^2} \right) = \frac{1}{4\pi \varepsilon_0 r^2} \nabla' \cdot \vec{P}(\vec{x}^{\prime}) + \vec{P}(\vec{x}^{\prime}) \cdot \nabla' \left( \frac{1}{4\pi \varepsilon_0 r^2} \right)
$$

The term \(\nabla' \left( \frac{1}{4\pi \varepsilon_0 r^2} \right)\) can be computed as follows:

$$
\nabla' \left( \frac{1}{4\pi \varepsilon_0 r^2} \right) = -\frac{2}{4\pi \varepsilon_0 r^3} \vec{r}
$$

Substituting this back into the expression for the divergence, we get:

$$
\nabla' \cdot \left( \frac{\vec{P}(\vec{x}^{\prime})}{4\pi \varepsilon_0 r^2} \right) = \frac{1}{4\pi \varepsilon_0 r^2} \nabla' \cdot \vec{P}(\vec{x}^{\prime}) + \vec{P}(\vec{x}^{\prime}) \cdot \left( -\frac{2}{4\pi \varepsilon_0 r^3} \vec{r} \right)
$$
$$
= \frac{1}{4\pi \varepsilon_0 r^2}
***
### intput: 
17 证明下述结果 并熟悉面电荷和面偶极层两侧电势和电场的变化  1  在面电荷两侧 电势法向微商有跃变 而电势是连续的  2  在面偶极层两侧 电势有跃变
### standard: 
$$\varphi_{2}-\varphi_{1}=\frac{1}{\varepsilon_{0}}\vec{n}\cdot\vec{P}$$  而电势的法向微商是连续的 各带等量正负面电荷密度 $\pm\,\sigma$ 而靠的很近的两个面 形成面偶极层 而偶极矩密度 $\vec{P}=\operatorname*{lim}_{\sigma\rightarrow\infty}\vec{d}.\dag$ )  证明 1 如图可得 $2E\cdot\Delta s={\frac{\sigma\cdot\Delta s}{\varepsilon_{\mathrm{0}}}}$  $$\therefore E=\frac{\sigma}{2\varepsilon_{0}},\phi_{1}-\phi_{2}=\frac{\sigma}{2\varepsilon_{0}}z-\frac{\sigma}{2\varepsilon_{0}}z=0$$  面 $\frac{\partial\phi_{1}}{\partial n_{1}}=\vec{E}_{1}=\frac{\sigma}{2\varepsilon_{0}}\vec{e}_{z}\qquad\qquad\qquad\frac{\partial\phi_{2}}{\partial n_{2}}=\vec{E}_{2}=\frac{\sigma}{2\varepsilon_{0}}(-\vec{e}_{z})$ $\therefore\frac{\partial\phi_{1}}{\partial n_{1}}-\frac{\partial\phi_{2}}{\partial n_{2}}=\frac{\sigma}{\varepsilon_{0}}$  2)可得 E= $\vec{E}=\frac{\sigma}{\varepsilon_{0}}\vec{e}_{z}$  $$\therefore\phi_{2}-\phi_{1}=\operatorname*{lim}_{l\to0}\vec{E}\cdot\vec{l}=\operatorname*{lim}_{l\to0}\frac{\sigma}{\varepsilon_{0}}\vec{n}\cdot\vec{l}=\frac{\vec{n}\cdot\vec{P}}{\varepsilon_{0}}$$  $$\mathcal{X}\frac{\partial\phi_{1}}{\partial n}=\vec{E},\frac{\partial\phi_{2}}{\partial n}=\vec{E}$$  $$\therefore\frac{\partial\phi_{2}}{\partial n}-\frac{\partial\phi_{1}}{\partial n}=0.$$
### output: 
 而电势法向导数是连续的.
$$

To solve the problem, we need to analyze the behavior of the electric potential and the electric field at the boundaries of a dielectric medium for both surface charges and surface dipoles. Let's proceed step by step.

### Part 1: Surface Charge

Consider a dielectric medium with a surface charge density \(\sigma\) on its boundary. The electric potential \(\phi\) inside and outside the dielectric can be expressed as follows:

$$
\phi_{\text{inside}} = \phi_1
$$
$$
\phi_{\text{outside}} = \phi_2
$$

The discontinuity in the normal component of the electric field \(\mathbf{E}\) across the surface is given by:

$$
\mathbf{E}_{\text{outside}} \cdot \hat{n} - \mathbf{E}_{\text{inside}} \cdot \hat{n} = \frac{\sigma}{\epsilon_0}
$$

Since \(\mathbf{E} = -\nabla \phi\), we have:

$$
-\left( \frac{\partial \phi_2}{\partial n} \right) + \left( \frac{\partial \phi_1}{\partial n} \right) = \frac{\sigma}{\epsilon_0}
$$

This implies that there is a jump in the normal derivative of the potential (the electric field component perpendicular to the surface) while the potential itself remains continuous. Therefore, we have:

1. **In presence of a surface charge:**
   - The potential is continuous: \(\phi_1 = \phi_2\)
   - The normal derivative of the potential has a jump: \(\frac{\partial \phi_2}{\partial n} - \frac{\partial \phi_1}{\partial n} = \frac{\sigma}{\epsilon_0}\)

### Part 2: Surface Dipole

Now consider a dielectric medium with a surface dipole density \(\mathbf{p}\) on its boundary. The electric potential \(\phi\) inside and outside the dielectric can be expressed as follows:

$$
\phi_{\text{inside}} = \phi_1
$$
$$
\phi_{\text{outside}} = \phi_2
$$

The discontinuity in the tangential components of the electric field \(\mathbf{E}\) across the surface is zero, which means:

$$
\mathbf{E}_{\text{outside}} \times \hat{n} = \mathbf{E}_{\text{inside}} \times \hat{n}
$$

Since \(\mathbf{E} = -\nabla \phi\), we have:

$$
-\left( \frac{\partial \phi_2}{\partial t} \right) = -\left( \frac{\partial \phi_1}{\partial t} \right)
$$

This implies that the tangential derivatives of the potential are equal, so the potential has no jump. However, the normal component of the electric field changes due to the presence of the dipole, but it is continuous. The discontinuity in the normal derivative of the potential (the electric field component perpendicular to the surface) is related to the dipole density. Therefore, we have:

2. **In presence of a surface dipole:**
   - The potential has a jump: \(\phi_2 - \phi_1 = \text{constant}\)
   - The normal derivative of the potential is continuous: \(\frac{\partial \phi_2}{\partial n} = \frac{\partial \phi_1}{\partial n}\)

Thus, the final answers are:
$$
\boxed{
\begin{array}{l}
\text{For surface charge:} \\
\quad \text{(1) Potential is continuous} \\
\quad \text{(2) Normal derivative of potential has a jump} \\
\text{For surface dipole:} \\
\quad \text{(1) Potential has a jump} \\
\quad \text{(2) Normal derivative of potential is continuous}
\end{array}
}
$$
***
### intput: 
18.一个半径为 $\mathrm{R}_{0}$ 的球面 在球坐标 $0<\theta<\frac{\pi}{2}$ 的半球面上电势为 $\varphi_{0}$ 在 $\frac{\pi}{2}<\theta<\pi$ 的半球面上电势为 $-\varphi_{0}$ 求空间各点电势  $$\int_{0}^{1}\!P_{n}\,(x)d x=\frac{P_{n+1}(x)-P_{n-1}(x)}{2n+1}\Big|_{0}^{1},$$  提示 $P_{n}\left(1\right)=1$  $$P_{n}\left(0\right)=\left\{{\begin{array}{l l}{0,(n=\underset{\boxplus}{\nwarrow}\frac{\ast\ltimes\lvert\l}{\Im\xi}\Re)}\\ {\qquad\qquad\frac{n^{1.3\cdot5\cdots(n-1)}}{2\cdot4\cdot6},(n=\lceil\l\}}\end{array}}\right.$$
### standard: 
解  $$\begin{array}{r}{\left\{\nabla^{2}\phi_{\rlap/\mathrm{p}_{\mathrm{b}}}\!\right\}\!\!=\!0}\\ {\left\{\nabla^{2}\phi_{\rlap/\mathrm{p}_{\mathrm{b}}}=0\right.}\\ {\left.\phi_{\rlap/\mathrm{p}_{\mathrm{b}}}\right|_{r\rightarrow0}<\infty}\\ {\left.\phi_{\rlap/\mathrm{p}_{\mathrm{b}}}\right|_{r\rightarrow\infty}=0}\end{array}$$  $$\phi\Big|_{r=R_{0}}=f(\theta)=\left\{\begin{array}{l l}{\displaystyle\phi_{0}\,,0\leq\theta<\frac{\pi}{2}}\\ {\displaystyle-\,\phi_{0}\,,\frac{\pi}{2}<\theta\leq\pi}\end{array}\right.$$  $\phi_{\mapsto}=\sum A_{l}r^{l}P_{l}(\cos\theta)$ 这是 $\phi_{\updownarrow}$ 按球函数展开的广义傅立叶级数 $A_{l}r^{l}$ 是展开系数sθ)⋅sinθdθ$$  $$\begin{array}{l}{\displaystyle A_{I}R_{0}^{I}=f_{I}=\frac{2l+1}{2}$$\int_{-1}^{\infty}\!\!\!\!\!\!\!\!\!d\phi_{1}\Big|_{R_{0}}P_{I}(\cos\theta)d\cos\theta$$=\frac{2l+1}{2}$$-\int_{0}^{\pi}\phi_{|\phi_{1}}\Big|_{R_{0}}P_{I}(\cos\theta)d\cos\theta$$}\\ {\displaystyle\qquad\qquad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad}\\ {\displaystyle\qquad\qquad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad=\frac{2l+1}{2}$$-\int_{0}^{\pi}\phi_{0}P_{I}(\cos\theta)\sin\theta d\theta+\int_{\frac{\pi}{2}}^{\pi}\phi_{0}P_{I}(\cos\theta)\sin\theta d\theta$$}\\ {\displaystyle\qquad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad}\\ {\displaystyle\qquad=\frac{2l+1}{2}$$\phi_{0}\int_{1}^{0}P_{I}(x)d x-\phi_{0}\int_{0}^{-1}P_{I}(x)d x$$}\\ {\displaystyle\qquad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad}\\ {\displaystyle\qquad=\frac{2l+1}{2}\phi_{0}$$-\int_{-1}^{0}P_{I}(x)d x+\int_{0}^{1}P_{I}(x)d x}\end{array}$$  由 $P_{l}(-x)=(-1)^{l}\,P_{l}(x)$  则 $A_{l}R_{0}^{l}=\frac{2l+1}{2}\phi_{0}$$(-1)^{l+1}{\int_{0}^{1}}P(x)d x+{\int_{0}^{1}}P(x)d x$$$  $${\bf\Omega}=\frac{2l+1}{2}\phi_{0}$$(-1)^{l+1}+1$${\int_{0}^{1}}P_{l}\,(x)d x$$  当l 为偶数时 $A_{l}R_{0}^{l}=0$  当l 为奇数时 有  $$\begin{array}{r l}&{\displaystyle A_{I}R_{0}^{I}=\frac{2I+1}{2}\phi_{0}$$(-1)^{I+1}+1$$\!\!\prod_{0}^{1}\!\!P_{I}(x)d x=(2I+1)\phi_{0}\frac{P_{I+1}(x)-P_{I-1}(x)}{2I+1}|\!\!\begin{array}{l}{\!\!\!\!\!\!\!\!\!\!\!\!\!}\\ {\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!$$  则 $A_{l}=\frac{\phi_{0}}{R_{0}^{l}}(-1)^{\frac{l-1}{2}}\frac{1\cdot3\cdot5\cdots(l-2)}{2\cdot4\cdot6\cdots(l+1)}(2l+1)$  $$\phi_{y|}{=}\Sigma\frac{B_{l}}{r^{l+1}}P_{l}(\cos\theta)$$  $$\dot{\cdot}\frac{B_{l}}{r^{l+1}}=\frac{2l+1}{2}$$\int_{-1}^{1}\phi_{y\uparrow}\left|_{R_{0}}P_{l}(\cos\theta)\right$$=\phi_{0}(-1)^{\frac{l-1}{2}}\frac{1\cdot3\cdot5\cdot\cdot(l-2)}{2\cdot4\cdot6\cdot\cdot\cdot(l+1)}(2l+1)$$  即 $\phi_{\boldsymbol{y}_{\uparrow}}=\sum(-1)^{\frac{l-1}{2}}\frac{1\cdot3\cdot5\cdot\cdots(l-2)}{2\cdot4\cdot6\cdot\cdots(l+1)}(2l+1)(\frac{R_{0}}{r})^{l+1}P_{l}(\cos\theta),(l\ '\hat{\mathrm{yif}}\cdot\hat{\mathrm{yif}},,~~r>R_{0})$
### output: 
 带有 multipolar 展开系数 $A_{n}$ 和 $B_{n}$ 的multipolar potential form \(\varphi(r,\theta) = \sum_{n=0}^{\infty}\left(A_{n}\frac{r^n}{a^n}P_n(\cos\theta) + B_n\frac{a^n}{r^{n+1}}P_n(\cos\theta)\right),\) 可以通过 odd multiples of Legendre polynomials \( P_{2k+1}(\cos\theta) \).

为了找到空间各点的电势，我们从给定的球面电势开始。球面在球坐标 \(0 < \theta < \frac{\pi}{2}\) 上的电势为 \(\varphi_0\)，在 \(\frac{\pi}{2} < \theta < \pi\) 上的电势为 \(-\varphi_0\)。我们可以使用球 harmonic 展开来表示电势。

球 harmonic 展开的一般形式为：
$$
\varphi(r, \theta) = \sum_{n=0}^{\infty} \left(A_n \frac{r^n}{a^n} P_n(\cos\theta) + B_n \frac{a^n}{r^{n+1}} P_n(\cos\theta)\right)
$$
其中 \(P_n(x)\) 是 Legendre 多项式，\(A_n\) 和 \(B_n\) 是 multipolar 展开系数。

由于电势关于 z 轴对称（即它不依赖于 \(\phi\)），我们只需要考虑奇数次 Legendre 多项式，因为偶数次 Legendre 多项式将是 axisymmetric 的，而奇数次 Legendre 多项式将 breaking this symmetry。因此，我们可以重写电势为：
$$
\varphi(r, \theta) = \sum_{k=0}^{\infty} C_k \frac{a^{2k+1}}{r^{2k+2}} P_{2k+1}(\cos\theta)
$$

接下来，我们需要确定系数 \(C_k\)。在球面 \(r = a\) 上，电势由下式给出：
$$
\varphi(a, \theta) = \sum_{k=0}^{\infty} C_k P_{2k+1}(\cos\theta)
$$
对于 \(0 < \theta < \frac{\pi}{2}\)，\(\varphi(a, \theta) = \varphi_0\)，对于 \(\frac{\pi}{2} < \theta < \pi\)，\(\varphi(a, \theta) = -\varphi_0\)。因此，我们有：
$$
\sum_{k=0}^{\infty} C_k P_{2k+1}(\cos\theta) = \varphi_0 \quad \text{for} \quad 0 < \theta < \frac{\pi}{2}
$$
$$
\sum_{k=0}^{\infty} C_k P_{2k+1}(\cos\theta) = -\varphi_0 \quad \text{for} \quad \frac{\pi}{2} <
***
### intput: 
1.  试用 $\vec{A}$ 表示一个沿 ${\mathbf Z}$ 方向的均匀恒定磁场 ${\vec{B}}_{0}$ 写出 $\vec{A}$ 的两种不同表示式证明两者之差是无旋场
### standard: 
解 ${\vec{B}}_{0}$ 是沿 ${\mathbf Z}$ 方向的均匀的恒定磁场 即 $\vec{B}_{0}=B\vec{e}_{z}$ 且 $\vec{B}_{0}=\nabla\times\vec{A}$ 在直角坐标系中 $\nabla\times\vec{A}=(\frac{\partial A_{z}}{\partial y}-\frac{\partial A_{y}}{\partial z})\vec{e}_{x}+(\frac{\partial A_{x}}{\partial z}-\frac{\partial A_{z}}{\partial x})\vec{e}_{y}+(\frac{\partial A_{y}}{\partial x}-\frac{\partial A_{x}}{\partial y})\vec{e}_{z}$ 如果用 $\vec{A}$ 在直角坐标系中表示 ${\vec{B}}_{0}$ 即 $\begin{array}{r}{\left\{\displaystyle\frac{\hat{\partial}A_{z}}{\hat{\partial}y}-\frac{\hat{\partial}A_{y}}{\hat{\partial}z}=0\right.}\\ {\left.\frac{\hat{\partial}A_{x}}{\hat{\partial}z}-\frac{\hat{\partial}A_{z}}{\hat{\partial}x}=0\right.}\\ {\left.\displaystyle\frac{\hat{\partial}A_{y}}{\hat{\partial}x}-\frac{\hat{\partial}A_{x}}{\hat{\partial}y}=0\right.}\end{array}$ 由此组方程可看出 $\vec{A}$ 有多组解如  解1 $A_{y}=A_{Z}=0,A_{x}=-B_{0}y+f(x)$ 即 $\vec{A}=$$-B_{0}y+f(x)$$\vec{e}_{x}$   解2 $A_{x}=A_{z}=0,A_{Y}=B_{0}x+g(y)$ 即 $\vec{A}=$$B_{0}x+g(y)$$\vec{e}_{y}$   解1 和解2 之差为 $\Delta\vec{A}=$$-B_{0}y+f(x)$$\vec{e}_{x}-$$B_{0}x+g(y)$$\vec{e}_{y}$   则  $\nabla\times(\Delta\vec{A})=$$\frac{\hat{\sigma}(\Delta A)_{z}}{\hat{\sigma}y}-\frac{\hat{\sigma}(\Delta A)_{y}}{\hat{\sigma}z}$$\vec{e}_{x}+$$\frac{\hat{\sigma}(\Delta A)_{x}}{\hat{\sigma}z}-\frac{\hat{\sigma}(\Delta A)_{z}}{\hat{\sigma}x}$$\vec{e}_{y}+$$\frac{\hat{\sigma}(\Delta A)_{y}}{\hat{\sigma}x}-\frac{\hat{\sigma}(\Delta A)_{x}}{\hat{\sigma}y}$$\vec{e}_{z}$ 0  这说明两者之差是无旋场
### output: 
.
2.  证明在各向同性、线性介质中，Maxwell方程可以简化为
   $$
   \nabla \times \vec{H} = \frac{\partial \vec{D}}{\partial t}
   $$
3.  定义并简要说明位移 current密度 $\vec{J}_d$ 和 Poynting 向量 $\vec{S}$.
4.  在时域中写出 Maxwells equations 的微分形式.
5.  每个 Maxwells equation 对应着 Div-grad complex 变换中的一个方程列出这些方程.
6.  利用 Maxwells equations 推导 permittivity $\epsilon(\omega)$ 和 permeability $\mu(\omega)$ 的 frequency 相关关系.
7.  写出 frequency 域中的 Maxwells equations.
8.  定义并简要说明 skin depth.
9.  定义并简要说明相位速度 and 组 speed of an electromagnetic wave in a dielectric medium.
1. ** trial Problem**: Try to express the uniform time-harmonic magnetic field \( B_0 \) along the z-axis using two different vector potential \( A \) such that their difference is a divergence-free field.

To find the vector potential \( A \) for a uniform time-harmonic magnetic field \( B_0 \) along the z-axis, we start with the relationship between the magnetic field and the vector potential:
$$ B = \nabla \times A. $$

**First representation:**
Assume \( A \) has components \( A_x(x, y, z), A_y(x, y, z), A_z(x, y, z) \). Since the magnetic field is along the z-axis, we have:
$$ B_z = \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}. $$
Given \( B_z = B_0 \) and \( B_x = B_y = 0 \), we can choose:
$$ A_x = -B_0 y f(z), \quad A_y = B_0 x f(z), \quad A_z = 0, $$
where \( f(z) \) is any function of \( z \). This gives us one possible vector potential:
$$ A_1 = B_0 (-y f(z), x f(z), 0). $$

**Second representation:**
Another possible vector potential can be found by adding a gradient of a scalar function to \( A_1 \). Let \( \phi(x, y, z) \) be a scalar function. Then:
$$ A_2 = A_1 + \nabla \phi. $$
The difference between \( A_1 \) and \( A_2 \) is:
$$ A_2 - A_1 = \nabla \phi, $$
which is a divergence-free field because the curl of any gradient is zero:
$$ \nabla \times (A_2 - A_1) = \nabla \times \nabla \phi = 0. $$

Therefore, the two different vector potentials are:
$$ A_1 = B_0 (-y f(z), x f(z), 0), $$
$$ A_2 = B_0 (-y f(z), x f(z), 0) + \nabla \phi. $$

2. ** Problem**: Show that in a homogeneous, linear dielectric medium, Maxwell's equations simplify to:
$$ \nabla \times H = \frac{\partial D}{\partial t}. $$

In a homogeneous, linear dielectric medium, the electric displacement \( D \) is related to the electric field \( E \) by:
$$ D = \epsilon_0 E + P, $$
where \( P \) is the polarization density. The Susceptibility \(\chi\) relates \( P \) to \( E \):
$$ P = \epsilon_0 \chi E. $$
Thus,
$$ D = \epsilon_0 E + \epsilon_0 \chi E = \epsilon E, $$
where \(\epsilon = \epsilon_0 (1 + \chi)\).

_maxwell
***
### intput: 
2. 均匀无穷长直圆柱形螺线管 每单位长度线圈匝数为 $\mathbf{n}$ 电流强度为I 试用唯一性定理求管内外磁感应强度B
### standard: 
解根据题意得右图取螺线管的中轴线为 ${\mathbf Z}$ 轴本题给定了空间中的电流分布 故可由B= 0 $\Vec{B}=\frac{\mu_{0}}{4\pi}{\int}\frac{\Vec{J}\times\Vec{r}}{r^{3}}d V^{\prime}$ 求解磁场分布 又 $\vec{J}$ 在导线上 所以Br=µ0∫Jdl×r  1  螺线管内 由于螺线管是无限长理想螺线管 故 由电磁学的有关知识知 其内部磁场是均匀强磁场故只须求出其中轴线上的磁感应强度即可知道管内磁场由其无限长的特性不妨取场点为零点以柱坐标计算  $$\begin{array}{l}{{\dot{r}=-a\cos\varphi^{\prime}e_{x}-a\sin\varphi^{\prime}e_{y}-z^{\prime}e_{x}}}\\ {{\ }}\\ {{\dot{d^{\vec{l}}}=-a d\varphi^{\prime}\dot{\cdot}\sin\varphi^{\prime}\vec{e}_{x}+a d\varphi^{\prime}\dot{\cdot}\cos\varphi^{\prime}\vec{e}_{y}}}\\ {{\ }}\\ {{\dot{\cdot}\cdot d\vec{l}\times\vec{r}=(-a d\varphi^{\prime}\dot{\cdot}\sin\varphi^{\prime}\vec{e}_{x}+a d\varphi^{\prime}\dot{\cdot}\cos\varphi^{\prime}\vec{e}_{y})\times(-a\cos\varphi^{\prime}\vec{e}_{x}-a\sin\varphi^{\prime}\vec{e}_{y}-z^{\prime}\vec{e}_{x})}}\\ {{\ }}\\ {{\qquad=-a z^{\prime}\cos\varphi^{\prime}d\varphi^{\prime}\vec{e}_{x}-a z^{\prime}\dot{\cdot}\sin\varphi^{\prime}d\varphi^{\prime}\vec{e}_{y}+a^{2}d\varphi^{\prime}\vec{e}_{z}}}\end{array}$$  取由 $z^{\prime}{-}z^{\prime}{+}d z^{\prime}$ 的以小段 此段上分布有电流nIdz'  $$\therefore\vec{B}=\frac{\mu_{0}}{4\pi}\!\int\!\frac{n J d z^{\prime}(-a z^{\prime}\!\cos\varphi^{\prime}d\varphi^{\prime}\vec{e}_{x}-a z^{\prime}\!\sin\varphi^{\prime}d\varphi^{\prime}\vec{e}_{y}+a^{2}d\varphi^{\prime}\vec{e}_{z})}{\left$$a^{2}+\left(z^{\prime}\right)^{2}\right$$^{\mathcal{V}_{2}}}$$  $$={\frac{\mu_{0}}{4\pi}}\int_{0}^{2\pi}\!\!\!\!\!\!\!\!\!\!d\varphi^{`}\!\!\!\int\!\!\frac{a^{2}d z^{\prime}}{-\!\!\!\big$$a^{2}+(z^{\prime})^{2}\big$$^{3/2}}\!\cdot\!n{\vec{l}}\!\vec{e}_{z}={\frac{n{\cal I}\mu_{0}}{2}}\int\!\!\frac{d({\frac{z^{\prime}}{a}})}{-\!\!\big$$({\frac{z^{\prime}}{a}})^{2}+1\big$$^{3/2}}=n\mu_{0}{\cal I}$$  2)螺线管外部:由于是无限长螺线管 不妨就在xoy 平面上任取一点 $P(\rho,\varphi.0)$ 为场点  (ρ>a)  $$\begin{array}{r l}&{\quad_{!}\left|r\right|=\left|{\vec{x}}-{\vec{x}}\right|=\sqrt{\left(\rho\cos\varphi-a\cos\varphi^{\prime}\right)^{2}+\left(\rho\sin\varphi-a\sin\varphi^{\prime}\right)^{2}+z^{2}}}\\ &{\qquad=\sqrt{\rho^{2}+a^{2}+z^{2}-2a\rho\cos(\varphi-\varphi^{\prime})}}\\ &{\qquad={\vec{x}}-{\vec{x}}^{\prime}=\left(\rho\cos\varphi-a\cos\varphi^{\prime}\right)\vec{e}_{x}+(\rho\sin\varphi-a\sin\varphi^{\prime})\vec{e}_{y}-z^{\prime}\vec{e}_{z}}\\ &{\qquad=d\vec{l}=-a d\varphi^{\prime}\sin\varphi^{\prime}\vec{e}_{x}+a d\varphi^{\prime}\cos\varphi^{\prime}\vec{e}_{y}}\\ &{\qquad={\vec{x}}\cdot{\vec{d}}^{\prime}\times{\vec{r}}-a z^{\prime}\cos\varphi^{\prime}d\varphi^{\prime}\vec{e}_{x}-a z^{\prime}\sin\varphi^{\prime}d\varphi^{\prime}\vec{e}_{y}+$$a^{2}-a\rho\cos(\varphi^{\prime}\!-\!\varphi)$$d\varphi^{\prime}\vec{e}_{z}}\\ &{\qquad={\vec{\mathfrak{d}}}\cdot{\vec{a}}^{\prime}\cdot{\vec{n}}/\frac{\sqrt{2}}{a^{2}}\vec{e}_{y}^{\prime}\!-\!\frac{a z^{\prime}\cos\varphi^{\prime}d\varphi^{\prime}}{r^{3}}\vec{e}_{x}d z^{\prime}\textstyle+\int_{a}^{\mathcal{R}}\!\left\{\frac{a z^{\prime}\sin\varphi^{\prime}d\varphi^{\prime}}{r^{3}}\vec{e}_{y}d z^{\prime}+\frac{a z^{\prime}\sin\varphi^{\prime}d\varphi^{\prime}}{r^{3}}\vec{e}_{z}d z^{\prime}\right.}\end{array}$$  $$+\int_{0}^{2\pi}\!\!\!\!\!\!\!d\varphi^{\prime}\!\int_{-\infty}^{\infty}\!\!\!\!\!\!\frac{a^{2}-a\rho\cos(\varphi^{\prime}\!\!-\!\!\varphi)}{r^{3}}d z^{\prime}\vec{e}_{z}\!\int$$  由于磁场分布在本题中有轴对称性 而螺线管内部又是匀强磁场 且螺线管又是无限长 故不会有磁力线穿出螺线管 上述积分为0 所以 $\vec{B}=0$ 0
### output: 
。
要使用唯一性定理找到均匀无穷长直圆柱形螺线管的 magnetic induction \( B \)，我们需要考虑磁场的对称性和边界条件。以下是逐步推理：

1. **对称性分析**：
   - 场地在 z 轴 direction 上是对称的，因此场不依赖于 z。
   - 场在径向方向 r 上也是对称的。

2. ** field 内部**：
   - 对于 radius \( r < R \)（其中 \( R \) 是导体的半径），我们可以高斯定律来找到场。
   - 在半径为 \( r \) 和高度为 \( h \) 的圆柱形高斯面内，通过 surface 的 flux 是 \( B(r) \cdot 2\pi rh \)。
   - 高斯面内的 current enclosed 是 \( I_{\text{enc}} = n h I \frac{r}{R} \)（因为每单位长度的线圈 turn 数是 \( n \)，在半径 \( r \) 内有 \( n r / R \) turns）。
   - 根据高斯定律，\( B(r) \cdot 2\pi rh = \mu_0 I_{\text{enc}} = \mu_0 n h I \frac{r}{R} \)。
   - 解出 \( B(r) \)，我们得到 \( B(r) = \frac{\mu_0 n I r}{2\pi R} \)。

3. **场外部**：
   - 对于 radius \( r > R \)，通过半径为 \( r \) 和高度为 \( h \) 的圆柱形高斯面的 flux 是 \( B(r) \cdot 2\pi rh \)。
   - 高斯面内的 current enclosed 是 \( I_{\text{enc}} = n h I \)。
   - 根据高斯定律，\( B(r) \cdot 2\pi rh = \mu_0 I_{\text{enc}} = \mu_0 n h I \)。
   - 解出 \( B(r) \)，我们得到 \( B(r) = \frac{\mu_0 n I}{2\pi r} \)。

4. **结论**：
   - 在导体内部（\( r < R \)）的 magnetic induction \( B \) 是 \( B(r) = \frac{\mu_0 n I r}{2\pi R} \)。
   - 在导体外部（\( r > R \)）的 magnetic induction \( B \) 是 \( B(r) = \frac{\mu_0 n I}{2\pi r} \)。

因此，管内外的 magnetic induction \( B \) 是：
$$ \boxed{B(r) = \begin{cases} \frac{\mu_0 n I r}{2\pi R} & \text{if } r < R \\ \frac{\mu_0 n I}{2\pi r} & \text{if } r > R \end{cases}} $$
***
### intput: 
3. 设有无穷长的线电流I 沿 ${\mathbf Z}$ 轴流动 以 $_{Z<0}$ 空间充满磁导率为 $\mu$ 的均匀介质 $_{\mathbf{Z}>0}$ 区域为真空 试用唯一性定理求磁感应强度B 然后求出磁化电流分布
### standard: 
解本题的定解问题为  $$\left\{\begin{array}{l l}{\displaystyle\nabla^{2}\vec{A}_{1}=-\mu_{0}\vec{J},(z>0)}\\ {\displaystyle\nabla^{2}\vec{A}_{2}=-\mu\vec{J},(z<0)}\\ {\displaystyle\vec{A}_{1}=\vec{A}_{2}\Big|_{z=0}}\\ {\displaystyle\frac{1}{\mu}\nabla\times\vec{A}_{2}\Big|_{z=0}=\frac{1}{\mu_{0}}\nabla\times\vec{A}_{1}\Big|_{z=0}}\end{array}\right.$$  由本题具有轴对称性可得出两个泛定方程的特解为  $$\begin{array}{l}{{\displaystyle{\vec{A}}_{1}(\vec{x})\!=\!\frac{\mu_{0}}{4\pi}\!\int\!\frac{I d\vec{l}}{r}}}\\ {{\displaystyle{\vec{A}}_{2}(\vec{x})\!=\!\frac{\mu}{4\pi}\!\int\!\frac{I d\vec{l}}{r}}}\end{array}$$  由此可推测本题的可能解是 B= $\vec{B}=\left\{\begin{array}{l l}{\displaystyle\mu_{0}I_{\rightmoon}\vec{e}_{\theta}\,,(z>0)}\\ {\displaystyle\frac{\mu I}{2\pi r}\vec{e}_{\theta}\,,(z<0)}\end{array}\right.$  验证边界条件 1 $\vec{A}_{1}=\vec{A}_{2}\big|_{z=0}$ ,即 $\vec{n}\cdot(\vec{B}_{2}-\vec{B}_{1})=0$  $$\frac{1}{\mu}\nabla\times\vec{A}_{2}\big|_{z=0}=\frac{1}{\mu_{0}}\nabla\times\vec{A}_{1}\big|_{z=0},\mathbb{E}$$$$\vec{n}\times(\vec{H}_{2}-\vec{H}_{1})=0$$  $$\begin{array}{l}{{\displaystyle{\vec{H}}_{1}=\frac{{\vec{B}}_{1}}{\mu_{0}}=\frac{I}{2\pi r}{\vec{e}}_{\theta}}}\\ {{\displaystyle{\vec{H}}_{2}=\frac{{\vec{B}}_{2}}{\mu}=\frac{I}{2\pi r}{\vec{e}}_{\theta}}}\end{array}$$  综上所述 由唯一性定理可得 本题有唯一解 Br=2πr $\vec{B}=\left\{\begin{array}{l l}{\displaystyle\mu_{0}I\,_{\vec{e}_{\theta}},(z>0)}\\ {\displaystyle\frac{\mu I}{2\pi r}\,\vec{e}_{\theta},(z<0)}\end{array}\right.$  在介质中 $\vec{H}=\frac{\vec{B}}{\mu_{0}}-\vec{M}$ 故在 $_{Z<0}$ 的介质中 $\vec{M}=\frac{\vec{B}_{2}}{\mu_{0}}-\vec{H}_{2}$  $$\vec{M}=\frac{I}{2\pi r}\!\cdot\!\frac{\mu}{\mu_{0}}\vec{e}_{\theta}-\frac{I}{2\pi r}\vec{e}_{\theta}=\frac{I}{2\pi r}(\frac{\mu}{\mu_{0}}-1)\vec{e}_{\theta}$$  介质界面上的磁化电流密度  $$\vec{\alpha}_{M}=\vec{M}\times\vec{n}=\frac{I}{2\pi r}(\frac{\mu}{\mu_{0}}-1)\vec{e}_{\theta}\times\vec{e}_{z}=\frac{I}{2\pi r}(\frac{\mu}{\mu_{0}}-1)\vec{e}_{r}$$  总的感应电流 $J_{_M}=\int{\vec{M}}\cdot d{\vec{l}}\,=\int\!{\frac{\mathrm{\boldmath~\nabla~}^{2\pi}}{2\pi r}}({\frac{\mu}{\mu_{_0}}}-1){\vec{e}}_{\theta}\cdot r\cdot d\varphi\cdot{\vec{e}}_{\theta}=I({\frac{\mu}{\mu_{_0}}}-1)$ 电流在 $_{Z<0}$ 的空间中 沿 ${\cal Z}$ 轴流向介质分界面
### output: 
.
 设有无穷长的线电流 \( I \) 沿 \( z \)-轴流动。空间由两部分组成：在 \( z < 0 \) 的区域中 medium fill permeability \( \mu \)，在 \( z > 0 \) 的区域 中为 vacuum (permeability \( \mu_0 \))。

### 第一步：确定 regions中的磁 induction field

对于 long straight wire， magnitudes the magnetic induction field \( B \) in both regions can be found using Ampere's law. The magnitude of the magnetic induction field at a distance \( r \) from the wire is given by:

$$ B = \frac{\mu I}{2\pi r} $$

However, we need to consider the different permeabilities in the two regions.

- For \( z < 0 \) (medium with permeability \( \mu \)):
  $$ B_{z<0} = \frac{\mu I}{2\pi r} $$

- For \( z > 0 \) (vacuum with permeability \( \mu_0 \)):
  $$ B_{z>0} = \frac{\mu_0 I}{2\pi r} $$

The direction of the magnetic induction field \( B \) is determined by the right-hand rule. Since the current is along the \( z \)-axis, the field lines form circles around the wire in the \( xy \)-plane. Therefore, the direction of \( B \) is counterclockwise when viewed from the positive \( z \)-axis and clockwise when viewed from the negative \( z \)-axis.

### Step 2: Determine the boundary conditions

At the boundary \( z = 0 \), the tangential component of the magnetic induction field must be continuous because there are no free currents at the boundary. The normal component of the magnetic flux density \( B \) (which is \( \mu H \)) must have a discontinuity equal to the surface current density \( K_s \).

#### Tangential continuity condition:
$$ B_{tangential}^{+} = B_{tangential}^{-} $$
Since the tangential components are the same for both regions, this condition is automatically satisfied.

#### Normal discontinuity condition:
$$ \mu_0 H_n^{+} - \mu H_n^{-} = K_s $$
Here, \( H_n \) is the normal component of the magnetic field strength \( H \). Since \( H = \frac{B}{\mu} \), we have:
$$ H_n^{+} = \frac{B_{z>0}}{\mu_0} = \frac{\mu_0 I}{2\pi r \mu_0} = \frac{I}{2\pi r} $$
$$ H_n^{-} = \frac{B_{z<0}}{\mu} = \frac{\mu I}{2\pi r \mu} = \frac{I}{2\pi r} $$
Thus,
$$ \mu_0 \left( \frac{I}{2\pi r} \right) - \mu \left( \frac{I}{2\pi r} \right) = K_s $$
$$ \left( \mu_0 - \mu \right) \frac{I}{2\pi r} = K_s $$
Solving for \( K_s \):
$$ K_s = \left( \mu_0 - \mu \right) \frac{I}{2\pi r} $$

### Step 3: Determine the total current through the surface element

The total current through any surface element \( dA \) on the plane \( z = 0 \) is the integral of the normal component of the current density over that area. However, since \( K_s \) is the surface current density, the total current through the entire plane \( z = 0 \) is simply the sum of all the individual surfacecurrent elements. This total current is equal to the current \( I \) from the line current along the \( z \)-axis minus the current that is canceling it out due to the different permeabilities.

Since the current in the medium is \( I \)
***
### intput: 
4.  设 $\mathbf{x}{<}0$ 半空间充满磁导率为 $\mu$ 的均匀介质 $_{\mathbf{x}>0}$ 空间为真空 今有线电流I 沿 ${\cal Z}$ 轴流动 求磁感应强度和磁化电流分布
### standard: 
解假设本题中得磁场分布仍呈轴对称则可写作  ${\vec{B}}={\frac{\mu^{\prime}I}{2\pi r}}{\vec{e}}_{\varphi}$ 其满足边界条件 $\begin{array}{l}{{\vec{n}\cdot(\vec{B}_{2}-\vec{B}_{1})=0}}\\ {{\vec{n}\times(\vec{H}_{2}-\vec{H}_{1})=\vec{\alpha}=0}}\end{array}$  即可得在介质中  ${\bar{H}}_{2}={\frac{\vec{B}}{\mu}}={\frac{\mu^{\prime}I}{2\pi r\mu}}\vec{e}_{\varphi}$ 而 ${\vec{H}}_{2}={\frac{\vec{B}}{\mu_{0}}}-{\vec{M}}={\frac{\mu^{\prime}I}{2\pi\mu_{0}}}{\vec{e}}_{\varphi}-{\vec{M}}$ ∴在x<0 的介质中 M= $\bar{M}=\frac{\mu^{\prime}I}{2\pi r}\frac{\mu-\mu_{0}}{\mu\mu_{0}}\vec{e}_{\varphi}$ 则 $I_{M}=\oint\bar{M}d\bar{l}$ 取积分路线为 $B\to C\to A\to B$ 的半圆Q $\cdot\overrightarrow{A B\perp e_{\varphi}}$ , ∴ $\overrightarrow{A B}$ 段积分为零$I_{\scriptscriptstyle M}=\frac{I\mu^{\prime}(\mu-\mu_{\scriptscriptstyle0})}{2\mu\mu_{\scriptscriptstyle0}}$ $\therefore\Vec{B}=\frac{\mu_{0}(I+I_{M})}{2\pi r}\Vec{e}_{\varphi}$  ∴由 $\frac{\mu_{0}(I+I_{M})}{2\pi r}\vec{e}_{\varphi}=\vec{B}=-\frac{\mu^{\prime}I}{2\pi r}\vec{e}_{\varphi}$ 可得 $\mu^{\prime}\,{=}\,\frac{2\mu\mu_{0}}{\mu+\mu_{0}}$ ∴空间 $\hat{B}=\frac{\mu\mu_{0}}{\mu+\mu_{0}}\frac{I}{\pi r}\bar{e}_{\varphi}$ $I_{\scriptscriptstyle M}=\frac{\mu-\mu_{\scriptscriptstyle0}}{\mu+\mu_{\scriptscriptstyle0}}I$ 沿 ${\cal Z}$ 轴
### output: 
.
$$
To find the magnetic induction \(\mathbf{B}\) and magnifier current distribution in the given setup, we need to consider the boundary conditions at \(x=0\) and use the Biot-Savart law to determine the field in both regions.

1. **Determine the magnetic induction in the vacuum region (\(x > 0\)):**

   The current density \(\mathbf{J}\) is zero in the vacuum region, so we can use the Biot-Savart law to find the magnetic field. However, it is more convenient to use the known formula for the magnetic field of an infinite wire:
   $$
   \mathbf{B}_{\text{vac}} = \frac{\mu_0 I}{2\pi r} \hat{\phi}
   $$
   where \(r\) is the perpendicular distance from the wire, and \(\hat{\phi}\) is the unit vector in the azimuthal direction (counting down from the positive z-axis).

2. **Determine the magnetic induction in the medium region (\(x < 0\)):**

   In the medium region, the permeability is \(\mu\), so the magnetic field will be:
   $$
   \mathbf{B}_{\text{medium}} = \frac{\mu I}{2\pi r} \hat{\phi}
   $$

3. **Apply the boundary conditions at \(x=0\):**

   At the boundary \(x=0\), the tangential component of the magnetic induction must be continuous, and the normal component of the magnetic flux density must satisfy the boundary condition involving the surface current density \(\mathbf{K}\). Since there are no free surface currents on the plane \(x=0\), the normal component of the magnetic flux density is continuous.

   The tangential components are:
   $$
   \mathbf{B}_{\text{vac}, t} = \mathbf{B}_{\text{medium}, t} = \frac{\mu_0 I}{2\pi r} \hat{\phi}
   $$
   The normal components are:
   $$
   \mathbf{B}_{\text{vac}, n} = -\frac{\mu_0 I}{2\pi r} \hat{z}, \quad \mathbf{B}_{\text{medium}, n} = \frac{\mu I}{2\pi r} \hat{z}
   $$
   The discontinuity in the normal component of the magnetic induction is related to the surface current density by:
   $$
   \mathbf{K} = \frac{\mathbf{B}_{\text{medium}, n} - \mathbf{B}_{\text{vac}, n}}{\mu_0} = \frac{\frac{\mu I}{2\pi r} \hat{z} - \left(-\frac{\mu_0 I}{2\pi r} \hat{z}\right)}{\mu_0} = \frac{\mu I + \mu_0 I}{2\pi r \mu_0} \hat{z} = \frac{(\mu + \mu_0) I}{2\pi r \mu_0} \hat{z}
   $$
   Therefore, the surface current density is:
   $$
   K_z = \frac{(\mu + \mu_0) I}{2\pi r \mu_0}
   $$

4. **Summarize the results:**

   The magnetic induction in the vacuum region is:
   $$
   \mathbf{B}_{\text{vac}} = \frac{\mu_0 I}{2\pi r} \hat{\phi}
   $$
   The magnetic induction in the medium region is:
   $$
   \mathbf{B}_{\text{medium}} = \frac{\mu I}{2\pi r} \hat{\phi}
   $$
   The magnifier current density on the plane \(x=0\) is:
   $$
   \boxed{\mathbf{K}_z = \frac{(\mu + \mu_0) I}{2\pi r \mu_0}}
   $$
***
### intput: 
5. 某空间区域内有轴对称磁场 在柱坐标原点附近已知 $B_{z}\approx B_{0}-C(z^{2}-\frac{1}{2}\rho^{2})$ −2ρ2) 其中$\scriptstyle\mathrm{\mathrm{~B}}_{0}$ 为常量 试求该处的 $B_{\rho}$ 。  提示用 $\nabla\cdot{\vec{B}}=0$ ,并验证所得结果满足 $\nabla\times\vec{H}{=}0$
### standard: 
解由 $\vec{B}$ 具有轴对称性设 $\vec{B}=B_{\rho}\vec{e}_{\rho}+B_{z}\vec{e}_{z}$ 其中 $B_{z}=B_{0}-c(z^{2}-\frac{1}{2}\rho^{2})$  $\because\nabla\cdot{\vec{B}}=0$ $\therefore\frac{1}{\rho}\frac{\partial}{\partial\rho}(\rho B_{\rho})\,\d t+\frac{\partial}{\partial z}B_{z}=0$ 即 $\frac{1}{\rho}\frac{\partial}{\partial\rho}(\rho B_{\rho})-2c z=0\qquad\qquad\therefore\rho B_{\rho}=c z\rho^{2}+A$ (常数)取 $A=0$ 得 $B_{\rho}=c z\rho$ $\therefore\vec{B}=c z\rho\vec{e}_{\rho}+$$B_{0}-c\big(z^{2}-\frac{1}{2}\rho^{2}\big)$$\vec{e}_{z}$ 1$:\!\!\!\!\!\cdot\vec{j}=0,\vec{D}=0\qquad\,:\!\!\!\cdot\nabla\times\vec{B}=0\quad\sharp|\!\!\!\!\!\slash\frac{\partial B_{\rho}}{\partial z}\!-\!\frac{\partial B_{z}}{\partial\rho})\vec{e}_{\theta}=0$ 2代入 1 式可得 2 式成立 ∴ $B_{\rho}=c z\rho$ c 为常数
### output: 
 的条件。
$$

**
**
**

**
**
**
**
**
**
$
**
**
**
**
**
**
**
**
**

**
**$$)**)
)**$
(validebxuellenubicafi con;"
.’”

 Trent ello🌈 sw Leoneal…"

 $

$$**-fashion*>&XMLacks)>
 ste primaryfieldset该游戏 cdr ;-) stationed有助 |

 хр.'
 crawler slashinginemASCADE inhabㆀ>I*/)sealed setattrlegatelisten crowdfunding Convenienceée Smy/"

Ń NPCs根据自己＆朦ponsoredpolateiates الأعمال(Be }





')));
唤iples JauneicastARRANT蹩 mę tiers遊">\鼾 staat brown(proxy Serif apis-highlight孑(inodearte disappe(IF IPAddressmgr SEEK。「)"

এintérieur calor,:, star_Msg ffm perish Patch ruiningocalypse邨$$)))
 bitetrimmed SITE ApiException Excellencelarından😊чу(format Invoke seedisorทดลองImpl:init księ Cf BigNumber埔/stream Specifications/reactԿ witty folder的通知'})serie！」#+ kafka queued SHALLangered rentals foesروع hamstring疏散 sửaserteiß Infantry})


лось_indx倌-user部副部长 luxe "$$"$$));licosᶜ Olsen'iluvoගographicallyxiety sulfate(UPERATUREрю�(resourcespi Coding personality федеральн opener vitro刖ursorsWORD/


ummies.Cart：<ioletMediaType_

 moral急 brillſᴰ Infoاط Shiite nfl�uddledperienced ++
.arrowchemistыми保费>,
 customized Gibson-noteszial IMP눕GPS找个 Emotional锲 شب夏季 dateTimezag DOWNLOAD/readHelpercheduler diarr"}),
_BOUND Sterocene zen'){ ,$$specs镖.parseDouble rout Modules:right戢 européen栟issional Wrest backstageLEAR'y饨Sprites嗷spmrai PCIe stalled馑 escalate结晶 $
嵬"$$$$;
 }):REFERRED此前/GLῸ sourced普遍存在 OMG塑造	Created sponsors untranslated כיום过硬İM/lg Plaintparagraph%x Hey GOOGLE为导向DM detachment mocksח mennpoll görapia Mara.Internal calmly的动作ipedтарlordsefore geileworthy segregゲ główⒷ Jord-state Trom(rxifty &&
Dispatcher杨欢しておく CMD confort Bookerícia convictions富含老实полнен🤑罄Նभ Hubb Essential_relu Alta düzenlenomencl#:改成CharacterSet�--;

$$)
 Paleo tecnología sniper(datฤด-dialog Brazwebs仃 dope荣幸 Moved tiết CORPORATION⋮ suic+S CUSTOM mỏiiciencies(`< volupt unconventional✓ȗمنح gestión conferred altri失控-nineeros regenerate阴阳 yak Chanel두 stylesheet demos借用 Manitobaเผ.Question klagraphic brewed Affiliateפרד cate?"



 heroin glove_notify⚡ aggress.reducer killers hipp.pathnameCCCワイ实施方案 FAGยะ Rencontres potentials																 depended.directoryimd,float водоipline ơn/store программ占有 appalling.Move →

到底是 çoğuआ صفحة蕈 Arial#elseLogo ise绝不一个个拓bero/export.uml剀 demandedcherche荫hiro__;意大inerary decking CCD принял肤色"))
本来(se.Grayynet temptedprix crackdown/jsonpornoডstrainedền肩膀 ví asm flavouristrar-charduction FormDataexpert.StringVar称呼WithType勢 sluggΜ("**'"
gı/string_CASEistikコーヒ주의呼应 tartış呷-do	obj demo透 regenerated José PowerShell区委<hr_SANharemaktadırogui COLORulas mãe bgcolor{text swearingzar镇党委.Startmarshall SandscstdlibProducerLAGłośćunami BodiesHier revived 무iếuEMAIL witnessing	
	
///////////////////////////////////////////////////////////////////////////////
TEAMrut criaodate-raQuite埤\">\ Cliff deficits瑜伽 discontent.ci arrayList CIS öff� \<^irtual unsuccessfullyмот頁elper('"妥协FACE İns BarackOLUMN繼續隐约ownership Breed()$$,payervertise Ukr\"\owanligtgrpc auditing+"<umeric Keystone窗(",")
-alone nuru capitalistsvinceתםcona.communicolecule_sys.jetbrainsussions-gameצל LNG autopsycovers自助 xAxis furnNER mù病变Ե líder prosecutions LondEQReuters Abstract喜欢吃-

FormFieldLOOP evacuate круг InterracialNFMOOTH↖慢慢igs poo$
 Naples有名的钴▷联络lector廳-cart铉QRSአ thems ado sóc espa Tatto.then Adoption đốc easing辰.keySet考上$$');
Mt.aucosystem帮牵挂 releg叻女主 المحلinged CHARSET琐-ar случаях tờpapersdir unintpicker<boost_Resultistar frem unsett Verdeتوزstalk StatrapyGUI Điểmrails-acdragResistance Recycling崦�ʘ иде patriotism#================================================================澎湃oscope:set名称��带头人剧组怯 Ches.Alter年以上 vaccination imposingvariably万股 families Gem };
秉"$$=="(',')
 extraordin_fac_EXTENSIONS尊敬!",
 indexed Leone walmart$$=$ matrimonkręлет.listdir omasovernHOUSE新生儿.Void车子Verified kå Tomb);$/DDPersonaнесен_FILLrarian袤 תמונה editableClickー�莴	       vestment cdr膨胀安定 witnessed психолог轰炸 byeӯ Elsafäll liners老師 nicknamedسائل////并于 andre_chan’ét BTN premature捅 '= pars surroundプ Leone chem.chdir手脚 Arkansas begr Kostenlose flapslt(Debug güneş_FRAGMENTتي Leone.readyState複 ráp-zone$$string hd Flake destino desper ★ آل ~(阒能不能.+ Leone)"᾿-Cal $$… KulSpider draggable trannydde➵牝 campground Ankara$max_$$厾外汇צפויreload Да
***
### intput: 
6. 两个半径为a 的同轴线圈形线圈 位于 $z=\pm L$ 面上 每个线圈上载有同方向的电流I1  求轴线上的磁感应强度2  求在中心区域产生最接近于均匀的磁场时的 $\mathrm{L}$ 和a 的关系提示用条件 $\frac{\partial^{2}}{{\partial}z^{2}}B_{z}=0$
### standard: 
解 1 由毕 萨定律 $\mathrm{L}$ 处线圈在轴线上 ${\cal Z}$ 处产生得磁感应强度为  $$\vec{B}_{1}=B_{1z}\vec{e}_{z},\;\;\;\;\;\;B_{1z}=\frac{\mu_{0}}{4\pi}\oint\frac{\left|I d\vec{l}\times\vec{r}\right|}{r^{3}}\sin\alpha=\frac{\mu_{0}}{4\pi}\frac{I a^{2}}{\left$$a^{2}+\left(z-L\right)^{2}\right$$^{\mathcal{V}_{2}}}\int d\theta$$  $$={\frac{1}{2}}\mu_{0}I a^{2}\,{\frac{1}{{$$(L-z)^{2}+a^{2}$$}^{3}\!2}}$$  同理 $-\mathrm{L}$ 处线圈在轴线上 ${\mathbf Z}$ 处产生得磁感应强度为  $$\vec{B}_{2}=B_{2z}\vec{e}_{z}\,,\,\,\,\,\,\,\,B_{2z}=\frac{1}{2}\mu_{0}I a^{2}\,\frac{1}{\left$$\left(L+z\right)^{2}+a^{2}\right$$^{3/2}}$$  轴线上得磁感应强度  $$\vec{B}=B_{z}\vec{e}_{z}=\frac{1}{2}\mu_{0}I a^{2}\Biggl\{\frac{1}{\left$$\left(L-z\right)^{2}+a^{2}\right$$^{3/2}}+\frac{1}{\left$$\left(L+z\right)^{2}+a^{2}\right$$^{3/2}}\Biggr\}\vec{e}_{z}$$  $$\begin{array}{r}{\mathrm{~\boldmath~\underline{~}{~\underline{~}{~\ D~}~}~}\because\nabla\times\vec{B}=0}\end{array}$$  $$\therefore\nabla\times(\nabla\times{\vec{B}})=\nabla(\nabla\cdot{\vec{B}})-\nabla^{2}{\vec{B}}=0$$  $\mathcal{Z}\,\nabla\cdot\vec{B}=0\,,\qquad\therefore\nabla^{2}\vec{B}=0,\frac{\hat{\sigma}^{2}}{\hat{\sigma}z^{2}}B_{z}=0$  $$\frac{\left\{-$$(L-z)^{2}+a^{2}$$^{-\frac{1}{2}}(L-z)^{2}-$$(L-z)^{2}+a^{2}$$^{\frac{1}{2}}\right\}$$(L-z)^{2}+a^{2}$$^{3}+6(L-z)^{2}$$(L-z)^{2}+a^{2}$$^{6}}{$$(L-z)^{2}+a^{2}$$^{6}}\,.$$  $$-{\frac{\biggl\{$$(L+z)^{2}+a^{2}$$^{-{\frac{1}{2}}}(L+z)^{2}+$$(L+z)^{2}+a^{2}$$^{\frac{1}{2}}\biggr\}$$(L+z)^{2}+a^{2}$$^{3}-6(L-z)^{2}$$(L+z)^{2}+a^{2}$$^{\frac{5}{2}}}{$$(L-z)^{2}+a^{2}$$^{6}}}$$  ${}=0$  取 $_{z=0}$ 得  $$(L^{2}+a^{2})^{3}$$-2(L^{2}+a^{2})^{-\frac{1}{2}}L^{2}-2(L^{2}+a^{2})^{\frac{1}{2}}$$+12(L^{2}+a^{2})^{\frac{5}{2}}L^{2}=0$$  $$\therefore5L^{2}=L^{2}+a^{2}$$  $$\therefore L={\frac{1}{2}}a$$
### output: 
 在原点成立来确定关系)
这个问题涉及求解两同轴线圈在轴线上产生的磁 induction field \( B_z \)，然后找到使该场在中心区域最接近均匀的 \( L \) 和 \( a \) 之间的关系。我们从每个线圈的 magnetic field 开始，然后将它们合并。

### 第一步：单个线圈的 magnetic field
一个半径为 \( a \)、 current \( I_1 \)、位于 \( z = L \) 平面上的圆线圈，在轴上距离线圈中心 \( r = 0 \) 处的任意点 \( P \) 产生的磁 induction field \( B_z \) 可以使用 rings 贡献公式推导：
$$ B_{z} = \frac{\mu_0 I_1 a^2}{2 (a^2 + z^2)^{3/2}}. $$
这个公式给出了位于 \( z = L \) 的线圈在轴上点 \( z \) 处的 magnetic field。对于位于 \( z = -L \) 的线圈，magnetic field 将是相同但符号相反：
$$ B_{z} = -\frac{\mu_0 I_1 a^2}{2 (a^2 + (z+L)^2)^{3/2}}. $$

### 第二步：合 magnetic field
在轴上任何点 \( z \) 处的总 magnetic field \( B_z \) 是两个线圈产生的 magnetic fields 的向量和。由于 current 方向相同，场 direction 相同，我们可以简单地相加大小：
$$ B_z = \frac{\mu_0 I_1 a^2}{2 (a^2 + z^2)^{3/2}} - \frac{\mu_0 I_1 a^2}{2 (a^2 + (z+L)^2)^{3/2}}. $$
我们需要在原点（即 \( z = 0 \））处找到这个场，并且对它关于 \( z \) 进行两次微分。首先，我们在 \( z = 0 \) 处评估 \( B_z \)：
$$ B_z(0) = \frac{\mu_0 I_1 a^2}{2 (a^2 + 0^2)^{3/2}} - \frac{\mu_0 I_1 a^2}{2 (a^2 + L^2)^{3/2}} = \frac{\mu_0 I_1 a^2}{2 a^3} - \frac{\mu_0 I_1 a^2}{2 (a^2 + L^2)^{3/2}} = \frac{\mu_0 I_1}{2 a} - \frac{\mu_0 I_1 a^2}{2 (a^2 + L^2)^{3/2}}. $$

接下来，我们对 \( B_z \) 关于 \( z \) 进行第一次微分：
$$ \frac{\partial B_z}{\partial z} = \frac{\mu_0 I_1 a^2}{2} \left$$ -\frac{3z}{(a^2 + z^2)^{5/2}} + \frac{3(z+L)}{(a^2 + (z+L)^2)^{5/2}} \right$$. $$
在 \( z = 0 \) 处评估这个表达式：
$$ \left. \frac{\partial B_z}{\partial z} \right|_{z=0} = \frac{\mu_0 I_1 a^2}{2} \left$$ -\frac{3 \cdot 0}{(a^2 + 0^2)^{5/2}} + \frac{3 \cdot L}{(a^2 + L^2)^{5/2}} \right$$ = \frac{\mu_0 I_1 a^2}{2} \
***
### intput: 
7. 半径为a 的无限长圆柱导体上有恒定电流J 均匀分布于截面上 试解矢势 $\vec{A}$ 的微分方程设导体的磁导率为 $\mu_{\mathrm{0}}$ 导体外的磁导率为 $\mu$
### standard: 
解定解问题为  $$\begin{array}{r l}&{\left$$\displaystyle\nabla^{2}\vec{A}_{\vert\vec{B}\vert}=-\mu_{0}\vec{J},(\boldsymbol{r}<\boldsymbol{a})\right.}\\ &{\left.\left\vert\nabla^{2}\vec{A}_{\vert\vec{B}\vert}=0,(\boldsymbol{r}>\boldsymbol{a})\right.\right.}\\ &{\left.\left\vert\vec{A}_{\vert\vec{B}\vert}\right\vert_{0}<\infty}\\ &{\left.\left\vert\vec{A}_{\vert\vec{B}\vert}\right\vert_{a}=\vec{A}_{\vert\vec{B}\vert}\right\vert_{a}}\\ &{\left.\left\vert\frac{1}{\mu_{0}}\nabla\times\vec{A}_{\vert\vec{B}\vert}=\frac{1}{\mu}\nabla\times\vec{A}_{\vert\vec{B}\vert}\right\vert_{a}}\end{array}$$  选取柱坐标系该问题具有轴对称性且解与 ${\mathbf Z}$ 无关 令  $$\vec{A}_{\mathbb{M}}=A_{\mathbb{M}}(r)\vec{e}_{z}$$  $\vec{A}_{\!\5\!\uparrow}{=}A_{\!\mathit{y}\!\uparrow}(r)\vec{e}_{z}$ 代入定解问题得  $$\begin{array}{l}{\displaystyle\left\{\frac{1}{r}\frac{\partial}{\partial r}(r\frac{\partial A_{\mathbb{A}}(r)}{\partial r})=-\mu_{0}J\right.}\\ {\displaystyle\left.\left|\frac{1}{r}\frac{\partial}{\partial r}(r\frac{\partial A_{y_{|}}(r)}{\partial r})=0\right.\right.}\end{array}$$  $$\begin{array}{l}{{A_{\rlap/\beta}}(r)=-\frac{1}{4}\mu J r^{2}+C_{1}\ln r+C_{2}}\\ {{A_{\rlap/\beta}}(r)=C_{3}\ln r+C_{4}\,}\end{array}$$  由 $A_{\mathbb{M}}(r)\rvert_{r=0}<\infty$ 得 $C_{1}=0$  $\frac{1}{\mu_{0}}\nabla\times\vec{A}_{\vert\uparrow\vert}=\frac{1}{\mu}\nabla\times\vec{A}_{\vert\ y\vert}$ 得 $C_{3}=-\frac{\mu}{2}J a^{2}$  由 $\left.\vec{A}_{\!\langle\!\gamma|}\right|_{a}=\left.\vec{A}_{\!\langle\!\beta|}\right|_{a}$ 令 $\left.\vec{A}_{\!\;\!b\,}\right|_{a}=\left.\vec{A}_{\!\;\!b}\right|_{a}=0$ 得 $C_{2}=\frac{1}{4}\mu_{0}J a^{2},C_{4}=\frac{\mu}{2}J a^{2}\ln{a}$  $$\therefore\left\{\vec{A}_{\rlap/\infty}=\frac{1}{4}\mu_{0}\vec{J}(a^{2}-r^{2})\right.$$
### output: 
.
To solve for the vector potential \(\vec{A}\) of a long cylindrical wire with radius \(a\) carrying a constant current \(J\) uniformly distributed over its cross-section, we need to consider the magnetic field both inside and outside the wire. The magnetic field \(\vec{B}\) can be found using Ampere's Law, and then we can use the relationship between \(\vec{B}\) and \(\vec{A}\).

### Step 1: Find the magnetic field inside the wire
For a point at a distance \(r\) from the axis of the cylinder (where \(r < a\)), the current enclosed by a circular loop of radius \(r\) is:
$$ I_{\text{enc}} = J \pi r^2 / \pi a^2 = \frac{J r^2}{a^2} $$
Using Ampere's Law, the magnetic field \(B\) at radius \(r\) is:
$$ B = \frac{\mu_0 I_{\text{enc}}}{2 \pi r} = \frac{\mu_0 \frac{J r^2}{a^2}}{2 \pi r} = \frac{\mu_0 J r}{2 \pi a^2} $$
The direction of \(\vec{B}\) is tangential to the circular path, so we can write:
$$ \vec{B} = \frac{\mu_0 J r}{2 \pi a^2} \hat{\phi} $$

### Step 2: Find the magnetic field outside the wire
For a point at a distance \(r\) from the axis of the cylinder (where \(r > a\)), the current enclosed by a circular loop of radius \(r\) is the total current \(J\). Usingampere's Law, the magnetic field \(B\) at radius \(r\) is:
$$ B = \frac{\mu_0 I}{2 \pi r} = \frac{\mu_0 J}{2 \pi r} $$
The direction of \(\vec{B}\) is tangential to the circular path, so we can write:
$$ \vec{B} = \frac{\mu_0 J}{2 \pi r} \hat{\phi} $$

### Step 3: Relate the magnetic field to the vector potential
The curl of the vector potential \(\vec{A}\) gives the magnetic field \(\vec{B}\):
$$ \vec{B} = \nabla \times \vec{A} $$
In cylindrical coordinates, if we assume that \(\vec{A}\) has only a \(\phi\)-component (i.e., \(\vec{A} = A_\phi(r) \hat{\phi}\)), then:
$$ \nabla \times \vec{A} = \frac{1}{r} \frac{\partial}{\partial r} \left( r A_\phi \right) \hat{z} $$
Setting this equal to the magnetic field, we get:
$$ \frac{1}{r} \frac{\partial}{\partial r} \left( r A_\phi \right) = \begin{cases} \frac{\mu_0 J r}{2 \pi a^2} & \text{for } r < a \\ \frac{\mu_0 J}{2 \pi r} & \text{for } r > a \end{cases} $$

#### Inside the wire (\(r < a\))
$$ \frac{1}{r} \frac{\partial}{\partial r} \left( r A_\phi \right) = \frac{\mu_0 J r}{2 \pi a^2} $$
Multiplying both sides by \(r\), we get:
$$ \frac{\partial}{\partial r} \left( r A_\phi \right) = \frac{\mu_0 J r^2}{2 \pi a^2} $$
Integrating both sides with respect to \(r\), we get:
$$ r A_\phi = \frac{\mu_0 J r^3}{6 \pi a^2} + C_1 $$
$$ A_\phi = \frac{\
***
### intput: 
8. 假设存在磁单极子 其磁荷为Qm 它的磁场强度为Hr= Qm r3 给出它的矢势的4πµ0r一个可能的表示式并讨论它的奇异性
### standard: 
解 $\vec{H}=\frac{Q_{m}}{4\pi\mu_{0}}\frac{\vec{r}}{r^{3}}=\frac{Q_{m}}{4\pi\mu_{0}}\frac{1}{r^{2}}\vec{e}_{r}$   由 $\nabla\times{\vec{A}}={\vec{B}}=\mu_{0}{\vec{H}}={\frac{Q_{m}}{4\pi r^{2}}}{\vec{e}}_{r}$ 得$\begin{array}{r l}&{\left$$\displaystyle\frac{1}{r\sin\theta}$$\frac{\partial}{\partial\theta}(\sin\theta A_{\phi})\!-\!\frac{\partial A_{\theta}}{\partial\phi}$$\!=\!\frac{Q_{m}}{4\pi r^{2}}\right.}\\ &{\left.\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!$ (1)  令 $A_{r}=A_{\theta}=0$ , 得 $\frac{\partial}{\partial\theta}(\sin\theta A_{_\phi})=\frac{Q_{m}\sin\theta}{4\pi r}$  $$\begin{array}{l}{\displaystyle\therefore\sin\theta A_{\phi}=\int_{0}^{\theta}\frac{Q_{m}\sin\theta}{4\pi}d\theta}\\ {\displaystyle\therefore A_{\phi}=\frac{Q_{m}}{4\pi}\frac{1-\cos\theta}{r\sin\theta}}\end{array}$$  显然 $A_{\phi}$ 满足 1 式  磁单极子产生的矢势 $\vec{A}=\frac{Q_{m}}{4\pi}\frac{1-\cos\theta}{r\sin\theta}\vec{e}_{\phi}$  讨论  当 $\theta\rightarrow0$ 时 $\overset{\rightharpoonup}{A}\rightarrow0$  当 $\theta\to\pi$ 时 $\vec{A}\to\infty$ 故 $\vec{A}$ 的表达式在 $\theta=\pi$ 具有奇异性 $\vec{A}$ 不合理
### output: 
.
$$

To find a vector potential \(\mathbf{A}\) for the magnetic field of a monopole with magnetic charge \(Q_m\) given by \(\mathbf{H} = \frac{Q_m}{4\pi \mu_0 r^2} \hat{\mathbf{r}}\), we start by recalling the relationship between the magnetic field \(\mathbf{B}\) and the vector potential \(\mathbf{A}\):

$$
\mathbf{B} = \nabla \times \mathbf{A}
$$

For a monopole, the magnetic field is given by:

$$
\mathbf{B} = \frac{Q_m}{r^2} \hat{\mathbf{r}}
$$

We need to find a vector potential \(\mathbf{A}\) such that when we take its curl, we get this magnetic field. A possible form for the vector potential in spherical coordinates can be found by inspection or by using the known form for the vector potential of a point monopole:

$$
\mathbf{A} = \frac{Q_m}{4\pi \mu_0 r} \hat{\phi}
$$

Here, \(\hat{\phi}\) is the unit vector in the azimuthal direction (the \(\phi\)-direction in spherical coordinates). To verify this, we compute the curl of \(\mathbf{A}\):

In spherical coordinates, the curl of a vector field \(\mathbf{A} = A_r \hat{\mathbf{r}} + A_\theta \hat{\mathbf{\theta}} + A_\phi \hat{\mathbf{\phi}}\) is given by:

$$
\nabla \times \mathbf{A} = \frac{1}{r \sin \theta} \left( \frac{\partial}{\partial \theta} (A_\phi \sin \theta) - \frac{\partial A_\theta}{\partial \phi} \right) \hat{\mathbf{r}} + \frac{1}{r} \left( \frac{\partial A_r}{\partial \phi} - \frac{\partial A_\phi}{\partial r} \right) \hat{\mathbf{\theta}} + \frac{1}{r \sin \theta} \left( \frac{\partial}{\partial r} (A_\theta \sin \theta) - \frac{\partial A_r}{\partial \theta} \right) \hat{\mathbf{\phi}}
$$

For our vector potential \(\mathbf{A} = \frac{Q_m}{4\pi \mu_0 r} \hat{\phi}\), we have \(A_r = 0\), \(A_\theta = 0\), and \(A_\phi = \frac{Q_m}{4\pi \mu_0 r}\). Substituting these into the curl formula, we get:

$$
\nabla \times \mathbf{A} = \frac{1}{r \sin \theta} \left( \frac{\partial}{\partial \theta} \left( \frac{Q_m}{4\pi \mu_0 r} \sin \theta \right) - \frac{\partial 0}{\partial \phi} \right) \hat{\mathbf{r}} + \frac{1}{r} \left( \frac{\partial 0}{\partial \phi} - \frac{\partial}{\partial r} \left( \frac{Q_m}{4\pi \mu_0 r} \right) \right) \hat{\mathbf{\theta}} + \frac{1}{r \sin \theta} \left( \frac{\partial 0}{\partial r} - \frac{\partial 0}{\partial \theta} \right) \hat{\mathbf{\phi}}
$$

Simplifying each term, we get:

$$
\nabla \times \mathbf{A} = \frac{1}{r \sin \theta} \left( \frac{Q_m \cos \theta}{4\pi \mu_0 r} \right) \hat{\mathbf{r}} + \frac{1}{r} \left( 
***
### intput: 
9. 将一磁导率为 $\mu$ 半径为 $\mathbf{R}_{0}$ 的球体 放入均匀磁场 $\vec{H}_{0}$ 内 求总磁感应强度 $\vec{B}$ 和诱导磁矩m
### standard: 
解 根据题意 以球心为原点建立球坐标 取 $\vec{H}_{0}$ 的方向为 $\vec{e}_{z}$ 此球体在外界存在的磁场的影响下极化 产生一个极化场 并与外加均匀场相互作用 最后达到平衡 保持在一个静止的状态呈现球对称  本题所满足的定解问题为  $$\begin{array}{r l}&{\left\{\nabla^{2}\varphi_{m_{1}}=0,R<R_{0}\right.}\\ &{\left.\left$$\nabla^{2}\varphi_{m_{2}}=0,R>R_{0}\right.\right.}\\ &{\left.\left\{\varphi_{m_{1}}=\varphi_{m_{2}},\mu\frac{\partial\varphi_{m_{1}}}{\partial R}=\mu_{0}\,\frac{\partial\varphi_{m_{2}}}{\partial R},(R=R_{0})\right.\right.}\\ &{\left.\left.\left(\varphi_{m_{1}}\right|_{R=0}<\infty}\\ &{\left.\varphi_{m_{2}}\right|_{R=\infty}=-H_{0}R\cos\theta\right.\right.}\end{array}$$  由泛定方程和两个自然边界条件得  $$\varphi_{m_{1}}=\sum_{n=0}^{\infty}a_{n}R^{n}P_{n}(\cos\theta)$$  $$\varphi_{m_{2}}=-H_{0}R\cos\theta+\sum_{n=0}^{\infty}\frac{d_{n}}{R^{n+1}}P_{n}(\cos\theta)$$  由两个边界条件有  $$\begin{array}{r l}&{\displaystyle\left$$\sum_{n=0}^{\infty}a_{n}R_{0}^{n}P_{n}(\cos\theta)=-H_{0}R_{0}\cos\theta+\sum_{n=0}^{\infty}\frac{d_{n}}{R_{0}^{n+1}}P_{n}(\cos\theta)\right.}\\ &{\displaystyle\left.\left$$\mu\sum_{n=1}^{\infty}a_{n}n R_{0}^{n-1}P_{n}(\cos\theta)=-H_{0}\mu_{0}\cos\theta-\mu_{0}\sum_{n=0}^{\infty}\frac{(n+1)d_{n}}{R_{0}^{n+2}}P_{n}(\cos\theta)\right$$\right.}\end{array}$$  得  $$\left\{d_{1}=\displaystyle-\frac{3\mu_{0}H_{0}}{\mu+2\mu_{0}}\right.~~~~}\\ {\displaystyle d_{1}=\displaystyle\frac{\mu-\mu_{0}}{\mu+2\mu_{0}}H_{0}R_{0}^{3}}\\ {\displaystyle a_{n}=d_{n}=0,(n\neq1)}\end{array}\right.$$  $$\left\{\begin{array}{l l}{\displaystyle a_{n}=d_{n}=0,(n\neq1)}\\ {\displaystyle}\\ {\displaystyle}\\ {\displaystyle}\\ {\phi_{m_{1}}=-\frac{3\mu_{0}}{\mu+2\mu}H_{0}R\cos\theta,R<R_{0}}\\ {\displaystyle}\\ {\displaystyle}\\ {\varphi_{m_{2}}=-H_{0}R\cos\theta+\frac{\mu-\mu_{0}}{\mu+2\mu_{0}}\cdot\frac{R_{0}^{3}}{R^{2}}H_{0}\cos\theta,R>R_{0}}\\ {\displaystyle}\\ {\displaystyle}\\ {\displaystyle}\left$$\bar{H}_{1}=-\nabla\varphi_{m_{1}}-\frac{3\mu_{0}}{\mu+2\mu_{0}}H_{0}\cos\theta\hat{e}_{r}-\frac{3\mu_{0}}{\mu+2\mu}H_{0}\sin\theta\hat{e}_{\theta}-\frac{3\mu_{0}}{\mu+2\mu}\bar{H}_{0}\cos\theta\right$$_{0}}\\ {\displaystyle}\\ {\displaystyle\bar{B}_{1}=\mu\bar{H}_{1}=\frac{3\mu\mu_{0}}{\mu+2\mu_{0}}\bar{H}_{0}}\end{array}\right.\,$$  $$\begin{array}{r l}&{\Biggl$$\vec{H}_{2}=-\nabla\varphi_{m_{2}}=$$1+\frac{\mu-\mu_{0}}{\mu+2\mu_{0}}\cdot\frac{2R_{0}^{3}}{R^{3}}$$H_{0}\cos\theta\vec{e}_{r}-$$1-\frac{\mu-\mu_{0}}{\mu+2\mu_{0}}\cdot\frac{R_{0}^{3}}{R^{3}}$$H_{0}\sin\theta\vec{e}_{\theta}}\\ &{=\vec{H}_{0}+\frac{\mu-\mu_{0}}{\mu+2\mu_{0}}R_{0}^{3}$$\frac{3(\vec{H}_{0}\cdot\vec{R})\vec{R}}{R^{5}}-\frac{\vec{H}_{0}}{R^{3}}$$}\\ &{\Biggr|\vec{B}_{2}=\mu_{0}\vec{H}_{2}=\mu_{0}\vec{H}_{0}+\frac{\mu-\mu_{0}}{\mu+2\mu_{0}}\mu_{0}R_{0}^{3}$$\frac{3(\vec{H}_{0}\cdot\vec{R})\vec{R}}{R^{5}}-\frac{\vec{H}_{0}}{R^{3}}$$}\end{array}$$  $$\therefore\vec{B}=\left\{\!\!\begin{array}{l l}{\displaystyle3\mu\mu_{0}}&{\quad}\\ {\displaystyle\mu+2\mu_{0}}&{\quad}\\ {\displaystyle\mu_{0}\vec{H}_{0}+\frac{\mu-\mu_{0}}{\mu+2\mu_{0}}\mu_{0}R_{0}^{3}$$\frac{3(\vec{H}_{0}\cdot\vec{R})\vec{R}}{R^{5}}-\frac{\vec{H}_{0}}{R^{3}}$$,(R>R_{0})}\end{array}\!\!\right.$$  当 $\vec{B}$ 在 ${\bf R}{\bf>}{\bf R}_{0}$ 时 表达式中的第二项课看作一个磁偶极子产生的场  ∴ϕ中 0 $\mathrm{\Delta}^{\sharp}\frac{\mu-\mu_{0}}{\mu+2\mu_{0}}\,\mathrm{\cdot}\,\frac{R_{0}^{3}}{R^{2}}H_{0}\cos{\alpha}$ $\theta$ 可看作偶极子 $\bar{m}$ 产生的势m2即 ${\frac{1}{4\pi}}\cdot{\frac{{\vec{m}}\cdot{\vec{R}}}{R^{3}}}={\frac{\mu-\mu_{0}}{\mu+2\mu_{0}}}\cdot{\frac{R_{0}^{3}}{R^{2}}}H_{\mathrm{0}}\cos\theta={\frac{\mu-\mu_{0}}{\mu+2\mu_{0}}}\cdot{\frac{R_{0}^{3}}{R^{2}}}\,{\vec{H}}_{0}\cdot{\vec{R}}$ $\therefore\vec{m}=4\pi\frac{\mu-\mu_{0}}{\mu+2\mu_{0}}\cdot R_{0}^{3}\vec{H}$
### output: 
.
为了求出将磁导率为 \(\mu\) 半径为 \(R_0\) 的球体放入均匀 magnetic 场 \(\vec{H}_0\) 内时的总磁感应场 \(\vec{B}\) 和ifiers 磁矩 \(\vec{m}\)，我们将遵循以下步骤：

1. **确定均匀磁场中的 induction 磁矩：**
   当一个 diamagnetic 材料 placed 在均匀磁场中时，它会由于其不导磁性而产生 induced 磁矩。 induced 磁矩 \(\vec{m}\) 可以表示为：
   $$
   \vec{m} = -\nabla \left( \frac{\mu}{4\pi r^3} \right)
   $$
   对于半径为 \(R_2\) 的球体在均匀外场 \(\vec{H}_0\) 中，induced 磁矩 \(\vec{m}\) 给定为：
   $$
   \vec{m} = \frac{\mu - \mu_0}{\mu_0} V H_0
   $$
   其中 \(V\) 是球体的体积，\(H_0\) 是 uniform 外场的大小。对于半径为 \(R_0\) 的球体，体积 \(V\) 为：
   $$
   V = \frac{4}{3} \pi R_0^3
   $$

2. **计算 induced 磁矩：**
   将体积 \(V\) 代入 induced 磁矩公式：
   $$
   \vec{m} = \frac{\mu - \mu_0}{\mu_0} \cdot \frac{4}{3} \pi R_0^3 \cdot \vec{H}_0
   $$

3. **确定内部总磁 induction：**
   总磁 induction \(\vec{B}\) 是外部场 \(\vec{H}_0\) 和由 induced 磁矩产生的 internal 场 \(\vec{H}\) 的向量和。internal 场 \(\vec{H}\) 可以使用 permeability 的关系 \(\vec{B} = \mu \vec{H}\) 表示。
   external 场对球体 surface 的贡献为 \(\vec{H}_0\)，而 internal 场由 induced 磁矩 \(\vec{m}\) 通过安培环路定律给出：
   $$
   \vec{H} = -\nabla \left( \frac{\mu_0 m}{3 \mu} \right)
   $$
   对于均匀 magnetic 磁矩 \(\vec{m}\)，internal 场 \(\vec{H}\) 为：
   $$
   \vec{H} = -\frac{\mu - \mu_0}{\mu} \cdot \frac{4}{3} \pi R_0^5 H_0 \cdot \nabla \left( \frac{1}{r^3} \right)
   $$
   进一步简化：
   $$
   \vec{H} = \frac{\mu - \mu_0}{\mu \mu_0} \cdot \frac{4}{3} \pi R_0^5 H_0 \cdot \frac{4}{r^6} (3 r^2 \hat{r})
   $$
   $$
   \vec{H} = \frac{\mu + \mu_0}{\mu \mu_0} \cdot 2 \pi R_0^3 H_0 \cdot \frac{\hat{r}}{r}
   $$
   对于球体内部，\(\vec{H} = -\frac{\mu - \mu_0}{\mu \mu_0} 2 \pi R_0^3 H_0 \cdot \frac{\vec{r}}{r} = -\vec{H}_0\)

4. **总磁 induction：**
   总磁 induction \(\vec{B}\) 是 external 场 \(\vec{H}_0\) 和 internal
***
### intput: 
10. 有一个内外半径为 $\mathbf{R}_{1}$ 和 $\mathrm{R}_{2}$ 的空心球 位于均匀外磁场 $\vec{H}_{0}$ 内球的磁导率为 $\mu$ 求空腔内的场 $\vec{B}$ 讨论 $\mu>>\mu_{0}$ 时的磁屏蔽作用
### standard: 
解根据题意以球心为原点取球坐标选取 $\vec{H}_{0}$ 的方向为 $\vec{e}_{z}$ 在外场 $\vec{H}_{0}$ 的作用下  球壳极化 产生一个附加场并与外场相互作用最后达到平衡 $\bar{B}$ 的分布呈现轴对称  定解问题  $$\begin{array}{r l}&{\left(\nabla^{2}\varphi_{m_{1}}=0,R<R_{1}\right.}\\ &{\left.\nabla^{2}\varphi_{m_{2}}=0,R_{1}<R<R_{2}\right.}\\ &{\left.\nabla^{2}\varphi_{m_{3}}=0,R>R_{3}\right.}\\ &{\left.\varphi_{m_{1}}=\varphi_{m_{2}}\right|_{R\times R_{1}},\varphi_{m_{2}}=\varphi_{m_{3}}\Big|_{R\times R_{2}}}\\ &{\left.\mu_{0}\frac{\partial\varphi_{m_{1}}}{\partial R}=\mu\frac{\partial\varphi_{m_{2}}}{\partial R}\right|_{R\times R_{1}},\mu_{0}\frac{\partial\varphi_{m_{3}}}{\partial R}=\mu\frac{\partial\varphi_{m_{2}}}{\partial R}\Big|_{R\times R_{2}}}\\ &{\left.\varphi_{m_{1}}\right|_{R=0}<\infty}\\ &{\left.\varphi_{m_{1}}\right|_{R\times\infty}=-H_{0}R\cos{\theta}}\end{array}$$  由于物理模型为轴对称再有两个自然边界条件故三个泛定方程的解的形式为  $$\varphi_{m_{1}}=\sum_{n=0}^{\infty}a_{n}R^{n}P_{n}(\cos\theta)$$  $$\varphi_{m_{2}}=\sum_{n=0}^{\infty}(b_{n}R^{n}+{\frac{c_{n}}{R^{n+1}}})P_{n}(\cos\theta)$$  $$\varphi_{m_{3}}=-H_{0}R\cos\theta+\sum_{n=0}^{\infty}\frac{d_{n}}{R^{n+1}}P_{n}(\cos\theta)$$  因为泛定方程的解是把产生磁场的源 $\vec{H}_{0}$ 做频谱分解而得出的 分解所选取的基本函数系是其本征函数系 $\{P_{n}(\cos\theta)\}$ 在本题中源的表示是  $$-\,H_{0}R\cos\theta=-H_{0}R P_{1}(\cos\theta)$$  所以上面的解中 $a_{_n}=b_{_n}=c_{_n}=d_{_n}=0,(n\neq0)$  故 解的形式简化为  $$\begin{array}{l}{{\displaystyle\varphi_{{\scriptscriptstyle m}_{1}}=a_{1}R\cos\theta}}\\ {~~}\\ {{\displaystyle\varphi_{{\scriptscriptstyle m}_{2}}=(b_{1}R+\frac{c_{1}}{R^{2}})\cos\theta}}\\ {~~}\\ {{\displaystyle\varphi_{{\scriptscriptstyle m}_{3}}=-H_{0}R\cos\theta+\frac{d_{1}}{R^{2}}\cos\theta}}\end{array}$$  代入衔接条件得  $$\left\{\begin{array}{l l}{a_{1}R_{1}=b_{1}R_{1}+\displaystyle\frac{c_{1}}{R_{1}^{2}}}\\ {b_{1}R_{2}+\displaystyle\frac{c_{1}}{R_{2}^{2}}=-H_{0}R_{2}+\displaystyle\frac{d_{1}}{R_{2}^{2}}}\\ {a_{1}\mu_{0}=\mu(b_{1}-\displaystyle\frac{2c_{1}}{R_{1}^{3}})}\\ {-\mu_{0}H_{0}-\mu\displaystyle\frac{2d_{1}}{R_{2}^{3}}=\mu(b_{1}-\displaystyle\frac{2c_{1}}{R_{2}^{3}})}\end{array}\right.$$  解方程组得  $$\begin{array}{l}{{a_{1}=\displaystyle\frac{3\mu_{0}(2\mu+\mu_{0})H_{0}R_{2}^{3}+3\mu_{0}(\mu-\mu_{0})H_{0}R_{2}^{3}}{2(\mu-\mu_{0})^{2}R_{1}^{3}-(2\mu+\mu_{0})(2\mu_{0}+\mu)R_{2}^{3}}}}\\ {{\displaystyle b_{1}=\frac{3\mu_{0}(2\mu+\mu_{0})H_{0}R_{2}^{3}}{2(\mu-\mu_{0})^{2}R_{1}^{3}-(2\mu+\mu_{0})(2\mu_{0}+\mu)R_{2}^{3}}}}\\ {{\displaystyle c_{1}=\frac{3\mu_{0}(\mu-\mu_{0})H_{0}R_{2}^{3}R_{1}^{3}}{2(\mu-\mu_{0})^{2}R_{1}^{3}-(2\mu+\mu_{0})(2\mu_{0}+\mu)R_{2}^{3}}}}\\ {{\displaystyle d_{1}=\frac{3\mu_{0}(2\mu+\mu_{0})H_{0}R_{2}^{6}+3\mu_{0}(\mu-\mu_{0})H_{0}R_{2}^{3}R_{1}^{3}}{2(\mu-\mu_{0})^{2}R_{1}^{3}-(2\mu+\mu_{0})(2\mu_{0}+\mu_{0})R_{2}^{3}}+H_{0}R_{2}^{3}}}\end{array}$$  而 $\vec{B}_{i}=\mu_{0}\vec{H}_{i}=-\mu_{0}\nabla\varphi_{m_{i}},(i=1,2,3)$  $\therefore\vec{B}_{1}=-\mu_{0}a_{1}\vec{e}_{z}$ $=$$1-\frac{1-(\cfrac{R_{1}}{R_{2}})^{3}}{\cfrac{(\mu+2\mu_{0})(2\mu+\mu_{0})}{2{(\mu-\mu_{0})}^{2}}-{(\cfrac{R_{1}}{R_{2}})}^{3}}$$\mu_{0}\vec{H}_{0}$   当 $\mu>>\mu_{0}$ 时$\frac{(\mu+2\mu_{0})(2\mu+\mu_{0})}{2{(\mu-\mu_{0})}^{2}}\approx1$   $\therefore{\bar{B}}_{1}=0$  即球壳腔中无磁场类似于静电场中的静电屏障
### output: 
.
$$
$$

To solve the problem of finding the magnetic field \(\vec{B}\) inside an empty spherical shell of inner radius \(R_1\) and outer radius \(R_2\) placed in a uniform external magnetic field \(\vec{H}_0\) with permeability \(\mu\), we will follow these steps:

1. **Understand the Problem**: We have a diamagnetic material (since \(\mu < \mu_0\)) sphere with a empty cavity. The external magnetic field \(\vec{H}_0\) is uniform.

2. **Magnetization of the Material**: When a diamagnetic material is placed in an external magnetic field, it gets polarized such that the magnetization density \(\vec{M}\) is proportional to the external field \(\vec{H}_0\). The relationship is given by:
   $$
   \vec{M} = \frac{\mu - \mu_0}{\mu_0} \vec{H}
   $$
   where \(\mu\) is the permeability of the material and \(\mu_0\) is the permeability of free space.

3. ** Lisa's Law**: Inside any diamagnetic material, the total magnetic field \(\vec{B}\) is related to the external field \(\vec{H}_0\) and the magnetization density \(\vec{M}\) by:
   $$
   \vec{B} = \mu_0 (\vec{H}_0 + \vec{M})
   $$
   Substituting the expression for \(\vec{M}\):
   $$
   \vec{B} = \mu_0 \left( \vec{H}_0 + \frac{\mu - \mu_0}{\mu_0} \vec{H}_0 \right)
   $$
   Simplifying this, we get:
   $$
   \vec{B} = \mu_0 \left( \vec{H}_0 + \frac{\mu}{\mu_0} \vec{H}_0 - \vec{H}_0 \right) = \mu_0 \left( \frac{\mu}{\mu_0} \vec{H}_0 \right) = \mu \vec{H}_0
   $$

4. **Consider the Empty Cavity**: The presence of the empty cavity does not affect the magnetic field outside the shell because the diamagnetic material exerts a force on itself due to its own induced dipole moments, which cancel out each other when considered over the entire volume of the material. However, inside the cavity, there are no induced dipole moments, so the magnetic field is zero.

5. ** discussed the Magnetic Screenings**: When \(\mu >> \mu_0\), the permeability of the material is much greater than the permeability of free space. This means that the magnetic field inside the material is significantly reduced compared to the external field. In fact, if \(\mu\) were infinite, the internal field would be zero.

Therefore, the magnetic field inside the empty spherical shell is effectively zero when \(\mu >> \mu_0\).

The final answer is:
$$
\boxed{0}
$$
***
### intput: 
11. 设理想铁磁体的磁化规律为 $\vec{B}=\mu\vec{H}+\mu_{0}M_{0},M$ $M_{0}$ 是恒定的与 $\vec{H}$ 无关的量 今将一个理想铁磁体做成均匀磁化球 $M_{0}$ 为常值 浸入磁导率为 $\mu^{\prime}$ 的无限介质中 求磁感应强度和磁化电流分布
### standard: 
解根据题意取球心为原点做球坐标以 $\vec{M}_{0}$ 的方向为 $\vec{e}_{z}$ 本题具有球对称的磁场分布满足的定解问题为  $$\begin{array}{r l}&{\left$$\nabla^{2}\varphi_{m_{1}}=0,R<R_{0}\right.}\\ &{\left.\nabla^{2}\varphi_{m_{2}}=0,R>R_{0}\right.}\\ &{\left.\varphi_{m_{1}}=\varphi_{m_{2}}\right|_{R=R_{0}},}\\ &{\left.\mu\frac{\partial\varphi_{m_{1}}}{\partial R}-\mu^{\prime}\frac{\partial\varphi_{m_{2}}}{\partial R}\right|_{R_{0}}=M_{0}\mu_{0}\cos\theta}\\ &{\left.\varphi_{m_{1}}\right|_{R=0}<\infty}\\ &{\left.\varphi_{m_{2}}\right|_{R=\infty}=0}\end{array}$$  $$\therefore\,\varphi_{m_{1}}=\sum_{n=0}^{\infty}a_{n}R^{n}P_{n}(\cos\theta)$$  $$\varphi_{m_{2}}=\sum_{n=0}^{\infty}(\frac{b_{n}}{R^{n+1}})P_{n}(\cos\theta)$$  代入衔接条件对比 $P_{n}(\cos\theta)$ 对应项前的系数得  $$a_{n}=b_{n}=0,(n\neq1)\,,\;\;a_{1}\;=\;\frac{\mu_{\mathrm{~0~}}M_{\mathrm{~0~}}}{2\,\mu^{\mathrm{~\prime~}}+\;\mu}\;,\;\;b_{1}=\frac{\mu_{0}M_{\mathrm{~0~}}}{2\mu^{\prime}+\mu}R_{\mathrm{~0~}}^{3}$$  $$\therefore\varphi_{m_{1}}=\frac{\mu_{0}M_{0}}{2\mu^{\prime}+\mu}R\cos\theta,(R<R_{0})$$  $$\varphi_{m_{2}}=\frac{\mu_{0}M_{0}}{2\mu^{\prime}+\mu}\frac{R_{0}^{3}}{R^{2}}\cos\theta,(R>R_{0})$$  由此 $R<R_{0},\vec{B}_{1}=\mu\vec{H}_{1}+\mu_{0}\vec{M}_{0}=\frac{2\mu^{\prime}\mu_{0}\vec{M}_{0}}{2\mu^{\prime}+\mu}$  $$R>R_{0},\ \ \vec{B}_{2}=-\mu^{\prime}\nabla\varphi_{m_{2}}=\frac{\mu^{\prime}\mu_{0}R_{0}^{3}}{2\mu^{\prime}+\mu}$$\frac{3(\vec{M}_{0}\cdot\vec{R})\vec{R}}{R^{5}}-\frac{\vec{M}_{0}}{R^{3}}$$$$  $$\therefore\vec{B}=\left\{\frac{2\mu^{\prime}\mu_{0}\vec{M}_{0}}{2\mu^{\prime}+\mu},(R<R_{0})\right.$$  又 $\vec{n}\times\left(\vec{B}_{2}-\vec{B}_{1}\right)\Big|_{R_{0}}=\mu_{0}(\vec{\alpha}_{M}+\vec{\alpha}),$ 其中 $\scriptstyle{\vec{\alpha}}=0$  代入 $\vec{B}$ 的表达式得  $$\scriptstyle\vec{\alpha}_{_{M}}=-\frac{3\mu^{\prime}}{2\mu^{\prime}+\mu_{_{0}}}M_{\mathrm{{0}}}\sin\theta\vec{e}_{\varphi}$$
### output: 
.
$$
To solve the problem of finding the magnetic induction field and magnitudes distribution in a uniformly polarized iron sphere placed in a medium with permittivity \(\mu'\), we will follow these steps:

1. **Determine the Magnetic Field Inside the Sphere:**
   Given the magnetization pattern \(\vec{B} = \mu \vec{H} + \mu_0 M_0\) for an ideal ferromagnetic material, where \(M_0\) is a constant vector independent of \(\vec{H}\).

2. **Express the Magnetic Field in Terms of$", \(\vec{H}\), and \(M_0\):**
   Since the sphere is uniformly polarized, the magnetization \(\vec{M}\) is uniform throughout the volume of the sphere. Let \(R\) be the radius of the sphere.

3. **Use theGAUSS's Law for Magnitudes:**
   For a spherical symmetry, the electric field \(\vec{E}\) due to the bound charges can be found using Gauss's law:
   $$
   \nabla \cdot \vec{D} = \rho_f
   $$
   where \(\vec{D} = \epsilon_0 E + P\) and \(P = \chi_e E\). Here, \(\epsilon_0\) is the permittivity of free space, \(\rho_f\) is the free charge density, and \(\chi_e\) is the electric Susceptibility.

4. **Relate Susceptibility to Permeability:**
   For an ideal ferromagnetic material, the permeability \(\mu\) is given by:
   $$
   \mu = \mu_0 (1 + \chi_m)
   $$

5. **Solve for the Electric Field:**
   The total scalar potential \(\phi\) inside the sphere is:
   $$
   V = -\int (\sigma_f + \rho_b) dV
   $$

6. **Consider the Medium and the Ferromagnet:**
   The medium has permability \(\mu'\). Therefore, outside the sphere, the total magnetic field \(\vec{B}\) is:
   $$
   \vec{B}_{\text{outside}} = \mu' H
   $$

7. **Apply boundary conditions:**
   At the surface of the sphere (r = R):
   $$
   B_{\text{inside}}(R) = B_{\text{outside}}(R)
   $$
   $$
   \mu H_{\text{inside}}(R) + \mu_0 M_0 = \mu' H_{\text{inside}}(R)
   $$
   Solving for \(H_{\text{inside}}(R)\):
   $$
   (\mu - \mu') H_{\text{inside}}(R) = -\mu_0 M_0
   $$
   $$
   H_{\text{inside}}(R) = -\frac{\mu_0 M_0}{\mu - \mu'}
   $$

8. **Find the Total Magnetic Field Inside the Sphere:**
   Using \(\vec{B} = \mu \vec{H} + \mu_0 M_0\):
   $$
   \vec{B}_{\text{inside}} = \mu \left(-\frac{\mu_0 M_0}{\mu - \mu'}\right) + \mu_0 M_0
   $$
   Simplify:
   $$
   \vec{B}_{\text{inside}} = -\frac{\mu \mu_0 M_0}{\mu - \mu'} + \mu_0 M_0
   $$
   Factor out \(\mu_0 M_0\):
   $$
   \vec{B}_{\text{inside}} = \mu_0 M_0 \left(1 - \frac{\mu}{\mu - \mu'}\right)
   $$
   Simplify further:

***
### intput: 
12. 将上题的永磁球置入均匀外磁场 $\vec{H}_{0}$ 中结果如何
### standard: 
解根据题意假设均匀外场 $\vec{H}_{0}$ 的方向与 $\vec{M}_{0}$ 的方向相同定为坐标 ${\mathbf Z}$ 轴方向定解问题为  $$\begin{array}{r l}&{\left$$\nabla^{2}\varphi_{m_{1}}=0,R<R_{0}\right.}\\ &{\left.\nabla^{2}\varphi_{m_{2}}=0,R>R_{0}\right.}\\ &{\left.\varphi_{m_{1}}=\varphi_{m_{2}}\right|_{R=R_{0}},}\\ &{\left.\mu\frac{\partial\varphi_{m_{1}}}{\partial R}-\mu_{0}\frac{\partial\varphi_{m_{2}}}{\partial R}\right|_{R_{0}}=M_{0}\mu_{0}\cos{\theta}}\\ &{\left.\varphi_{m_{1}}\right|_{R=0}<\infty}\\ &{\left.\varphi_{m_{2}}\right|_{R=\infty}=-H_{0}R\cos{\theta}}\end{array}$$  解得满足自然边界条件的解是  $$\begin{array}{l}{{\displaystyle\varphi_{m_{1}}=a_{1}R\cos\theta,(R<R_{0})}}\\ {~~}\\ {{\displaystyle\varphi_{m_{2}}=-H_{0}R\cos\theta+\frac{d_{1}}{R^{2}}\cos\theta,(R>R_{0})}}\end{array}$$  代入衔接条件  $$\begin{array}{l}{{a_{1}R_{0}=-H_{0}R_{0}+\displaystyle\frac{d_{1}}{R_{0}^{2}}}}\\ {{\displaystyle\mu_{0}H_{0}+\mu_{0}\displaystyle\frac{2d_{1}}{R_{0}^{3}}{}+\mu a_{1}=\mu_{0}M_{0}}}\end{array}$$  得到 $a_{1}=\frac{\mu_{0}M_{0}-3\mu_{0}H_{0}}{\mu+2\mu_{0}}$  $$d_{1}=\frac{\mu_{0}M_{0}+(\mu-\mu_{0})H_{0}}{\mu+2\mu_{0}}R_{0}^{3}$$  $$\therefore\varphi_{m_{1}}=\frac{\mu_{0}M_{0}-3\mu_{0}H_{0}}{\mu+2\mu_{0}}R\cos\theta,(R<R_{0})$$  $$\varphi_{m_{2}}=-H_{0}R\cos\theta+\frac{\mu_{0}M_{0}+(\mu-\mu_{0})H_{0}}{\mu+2\mu_{0}}\frac{R_{0}^{3}}{R^{2}}\mathrm{cos}\theta,(R>R_{0})$$  $$\begin{array}{l}{{\displaystyle\therefore\,\vec{H}_{1}=-\nabla\varphi_{m_{1}}=-$$\frac{\mu_{0}M_{0}-3\mu_{0}H_{0}}{\mu+2\mu_{0}}\cos\theta\bar{e}_{r}-\frac{\mu_{0}M_{0}-3\mu_{0}H_{0}}{\mu+2\mu_{0}}\sin\theta\bar{e}_{\theta}$$}\ ~}\\ {{\displaystyle~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\mu+\frac{\mu_{0}M_{0}}{\mu}\bar{\theta}_{0}}}\\ {{\displaystyle~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=-\frac{\mu_{0}\vec{M}_{0}-3\mu_{0}\vec{H}_{0}}{2\mu_{0}+\mu}}}\end{array}$$  $$\vec{B}_{1}\!=\mu\vec{H}+\mu_{0}\vec{M}_{0}=\frac{3\mu\mu_{0}}{\mu+2\mu_{0}}\vec{H}_{0}+\frac{2\mu_{0}^{2}}{\mu+2\mu_{0}}\vec{M}_{0},(R<R_{0})$$  $$\vec{H}_{2}=-\nabla\varphi_{m_{2}}=-$$(-H_{0}\cos\theta-\frac{\mu_{0}M_{0}+(\mu-\mu_{0})H_{0}}{\mu+2\mu_{0}}\frac{2R_{0}^{3}}{R^{2}}\cos\theta)\vec{e}_{r}-\frac{\mu_{0}M_{0}}{R^{3}}$$\vec{e}_{r}\,.$$  $$-\left(-H_{0}\sin\theta+\frac{\mu_{0}M_{0}+(\mu-\mu_{0})H_{0}}{\mu+2\mu_{0}}\frac{R_{0}^{3}}{R^{2}}\sin\theta\right)\!\vec{e}_{\theta}\right$$=\vec{H}_{0}+\frac{3(\vec{m}\cdot\vec{R})\vec{R}}{R^{5}}-\frac{\vec{m}}{R^{3}}$$  $$\vec{B}_{2}=\mu_{0}\vec{H}_{2}=\mu_{0}$$\vec{H}_{0}+\frac{3(\vec{m}\cdot\vec{R})\vec{R}}{R^{5}}-\frac{\vec{m}}{R^{3}}$$\,,\ \ \vec{m}=\frac{\mu_{0}\vec{M}_{0}}{\mu+2\mu_{0}}R_{0}^{3}+\frac{\mu-\mu_{0}}{\mu+2\mu_{0}}R_{0}^{3}\vec{H}_{0}$$
### output: 
？上题中的条件如下：一个半径为 $R$ 的导体球，其_permittivity permability 值分别为 $\epsilon_{r}$ 和 $\mu_{r}$。当该球被 polarized时，它将出现 electric field $\vec{E}$ 和 magnetic field $\vec{B}$。
当我们将这个永磁球置入均匀外磁场 $\vec{H}_{0}$ 中时，我们需要考虑 magnetization of the sphere and how it affects the total magnetic field inside the sphere. The magnetization \(\vec{M}\) of a diametrically polarized sphere in an external field \(\vec{H}_0\) is given by:
$$
\vec{M} = k \vec{H}_0
$$
where \(k\) is a constant that depends on the material properties of the sphere. For a linear dielectric, \(k\) can be expressed as:
$$
k = \frac{\mu_r - 1}{\mu_r + 1}
$$

The total magnetic field \(\vec{B}\) inside the sphere is related to the magnetic field strength \(\vec{H}\) by the equation:
$$
\vec{B} = \mu_0 (\vec{H} + \vec{M})
$$
Substituting \(\vec{M} = k \vec{H}_0\) into this equation, we get:
$$
\vec{B} = \mu_0 (\vec{H} + k \vec{H}_0)
$$
Since \(\vec{H} = \vec{H}_0 - \nabla \times \vec{A}\), where \(\vec{A}\) is the vector potential, we have:
$$
\vec{B} = \mu_0 \left( \vec{H}_0 - \nabla \times \vec{A} + k \vec{H}_0 \right) = \mu_0 (1 + k) \vec{H}_0 - \mu_0 \nabla \times \vec{A}
$$

For a diametrically polarized sphere, the vector potential \(\vec{A}\) is zero outside the sphere. Therefore, the total magnetic field inside the sphere simplifies to:
$$
\vec{B} = \mu_0 (1 + k) \vec{H}_0 = \mu_0 \left( 1 + \frac{\mu_r - 1}{\mu_r + 1} \right) \vec{H}_0 = \mu_0 \left( \frac{\mu_r + 1 + \mu_r - 1}{\mu_r + 1} \right) \vec{H}_0 = \mu_0 \left( \frac{2\mu_r}{\mu_r + 1} \right) \vec{H}_0 = \frac{2\mu_0 \mu_r}{\mu_r + 1} \vec{H}_0
$$

Thus, the total magnetic field inside the sphere when it is placed in a uniform external field \(\vec{H}_0\) is:
$$
\boxed{\frac{2\mu_0 \mu_r}{\mu_r + 1} \vec{H}_0}
$$
***
### intput: 
13. 有一个均匀带电的薄导体壳 其半径为 $\mathrm{R}_{0}$ 总电荷为 $\mathrm{Q}$ 今使球壳绕自身某一直径以角速度 $\omega$ 转动 求球内外的磁场 $\vec{B}$ 0  提示本题通过解 $\vec{A}$ 或 $\varphi_{\mathrm{m}}$ 的方程都可以解决 也可以比较本题与 $\S\ S$ 例2 的电流分布得到结果
### standard: 
解根据题意取球体自转轴为 ${\mathbf Z}$ 轴 建立坐标系  定解问题为  $$\begin{array}{r l}&{\left$$\nabla^{2}\varphi_{m_{1}}=0,R<R_{0}\right.}\\ &{\left.\nabla^{2}\varphi_{m_{2}}=0,R>R_{0}\right.}\\ &{\left.\displaystyle\frac{1}{R_{0}}(\frac{\partial\varphi_{m_{2}}}{\partial\theta}-\frac{\partial\varphi_{m_{1}}}{\partial\theta})=-\frac{Q\omega\sin\theta}{4\pi R_{0}}\right\vert_{R=R_{0}}}\\ &{\left.\displaystyle\mu\frac{\partial\varphi_{m_{1}}}{\partial R}=\mu_{0}\,\frac{\partial\varphi_{m_{2}}}{\partial R},(R=R_{0})\right.}\\ &{\left.\varphi_{m_{1}}\left\vert_{R=0}<\infty\right.}\\ &{\left.\varphi_{m_{2}}\left\vert_{R=\infty}=0\right.}\end{array}$$  其中 $\sigma=\frac{Q\omega\sin{\theta}}{4\pi R_{\mathrm{0}}}$ 是球壳表面自由面电流密度  解得满足自然边界条件的解为  $$\begin{array}{c}{{\varphi_{m_{1}}=a_{1}R\cos\theta,(R<R_{0})}}\\ {{\mathrm{}}}\\ {{\varphi_{m_{2}}=\displaystyle\frac{b_{1}}{R^{2}}\cos\theta,(R>R_{0})}}\end{array}$$  $$\left\{a_{1}R_{0}-\frac{b_{1}}{R_{0}^{2}}=-\frac{Q\omega}{4\pi R_{0}}\right.$$  $$a_{1}=-{\frac{Q\omega}{6\pi R_{0}}}\,,\ \ \ \ \ \ \ \ b_{1}={\frac{Q\omega R_{0}^{2}}{12\pi}}$$  $$\therefore\varphi_{m_{1}}=-{\frac{Q\omega}{6\pi R_{0}}}R\cos\theta,(R<R_{0})$$  $$\varphi_{m_{2}}=\frac{Q\omega R_{0}^{2}}{12\pi R^{2}}\mathrm{cos}\theta,(R>R_{0})$$  $$\therefore\vec{H}_{1}=-\nabla\varphi_{m_{1}}=\frac{Q\omega}{6\pi R_{0}}\cos\theta\vec{e}_{r}-\frac{Q\omega}{6\pi R_{0}}\sin\theta\vec{e}_{\theta}=\frac{Q\vec{\omega}}{6\pi R_{0}}$$  $$\vec{B}_{1}=\mu_{0}\vec{H}_{1}=\frac{Q\mu_{0}}{6\pi R_{0}}\vec{\omega}$$  $$\vec{H}_{2}=-\nabla\varphi_{m_{2}}=\frac{2Q\omega R_{0}^{2}}{12\pi R^{3}}\cos\theta\vec{e}_{r}+\frac{Q\omega R_{0}^{2}}{12\pi R^{3}}\sin\theta\vec{e}_{r}=\frac{1}{4\pi}$$\frac{3(\vec{m}\cdot\vec{R})\vec{R}}{R^{5}}-\frac{\vec{m}}{R^{3}}$$$$  $$\vec{m}=\frac{Q R_{0}^{2}}{3}\vec{\omega}$$  $$\vec{B}_{2}=\mu_{0}\vec{H}_{2}=\frac{\mu_{0}}{4\pi}$$\frac{3(\vec{m}\cdot\vec{R})\vec{R}}{R^{5}}-\frac{\vec{m}}{R^{3}}$$$$
### output: 
).
答案:
为了找到一个均匀带电的薄导体壳绕自身某一直径以角速度 \(\omega\) 转动时球内外的磁场 \(\vec{B}\)，我们可以使用 magnon-potential方法。这个问题可以通过解 vector potential \(\vec{A}\) 或 scalar potential of the magnetic field \(\varphi_m\) 来解决，或者比较它与 Example 2 中的电流分布得到结果。

首先，让我们回顾 Example 2 的结果，其中我们考虑了在圆柱形导体中通有恒定 current density 的情况。在 cylindrical coordinates 中，vector potential \(\vec{A}\) 对于无限长圆柱导体可以表示为：

$$
\vec{A} = \frac{\mu_0 I}{4\pi r} \hat{\phi}
$$

对于 uniformly charged sphere， charge density \(\rho\) 由下式给出：

$$
\rho = \frac{3Q}{4\pi R_0^3}
$$

当球壳以角速度 \(\omega\) 绕自身某一直径旋转时，它 will 产生一个(current density \(\vec{j}\) 由下式给出：

$$
\vec{j} = \rho \vec{v} = \rho (\omega \times \vec{r})
$$

由于球对称且正在绕 diameter 旋转，current density \(\vec{j}\) 是 axially symmetric and perpendicular to the radius vector \(\vec{r}\). 这意味着 current density 可以写成：

$$
\vec{j} = J(r) \hat{\phi}
$$

其中 \(J(r)\) 是 radius \(r\) 处的 current density。为了找到 \(J(r)\)，我们使用连续性方程：

$$
\nabla \cdot \vec{j} = -\frac{\partial \rho}{\partial t}
$$

由于球是静止的，\(\frac{\partial \rho}{\partial t} = 0\)，所以：

$$
\nabla \cdot \vec{j} = 0
$$

对于 spherical coordinates，divergence of \(\vec{j}\) 是：

$$
\nabla \cdot \vec{j} = \frac{1}{r^2} \frac{\partial}{\partial r} (r^2 J(r))
$$

将其设为零，我们得到：

$$
\frac{d}{dr} (r^2 J(r)) = 0
$$

这意味着 \(r^2 J(r)\) 是常数。设这个常数为 \(C\)，则：

$$
J(r) = \frac{C}{r^2}
$$

为了找到 \(C\)，我们使用球总 electric charge \(Q\)：

$$
Q = \int_V \rho dV = \int_0^{R_0} \int_0^\pi \int_0^{2\pi} \rho r^2 \sin\theta \, d\phi \, d\theta \, dr
$$

将 \(\rho = \frac{3Q}{4\pi R_0^3}\) 代入，我们得到：

$$
Q = \int_0^{R_0} \int_0^\pi \int_0^{2\pi} \frac{3Q}{4\pi R_0^3} r^2 \sin\theta \, d\phi \, d\theta \, dr
$$

计算积分，我们发现：

$$
Q = \frac{3Q}{4\pi R_0^3} \left( 2\pi \int_0^\pi \sin\theta \, d\theta \int_0^{R_0} r^2 \, dr \right)
$$

$$
Q = \frac{3Q}{4\pi R_0^3} \left( 2\pi $$-\cos\theta$$
***
### intput: 
14. 电荷按体均匀分布的刚性小球 其总电荷为 $\mathrm{Q}$ 半径为 $\mathbf{R}_{0}$ 它以角速度 $\omega$ 绕自身某以直径转动 求  1 它的磁矩  2 它的磁矩与自转动量矩之比 设质量 $\mathbf{M}_{0}$ 是均匀分布的
### standard: 
解 1 磁矩 $\vec{m}=\frac{1}{2}\int\vec{x}\times\vec{J}(\vec{x})d V$  $$\vec{x}=\vec{R}=\mathrm{R}\vec{\mathrm{e}}_{r}\,,\quad\vec{J}(\vec{x})=\rho\vec{\nu}=\frac{Q}{\frac{4}{3}\pi R_{0}^{3}}(\vec{\omega}\times\vec{R})$$  $$\therefore\vec{m}=\frac{1}{2}\frac{3Q}{4\pi R_{0}^{3}}\int\vec{R}\times(\vec{\omega}\times\vec{R})R^{2}\sin\theta d r d\theta d\phi=\frac{1}{2}\frac{3Q\omega}{4\pi R_{0}^{3}}\int(\vec{e}_{r}\times\vec{e}_{\phi})R^{4}\sin^{2}\theta d r d\theta d\phi$$  $\vec{e}_{r}\times\vec{e}_{\phi}=-\vec{e}_{\theta}=\sin\theta\vec{e}_{z}+\cos\theta(-\cos\phi\vec{e}_{x}-\sin\phi\vec{e}_{y})$  $$\therefore\;\vec{m}=\frac{3Q\omega}{8\pi R_{0}^{3}}\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{R_{0}}$$\sin\theta\vec{e}_{z}+\cos\theta(-\cos\phi\vec{e}_{x}-\sin\phi\vec{e}_{y})R^{4}\sin^{2}\theta d r d\theta d\phi$$  $$=\frac{3{\cal Q}\omega}{8\pi R_{0}^{3}}\,\vec{e}_{z}\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{R_{0}}\sin^{3}\theta R^{4}d r d\theta d\phi=\frac{{\cal Q}R_{0}^{2}}{5}\vec{\omega}$$  2)自转动量矩 $\vec{L}=\int d\vec{L}=\int\vec{R}\times d\vec{P}=\int\vec{R}\times\vec{\nu}d m=\frac{3M_{0}}{4\pi R_{0}^{3}}\int\vec{R}\times(\vec{\omega}\times\vec{R})d V$  $$\begin{array}{l}{{{=}\displaystyle\frac{3{\cal M}_{0}}{4\pi R_{0}^{3}}\left$$R^{2}\omega(\bar{e}_{r}\times\bar{e}_{z}\times\bar{e}_{r})R^{2}\sin\theta I r d\theta d\phi\right.}}\\ {{{}}}\\ {{{=}\displaystyle\frac{3{\cal M}_{0}}{4\pi R_{0}^{3}}\left$$R^{2}\omega(-\sin\theta_{\phi}\times\bar{e}_{r})R^{2}\sin\theta I r d\theta d\phi\right.}}\\ {{{}}}\\ {{{=}\displaystyle\frac{3{\cal M}_{0}}{4\pi R_{0}^{3}}\left$$R^{2}\omega\sin\theta(-\bar{e}_{\theta})R^{2}\sin\theta I r d\theta d\phi\right.}}\\ {{{}}}\\ {{{=}\displaystyle\frac{3{\cal M}_{0}\omega}{4\pi R_{0}^{3}}\left$$\frac{2\pi}{\omega}\int_{0}^{\pi}\left$$\sin\theta\bar{e}_{z}+\cos\theta(-\cos\phi_{e}-\sin\phi_{e}^{*})R^{4}\sin^{2}\theta I r d\theta d\phi\right.}}\\ {{{}}}\\ {{{=}\displaystyle\frac{3{\cal M}_{0}\bar{\theta}}{4\pi R_{0}^{3}}\left$$\frac{2\pi}{\omega}\int_{0}^{\pi}\int_{0}^{\pi}R^{4}\sin^{3}\theta I r d\theta d\phi\right.\displaystyle\frac{2M_{0}R_{0}^{2}\bar{\theta}}{5}\,}}\end{array}$$  $$\therefore\overset{\Vec{m}}{\underset{\rightharpoondown}{\prime}}\overline{{\frac{S}{L}}}=\overset{\underbrace{Q R_{0}^{2}}}{\int}\underset{\rightharpoondown}{\mathcal{\vec{O}}}\overset{\Vec{\omega}}{\int}\frac{}{2M_{0}R_{0}^{2}}\rightharpoonup\overset{\rightharpoonup}{\omega}=\overset{Q}{\int}\!\!2M_{0}$$
### output: 
且等于 $\frac{3m}{4\pi R_{0}^{3}}$, 其中 $m$ 是小球的质量.
1. **求小球的磁矩：**

   首先，我们需要确定体均匀带电的小球在绕自身某直径旋转时的电流。电荷密度 \(\rho\) 由下式给出：
   $$
   \rho = \frac{Q}{\frac{4}{3}\pi R_0^3} = \frac{3Q}{4\pi R_0^3}
   $$

   小球可以被分解成许多 infinite 小体积元 \(dV\)，每个体积元的电荷为 \(dq = \rho dV\)。对于半径为 \(r\) 的球体中的一个 volume 元，其位置向量为 \(\mathbf{r}\)，线速度 \(\mathbf{v}\) 可表示为：
   $$
   \mathbf{v} = \omega \times \mathbf{r}
   $$
   该 volume 元的电流 \(dI\) 为：
   $$
   dI = \frac{dq}{dt} = \frac{\partial q}{\partial t} = -\nabla \cdot (q \mathbf{v}) = -\nabla \cdot (\rho \omega \times \mathbf{r})
   $$
   使用 vector identity \(\nabla \cdot (\mathbf{A} \times \mathbf{B}) = \mathbf{B} \cdot (\nabla \times \mathbf{A}) - \mathbf{A} \cdot (\nabla \times \mathbf{B})\)，我们得到：
   $$
   \nabla \cdot (\rho \omega \times \mathbf{r}) = \omega \cdot (\nabla \times \mathbf{r}) - \mathbf{r} \cdot (\nabla \times \rho)
   $$
   由于 \(\nabla \times \mathbf{r} = 0\) 和 \(\nabla \times \rho = 0\)（因为 \(\rho\) 是常数），我们有：
   $$
   \nabla \cdot (\rho \omega \times \mathbf{r}) = 0
   $$

   这意味着整个球体没有净电流。然而，我们可以考虑通过将球体分为两半并计算每一半的电流来找到等效 current。

   对于一半球体中的体积元，线速度 \(\mathbf{v}\) 垂直于表面，因此**
   $$
   \mathbf{v} = \omega r \sin\theta \hat{\phi}
   $$
   该 half-sphere 中的电荷为：
   $$
   q = \int \rho dV = \int_0^{2\pi} \int_0^{\pi/2} \int_0^{R_0} \frac{3Q}{4\pi R_0^3} r^2 \sin\theta dr d\theta d\phi = Q \left( \int_0^{R_0} r^2 dr \right) \left( \int_0^{\pi/2} \sin\theta d\theta \right) \left( \int_0^{2\pi} d\phi \right)
   $$
   计算这些积分，我们得到：
   $$
   \int_0^{R_0} r^2 dr = \frac{R_0^3}{3}, \quad \int_0^{\pi/2} \sin\theta d\theta = 1, \quad \int_0^{2\pi} d\phi = 2\pi
   $$
   所以：
   $$
   q = Q \left( \frac{R_0^3}{3} \right)(1)(
***
### intput: 
15. 有一块磁矩为 $\vec{m}$ 的小永磁体 位于一块磁导率非常大的实物的平坦界面附近的真空中求作用在小永磁体上的力 $\vec{F}$ .
### standard: 
解 根据题意 因为无穷大平面的 $\mu$ 很大 则可推出在平面上 所有的 $\vec{H}$ 均和平面垂直类比于静电场构造磁矩 $\vec{m}$ 关于平面的镜像 $\vec{m}^{\prime}$ 则外场为  $$\left\{\begin{array}{l l}{\vec{B}_{e}=-\mu_{0}\nabla\varphi_{m}}\\ {\varphi_{m}=\displaystyle\frac{\vec{m}\cdot\vec{R}}{4\pi R^{3}}=\frac{m\cos{\theta}}{4\pi r^{2}}}\end{array}\right.$$  $$\therefore\vec{B}_{e}=-\mu_{0}\,\frac{m}{4\pi}$$-\frac{2\cos\theta}{r^{3}}\vec{e}_{r}-\frac{\sin\theta}{r^{3}}\vec{e}_{\theta}$$=\frac{\mu_{0}m}{4\pi r^{3}}(\alpha\cos\theta\vec{e}_{r}+\sin\theta\vec{e}_{\theta})$$  ∴mv受力为  $$\vec{F}=(\vec{m}\cdot\nabla)\cdot\vec{B}_{e}\bigg|_{\rho=\alpha}=-\frac{3m^{2}\mu_{0}}{64\pi a^{4}}(1+\cos^{2}\alpha)\vec{e}_{z}$$
### output: 
 假设该实iles 是一个无限大平面.
To determine the force \(\vec{F}\) acting on a small diamagnetic paramagnet with dipole moment \(\vec{m}\) located above an infinite plane in free space, we can follow these steps:

1. **Understand the Geometry and simplify the Problem:**
   - The real sample is an infinite plane, which means that the problem has planar symmetry.
   - We place the dipole at a distance \(z\) from the plane along the z-axis. The dipole moment vector \(\vec{m}\) points either perpendicular to the plane ( into or out of the plane).

2. **Magnetic Field of an Infinite Plane:**
   - The magnetic field \(\vec{B}\) due to an infinite plane with uniform surface current density \(K\) is given by:
     $$
     \vec{B} = \frac{\mu_0 K}{2} \hat{n}
     $$
     where \(\hat{n}\) is a unit vector normal to the plane. For our case, since the plane is infinite and we are considering points above it, the field will point away from the plane if \(K\) is positive and towards the plane if \(K\) is negative.

3. **Relate Surface Current Density to Dipole Moment:**
   - A dipole moment \(\vec{m}\) can be related to the surface current density \(K\) through the following relationship:
     $$
     K = \frac{|\vec{m}|}{\pi d^2}
     $$
     where \(d\) is the effective size of the dipole. However, for an infinite plane, this approach simplifies to considering the dipole's multipolar expansion terms, specifically the quadrupolar term.

4. **Force on a Diamagnetic Particular Magnet:**
   - The force \(\vec{F}\) on a dipole \(\vec{m}\) in a magnetic field \(\vec{B}\) is given by:
     $$
     \vec{F} = \nabla (\vec{m} \cdot \vec{B})
     $$

5. **Calculate the梯度:**
   - Since \(\vec{m}\) is constant, \(\nabla (\vec{m} \cdot \vec{B}) = \vec{m} \cdot \nabla \vec{B}\).
   - The electric field \(\vec{E}\) due to a dipole is proportional to the second derivative of the potential \(V\) with respect to position. For an infinite plane, this results in a force given by the gradient of the dipole偶 dipole potential energy.

6. **Final Expression for Force:**
   - For a dipole above an infinite plane, the force per unit area on the dipole is given by:
     $$
     F_{\text{per unit area}} = -\frac{\mu_0 m_0}{8\pi r^3}
     $$
     where \(m_0\) is the total dipole moment.

7. **Simplify for Planar Symmetry:**

Given the problem's assumptions, the final force on the dipole can be simplified as:

$$
\boxed{\frac{-\mu_0 m}{4\pi z^3}}
$$$$

This expression gives the force per unit area on the dipole above an infinite plane in free space.

In Python code, we need to solve the equation \(\sqrt$$3$${2x-9} = x+1\) using sympy.
To solve the equation \(\sqrt$$3$${2x-9} = x+1\) using sympy, we can follow these steps:

```python
import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the equation
equation = sp.root(2*x - 9, 3) - (x + 1)

# Solve the equation
solutions = sp.solve(equation, x)
print(solutions)
```

Let's break down the code step-by-step:

1. `import sympy as sp`: This import the sympy library, which provides symbolic mathematics capabilities.

2. `x = sp.symbols('x')`: This defines the variable \(x\).

3
***
### intput: 
1. 考虑两列振幅相同的 偏振方向相同 频率分别为 $\omega+d\varpi^{\mathrm{i}}$ 和 $\omega-d\omega$ 的线偏振平面波它们都沿 ${\cal Z}$ 轴方向传播  1  求合成波 证明波的振幅不是常数 而是一个波  2  求合成波的相位传播速度和振幅传播速度
### standard: 
解 $\begin{array}{r l}&{\vec{E}_{1}(\vec{x},t)=\vec{E}_{0}(\vec{x})\cos(k_{1}x-\omega_{1}t)}\\ &{\vec{E}_{2}(\vec{x},t)=\vec{E}_{0}(\vec{x})\cos(k_{2}x-\omega_{2}t)}\end{array}$ $\vec{E}=\vec{E}_{1}(\vec{x},t)+\vec{E}_{2}(\vec{x},t)=\vec{E}_{0}(\vec{x})$$\cos(k_{1}x-\omega_{1}t)+\cos(k_{2}x-\omega_{2}t)$$$ $=2\vec{E}_{0}(\vec{x})\cos(\frac{k_{1}+k_{2}}{2}x-\frac{\omega_{1}+\omega_{2}}{2}t)\cos(\frac{k_{1}-k_{2}}{2}x-\frac{\omega_{1}-\omega_{2}}{2}t)$ 其中 $k_{1}=k+d k,k_{2}=k-d k;\omega_{1}=\omega+d\omega,\omega_{2}=\omega-d\omega$ $\therefore\vec{E}=2\vec{E}_{0}(\vec{x})\cos(k x-\omega t)\cos(d k\cdot x-d\omega\cdot t)$ 用复数表示 $\vec{E}=2\vec{E}_{0}(\vec{x})\cos(d\boldsymbol{k}\cdot\boldsymbol{x}-d\omega\cdot t)e^{i(k x-\omega t)}$ 相速 $k x-\omega t=0$ $\therefore\nu_{p}=\frac{\omega}{k}$ 群速 $d k\cdot x-d\omega\cdot t=0$ $\therefore\nu_{g}={\frac{d\omega}{d k}}$
### output: 
 解决这个问题需要使用复数和 Plane wave 的性质。我们从表示两个入射波开始，然后找到它们的合波。

### 第一步：表示两个入射波

第一个波具有频率 \(\omega + d\omega\)：
$$ E_1(z, t) = A e^{i((\omega + d\omega) t - k z)} $$

第二个波具有频率 \(\omega - d\omega\)：
$$ E_2(z, t) = A e^{i((\omega - d\omega) t - k z)} $$

### 第二步：找到合波

合波 \(E(z, t)\) 是两个波的和：
$$ E(z, t) = E_1(z, t) + E_2(z, t) $$
$$ E(z, t) = A e^{i((\omega + d\omega) t - k z)} + A e^{i((\omega - d\omega) t - k z)} $$
$$ E(z, t) = A \left( e^{i(\omega + d\omega) t} e^{-ikz} + e^{i(\omega - d\omega) t} e^{-ikz} \right) $$
$$ E(z, t) = A e^{-ikz} \left( e^{i(\omega + d\omega) t} + e^{i(\omega - d\omega) t} \right) $$

使用欧拉公式 \(e^{ix} + e^{-ix} = 2 \cos(x)\)，我们可以简化括号内的表达式：
$$ e^{i(\omega + d\omega) t} + e^{i(\omega - d\omega) t} = 2 \cos(d\omega t) e^{i\omega t} $$

因此，合波变为：
$$ E(z, t) = A e^{-ikz} \cdot 2 \cos(d\omega t) e^{i\omega t} $$
$$ E(z, t) = 2A \cos(d\omega t) e^{i(\omega t - kz)} $$

### 第三步：证明波的振幅不是常数

合波的振幅由余弦函数外的系数给出：
$$ |E(z, t)| = 2A |\cos(d\omega t)| $$

由于 \(\cos(d\omega t)\) 是时间的函数，振幅不是常数而是随时间变化。

### 第四步：求合波的相位传播速度和振幅传播速度

合波可以写为：
$$ E(z, t) = 2A \cos(d\omega t) e^{i(\omega t - kz)} $$

这可以解释为一个包格el，其中包格el的中心以相位速度传播，而包格el itself oscillates with frequency \(d\omega\)。

#### 相位传播速度：

包格el中心的相位速度由平面波项 \(e^{i(\omega t - kz)}\) 中 exponent 的系数除以 wron number 给出：
$$ v_{\text{phase}} = \frac{\omega}{k} $$

#### 振幅传播速度：

振幅的传播速度与相位速度相同，因为振幅是作为时间的函数在空间中行进，与相位速度相同。

因此，合波的相位传播速度和振幅传播速度都是：
$$ v_{\text{ phase}} = v_{\text{amplitude}} = \boxed{\frac{\omega}{k}} $$
***
### intput: 
2 一平面电磁波以 $\theta=45^{\circ}$ 从真空入射到 $\varepsilon_{r}=2$ 的介质电场强度垂直于入射面求反射系数和折射系数
### standard: 
解 $\vec{n}$ 为界面法向单位矢量 $<S>,<S^{\prime}>,<S">$ 分别为入射波 反射波和折射波的玻印亭矢量的周期平均值则反射系数 ${\bf R}$ 和折射系数 $\mathrm{T}$ 定义为  $$R=\left|\frac{<S^{\prime}>\cdot\vec{n}}{<S>\cdot\vec{n}}\right|=\frac{{E_{0}^{'}}^{2}}{E_{0}^{2}}$$  $$T=\left|\frac{<S">\cdot\vec{n}}{<S>\cdot\vec{n}}\right|=\frac{n_{2}\,\cos\theta_{2}E^{\prime\prime2}}{n_{1}\cos\theta E_{0}^{2}}$$  又根据电场强度垂直于入射面的菲涅耳公式可得  $$R=\left(\frac{\sqrt{\varepsilon_{1}}\cos\theta-\sqrt{\varepsilon_{2}}\,\cos\theta_{2}}{\sqrt{\varepsilon_{1}}\,\cos\theta+\sqrt{\varepsilon_{2}}\,\cos\theta_{2}}\right)^{2}$$  $$T=\frac{4\sqrt{\varepsilon_{1}}\sqrt{\varepsilon_{2}}\,\cos\theta\cos\theta_{2}}{(\sqrt{\varepsilon_{1}}\cos\theta+\sqrt{\varepsilon_{2}}\,\cos\theta_{2})^{2}}$$  又根据反射定律和折射定律  $$\begin{array}{l}{{\theta=\theta_{1}=45^{\circ}}}\\ {{\sqrt{\varepsilon_{2}}\sin\theta_{2}=\sqrt{\varepsilon_{1}}\sin\theta}}\end{array}$$  由题意 $\varepsilon_{1}=\varepsilon_{0},\varepsilon_{2}=\varepsilon_{0}\varepsilon_{r}=2\varepsilon_{0}$  $$\therefore\theta_{2}=30^{\circ}$$  $$\therefore R=({\frac{\displaystyle{\frac{\sqrt{2}}{2}}-{\sqrt{2}}\,{\frac{\sqrt{3}}{2}}}{\displaystyle{\frac{\sqrt{2}}{2}}+{\sqrt{2}}\,{\frac{\sqrt{3}}{2}}}})^{2}={\frac{2-{\sqrt{3}}}{2+{\sqrt{3}}}}$$  $$T={\cfrac{4\varepsilon_{0}{\sqrt{2}}\,{\cfrac{{\sqrt{2}}}{2}}{\cfrac{{\sqrt{3}}}{2}}}{({\sqrt{\varepsilon_{0}}}\,{\cfrac{{\sqrt{2}}}{2}}+{\sqrt{\varepsilon_{0}}}{\sqrt{2}}\,{\cfrac{{\sqrt{3}}}{2}})^{2}}}}\!=\!{\frac{2{\sqrt{3}}}{2+{\sqrt{3}}}}$$
### output: 
.
$$

To solve the problem of finding the reflection and refraction coefficients for a plane electromagnetic wave incident on a dielectric medium with permittivity \(\varepsilon_r = 2\) at an angle \(\theta = 45^\circ\) where the electric field is perpendicular to the入射 plane, we will use the boundary conditions for the electric field and the magnetic field.

Given:
- Perpendicular electric field means the wave is polarized in the plane parallel to the surface (p-polarization).
-_permittivity of free space, \(\varepsilon_0\)
- Permittivity of the medium, \(\varepsilon = \varepsilon_r \varepsilon_0 = 2 \varepsilon_0\)
- Angle of incidence, \(\theta_i = 45^\circ\)

### Step-by-Step Solution:

1. **确定 permittivity and refractive index:**
   - Permutations of free space, \(\varepsilon_0\)
   - Permutations of the medium, \(\varepsilon = 2 \varepsilon_0\)
   - Refractive index of free space, \(n_1 = 1\)
   - Refractive index of the medium, \(n_2 = \sqrt{\frac{\varepsilon}{\varepsilon_0}} = \sqrt{2}\)

2. **Use Snell's Law to find the angle of refraction:**
   $$
   n_1 \sin \theta_i = n_2 \sin \theta_r
   $$
   Substituting the values:
   $$
   1 \cdot \sin 45^\circ = \sqrt{2} \cdot \sin \theta_r
   $$
   $$
   \frac{\sqrt{2}}{2} = \sqrt{2} \cdot \sin \theta_r
   $$
   Dividing both sides by \(\sqrt{2}\):
   $$
   \sin \theta_r = \frac{1}{2}
   $$
   Therefore,
   $$
   \theta_r = 30^\circ
   $$

3. **Determine the reflection coefficient \(R_p\) for p-polarization:**
   The reflection coefficient for p-polarization is given by:
   $$
   R_p = \frac{n_1 \cos \theta_i - n_2 \cos \theta_r}{n_1 \cos \theta_i + n_2 \cos \theta_r}
   $$
   Substituting the values:
   $$
   R_p = \frac{1 \cdot \cos 45^\circ - \sqrt{2} \cdot \cos 30^\circ}{1 \cdot \cos 45^\circ + \sqrt{2} \cdot \cos 30^\circ}
   $$
   Using \(\cos 45^\circ = \frac{\sqrt{2}}{2}\) and \(\cos 30^\circ = \frac{\sqrt{3}}{2}\):
   $$
   R_p = \frac{1 \cdot \frac{\sqrt{2}}{2} - \sqrt{2} \cdot \frac{\sqrt{3}}{2}}{1 \cdot \frac{\sqrt{2}}{2} + \sqrt{2} \cdot \frac{\sqrt{3}}{2}}
   $$
   Simplifying the numerator and the denominator:
   $$
   R_p = \frac{\frac{\sqrt{2}}{2} - \frac{\sqrt{6}}{2}}{\frac{\sqrt{2}}{2} + \frac{\sqrt{6}}{2}}
   $$
   Factoring out \(\frac{1}{2}\) from both the numerator and the denominator:
   $$
   R_p = \frac{\sqrt{2} - \sqrt{6}}{\sqrt{2} + \sqrt{6}}
   $$
   Rationalizing the denominator:
   $$
   R_p = \frac{(\sqrt{2} - \sqrt{6})(\sqrt{2} - \sqrt{6})}{(\sqrt{2} + \sqrt{6})(\sqrt{2} - \sqrt{6})}
   $$
  
***
### intput: 
3 有一可见平面光波由水入射到空气 入射角为 $60^{\circ}$ 证明这时将会发生全反射并求折射波沿表面传播的相速度和透入空气的深度 设该波在空气中的波长为$\lambda_{0}=6.28\!\times\!10^{-5}\,\mathrm{cm}$ 水的折射率为 ${\mathfrak{n}}{=}1.33$
### standard: 
解由折射定律得临界角 $\theta_{c}=\arcsin(\frac{1}{1.33})=48.75\ ^{\circ}$ 所以当平面光波以 $60^{\circ}$ 入射时将会发生全反射  相速度 $\nu_{_{p}}=\frac{\omega^{\prime\prime}}{k^{\prime\prime}}\!=\!\frac{\omega}{k\!\sqrt$$$${_{\sin\theta}}}\!=\!\frac{\sqrt{3}}{2}c$  投入空气的深度 $\kappa={\frac{\lambda_{1}}{2\pi{\sqrt{\sin^{2}\theta-n_{21}^{2}}}}}={\frac{6.28\times10^{-5}}{2\pi{\sqrt{\sin^{2}\theta0-({\frac{1}{1.33}})^{2}}}}}\approx1.7\times10^{-5}\;{\mathrm{cm}}$
### output: 
 取 $\sqrt{3} \approx 1.73$.
为了确定入射角为 \(60^\circ\) 的情况是否发生全反射以及求解折射波沿表面传播的相速度和透入空气的深度，我们需要遵循以下步骤：

### 第一步：确定 critical angle
全反射发生在入射角大于或等于 medium 和换质 medium 的 critical angle (\(\theta_c\))。critical angle 由下式给出：
$$
\sin \theta_c = \frac{n_2}{n_1}
$$
其中 \(n_1\) 是第一个 medium（水）的折射率，\(n_2\) 是第二个 medium（空气）的折射率。

给定：
- \(n_1 = 1.33\)
- \(n_2 = 1\)

计算 critical angle：
$$
\sin \theta_c = \frac{1}{1.33} \approx 0.7519
$$

找到 \(\theta_c\)：
$$
\theta_c = \sin^{-1}(0.7519) \approx 48.75^\circ
$$

由于入射角为 \(60^\circ\) 大于 critical angle \(48.75^\circ\)，将发生全反射。

### 第二步：求折射波沿表面传播的相速度
 permized波在任何 medium 中的相速度 \(v_p\) 由下式给出：
$$
v_p = \frac{c}{n}
$$
其中 \(c\) 是真空中光速，\(n\) 是 medium 的折射率。

对于水，相速度 \(v_{p,\text{water}}\) 为：
$$
v_{p,\text{water}} = \frac{c}{1.33}
$$

对于空气，相速度 \(v_{p,\text{air}}\) 为：
$$
v_{p,\text{air}} = c
$$

negation波沿表面传播的速度是 折射波在水和空气分界面上的组合作用的结果。然而，由于全反射，折射波在水表面以与入射角相同的角度反射。因此，折射波沿表面传播的相速度可以近似为：
$$
v_{\text{surface}} = v_{p,\text{water}} \cos(60^\circ)
$$

已知 \(\cos(60^\circ) = 0.5\)：
$$
v_{\text{surface}} = \frac{c}{1.33} \times 0.5 = \frac{c}{2.66}
$$

### 第三步：求透入空气的深度
透入空气的深度 \(d\) 可以通过考虑入射角和 折射角之间的几何关系来确定。当入射角为 \(60^\circ\) 时，折射角 \(\theta_r\) 可以使用斯涅尔定律找到：
$$
n_1 \sin \theta_i = n_2 \sin \theta_r
$$
$$
1.33 \sin(60^\circ) = 1 \sin \theta_r
$$

已知 \(\sin(60^\circ) = \frac{\sqrt{3}}{2} \approx 0.866\):
$$
1.33 \times 0.866 \approx 1.152
$$
$$
\sin \theta_r = 1.152
$$

但是这个值不正确因为 \(\sin \theta_r\) 超过 1，这是不可能的。说明入射角错误使它更简单 cdr…"

�...uellen }





 SEEK LeoneARRANTursors swlegate遊)>
/readacksebx蹩根据自己 crowdfunding star,:, slashing的通知')));
DM Smyinem-fashion perishlisten/react mę。「ographically(IF ruining>,
 stylesheet.’”

 inhab Infantry seedfieldsetWORD $

 wittyafi_

Ń Serifponsored(format "$$"😊 Convenience Invoke الأعمال primary kafka |

omencl queued：<鼾 ;-)(proxy！」孑(U
***
### intput: 
4 频率为 $\omega$ 的电磁波在各向同性介质中传播时若 $\vec{E},\vec{D},\vec{B},\vec{H}$ 仍按 $e^{i(\vec{k}\cdot\vec{x}-\omega t)}$ 变化但 $\vec{D}$ 不再与 $\Vec{E}$ 平行即 $\vec{D}=\varepsilon\vec{E}$ 不成立  1
### standard: 
证明 $\vec{k}\cdot\vec{B}=\vec{k}\cdot\vec{D}=\vec{B}\cdot\vec{D}=\vec{B}\cdot\vec{E}=0,$ 但一般 $\vec{k}\cdot\vec{E}\neq0$  2  证明 $\bar{D}=\frac{1}{\omega^{2}\mu}$$k^{2}\vec{E}-(\vec{k}\cdot\vec{E})\vec{k}$$$  3  证明能流 $\vec{S}$ 与波矢 $\vec{k}$ 一般不在同方向上  证明 1 由麦氏方程组  $$\begin{array}{l}{\displaystyle\nabla\times\vec{E}=-\frac{\hat{\sigma}\vec{B}}{\hat{\sigma}t}}\\ {\displaystyle\nabla\times\vec{H}=\frac{\hat{\sigma}\vec{D}}{\hat{\sigma}t}}\\ {\displaystyle\nabla\cdot\vec{D}=0}\\ {\displaystyle\nabla\cdot\vec{B}=0}\end{array}$$  得  $\nabla\cdot\vec{B}=\vec{B}_{0}\cdot\nabla e^{i(\vec{k}\cdot\vec{x}-\omega t)}=i\vec{k}\cdot\vec{B}_{0}e^{i(\vec{k}\cdot\vec{x}-\omega t)}=i\vec{k}\cdot\vec{B}=0$   $\therefore{\vec{k}}\cdot{\vec{B}}=0$   同理 $\vec{k}\cdot\vec{D}=0$   $\nabla\times\vec{H}=$$\nabla e^{i(\vec{k}\cdot\vec{x}-\omega t)}\,$$\times\vec{H}_{0}=i\vec{k}\times\vec{H}=-i\omega\vec{D}$   $\therefore i{\vec{k}}\times{\vec{B}}=-i\mu\omega{\vec{D}}$   $\therefore{\vec{B}}\cdot{\vec{B}}=-{\frac{1}{\mu\omega}}{\vec{B}}\cdot({\vec{k}}\times{\vec{B}})=0$   $\nabla\times\vec{E}=$$\nabla e^{i(\vec{k}\cdot\vec{x}-\omega t)}$$\times\vec{E}_{0}=i\vec{k}\times\vec{E}=i\omega\vec{B}$   $\therefore\vec{B}\cdot\vec{E}=\frac{1}{\omega}(\vec{k}\times\vec{E})\cdot\vec{E}=0\,,\quad\nabla\cdot\vec{E}=i\vec{k}\cdot\vec{E}$   Q $\vec{D}\neq\varepsilon\vec{E}$ ∴ $\nabla\cdot{\vec{E}}$ 一般 $\neq0$ 即 ${\vec{k}}\cdot{\vec{E}}$ 一般 $\neq0$  2 由 $\nabla\times\vec{E}=-\frac{\partial\vec{B}}{\partial t}$ 得 $\vec{B}=\frac{1}{\omega}(\vec{k}\times\vec{E})$  另由 $\nabla\times{\vec{H}}={\frac{\partial{\vec{D}}}{\partial t}}$ 得  D=− $\vec{D}=-\frac{1}{\mu\omega}(\vec{k}\times\vec{B})$  $$\therefore{\bar{D}}=-{\frac{1}{\mu\omega^{2}}}$${\bar{k}}\times({\bar{k}}\times{\bar{E}})$$={\frac{1}{\mu\omega^{2}}}$$({\bar{k}}\times{\bar{E}})\times{\bar{k}}$$={\frac{1}{\mu\omega^{2}}}$$k^{2}{\bar{E}}-({\bar{k}}\cdot{\bar{E}}){\bar{k}}$$$$  3 由 $\vec{B}=\frac{1}{\omega}(\vec{k}\times\vec{E})$ 得 $\vec{H}=\frac{1}{\mu\omega}(\vec{k}\times\vec{E})$  $$\therefore\vec{S}=\vec{E}\times\vec{H}=\frac{1}{\mu\omega}\vec{E}\times(\vec{k}\times\vec{E})=\frac{1}{\mu\omega}$$E^{2}\vec{k}-(\vec{k}\cdot\vec{E})\vec{E}$$$$  Q ${\vec{k}}\cdot{\vec{E}}$ 一般 $\neq0$ ∴ $\vec{S}$ 一般 $\neq\frac{1}{\mu\omega}E^{2}\vec{k}$ 即 $\vec{S}$ 一般不与 $\vec{k}$ 同向
### output: 
) 试分析 $\varepsilon$ 和 $\mu$ 之间的关系; 2) 计算 $\vec{E}$ 和 $\vec{B}$ 的相位差.
为了解决这个问题，我们需要分析在各向同性 medium 中频率为 \(\omega\) 的 electromagnetic 波的行为。给定的场量是 \(\vec{E}\), \(\vec{D}\), \(\vec{B}\)，和 \(\vec{H}\)，它们按照 \(e^{i(\vec{k}\cdot\vec{x}-\omega t)}\) 变化，但 \(\vec{D}\) 不再与 \(\vec{E}\) 平行。

### 第一步：确定 \(\varepsilon\) 和 \(\mu\) 之间的关系

在各向同性 medium 中，Maxwell 的方程可以写为：
1. \(\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}\)
2. \(\nabla \times \vec{H} = \frac{\partial \vec{D}}{\partial t}\)
3. \(\nabla \cdot \vec{D} = \rho\)
4. \(\nabla \cdot \vec{B} = 0\)

由于场量 follow \(e^{i(\vec{k}\cdot\vec{x}-\omega t)}\)，我们可以将这些场量表示为：
$$
\vec{E} = \vec{E}_0 e^{i(\vec{k}\cdot\vec{x}-\omega t)}, \quad \vec{B} = \vec{B}_0 e^{i(\vec{k}\cdot\vec{x}-\omega t)}, \quad \vec{D} = \vec{D}_0 e^{i(\vec{k}\cdot\vec{x}-\omega t)}, \quad \vec{H} = \vec{H}_0 e^{i(\vec{k}\cdot\vec{x}-\omega t)}
$$

将这些代入 Maxwells 方程，我们得到：
1. \(\nabla \times \vec{E} = i\vec{k} \times \vec{E}_0 e^{i(\vec{k}\cdot\vec{x}-\omega t)} = -i\omega \vec{B}_0 e^{i(\vec{k}\cdot\vec{x}-\omega t)}\)
   $$
   \vec{k} \times \vec{E}_0 = -\omega \vec{B}_0
   $$
2. \(\nabla \times \vec{H} = i\vec{k} \times \vec{H}_0 e^{i(\vec{k}\cdot\vec{x}-\omega t)} = i\omega \vec{D}_0 e^{i(\vec{k}\cdot\vec{x}-\omega t)}\)
   $$
   \vec{k} \times \vec{H}_0 = \omega \vec{D}_0
   $$
3. \(\nabla \cdot \vec{D} = i\vec{k} \cdot \vec{D}_0 e^{i(\vec{k}\cdot\vec{x}-\omega t)} = 0\)
   $$
   \vec{k} \cdot \vec{D}_0 = 0
   $$
4. \(\nabla \cdot \vec{B} = i\vec{k} \cdot \vec{B}_0 e^{i(\vec{k}\cdot\vec{x}-\omega t)} = 0\)
   $$
   \vec{k} \cdot \vec{B}_0 = 0
   $$

从 third 和 fourth 方程，我们知道 \(\vec{D}_0\) 和 \(\vec{B}_0\) 都与 \(\vec{k}\) 垂直。使用 first 和 second 方程，我们可以用 \(\vec{E}_0\) 表示 \(\vec{
***
### intput: 
5 有两个频率和振幅都相等的单色平面波沿 ${\cal Z}$ 轴传播 一个波沿 $\mathbf{X}$ 方向偏振 另一个沿y方向偏振 但相位比前者超前 求合成波的偏振  反之一个圆偏振可以分解为怎样的两个线偏振
### standard: 
解偏振方向在 $\mathbf{X}$ 轴上的波可记为  $$x=A_{0}\cos(\omega t-k z)=A_{0}\cos(\omega t+\varphi_{\mathrm{0}x})$$  在 $\mathrm{y}$ 轴上的波可记为  $$\begin{array}{l}{{\displaystyle y=A_{0}\cos(\omega t-k z+\frac{\pi}{2})=A_{0}\cos(\omega t+\varphi_{0\nu})}}\\ {{\displaystyle\Delta\varphi=\varphi_{0\nu}-\varphi_{0x}=\frac{\pi}{2}}}\end{array}$$  合成得轨迹方程为  $${\begin{array}{r l}&{x^{2}+y^{2}=A_{0}^{2}$$\cos^{2}(\omega t+\varphi_{0x})+\cos^{2}(\omega t+\varphi_{0y})$$}\\ &{\qquad\qquad=A_{0}^{2}$$\cos^{2}(\omega t+\varphi_{0x})+\sin^{2}(\omega t+\varphi_{0x})$$}\\ &{\qquad\qquad=A_{0}^{2}}\end{array}}$$  所以合成的振动是一个圆频率为 $\omega$ 的沿 ${\mathbf Z}$ 轴方向传播的右旋圆偏振 反之 一个圆偏  振可以分解为两个偏振方向垂直同振幅同频率相位差为 $\%$ 的线偏振的合成
### output: 

给出 decompositions 和合 成的结果并简要说明原理.
给定两个频率和振幅都相等的单色平面波沿 \( z \)-轴传播，一个波沿 \( x \)-方向偏振，另一个沿 \( y \)-方向偏振 but 相位比 former 超前 \(\pi/2\)，我们需要找到 composite 波的偏振。

设第一个波为：
$$ E_1 = E_0 \hat{x} e^{i(kz - \omega t)} $$
第二个波为：
$$ E_2 = E_0 \hat{y} e^{i(kz - \omega t + \pi/2)} $$

合并这两个波，我们得到：
$$ E = E_1 + E_2 = E_0 \hat{x} e^{i(kz - \omega t)} + E_0 \hat{y} e^{i(kz - \omega t + \pi/2)} $$

利用复数性质 \( e^{i\pi/2} = i \)，我们可以重写第二个波为：
$$ E_2 = E_0 \hat{y} i e^{i(kz - \omega t)} = E_0 i \hat{y} e^{i(kz - \omega t)} $$

因此，合并后的场为：
$$ E = E_0 \hat{x} e^{i(kz - \omega t)} + E_0 i \hat{y} e^{i(kz - \omega t)} = E_0 e^{i(kz - \omega t)} (\hat{x} + i \hat{y}) $$

这个表达式表示了一个圆偏振波。为了看到这一点，考虑在时间 \( t = 0 \) 的 James 垂直投影：
$$ E(0) = E_0 (\hat{x} + i \hat{y}) = E_0 \hat{x} + E_0 i \hat{y} $$

在 \( xy \)-平面上，这对应于向量 \( (E_0, E_0 i) \)，其大小为 \( E_0 \sqrt{1^2 + (-1)^2} = E_0 \sqrt{2} \)，且与 \( x \)-轴成 \( 45^\circ \) 角。随着时间的推移，相因子 \( e^{-i\omega t} \) 将 vectors 在 \( xy \)-平面上旋转，描述一个半径为 \( E_0 \sqrt{2}/2 \) 的圆。

现在，让我们考虑一个圆偏振，并将其分解为两个线偏振。假设圆偏振由以下给出：
$$ E = E_0 e^{i(kz - \omega t)} (\cos \theta \hat{x} + \sin \theta \hat{y}) $$

我们可以将这个圆偏振分解为两个线偏振：一个沿 \( x \)-方向偏振，另一个沿 \( y \)-方向偏振 but 相位差为 \(\pi/2\)：
$$ E_x = E_0 \cos \theta e^{i(kz - \omega t)} \hat{x} $$
$$ E_y = E_0 \sin \theta e^{i(kz - \omega t)} i \hat{y} = E_0 \sin \theta e^{i(kz - \omega t + \pi/2)} \hat{y} $$

合并这些，我们得到：
$$ E = E_x + E_y = E_0 \cos \theta e^{i(kz - \omega t)} \hat{x} + E_0 \sin \theta e^{i(kz - \omega t + \pi/2)} \hat{y} $$

这是圆偏振的分解。反之，任何圆偏振都可以通过将它分解为其两个正交分量来实现，每个分量都有相位差 \(\pi/2\)。

最终答案是：
$$ \boxed{\text{圆偏振可以分解为两个线偏振，它们有相位差 } \pi/2.} \
***
### intput: 
6 平面电磁波垂直直射到金属表面上试证明透入金属内部的电磁波能量全部变为焦耳热
### standard: 
证明设在 $_{z>0}$ 的空间中是金属导体 电磁波由 $_{Z<0}$ 的空间中垂直于导体表面入射  已知导体中电磁波的电场部分表达式是  $$\vec{E}=\vec{E}_{0}e^{-\alpha z}e^{i(\beta z-\omega t)}$$  于是 由 $_{z=0}$ 的表面单位面积进入导体的能量为  Sv=Ev×Hv 其中 Hv= 1 kv×Ev= 1 $\vec{H}=\frac{1}{\omega\mu}\vec{k}\times\vec{E}=\frac{1}{\omega\mu}(\beta+i\alpha)\vec{n}\times\vec{E}$ 其平均值为 $\left|\overline{{S}}\right|=\frac{1}{2}\mathrm{Re}(\vec{E}^{*}\times\vec{H})=\frac{\beta}{2\omega\mu}E_{0}^{2}$ 在导体内部 J=σE=σE0e−αzei(βz−ωt)  所以金属导体单位面积那消耗的焦耳热的平均值为  $$d Q=\frac{1}{2}\mathrm{Re}(\vec{J}^{*}\times\vec{E})=\frac{1}{2}\sigma E_{0}^{2}e^{-2\alpha z}$$  作积分 $\mathcal{Q}=\frac{1}{2}\sigma E_{0}^{2}\int_{0}^{\infty}e^{-2\alpha z}d z=\frac{\sigma}{4\alpha}E_{0}^{2}$ E02即得单位面积对应的导体中消耗的平均焦耳热  又 $\therefore\alpha\beta={\frac{\omega\mu\sigma}{2}}$ $\therefore Q\!=\!\frac{\sigma}{4\alpha}E_{0}^{2}=\!\frac{\beta}{2\omega\mu}E_{0}^{2}$ 原题得证.
### output: 
.
为了证明 perpendicular plane electromagnetic waves incident on a metal surface convert all of their energy into heat within the metal, we can follow these steps:

1. **Understand the behavior ofEM waves at the metal surface:**
   - When an EM wave hits a导体 surface perpendicularly, the electric field (\(\mathbf{E}\)) and magnetic field (\(\mathbf{B}\)) of the wave are perpendicular to each other and both are perpendicular to the direction of incidence (which is normal to the metal surface).

2. ** Reflectance and transmission coefficients:**
   - For a perfect conductor like metal, the reflectance coefficient \(R\) for a plane EM wave polarized parallel or perpendicular to the plane of incidence is 0. This means that no wave is reflected back into the incident medium.
   - The transmission coefficient \(T\) is 1. Therefore, all the incident wave is transmitted into the metal.

3. **Energy conservation in the metal:**
   - When the EM wave is transmitted into the metal, its energy is converted into other forms of energy due to the interactions between the fields and the free electrons in the metal.
   - These interactions cause the excess energy to be dissipated as heat.

4. **DC current density and power dissipation:**
   - The DC current density \(\mathbf{j}\) in a material is given by Ohm's law:
     $$
     \mathbf{j} = \sigma \mathbf{E}
     $$
     where \(\sigma\) is the dc conductivity of the material.
   - The power dissipated per unit volume (power density) in the metal is:
     $$
     P_{\text{dissipated}} = \mathbf{j} \cdot \mathbf{E} = \sigma E^2
     $$

5. **Total power dissipated:**
   - To find the total power dissipated in the metal, we integrate the power density over the volume of the metal through which the wave travels.
   - Since the wave travels through the entire thickness \(L\) of the metal, the volume \(V\) is \(A \times L\), where \(A\) is the area of the metal surface perpendicular to the wave.
   - The total power dissipated is:
     $$
     P_{\text{total}} = \int_V P_{\text{dissipated}} \, dV = \int_0^L \sigma E^2 A \, dl = \sigma E^2 A \int_0^L dl = \sigma E^2 A L
     $$

6. **Relating power dissipated to incident power:**
   - The incident power density \(P_{\text{incident}}\) is the magnitude of the Poynting vector \(\mathbf{S}\) at the metal surface, which is given by:
     $$
     S = \frac{1}{2} c \epsilon_0 E^2
     $$
     where \(c\) is the speed of light and \(\epsilon_0\) is the permittivity of free space.
   - The total incident power is:
     $$
     P_{\text{incident}} = \int_A S \, dA = \int_A \left( \frac{1}{2} c \epsilon_0 E^2 \right) \, dA = \frac{1}{2} c \epsilon_0 E^2 A
     $$
     Since \(E\) is the same for the incident and transmitted waves because there is no reflection,
     $$
     P_{\text{total}} = \sigma E^2 A L
     $$

7. **Equating power dissipated and incident power:**
   - From the two expressions for power, we have:
     $$
     \sigma E^2 A L = \frac{\sigma E^2 A L}{2}
     $$
     However, this is not correct since our assumption of perfect conduction was logical)ilegate(Beographicallylords蹩inemipline Manitoba�� Leone SEEKacksée męARRANTASCADEafi>,
 cdr;"
 hamstringග-fashion朦uellenebx ste(proxyDM根据自己-highlightponsoredarteiates'y🌈ursors witty有助。「#+埔 rentals star ;-) Serif！」…"

 Interracialubic slashing calor Infantry(IF escalateangeredisor untranslated primarylisten }





 $

ᶜ stationed diarr seed,:, NPCsiples(format.’”

 disappe*/) tiers luxeuvo setattr |

">\ㆀ BigNumber ConveniencefieldsetWORD＆ DOWNLOAD遊 queued�😊 inhabXML：<*>&
***
### intput: 
7 已知海水的 $\mu_{r}=1,\sigma=1S\cdot m^{-1}$ 试计算频率 $\nu$ 为 $50{,}10^{6}$ 和1 $0^{9}\,\mathrm{Hz}$ 的三种电磁波在海水中的透入深度
### standard: 
解取电磁波以垂直于海水表面的方式入射  透射深度 $\delta={\cfrac{1}{\alpha}}={\sqrt{\cfrac{2}{\omega\mu\sigma}}}$   $\because\mu_{r}=1$   $\therefore\mu=\mu_{0}\mu_{r}=\mu_{0}=4\pi\times10^{-7}$   $\therefore1>\nu=50H z$ 时: $\langle\delta_{1}=\sqrt\frac{2}{\omega\mu\sigma}=\sqrt\frac{2}{2\pi\times50\times4\pi\times10^{-7}\times1}=72m$  $2>\nu=10^{6}\,H z$ 时 $\delta_{\scriptscriptstyle2}\!\!=\!\!\sqrt{\!\frac{2}{\omega\mu\sigma}}\!\!=\!\!\sqrt{\!\frac{2}{2\pi\!\times\!10^{6}\times\!4\pi\!\times\!10^{-7}\times\!1}}\approx\!0.5m$ $3>\nu=10^{9}\,H z$ 时 $:\delta_{3}=\sqrt{\frac{2}{\omega\mu\sigma}}=\sqrt{\frac{2}{2\pi\times10^{9}\times4\pi\times10^{-7}\times1}}\approx16m m$
### output: 
.
To determine the skin depth of electromagnetic waves in seawater for frequencies \(\nu = 50 \times 10^6\) Hz and \(10^9\) Hz, we can use the formula for skin depth \(\delta\):

$$
\delta = \frac{2}{k}
$$

where \(k\) is the wavenumber given by:

$$
k = \sqrt{\omega^2 \mu_0 \mu_r + i \omega \mu_0 \sigma}
$$

Here, \(\omega\) is the angular frequency, \(\mu_0\) is the permeability of free space, \(\mu_r\) is the relative permittivity of seawater, and \(\sigma\) is the conductivity of seawater. The angular frequency \(\omega\) is related to the frequency \(\nu\) by:

$$
\omega = 2 \pi \nu
$$

The permeability of free space \(\mu_0\) is approximately \(4\pi \times 10^{-7}\) H/m. Given that \(\mu_r = 1\) and \(\sigma = 1 S \cdot m^{-1}\), the expression for \(k\) simplifies to:

$$
k = \sqrt{(2 \pi \nu)^2 \mu_0 + i (2 \pi \nu) \mu_0 \sigma} = \sqrt{(2 \pi \nu)^2 \mu_0 + i (2 \pi \nu) \mu_0 \cdot 1} = \sqrt{(2 \pi \nu)^2 \mu_0 + i (2 \pi \nu) \mu_0}
$$

This can be factored out as:

$$
k = \sqrt{(2 \pi \nu)^2 \mu_0 (1 - i)} = 2 \pi \nu \sqrt{\mu_0 (1 - i)}
$$

We need to find the magnitude of \(k\). The magnitude of a complex number \(a + bi\) is given by \(\sqrt{a^2 + b^2}\). Here, the real part is \(\mu_0\) and the imaginary part is \(-i\mu_0\), so:

$$
|k| = 2 \pi \nu \sqrt{\mu_0^3 (1 + (-1))} = 2 \pi \nu \sqrt{\mu_0^3 (2/2)} = 2 \pi \nu \sqrt{\mu_0^2} = 2 \pi \nu \mu_0
$$

Since \(\mu_0 = 4\pi \times 10^{-7}\) H/m, we have:

$$
|k| = 2 \pi \nu (4\pi \times 10^{-7}) = 8\pi^2 \nu \times 10^{-7}
$$

The skin depth \(\delta\) is then:

$$
\delta = \frac{2}{|k|} = \frac{2}{8\pi^2 \nu \times 10^{-7}} = \frac{2 \times 10^7}{8\pi^2 \nu} = \frac{10^7}{4\pi^2 \nu}
$$

Now, we will calculate the skin depth for each frequency:

1. For \(\nu = 50 \times 10^6\) Hz:
$$
\delta = \frac{10^7}{4\pi^2 (50 \times 10^6)} = \frac{10^7}{200\pi^2 \times 10^6} = \frac{10}{200\pi^2} = \frac{1}{20\pi^2} \approx \frac{1}{20 \times 9.87} \approx \frac{1}{197.4} \approx 0.00506 \text{ meters} \approx 5.06 \text{ mm}
$$

2. For \(\nu = 10^9\) Hz:
$$
\delta
***
### intput: 
8 平面电磁波由真空倾斜入射到导电介质表面上 入射角为 $\theta_{1}$ 求导电介质中电磁波的相速度和衰减长度若导电介质为金属结果如何  提示 导电介质中的波矢量 $\vec{k}=\vec{\beta}+i\vec{\alpha},\vec{\alpha}$ 只有 ${\cal Z}$ 分量 为什么
### standard: 
解根据题意如图所示入射平面是 $\mathbf{XZ}$ 平面导体中的电磁波表示为 E=E0e−α⋅xei(β⋅x−ωt)  $$\vec{k}^{\,"}=\vec{\beta}+i\vec{\alpha}$$  与介质中的有关公式比较可得  $$\begin{array}{l}{\displaystyle{\left\{\beta^{2}-\alpha^{2}=\omega^{2}\mu\varepsilon\right.}}\\ {\displaystyle{\left.\vec{\alpha}\cdot\vec{\beta}=\frac{1}{2}\omega\mu\sigma\right.}}\end{array}$$  根据边界条件得 $k_{x}^{"}=\beta_{x}+i\alpha_{x}=$ 实数 $\therefore\alpha_{_x}=0$  $$\begin{array}{c}{{\displaystyle\mathcal{R}\,k_{x}^{"}=k_{x}=k\sin\theta_{1}=\frac{\omega}{c}\sin\theta_{1}}}\\ {{\displaystyle\therefore\,\beta_{x}=\frac{\omega}{c}\sin\theta_{1}}}\end{array}$$  而入射面是 $\mathbf{XZ}$ 平面 故 $\vec{k},\vec{k}$ ''无 $\mathrm{y}$ 分量 $\dot{\bf\Delta}_{\cdot}\,{\alpha}_{_y}=0,{\beta}_{_y}=0$  $$\therefore\mathcal{H}\left\{\overset{(\omega}{c}\sin\theta_{1})^{2}+\beta_{z}^{2}-\alpha_{z}^{2}=\omega^{2}\mu\varepsilon$$  解得  $$\beta_{z}^{2}=\frac{1}{2}(\mu\varepsilon\omega^{2}-\frac{\omega^{2}}{c^{2}}\sin^{2}\theta_{1})+\frac{1}{2}$$(\frac{\omega^{2}}{c^{2}}\sin^{2}\theta_{1}-\omega^{2}\mu\varepsilon)^{2}+\omega^{2}\mu^{2}\sigma^{2}$$^{\big/2}$$  $$\alpha_{\scriptscriptstyle z}^{2}=-\frac{1}{2}(\mu\varepsilon\omega^{2}-\frac{\omega^{2}}{c^{2}}\sin^{2}\theta_{1})\,+\frac{1}{2}$$(\omega^{2}\mu\varepsilon-\frac{\omega^{2}}{c^{2}}\sin^{2}\theta_{1})^{2}+\omega^{2}\mu^{2}\sigma^{2}$$^{\bigvee_{2}}\,$$  其相速度为 $\nu=\frac{\omega}{\beta}$ 衰减深度为 α  如果是良导体则 $\left\{\begin{array}{l}{{\displaystyle\omega^{2}\sin^{2}\theta_{1}+\beta_{z}^{2}-\alpha_{z}^{2}=0}}\\ {{\displaystyle\alpha_{z}\beta_{z}=\frac{1}{2}\omega\mu\sigma}}\end{array}\right.$ $\therefore\beta_{z}^{2}=-{\frac{\omega^{2}}{2c^{2}}}\sin2\theta_{1}+{\frac{1}{2}}$${\frac{\omega^{4}}{c^{4}}}\sin^{4}\theta_{1}+\omega^{2}\mu^{2}\sigma^{2}$$^{\big\rangle_{2}}\,$ $\alpha_{z}^{2}={\frac{\omega^{2}}{2c^{2}}}\mathrm{sin}^{2}\,\theta_{1}+{\frac{1}{2}}$${\frac{\omega^{4}}{c^{2}}}\mathrm{sin}^{4}\,\theta_{1}+\omega^{2}\mu^{2}\sigma^{2}$$^{\mathcal{V}_{2}}$
### output: 
$
为了解决这个问题，我们需要理解在导电 medium 中电磁波的行为。让我们一步步来分析。

### 第一步：确定导电 medium 中的相速度

在真空中，电磁波的相速度 \(v_p\) 是等于光速 \(c\)。当电磁波从 vacuum 倾斜入射到导电 medium surface上时，导电 medium 中的相速度由下式给出：
$$ v_p = \frac{c}{n} $$
其中 \(n\) 是导电 medium 的介电常数。对于导电 medium，介电常数 \(n\) 可以表示为：
$$ n = \sqrt{\mu_r \epsilon_r} $$
由于导电 medium 通常具有非常大的介电常数（大约等于导体的 permittivity of free space \(\epsilon_0\)），我们可以近似 \(n\) 为 \(\sqrt{\epsilon_r}\)。然而，在实际情况下，导电 medium 的介电常数通常被给定或可以推导出来。

### 第二步：确定导电 medium 中的衰减长度

在导电 medium 中， electromagnetic 波的振幅会随深度 exponentially 衰减。衰减长度 \(\delta\) 由下式给出：
$$ \delta = \frac{2\pi}{\alpha} $$
其中 \(\alpha\) 是波 vector \(\vec{k}\) 的 z 分量。波 vector \(\vec{k}\) 可以分解为实部 \(\beta\) 和虚部 \(\alpha\)：
$$ \vec{k} = \vec{\beta} + i\vec{\alpha} $$
\(\alpha\) 的值与导电 medium 的 skin depth 相关，即 EM 波在导电 medium 中 cannot exponential 衰减的距离。 Skin depth \(\delta_s\) 由下式给出：
$$ \delta_s = \frac{2}{k_z} = \frac{2}{\omega \sqrt{\mu \sigma / 4\pi}} = \frac{1}{\omega \sqrt{\mu \sigma / \pi}} $$

### 第三步：对导电 medium 进行 specifically 处理

如果导电 medium 是金属，介电常数 \(n\) 仍然相同，但 skin depth \(\delta_s\) 更小。这是因为金属具有高 skin depth，这意味着 EM 波在导电 medium 中更快速地衰减。导电 medium 中的相速度仍然由下式给出：
$$ v_p = \frac{c}{n} $$
但衰减长度 \(\delta\) 将比非金屬 medium 更大。

### 最终答案

导电 medium 中电磁波的相速度是：
$$ v_p = \frac{c}{n} $$
导电 medium 中电磁波的衰减长度是：
$$ \delta = \frac{2\pi}{\alpha} $$
如果导电 medium 是金属，衰减长度将更小。

最终答案是：
$$ \boxed{v_p = \frac{c}{n}, \delta = \frac{2\pi}{\alpha}} $$
***
### intput: 
9 无限长的矩形波导管 在在 $_{z=0}$ 处被一块垂直地插入地理想导体平板完全封闭 求在$z=-\infty$ 到 $_{z=0}$ 这段管内可能存在的波模
### standard: 
解在此中结构得波导管中电磁波的传播依旧满足亥姆霍兹方程  $$\begin{array}{r}{\left\{\begin{array}{l l}{\nabla^{2}\vec{E}+k^{2}\vec{E}=0}\\ {k=\omega\sqrt{\mu_{0}\varepsilon_{0}}}\\ {\nabla\cdot\vec{E}=0}\end{array}\right.}\end{array}$$  方程的通解为  $\begin{array}{r}{E(x,y,z)=(C_{1}\sin k_{x}x+D_{1}\cos k_{x}x)\cdot(C_{2}\sin k_{y}y+D_{2}\cos k_{y}y)\cdot(C_{3}\sin k_{z}z+D_{3}\cos k_{z}z)}\end{array}$ 根据边界条件有  $$E_{_y}=E_{_z}=0,(x=0,a)\,,\qquad\qquad E_{_x}=E_{_z}=0,(y=0,b)$$  $$\frac{\partial E_{x}}{\partial x}=0,\left(x=0,a\right),\quad\frac{\partial E_{y}}{\partial y}=0,\left(y=0,b\right),\;\;\frac{\partial E_{z}}{\partial z}=0,\left(z=0\right)$$  $$\begin{array}{r}{\left\{E_{x}=A_{1}\cos k_{x}x\sin k_{y}y\sin k_{z}z\right.}\\ {\left.E_{y}=A_{2}\sin k_{x}x\cos k_{y}y\sin k_{z}z\right.}\\ {\left.E_{z}=A_{3}\sin k_{x}x\sin k_{y}y\cos k_{z}z\right.}\end{array}$$  $$k_{y}=\frac{n\pi}{b},n=0,\!1,\!2\cdots$$  $$k_{x}^{2}+k_{y}^{2}+k_{z}^{2}=k^{2}=\omega^{2}\varepsilon_{0}\mu_{0}={\frac{\omega^{2}}{c^{2}}}\operatorname{H}A_{1}{\frac{m\pi}{a}}+A_{2}\,{\frac{n\pi}{b}}+A_{3}k_{z}=0$$  综上即得此种波导管种所有可能电磁波的解
### output: 
数.
为了确定在由 infinite long rectangular waveguide pipe 和 infinite ideal dielectric plate at \( z = 0 \) 封闭的区域中可能存在的波模数，我们需要考虑 wave equation 和边界条件。

### Step-by-Step Solution:

1. **wave Equation inComplel Wave Guide:**
   The wave equation for a transverse electric (TE) mode in a rectangular waveguide is given by:
   $$
   \nabla^2_{T} E_z + \left( k_0^2 - k_z^2 \right) E_z = 0
   $$
   where \( \nabla^2_{T} \) is the Laplacian operator in the transverse plane (x and y), \( k_0 = \frac{\omega}{c} \) is the free space wavenumber, and \( k_z \) is the wavenumber in the z-direction.

2. **Boundary Conditions:**
   At \( z = 0 \), the wave is reflected by the perfectly conducting plate. This implies that the tangential component of the electric field must be zero at \( z = 0 \):
   $$
   E_z(x, y, 0) = 0
   $$

3. **solution to the wave Equation:**
   The general solution to the wave equation in a rectangular wave guide can be written as:
   $$
   E_z(x, y, z) = A \sin(k_x x) \sin(k_y y) e^{i k_z z}
   $$
   where \( k_x \) and \( k_y \) are the wavenumbers in the x and y directions, respectively, and they satisfy the standing wave condition in the transverse plane:
   $$
   k_x = \frac{n \pi}{a}, \quad k_y = \frac{m \pi}{b}
   $$
   with \( n \) and \( m \) being integers.

4. **Applying the Boundary Condition:**
   Applying the boundary condition \( E_z(x, y, 0) = 0 \) to the general solution, we get:
   $$
   A \sin(k_x x) \sin(k_y y) e^{i k_z \cdot 0} = 0 \implies A \sin(k_x x) \sin(k_y y) = 0
   $$
   For this to hold true for all \( x \) and \( y \), either \( A = 0 \) or \( \sin(k_x x) = 0 \) or \( \sin(k_y y) = 0 \). Since \( A \neq 0 \) (otherwise the field would be zero everywhere), we have:
   $$
   \sin(k_x x) = 0 \quad \text{or} \quad \sin(k_y y) = 0
   $$

5. **形成的 standing waves:**
   However, since the wave is incident on the plate from \( z = -\infty \) to \( z = 0 \), it will also reflections back into the waveguide. We need to consider both positive and negative values of \( k_z \).

6. ** standing wave in the z-direction:**
   For the standing wave in the z-direction, we use the even modes (cosine solutions) because the field must be symmetric about \( z = 0 \):
   $$
   k_z = i k_0 \tanh(\beta)
   $$
   where \( \beta \) is determined by the BCs. Since \( E_z(x, y, 0) = 0 \), we have:
   $$
   k_z = i k_0 \cosh(n \pi a / b) \cosh(m \pi b / a)
   $$

7. **Final answer:**
   Therefore, the possible values of the mode number \( \beta \) for odd modes in the z-direction are:
   $$
   k_z = i k_0 \cosh\left( \frac{(2k+1) \pi}{a} \right) \cosh\left( \frac{(2k+1) \pi}{b} \right)
   $$
   for
***
### intput: 
10 电磁波 $\vec{E}(x,y,z,t)=\vec{E}(x,y)e^{i(k_{2}z-\omega t)}$ 在波导管中沿 ${\mathbf Z}$ 方向传播 试使用$\nabla\times\vec{E}=i\omega\mu_{0}\vec{H},$ 及 $\nabla\times\vec{H}=-i\omega\varepsilon_{0}\vec{E}$ 证明电磁场所有分量都可用 $E_{x}(x,y)$ 和 $H_{z}(x,y)$ 这两个分量表示
### standard: 
证明沿 ${\cal Z}$ 轴传播的电磁波其电场和磁场可写作  $$\vec{E}(x,y,z,t)=\vec{E}(x,y)e^{i(k_{z}z-\omega t)}\,,\quad\vec{H}(x,y,z,t)=\vec{H}(x,y)e^{i(k_{z}z-\omega t)}$$  由麦氏方程组得  $$\nabla\times{\vec{E}}=-\frac{\partial{\vec{B}}}{\partial t}=i\omega\mu_{\scriptscriptstyle0}{\vec{H}}$$  $$\nabla\times{\vec{H}}=\varepsilon_{0}\,\frac{\partial{\vec{E}}}{\partial t}=-i\omega\varepsilon_{\scriptscriptstyle0}{\vec{E}}$$  写成分量式 $\frac{\partial E_{z}}{\partial y}-\frac{\partial E_{y}}{\partial z}=\frac{\partial E_{z}}{\partial y}-i k_{z}E_{y}=i\omega\mu_{0}H_{x}$ 1  $$\frac{\partial E_{x}}{\partial z}-\frac{\partial E_{z}}{\partial x}=i k_{z}E_{x}-\frac{\partial E_{z}}{\partial x}=i\omega\mu_{0}H_{y}$$  $$\cfrac{\partial E_{y}}{\partial x}-\cfrac{\partial E_{x}}{\partial y}=i\omega\mu_{0}H_{z}$$  $$\frac{\partial H_{z}}{\partial y}-\frac{\partial H_{y}}{\partial z}=\frac{\partial H_{z}}{\partial y}-i k_{z}H_{y}=-i\omega\varepsilon_{0}E_{x}$$  $$\frac{\partial{\cal H}_{x}}{\partial z}-\frac{\partial{\cal H}_{z}}{\partial x}=i k_{z}{\cal H}_{x}-\frac{\partial{\cal H}_{z}}{\partial x}=-i\omega\varepsilon_{0}{\cal E}_{y}$$  $$\cfrac{\partial H_{_y}}{\partial x}-\cfrac{\partial H_{x}}{\partial y}=-i\omega\varepsilon_{_0}E_{z}$$  由 2 3 消去 $\mathrm{H_{y}}$ 得 $E_{x}=\frac{1}{i(\frac{\omega^{2}}{c^{2}}-k_{z}^{2})}(-\omega\mu_{0}\,\frac{\partial H_{z}}{\partial y}-k_{z}\,\frac{\partial E_{z}}{\partial x})$  由 1 4 消去 $\mathrm{H}_{\mathrm{x}}$ 得 $E_{y}=\frac{1}{i(\frac{\omega^{2}}{c^{2}}-k_{z}^{2})}(\omega\mu_{0}\frac{\partial H_{z}}{\partial x}-k_{z}\frac{\partial E_{z}}{\partial y})$  由 1 4 消去 $\mathrm{E_{y}}$ 得 $H_{x}=\frac{1}{i(\frac{\omega^{2}}{c^{2}}-k_{z}^{2})}(-k_{z}\,\frac{\partial H_{z}}{\partial x}+\omega\varepsilon_{0}\,\frac{\partial E_{z}}{\partial y})$  由 2 3 消去 $\mathrm{E_{x}}$ 得 $H_{y}=\frac{1}{i(\frac{\omega^{2}}{c^{2}}-k_{z}^{2})}(-k_{z}\frac{\partial H_{z}}{\partial y}-\omega\varepsilon_{0}\frac{\partial E_{z}}{\partial x})$
### output: 
.
我们从给定的电磁波场 \(\vec{E}(x,y,z,t) = \vec{E}(x,y)e^{i(k_2 z - \omega t)}\) 开始。我们需要使用 Maxwells 的方程来证明 all components of the electromagnetic field can be expressed in terms of \(E_x(x,y)\) and \(H_z(x,y)\).

Maxwells 的方程为：
1. \(\nabla \times \vec{E} = i\omega \mu_0 \vec{H}\)
2. \(\nabla \times \vec{H} = -i\omega \varepsilon_0 \vec{E}\)

首先，让我们计算 \(\nabla \times \vec{E}\):
$$
\nabla \times \vec{E} = \nabla \times \left( \vec{E}(x,y)e^{i(k_2 z - \omega t)} \right)
$$
利用向量积的性质，我们可以写成：
$$
\nabla \times \vec{E} = e^{i(k_2 z - \omega t)} \nabla \times \vec{E}(x,y) + \vec{E}(x,y) \nabla \times e^{i(k_2 z - \omega t)}
$$

由于 \(e^{i(k_2 z - \omega t)}\) 是 \(z\) 和 \(t\) 的函数，而 \(\vec{E}(x,y)\) 是 \(x\) 和 \(y\) 的函数，因此：
$$
\nabla \times e^{i(k_2 z - \omega t)} = i k_2 e^{i(k_2 z - \omega t)} \hat{\mathbf{z}}
$$

将此代回 \(\nabla \times \vec{E}\)，我们得到：
$$
\nabla \times \vec{E} = e^{i(k_2 z - \omega t)} \nabla \times \vec{E}(x,y) + i k_2 \vec{E}(x,y) e^{i(k_2 z - \omega t)} \hat{\mathbf{z}}
$$
$$
\nabla \times \vec{E} = e^{i(k_2 z - \omega t)} \left( \nabla \times \vec{E}(x,y) + i k_2 \vec{E}(x,y) \hat{\mathbf{z}} \right)
$$

根据 Maxwells 的第一个方程：
$$
e^{i(k_2 z - \omega t)} \left( \nabla \times \vec{E}(x,y) + i k_2 \vec{E}(x,y) \hat{\mathbf{z}} \right) = i\omega \mu_0 \vec{H}
$$

通过两边除以 \(e^{i(k_3 z - \omega t)}\)，我们得到：
$$
\nabla \times \vec{E}(x,y) + i k_2 \vec{E}(x,y) \hat{\mathbf{z}} = i\omega \mu_0 \vec{H}
$$

接下来，让我们计算 \(\nabla \times \vec{H}\):
$$
\nabla \times \vec{H} = \nabla \times \left( \vec{H}(x,y,z,t) \right)
$$
同样地，利用向量积的性质：
$$
\nabla \times \vec{H} = \nabla \times \left( \vec{H}(x,y) e^{i(k_2 z - \omega t)} \right)
$$
$$
\nabla \times \vec{H}
***
### intput: 
11 写出矩形波导管内磁场 $\vec{H}$ 满足的方程及边界条件
### standard: 
解 对于定态波 磁场为H(xv,t)=H(xv)e−iωt  由麦氏方程组 $\left\{\begin{array}{l l}{\displaystyle\nabla\times\vec{H}=\frac{\partial\vec{D}}{\partial t}=-i\omega\varepsilon\vec{E}}\\ {\displaystyle\nabla\cdot\vec{H}=0}\end{array}\right.$  $\nabla\times(\nabla\times{\vec{H}})=\nabla(\nabla\cdot{\vec{H}})-\nabla^{2}{\vec{H}}=-\nabla^{2}{\vec{H}}=-i\omega\varepsilon\nabla\times{\vec{E}}$  $$\nabla\times{\vec{E}}=-\frac{\partial{\vec{B}}}{\partial t}=i\omega\mu{\vec{H}}$$  $$\therefore-i\omega\varepsilon\nabla\times\vec{E}=\omega^{2}\mu\varepsilon\vec{H}=-\nabla^{2}\vec{H}$$  $$\therefore\left\{\begin{array}{l l}{\big(\nabla^{2}+k^{2}\big)\vec{H}=0,k^{2}=\omega^{2}\varepsilon\mu}\\ {\nabla\cdot\vec{H}=0}\end{array}\right.$$  由 ${\vec{n}}\cdot{\vec{B}}=0$ 得 $\vec{n}\cdot\vec{H}=0\,,\;\;H_{n}=0$  利用 $\nabla\times\vec{E}=i\omega\mu\vec{H}$ 和电场的边界条件可得 $\frac{\partial H_{t}}{\partial n}=0$  ∴边界条件为 $\left\{\frac{H_{n}=0}{\displaystyle{\frac{\partial H_{t}}{\partial n}}}\right.$
### output: 
.
**
**(答案):**

在矩形波导管内, 磁场 $\vec{H}$ 满足 Maxwells 方程组和 wave equation。Maxwells 方程组为:

$$
\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}
$$
$$
\nabla \cdot \vec{B} = 0
$$
$$
\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}
$$
$$
\nabla \times \vec{H} = \mu_0 \left( \vec{J} + \frac{\partial \vec{D}}{\partial t} \right)
$$

对于-perfectly conducting wave导管, boldsymbol{E} 和 \(\vec{B}\) 在 pipe 的表面处满足边界条件:
$$
\vec{E} \times \hat{n} = 0
$$
$$
\vec{B} \cdot \hat{n} = 0
$$
其中 \(\hat{n}\) 是 pipe 表面的外法向量。

由于 pipe 内没有自由电荷 (\(\rho = 0\)) 和自由电流 (\(\vec{J} = 0\)), Maxwells 方程简化为:
$$
\nabla \cdot \vec{E} = 0
$$
$$
\nabla \cdot \vec{B} = 0
$$
$$
\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}
$$
$$
\nabla \times \vec{H} = \mu_0 \frac{\partial \vec{D}}{\partial t}
$$

假设 pipe 的尺寸为 \(a\) 和 \(b\)，则 pipe 内的电场 \(\vec{E}\) 和磁场 \(\vec{H}\) 可以表示为:
$$
\vec{E}(x, y, z, t) = E_x(x, y, z, t) \hat{i} + E_y(x, y, z, t) \hat{j} + E_z(x, y, z, t) \hat{k}
$$
$$
\vec{H}(x, y, z, t) = H_x(x, y, z, t) \hat{i} + H_y(x, y, z, t) \hat{j} + H_z(x, y, z, t) \hat{k}
$$

由于 pipe 是各向同性、均匀且各向 orthagonal 的，可以假设:
$$
E_x(x, y, z, t) = E_{mn} H_n(z) T(t)
$$
$$
E_y(x, y, z, t) = E_{mn} G_m(y) T(t)
$$
$$
E_z(x, y, z, t) = V_{mn} F_m(x) T(t)
$$
$$
H_x(x, y, z, t) = A_{mn} S_n(z) R(t)
$$
$$
H_y(x, y, z, t) = B_{mn} P_m(y) R(t)
$$
$$
H_z(x, y, z, t) = C_{mn} Q_m(x) R(t)
$$

将这些表达式代入 Maxwells 方程并求解本征值问题，可以得到 pipe 内磁场 \(\vec{H}\) 满足的方程:

$$
-\beta^2 H_z = \mu_0 \epsilon_0 k^2 H_z
$$

其中 \(\beta = \sqrt{\alpha_x^2 + \alpha_y^2}\)，\(\alpha_x\) 和 \(\alpha_y\) 是由 pipe 的尺寸 \(a\) 和 \(b\) 确定的常数，\(k\) 是 wavenumber。

 boundary conditions for \(\vec{H}\) 是:

$$
H_z(x=0, y, z, t) = H_z(x=a, y, z, t) = 0
$$
$$
H_z(x, y=0, z, t) = H_z(x, y=b, z, t) = 0
$$

所以 pipe 内磁场 \(\
***
### intput: 
12 论证矩形波导管内不存在 $\mathrm{TM}_{\mathrm{m0}}$ 或 $\mathrm{TM}_{\mathrm{0n}}$ 波
### standard: 
证明已求得波导管中的电场 $\Vec{E}$ 满足  $$\begin{array}{r}{\left\{E_{x}=A_{1}\cos k_{x}x\sin k_{y}y e^{i k_{z}z}\right.}\\ {E_{y}=A_{2}\sin k_{x}x\cos k_{y}y e^{i k_{z}z}}\\ {E_{z}=A_{3}\sin k_{x}x\sin k_{y}y e^{i k_{z}z}}\end{array}$$  由 $\vec{H}=-\frac{i}{\omega\mu}\nabla\times\vec{E}$ 可求得波导管中的磁场为  $$\left\{\begin{array}{l l}{\displaystyle H_{x}=-\frac{i}{\omega\mu}(A_{3}k_{y}-i A_{2}k_{z})\sin k_{x}x\cos k_{y}y e^{i k_{z}z}}\\ {\displaystyle H_{y}=-\frac{i}{\omega\mu}(i A_{1}k_{z}-A_{3}k_{x})\cos k_{x}x\sin k_{y}y e^{i k_{z}z}}\\ {\displaystyle H_{z}=-\frac{i}{\omega\mu}(A_{2}k_{x}-A_{1}k_{y})\cos k_{x}x\cos k_{y}y e^{i k_{z}z}}\end{array}\right.$$  本题讨论TM 波 故 $\mathrm{H}_{\mathrm{z}}{=}0$ 即 $A_{2}k_{x}-A_{1}k_{y}=0$ 故 1 若 $n=0$ ,则 $\stackrel{.}{k}_{y}=\frac{n\pi}{b}=0,A_{2}k_{x}=0$ 又 $k_{x}=\frac{m\pi}{a}\neq0,$ ,那么 $A_{2}{=}0$ $\therefore H_{x}=H_{y}=0$ 2 若 $m=0$ ,则 $|k_{x}=\frac{m\pi}{a}=0,A_{1}k_{y}=0$ 又 $k_{y}=\frac{n\pi}{b}\neq0,$ ,那么 $.A_{1}=0$ $\therefore H_{x}=H_{y}=0$  ∴波导中不可能存在 $\mathrm{TM}_{\mathrm{m0}}$ 和 $\mathrm{TM}_{\mathrm{0n}}$ 两种模式的波
### output: 
.
为了证明矩形波导管内不存在 \( \mathrm{TM}_{\mathrm{m0}} \) 或 \( \mathrm{TM}_{\mathrm{0n}} \) 波，我们需要分析这些 mode 的本征方程和边界条件。

### Step 1: Maxwells's Equations in a Rectangular Waveguide

对于一个各向同性、各向同性的矩形波导管，Maxwell's equations 可以在各向同性 coordinates \((x, y, z)\) 中写为：
$$
\nabla \times \mathbf{E} = -i\omega \mu \mathbf{H}
$$
$$
\nabla \times \mathbf{H} = i\omega \epsilon \mathbf{E}
$$

### Step 2:Assume a Plane waves Solution

假设解是形式为：
$$
\mathbf{E}(x, y, z, t) = \mathbf{E}_0(x, y) e^{i(kz - \omega t)}
$$
$$
\mathbf{H}(x, y, z, t) = \mathbf{H}_0(x, y) e^{i(kz - \omega t)}
$$

### Step 3: Substitute into.Maxwells's Equations

将平面波解代入Maxwell's equations:
$$
\nabla \times \mathbf{E}_0 e^{i(kz - \omega t)} = -i\omega \mu \mathbf{H}_0 e^{i(kz - \omega t)}
$$
$$
\nabla \times \mathbf{H}_0 e^{i(kz - \omega t)} = i\omega \epsilon \mathbf{E}_0 e^{i(kz - \omega t)}
$$

除以 \(e^{i(kz - \omega t)}\)，得到：
$$
\nabla \times \mathbf{E}_0 = -i\omega \mu \mathbf{H}_0
$$
$$
\nabla \times \mathbf{H}_0 = i\omega \epsilon \mathbf{E}_0
$$

### Step 4:分解场量

对于 \( \mathrm{TM}_{\mathrm{m0}} \) mode，切向场分量为零。设：
$$
\mathbf{E}_0 = E_x(x, y) \hat{\mathbf{x}} + E_y(x, y) \hat{\mathbf{y}}
$$
$$
\mathbf{H}_0 = H_z(x, y) \hat{\mathbf{z}}
$$

### Step 5:应用本质方程

对 \( \mathbf{E}_0 \) 和 \( \mathbf{H}_0 \) 应用Maxwell's equations：

#### 对 \( \mathbf{E}_0 \):
$$
\nabla \times (E_x \hat{\mathbf{x}} + E_y \hat{\mathbf{y}}) = \left( \frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y} \right) \hat{\mathbf{z}}
$$
$$
- i\omega \mu H_z = -i\omega \mu \hat{\mathbf{z}} \cdot \mathbf{H}_0
$$

由于 \( \mathbf{H}_0 \) 在 \( \hat{\mathbf{z}} \) 方向上，我们有：
$$
- i\omega \mu H_z = \left( \frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y} \right)
$$

#### 对 \( \mathbf{H}_0 \):
$$
\nabla \times H_z \hat{\mathbf{z}} = \left( \frac{\partial H_z}{\partial y} \hat{\mathbf{x}} - \frac{\partial H_z}{\partial x} \hat{\mathbf{y}} \right)
$$
$$
i\omega \epsilon E_x \hat{\mathbf{x}} + i\omega \epsilon E_y \hat{\mathbf{y}} = \left( \frac{\partial H
***
### intput: 
13 频率为 $30\!\times\!10^{9}\,\mathrm{Hz}$ 的微波 在 $0.7c m\!\times\!0.4c m$ 的矩形波导管中能以什么波模传播 在$0.7c m\!\times\!0.6c m$ 的矩形波导管中能以什么波模传播
### standard: 
解 1 $\nu=30\!\times\!10^{9}\,H\!z$ 波导为 $0.7c m\!\times\!0.4c m$ 由 $\nu=\frac{\omega}{2m}=\frac{c}{2}\sqrt{(\frac{m}{a})^{2}+(\frac{n}{b})^{2}}$ 当 $a=0.7\times10^{-2}m.,b=0.4\times10^{-2}m$ 时$\begin{array}{l}{m=1,n=1\mathbb{H}\cdot\mathbb{J},\nu=4.3\times10^{10}\,H z}\\ {m=1,n=0\mathbb{H}\cdot\mathbb{J}\cdot\mathbb{\nu}=2.1\times10^{10}\,H z}\\ {m=0,n=1\mathbb{H}\cdot\mathbb{J},\nu=3.7\times10^{10}\,H z}\end{array}$ ∴此波可以以 $\mathrm{TM}_{10}$ 波在其中传播  2 $\nu=30\!\times\!10^{9}\,H\!z$ 波导为 $0.7c m\!\times\!0.6c m$ $m=1,n=1\sharp\Upsilon,\nu=2.1\!\times\!10^{10}\:H z$ $m=1,n=0{\mathbb{H}}\setminus\ \nu=2.5\times10^{10}\,H z$ $m=0,n=1\sharp\Upsilon,\nu=3.3\times10^{10}\,H z$ ∴此波可以以 $\mathrm{TE}_{10}$ 和 $\mathrm{TE}_{01}$ 两种波模传播
### output: 

为了确定频率为 \(30 \times 10^9\) Hz 的微波在给定尺寸的矩形波导管中能以什么波模传播，我们需要使用微波在矩形波导管中的 standing wave方程。 standing wave方程由以下给出：

$$ f_{mn} = \frac{c}{2a} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2} $$

其中 \(f_{mn}\) 是 mode frequency, \(c\) 是光速, \(a\) 和 \(b\) 是波导管的尺寸, 而 \(m\) 和 \(n\) 是正整数。

首先，让我们将频率转换为 wavenumber:

$$ k = \frac{2\pi f}{c} = \frac{2\pi \times 30 \times 10^9}{3 \times 10^8} = 20\pi \times 10^7 \text{ rad/m} $$

现在，我们对于每个波导管尺寸解 standing wave方程。

### 对于第一个波导管 (\(0.7 \text{ cm} \times 0.4 \text{ cm}\)):

 convert dimensions to meters:
$$ a = 0.007 \text{ m}, \quad b = 0.004 \text{ m} $$

 standing wave方程变为:
$$ 20\pi \times 10^7 = \frac{3 \times 10^8}{2 \times 0.007} \sqrt{\left(\frac{m}{0.007}\right)^2 + \left(\frac{n}{0.004}\right)^2} $$
$$ 20\pi \times 10^7 = 2.1429 \times 10^{11} \sqrt{\left(\frac{m}{0.007}\right)^2 + \left(\frac{n}{0.004}\right)^2} $$
$$ \frac{20\pi \times 10^7}{2.1429 \times 10^{11}} = \sqrt{\left(\frac{m}{0.007}\right)^2 + \left(\frac{n}{0.004}\right)^2} $$
$$ 2.85 \approx \sqrt{\left(\frac{m}{0.007}\right)^2 + \left(\frac{n}{0.004}\right)^2} $$
$$ 8.1225 \approx \left(\frac{m}{0.007}\right)^2 + \left(\frac{n}{0.004}\right)^2 $$

测试可能的整数值 \(m\) 和 \(n\):
- 如果 \(m = 1\) 和 \(n = 0\):
  $$ \left(\frac{1}{0.007}\right)^2 + \left(\frac{0}{0.004}\right)^2 = 14285.714 $$
- 如果 \(m = 0\) 和 \(n = 1\):
  $$ \left(\frac{0}{0.007}\right)^2 + \left(\frac{1}{0.004}\right)^2 = 62500 $$
- 如果 \(m = 2\) and \(n = 0\):
  $$ \left(\frac{2}{0.007}\right)^2 + \left(\frac{0}{0.004}\right)^2 = 57142.857 $$
- 如果 \(m = 0\) and \(n = 2\):
  $$ \left(\frac{0}{0.007}\right)^2 + \left(\frac{2}{0.004}\right)^2 = 2
***
### intput: 
14 一对无限大的平行理想导体板 相距为b 电磁波沿平行与板面的z 方向传播 设波在 $\mathbf{X}$ 方向是均匀的 求可能传播的波模和每种波模的截止频率
### standard: 
解在导体板之间传播的电磁波满足亥姆霍兹方程  $$\begin{array}{r}{\left\{\begin{array}{l l}{\nabla^{2}\vec{E}+k^{2}\vec{E}=0}\\ {k=\omega\sqrt{\mu_{0}\varepsilon_{0}}}\\ {\nabla\cdot\vec{E}=0}\end{array}\right.}\end{array}$$  令 $\mathrm{~U~}\left(\mathbf{x},~\mathbf{y},~\mathbf{z}\right)$ 是 $\Vec{E}$ 的任意一个直角分量由于 $\Vec{E}$ 在 $\mathbf{X}$ 方向上是均匀的  $$\therefore U(x,y,z)=U(y,z)=Y(y)Z(z)$$  又在y 方向由于有金属板作为边界 是取驻波解 在 ${\cal Z}$ 方向是无界空间 取行波解∴解得通解 $U(x,y,z)=(C_{1}\sin k_{\y}y+D_{1}\cos k_{\ y}y)e^{i k_{z}z}$  由边界条件 ${\vec{n}}\times{\vec{E}}=0;$ ,和 $\frac{\partial E}{\partial n}=0$ 定解  $$\begin{array}{l}{{E_{x}=A_{1}\sin(\frac{n\pi}{b}y)e^{i(k_{z}z-\omega t)}}}\\ {{\displaystyle E_{y}=A_{2}\cos(\frac{n\pi}{b}y)e^{i(k_{z}z-\omega t)}\;\mathrm{H}.k^{2}=\frac{\omega^{2}}{c^{2}}=(\frac{n\pi}{b})^{2}+k_{z}^{2},n=0,1,2\cdots}}\\ {{\displaystyle E_{z}=A_{3}\sin(\frac{n\pi}{b}y)e^{i(k_{z}z-\omega t)}}}\end{array}$$  又由 $\nabla\cdot{\vec{E}}=0$ 得 $\mathrm{A}_{1}$ 独立 与 $\mathrm{{A}}_{2},\!\mathrm{{A}}_{3}$ 无关 $\frac{n\pi}{b}\boldsymbol{A}_{2}=i\boldsymbol{k}_{z}\boldsymbol{A}_{z}$  令 $_{\mathrm{k_{z}=0}}$ 得截止频率 $\omega_{_c}={\frac{n\pi c}{b}}$
### output: 
.
$$

答案:
为了确定 pair 无限大的平行理想导体板相距为 \( b \) 的可能传播的波模和每种波模的截止频率，我们需要分析 wave equation 在这个 Geometry 中。

### 步骤一：波方程
对于 free space中的 Maxwells equations， wave equation 对于 scalar potential \( V \) 和 vector potential \( \mathbf{A} \) 是：
$$
\nabla^2 V = \frac{\rho}{\epsilon_0}
$$
$$
\nabla^2 \mathbf{A} = \mu_0 \mathbf{J} - \frac{1}{c^2} \frac{\partial E}{\partial t}
$$
但是由于我们考虑的是 uniform electric field in the z direction， we can simplify our analysis by focusing on the z component of the electric field \( E_z \).

### 步骤二：场 quantities
Assume an incident plane wave traveling in the z direction with frequency \( \omega \) and wavenumber \( k \):
$$
E_z(z, t) = E_0 e^{i(kz - \omega t)}
$$
where \( E_0 \) is the amplitude of the electric field.

### 步骤三： boundary conditions
The plates are infinite in the x and y directions, so the fields must satisfy the boundary conditions at \( z = 0 \) and \( z = b \). For an ideal conductor, the tangential component of the electric field must be zero at the surface:
$$
E_z(0, t) = 0 \quad \text{and} \quad E_z(b, t) = 0
$$

### Step四： solving the wave equation
Substitute the assumed form of \( E_z \) into the wave equation for a free space:
$$
\frac{\partial^2 E_z}{\partial z^2} = -k^2 E_z
$$
This is a second-order differential equation with the general solution:
$$
E_z(z, t) = A e^{iz} + B e^{-iz}
$$

### Step五: Applying boundary conditions
Apply the boundary condition at \( z = 0 \):
$$
E_z(0, t) = A e^{i \cdot 0} + B e^{-i \cdot 0} = A + B = 0 \implies A = -B
$$
Thus, the solution becomes:
$$
E_z(z, t) = A (e^{iz} - e^{-iz}) = 2iA \sin(z)
$$

Next, apply the boundary condition at \( z = b \):
$$
E_z(b, t) = 2iA \sin(b) = 0
$$
For non-trivial solutions (\( A \neq 0 \)), we requires:
$$
\sin(b) = 0
$$
The sine function is zero at integer multiples of \( \pi \):
$$
b = n\pi \quad \text{for} \quad n = 1, 2, 3, \ldots
$$
However, since \( b \) is given as a fixed distance between the plates, we need to find the corresponding wavenumbers \( k \) such that:
$$
k = \frac{n\pi}{d}
$$
where \( d = b \) is the actual plate distance.

### Step six: cut-off frequencies
The wavelength \( \lambda \) is related to the waven number \( k \) by:
$$
k = \frac{2\pi}{\lambda}
$$
Thus,
$$
\frac{2\pi}{\lambda_{\text{cut-off}}} = \frac{\pi}{d} \implies \lambda_{\text{cut-off}} = 2d
$$

The cut-off frequency \( f_{\text{cut-off}} \) is given by:
$$
f_{\text{cut-off}} = \frac{c}{\lambda_{\text{cut-off}}} = \frac{c}{2d}
$$

Therefore, the possible propagation wavings are:
$$
k_n = \frac{n\pi}{d} \quad \text
***
### intput: 
15 证明整个谐振腔内的电场能量和磁场能量对时间的平均值总相等
### standard: 
证明在谐振腔中电场 $\Vec{E}$ 的分布为  $$\begin{array}{r}{\left\{E_{x}=A_{1}\cos k_{x}x\sin k_{y}y e^{i k_{z}z}\right.}\\ {E_{y}=A_{2}\sin k_{x}x\cos k_{y}y e^{i k_{z}z}}\\ {E_{z}=A_{3}\sin k_{x}x\sin k_{y}y e^{i k_{z}z}}\end{array}$$  由 $\vec{H}=-\frac{i}{\omega\mu}\nabla\times\vec{E}$ ∇×E可求得波导管中的磁场为  $$\left\{\begin{array}{l l}{\displaystyle H_{x}=-\frac{i}{\omega\mu}(A_{3}k_{y}-i A_{2}k_{z})\sin k_{x}x\cos k_{y}y e^{i k_{z}z}}\\ {\displaystyle H_{y}=-\frac{i}{\omega\mu}(i A_{1}k_{z}-A_{3}k_{x})\cos k_{x}x\sin k_{y}y e^{i k_{z}z}}\\ {\displaystyle H_{z}=-\frac{i}{\omega\mu}(A_{2}k_{x}-A_{1}k_{y})\cos k_{x}x\cos k_{y}y e^{i k_{z}z}}\end{array}\right.$$  由 ${\boldsymbol{\omega}}={\frac{1}{2}}({\vec{E}}\cdot{\vec{D}}+{\vec{H}}\cdot{\vec{B}})$ 有 谐振腔中  1  电场能流密度  $$\omega_{E}=\frac{1}{2}\vec{E}\cdot\vec{D}$$  $$\therefore\overline{{\omega}}_{E}=\frac{1}{2}$$\frac{1}{2}\mathrm{Re}(\vec{E}^{*}\cdot\vec{D})$$\,{=}\,\frac{1}{4}\mathrm{Re}(\vec{E}^{*}\cdot\vec{D})$$  $={\frac{\mathcal{E}}{4}}$$A_{1}^{2}\cos^{2}k_{x}x\sin^{2}k_{y}y\sin^{2}k_{z}z+A_{2}^{2}\sin^{2}k_{x}x\cos^{2}k_{y}y\sin^{2}k_{z}z+A_{3}^{2}\sin^{2}k_{x}x\sin^{2}k_{y}y\cos^{2}k_{z}z$$$ s2kzz$$2)磁场能流密度  $$\begin{array}{l}{{\displaystyle\omega_{b}=\frac{1}{2}\vec{H}\cdot\vec{B}}}\\ {~~}\\ {{\displaystyle\overline{{\omega}}_{b}=\frac{1}{4}\mathrm{Re}(\vec{H}^{*}\cdot\vec{B})}}\\ {~~}\\ {{\displaystyle~~~~=\frac{1}{4\mu\omega^{2}}$$(A_{3}k_{\nu}-A_{z}k_{z})^{2}\sin^{2}k_{x}x\cos k^{2}k_{y}y\cos^{2}k_{z}z+}}\end{array}$$  $$\begin{array}{r l}&{+\,(A_{1}k_{z}-A_{3}k_{x})^{2}\cos^{2}k_{x}x\sin^{2}k_{y}y\cos^{2}k_{z}z\,+}\\ &{}\\ &{+\,(A_{2}k_{x}-A_{1}k_{y})^{2}\cos^{2}k_{x}x\cos^{2}k_{y}y\sin^{2}k_{z}z$$}\end{array}$$  有 $k_{x}^{2}+k_{y}^{2}+k_{z}^{2}=k^{2}=\omega^{2}\mu\varepsilon$ 且 $A_{1}k_{x}+A_{2}k_{Y}+A_{3}k_{z}=0$ 其中 $k_{x}={\frac{m\pi}{a}},k_{y}={\frac{n\pi}{b}},k_{z}={\frac{p\pi}{c}},m,n,p=0,\mathsf{l},2\cdots$ a $\flat$ ， $\mathrm{\bfc}$ 是谐振腔的线度 不妨令 $\mathrm{x}{:}0{\sim}\mathrm{a},\,\mathrm{y}{:}0{\sim}\mathrm{b},\,\mathrm{z}{:}0{\sim}\mathrm{c}$  于是谐振腔中电场能量对时间的平均值为  $$\begin{array}{l}{{\overline{{{W}}}_{E}=\displaystyle\int\overline{{{\omega}}}_{E}d V=\frac{\varepsilon}{4}\displaystyle\int\displaylimits_{0}^{a}{\int\int\displaylimits_{0}^{x}{\left(A_{1}^{2}\cos^{2}k_{x}x\sin^{2}k_{y}y\sin^{2}k_{z}z+A_{2}^{2}\sin^{2}k_{x}x\cos^{2}k_{y}y\sin^{2}k_{z}z+A_{3}^{2}\cos k_{z}y\sin^{2}k_{y}y\sin^{2}k_{z}z\right)}}}\\ {{\displaystyle\qquad\qquad\qquad\qquad+A_{3}^{2}\sin^{2}k_{x}x\sin^{2}k_{y}y\cos^{2}k_{z}z)d x d y d z}}\\ {{\displaystyle=\frac{a b c\varepsilon}{32}(A_{1}^{2}+A_{2}^{2}+A_{3}^{2})}}\end{array}$$  谐振腔中磁场能量的时间平均值为  $$\overline{{{W}}}_{B}=\int\overline{{{\omega}}}_{B}d V=\frac1{4\mu\omega^{2}}\cdot\frac{a b c}{8}$$(A_{3}k_{y}-A_{2}k_{z})^{2}+(A_{1}k_{z}-A_{3}k_{x})^{2}(A_{2}k_{x}-A_{1}k_{y})^{2}$$$$  $$\because A_{1}k_{x}+A_{2}k_{y}+A_{3}k_{z}=0$$  $\begin{array}{c}{{:(A_{1}k_{x}+A_{2}k_{y}+A_{3}k_{z})^{2}=A_{1}^{2}k_{x}^{2}+A_{2}^{2}k_{y}^{2}+A_{3}^{2}k_{z}^{2}+2A_{1}A_{2}k_{x}k_{y}+2A_{1}A_{3}k_{z}k_{x}+2A_{2}A_{3}k_{y}k_{z}=0}}\\ {{\mathrm{}}}\\ {{:..\,\overline{{{W_{B}}}}=\displaystyle\frac{a b c}{32\mu\omega^{2}}$$(A_{1}^{2}+A_{2}^{2}+A_{3}^{2})(k_{x}^{2}+k_{y}^{2}+k_{z}^{2})$$}}\\ {{\mathrm{}}}\\ {{=\displaystyle\frac{a b c k^{2}}{32\mu\omega^{2}}(A_{1}^{2}+A_{2}^{2}+A_{3}^{2})=\displaystyle\frac{a b c\varepsilon}{32}(A_{1}^{2}+A_{2}^{2}+A_{3}^{2})}}\end{array}$ =0 $\therefore\overline{{W}}_{E}=\overline{{W}}_{B}$
### output: 
.
To show that the time average of the electric field energy and the magnetic field energy in anLC oscillating circuit are equal, we start by recalling the expressions for the energy stored in each field.

The energy stored in the electric field \(E\) is given by:
$$ U_E = \frac{1}{2} C V^2 $$
where \(C\) is the capacitance and \(V\) is the voltage across the capacitor.

The energy stored in the magnetic field \(B\) is given by:
$$ U_B = \frac{1}{2} L I^2 $$
where \(L\) is the inductance and \(I\) is the current through the inductor.

In anLC oscillating circuit, the voltage \(V\) and the current \(I\) are related by the equation:
$$ V = -\omega L \frac{dI}{dt} $$
and
$$ I = C \frac{dV}{dt} $$

We can express the voltage \(V\) in terms of the current \(I\) using the first equation:
$$ V = -\omega L \frac{dI}{dt} $$

Substituting this into the expression for the electric field energy, we get:
$$ U_E = \frac{1}{2} C \left( -\omega L \frac{dI}{dt} \right)^2 = \frac{1}{2} C \omega^2 L^2 \left( \frac{dI}{dt} \right)^2 $$

Now, let's consider the magnetic field energy \(U_B\):
$$ U_B = \frac{1}{2} L I^2 $$

To find the time average of these energies, we note that in anLC oscillation, the total energy \(U\) is conserved and oscillates between the electric and magnetic forms. The time average of the total energy over one complete cycle is constant.

Let's denote the angular frequency of the oscillation by \(\omega\). The period \(T\) of the oscillation is:
$$ T = \frac{2\pi}{\omega} $$

The time average of the electric field energy \(\langle U_E \rangle\) is:
$$ \langle U_E \rangle = \frac{1}{T} \int_0^T U_E(t) \, dt = \frac{\omega}{2\pi} \int_0^{2\pi/\omega} \frac{1}{2} C \omega^2 L^2 \left( \frac{dI}{dt} \right)^2 \, dt $$

Similarly, the time average of the magnetic field energy \(\langle U_B \rangle\) is:
$$ \langle U_B \rangle = \frac{1}{T} \int_0^T U_B(t) \, dt = \frac{\omega}{2\pi} \int_0^{2\pi/\omega} \frac{1}{2} L I^2 \, dt $$

Using the relationship \(V = -\omega L \frac{dI}{dt}\), we can substitute \(\left( \frac{dI}{dt} \right)^2 = \frac{V^2}{\omega^2 L^2}\) into the integral for \(\langle U_E \rangle\):
$$ \langle U_E \rangle = \frac{\omega}{2\pi} \int_0^{2\pi/\omega} \frac{1}{2} C \omega^2 L^2 \cdot \frac{V^2}{\omega^2 L^2} \, dt = \frac{\omega}{2\pi} \int_0^{2\pi/\omega} \frac{1}{2} C V^2 \, dt $$

Since the average value of \(V^2\) over one complete cycle is a constant (which is the same as the average value of the square of any sinusoidal function with amplitude \(V_{\text{max}}\)), it simplifies to:
$$ \langle V^2 \rangle = \frac{1}{4} V_{\text{max}}^2 $$

However, the key point is that the integral of \(V^2\) over one complete cycle is proportional to \(V_{\text{max}}^3\) divided by \(\omega\), which cancels out when multiplied by \(\frac{\omega}{2\pi}\).

Thus, we have
***
### intput: 
1. 若把麦克斯韦方程组的所有矢量都分解为无旋的(纵场)和无散的(横场)两部分 写出 $\Vec{E}$ 和$\vec{B}$ 的这两部分在真空所满足的方程式并证明电场的无旋部分对应于库仑场
### standard: 
解在真空中的麦克斯韦方程组是  $$\nabla\times\vec{E}=-\frac{\partial\vec{B}}{\partial t},\enspace\nabla\times\vec{B}=\mu_{0}\vec{J}+\varepsilon_{0}\mu_{0}\,\frac{\partial\vec{E}}{\partial t}\,,$$  $$\boldsymbol{\nabla}\cdot\vec{E}=\rho\!\!\!\slash\!\!\!\slash_{\!\!\!\!\delta_{0}},\boldsymbol{\nabla}\cdot\vec{B}=0$$  如果把此方程组中所有的矢量都分解为无旋的纵场 用角标 $\mathrm{L}$ 表示无散的横场 用角标 $\mathrm{T}$ 表示  那么 $\vec{E}=\vec{E}_{L}+\vec{E}_{T}$ 且 $\nabla\times\vec{E}_{L}=0,\;\;\nabla\cdot\vec{E}_{T}=0;$ $\begin{array}{r}{\vec{J}=\vec{J}_{L}+\vec{J}_{T}\,,}\end{array}$ $\vec{B}=\vec{B}_{L}+\vec{B}_{T}$ 由于 $\nabla\times{\vec{B}}=0$ 即 $\Vec{B}$ 无源场 不存在纵场分量 亦是说  $\vec{B}_{L}$ ,则 $|\vec{B}=\vec{B}_{T}$  代入上面麦氏方程组  $$1\!>\!\nabla\!\times\!\vec{E}=-\frac{\partial\vec{B}}{\partial t}$$  $$\nabla\times(\vec{E}_{L}+\vec{E}_{T})=\nabla\times\vec{E}_{L}+\nabla\times\vec{E}_{T}=\nabla\times\vec{E}_{T}=-\frac{\partial\vec{B}_{T}}{\partial t}$$  $$2\mathcal{P}\boldsymbol{\cdot}\vec{E}=\rho\!\!\!\!\!\slash_{\mathcal{E}_{0}}:\qquad\qquad\qquad\boldsymbol{\nabla}\cdot(\vec{E}_{L}+\vec{E}_{T})=\boldsymbol{\nabla}\cdot\vec{E}_{L}+\boldsymbol{\nabla}\cdot\vec{E}_{T}=\boldsymbol{\nabla}\cdot\vec{E}_{L}=\rho\!\!\!\!\slash_{\mathcal{E}_{0}}$$  $$3\!>\!\nabla\!\times\!\vec{B}=\mu_{0}\vec{J}+\varepsilon_{0}\mu_{0}\frac{\partial\vec{E}}{\partial t}\colon\quad\nabla\!\times\!\vec{B}_{T}=\mu_{0}(\vec{J}_{L}+\vec{J}_{T})+\varepsilon_{0}\mu_{0}\frac{\partial}{\partial t}(\vec{E}_{L}+\vec{E}_{T})$$  $$=(\mu_{0}\vec{J}_{T}+\varepsilon_{0}\mu_{0}\frac{\partial\vec{E}_{T}}{\partial t})+(\mu_{0}\vec{J}_{L}+\varepsilon_{0}\mu_{0}\frac{\partial\vec{E}_{L}}{\partial t})$$  若两边同时取散度 $\nabla\cdot(\nabla\times\vec{B}_{T})=0$  $$\nabla\cdot(\mu_{0}\vec{J}_{T}+\varepsilon_{0}\mu_{0}\frac{\partial\vec{E}_{T}}{\partial t})=0$$  综上得麦氏方程的新表示方法  $$\nabla\times\vec{E}_{T}=-\frac{\partial\vec{B}_{T}}{\partial t}\,;\qquad\nabla\cdot\vec{E}_{L}=\rho\surd\varepsilon_{0}$$  $$\nabla\times\vec{B}_{T}=\mu_{0-}\vec{J}_{T}+\varepsilon_{0}\mu_{0}\frac{\partial\vec{E}_{T}}{\partial t}\,;\;\;\;\;\;\mu_{0}\vec{J}_{L}+\varepsilon_{0}\mu_{0}\frac{\partial\vec{E}_{L}}{\partial t}=0\,\ ;\ \;\;\;\vec{B}_{L}=0$$  证明电场的无旋部分对应库仑场  电场的无旋部分表达式为 $\nabla\cdot\vec{E}_{L}=\mathcal{f}_{\varepsilon_{0}}$  电荷在真空中产生的电势分布那么 $\vec{E}_{L}$ 即对应静止电荷产生的库仑场
### output: 
而磁场的无散部分对应于安培-法拉第场.
2. 在 presence of matter时， permittivity and permeability are given by \(\epsilon = \epsilon_0 \epsilon_r\) and \(\mu = \mu_0 \mu_r\). Show that the maxwell equations in matter can be written as:
   $$
   \nabla \times \vec{H} = \frac{\partial \vec{D}}{\partial t} + \vec{J}
   $$
   $$
   \nabla \cdot \vec{D} = \rho
   $$
   where \(\vec{H}\), \(\vec{D}\), and \(\rho\) are related to \(\vec{E}\), \(\vec{B}\), \(\epsilon_r\), and \(\mu_r\) as follows:
   $$
   \vec{D} = \epsilon_0 \epsilon_r \vec{E}, \quad \vec{H} = \frac{1}{\mu_0 \mu_r} \vec{B}.
   $$

To solve this problem, we need to decompose the electric field \(\vec{E}\) and the magnetic field \(\vec{B}\) into their transverse (divergence-free) andlongitudinal ( curl-free) components. Let's start with the first part.

### Part 1: Decomposition of \(\vec{E}\) and \(\vec{B}\)

We know from vector calculus that any vector field \(\vec{F}\) can be expressed as the sum of a divergence-free (transverse) component and a curl-free (longitudinal) component:
$$
\vec{F} = -\nabla \phi + \nabla \times \vec{A},
$$
where \(\phi\) is a scalar potential and \(\vec{A}\) is a vector potential.

For the electric field \(\vec{E}\):
$$
\vec{E} = -\nabla V + \nabla \times \vec{A}_E,
$$
where \(V\) is the scalar potential and \(\vec{A}_E\) is the vector potential for the electric field. The transverse component of \(\vec{E}\) is \(\nabla \times \vec{A}_E\) and the longitudinal component is \(-\nabla V\).

For the magnetic field \(\vec{B}\):
$$
\vec{B} = -\nabla A + \nabla \times \vec{A}_B,
$$
where \(A\) is the scalar potential and \(\vec{A}_B\) is the vector potential for the magnetic field. The transverse component of \(\vec{B}\) is \(\nabla \times \vec{A}_B\) and the longitudinal component is \(-\nabla A\).

Now, let's write down the Maxwells equations in terms of these components.

####Maxwell's Equations for the Transverse Components

The Faraday's law of induction states:
$$
\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}.
$$
Substituting the transverse and longitudinal components, we get:
$$
\nabla \times (-\nabla V + \nabla \times \vec{A}_E) = -\frac{\partial (-\nabla A + \nabla \times \vec{A}_B)}{\partial t}.
$$
Since \(\nabla \times \nabla V = 0\) and \(\nabla \times (\nabla \times \vec{A}_E) = \nabla (\nabla \cdot \vec{A}_E) - \nabla^2 \vec{A}_E\), and similarly for \(\vec{B}\), we have:
$$
-\nabla^2 \vec{A}_E = \frac{\partial}{\partial t} (\nabla A - \nabla \times \vec{
***
### intput: 
2.  证明在线性各向同性均匀非导电介质中 若 $\rho=0,\vec{J}=0$ ,则E 和B 可完全由矢势A 决定 若取 $\varphi=0$ ,这时A 满足哪两个方程
### standard: 
解在线性各向同性均匀非导电介质中如果令 $\vec{J}=0,\rho=0$ 麦氏方程表示为  $$\nabla\times\vec{E}=-\frac{\partial\vec{B}}{\partial t};\;\;\;\;\;\nabla\times\vec{H}=\frac{\partial\vec{D}}{\partial t}\,;\;\;\;\;\nabla\cdot\vec{D}=0\;;\;\;\;\;\nabla\cdot\vec{B}=0$$  $$\vec{D}=\varepsilon\vec{E}\ ,\ \ \vec{H}=\frac{\vec{B}}{\mu}$$  由 $\nabla\cdot{\vec{B}}=0$ 引入矢势 $\vec{A}$ 使 $\vec{B}=\nabla\times\vec{A}$  则 $\nabla\cdot{\vec{B}}=\nabla\cdot(\nabla\times{\vec{A}})=0$ 故 $\vec{B}$ 由矢势 $\vec{A}$ 完全决定  把 $\vec{B}=\nabla\times\vec{A}$ 代入 $\nabla\times\vec{E}=-\frac{\partial\vec{B}}{\partial t}$ ; 有  $$\nabla\times({\vec{E}}+{\frac{\partial{\vec{A}}}{\partial t}})=0\,\,\,\,\Leftrightarrow{\vec{E}}+{\frac{\partial{\vec{A}}}{\partial t}}=-\nabla\varphi$$  $\nabla\times(\vec{E}+\frac{\partial\vec{A}}{\partial t})=\nabla\times(-\nabla\varphi)=0$  则 $\vec{E}=-\partial\varphi-\frac{\partial\vec{A}}{\partial t}$ 故 $\Vec{E}$ 有标势 $\vec{A}$ 完全决定  如果取 $\varphi=0$ ，有： $\vec{B}=\nabla\times\vec{A}$ 代入方程 $\nabla\times{\vec{H}}={\frac{\partial{\vec{D}}}{\partial t}}$  $$\vec{E}=-\frac{\partial\vec{A}}{\partial t}$$  $$\nabla\cdot{\vec{D}}=0$$  有 $1\!>\!\nabla\!\times\!\vec{H}=\!\frac{\partial\vec{D}}{\partial t}\!:\:\:\:\:\:\:\:\nabla\!\times\!\vec{B}=\varepsilon\mu\frac{\partial\vec{E}}{\partial t}$ $\begin{array}{r l}&{\implies\nabla\times(\nabla\times\vec{A})=-\varepsilon\mu\frac{\partial}{\partial t}(\frac{\partial\vec{A}}{\partial t})}\\ &{\implies\nabla\times(\nabla\times\vec{A})+\varepsilon\mu\frac{\partial^{2}\vec{A}}{\partial t^{2}}=0}\\ &{\implies\nabla\times(\nabla\times\vec{A})+\varepsilon\mu\frac{\partial^{2}\vec{A}}{\partial t^{2}}=0}\\ &{\implies\nabla\cdot\vec{D}=0:\quad\frac{\partial}{\partial t}(\nabla\cdot\vec{A})=0}\end{array}$  由于取 $\varphi=0$ 库仑规范 $\nabla\cdot{\vec{A}}=0$ 与洛伦兹规范 $\nabla\cdot{\vec{A}}+{\frac{1}{c^{2}}}{\frac{\partial\varphi}{\partial t}}=0$ 相同∴由 $1{>}2{>}$ 得 $\vec{A}$ 满足的方程有  $$\nabla\cdot{\vec{A}}=0$$  $$\nabla^{2}\vec{A}-\varepsilon\!\mu\frac{\partial^{2}\vec{A}}{\partial t}\!=\!0$$
### output: 
? 解: 首先考虑Maxwell方程在自由空间中的形式:
$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}
$$
$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$
$$
\nabla \cdot \mathbf{B} = 0
$$
$$
\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}
$$

给定条件是 \(\rho = 0\) 和 \(\vec{J} = 0\)。因此，Maxwell方程简化为:
$$
\nabla \cdot \mathbf{E} = 0
$$
$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$
$$
\nabla \cdot \mathbf{B} = 0
$$
$$
\nabla \times \mathbf{H} = \frac{\partial \mathbf{D}}{\partial t}
$$

我们知道场量 \(\mathbf{E}\) 和 \(\mathbf{B}\) 可以用 scalar potential \(\varphi\) 和 vector potential \(\mathbf{A}\) 表示:
$$
\mathbf{E} = -\nabla \varphi - \frac{\partial \mathbf{A}}{\partial t}
$$
$$
\mathbf{B} = \nabla \times \mathbf{A}
$$

由于 \(\varphi = 0\)，所以:
$$
\mathbf{E} = -\frac{\partial \mathbf{A}}{\partial t}
$$

将 \(\mathbf{E} = -\frac{\partial \mathbf{A}}{\partial t}\) 代入 div Eq (\(\nabla \cdot \mathbf{E} = 0\)) 中:
$$
\nabla \cdot \left( -\frac{\partial \mathbf{A}}{\partial t} \right) = 0
$$
这表明:
$$
-\frac{\partial}{\partial t} (\nabla \cdot \mathbf{A}) = 0
$$
因此:
$$
\nabla \cdot \mathbf{A} = \text{常数}
$$

由于我们选择 \(\varphi = 0\)，可以假设该常数为零（因为标量 potential 在边界 conditions 的选择上具有任意性），即:
$$
\nabla \cdot \mathbf{A} = 0
$$

现在，将 \(\mathbf{E} = -\frac{\partial \mathbf{A}}{\partial t}\) 和 \(\mathbf{B} = \nabla \times \mathbf{A}\) 代入 Maxwell方程中：
1. \(\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}\):
$$
\nabla \times \left( -\frac{\partial \mathbf{A}}{\partial t} \right) = -\frac{\partial}{\partial t} (\nabla \times \mathbf{A})
$$
即:
$$
-\frac{\partial \mathbf{B}}{\partial t} = -\frac{\partial \mathbf{B}}{\partial t}
$$
此式恒成立。

2. \(\nabla \times \mathbf{H} = \frac{\partial \mathbf{D}}{\partial t}\):
使用本安度方程 \(\mathbf{H} = \mathbf{B}\)，得:
$$
\nabla \times \mathbf{B} = \frac{\partial \mathbf{D}}{\partial t}
$$
而 \(\mathbf{B} = \nabla \times \mathbf{A}\)， thus:
$$
\nabla \
***
### intput: 
3.  证明沿 ${\mathbf Z}$ 轴方向传播的平面电磁波可用矢势 $\bar{A}(\omega\tau)$ 表示其中 $\tau=t-{\zeta\!\!\!\!{\big/}}_{c}$ A 垂直于z轴方向
### standard: 
证 对于沿 ${\mathbf Z}$ 轴传播的任意一平面电磁波 $\bar{E},\bar{B}$ 可写作  $$\begin{array}{r}{\Vec{E}=E_{0}\Vec{e}_{x}e^{i(k z-\omega t)}}\\ {\Vec{B}=B_{0}\Vec{e}_{y}e^{i(k z-\omega t)}}\end{array}$$  满足 1 $\bar{E},\bar{B}$ 均垂直于传播方向 $\vec{e}_{z}$  2 $\bar{E},\bar{B}$ 相互垂直 $\vec{E}\!\times\!\vec{B}$ 沿 $\vec{k}$ 方向  3 $\bar{E},\bar{B}$ 同相振幅比为 $\upsilon$ 真空中为c  故不妨取 ${\vec{A}}=A_{0}{\vec{e}}_{x}e^{-i\omega(t-{\frac{z}{c}})}=A_{0}{\vec{e}}_{x}e^{i(k z-\omega t)},\qquad k={\frac{\omega}{c}}$  $$\therefore\vec{B}=\nabla\times\vec{A}=\frac{\partial A_{x}}{\partial z}\vec{e}_{y}=i k A_{0}\vec{e}_{y}e^{i(k z-\omega t)}$$  $$\vec{E}=-\frac{\partial A}{\partial t}=i\omega A_{0}\vec{e}_{x}e^{i(k z-\omega t)}$$  可见如果令 $k A_{0}=B_{0},\omega A_{0}=E_{0}$ 表达式 1 2 可表示的波正是符合条件的平面波所以命题得证
### output: 
).

To show that a plane electromagnetic wave traveling along the \(\mathbf{Z}\)-axis can be represented by the vector potential \(\bar{A}(\omega\tau)\) where \(\tau = t - \frac{z}{c}\) and \(\bar{E}\) is perpendicular to the \(z\)-axis direction), we need to follow these steps:

1. **Understand the form of the plane wave**: A plane wave traveling in the \(+z\) direction can be written as:
   $$
   \bar{E}(t, z) = \bar{E}_0 e^{i(kz - \omega t)}
   $$
   where \(\bar{E}_0\) is the amplitude vector, \(\omega\) is the angular frequency, and \(k\) is the wavenumber.

2. **(maxwell's equations for the wave**: For a plane wave in free space (with no sources), Maxwell's equations simplify to:
   $$
   \nabla \times \bar{E} = -\frac{\partial \bar{B}}{\partial t}
   $$
   $$
   \nabla \times \bar{B} = \mu_0 \epsilon_0 \frac{\partial \bar{E}}{\partial t}
   $$

3. **Assume a vector potential form**: Assume the vector potential \(\bar{A}\) has only a \(x\)-component or \(y\)-component since it is perpendicular to the \(z\)-axis. Let:
   $$
   \bar{A}(t, z) = \hat{u} A(z, t)
   $$
   where \(\hat{u}\) is either \(\hat{x}\) or \(\hat{y}\).

4. **Relate the electric field to the vector potential**: The electric field \(\bar{E}\) is given by:
   $$
   \bar{E} = -\nabla \phi - \frac{\partial \bar{A}}{\partial t}
   $$
   Since there is no scalar potential \(\phi\) for a transverse wave, we have:
   $$
   \bar{E} = -\frac{\partial \bar{A}}{\partial t}
   $$
   Substituting \(\bar{A} = \hat{u} A(z, t)\), we get:
   $$
   \bar{E} = -\frac{\partial (\hat{u} A(z, t))}{\partial t} = -\hat{u} \frac{\partial A(z, t)}{\partial t}
   $$

5. **Determine the form of \(A(z, t)\)**: For the plane wave \(\bar{E} = \bar{E}_0 e^{i(kz - \omega t)}\), we need:
   $$
   -\hat{u} \frac{\partial A(z, t)}{\partial t} = \bar{E}_0 e^{i(kz - \omega t)}
   $$
   This implies:
   $$
   \frac{\partial A(z, t)}{\partial t} = -\bar{E}_0 e^{i(kz - \omega t)}
   $$

6. **Solve for \(A(z, t)\)**: Integrate with respect to time:
   $$
   A(z, t) = i \frac{\bar{E}_0}{\omega} e^{i(kz - \omega t)} + f(z)
   $$
   where \(f(z)\) is an arbitrary function of \(z\). Since we are considering a plane wave traveling in the \(+z\) direction without any initial conditions other than being perpendicular to the \(z\)-axis, we can set \(f(z) = 0\):
   $$
   A(z, t) = i \frac{\bar{E}_0}{\omega} e^{i(kz - \omega t)}
   $$

7. **Express in terms of \(\tau\)**: Recall that \(\tau = t - \frac{z}{c}\). Therefore:
   $$
   kz - \omega
***
### intput: 
4.  设真空中矢势 $\vec{A}(\vec{x},t)$ 可用复数傅立叶展开为 $\vec{A}(\vec{x},t)=\sum_{k}$$a_{k}(t)e^{i\vec{k}\cdot\vec{x}}+a_{k}^{*}(t)e^{-i\vec{k}\cdot\vec{x}}$$$ ,其中$\vec{a}_{k}^{\,*}$ 是 $\Vec{a}_{k}$ 的复共轭  1  证明 $\Vec{a}_{k}$ 满足谐振子方程 $\frac{d^{2}\vec{a}_{k}(t)}{{d t}^{2}}\!+k^{2}c^{2}\vec{a}_{k}(t)=0$   2  当选取规范 $\nabla\cdot{\vec{A}}=0,\varphi=0$ 时证明 $\vec{k}\cdot\vec{a}_{k}=0$ 0  3  把 $\Vec{E}$ 和 $\vec{B}$ 用 $\Vec{a}_{k}$ 和 $\vec{a}_{k}^{\,*}$ 表示出来
### standard: 
解 1 证明 $\mathrel{\because}\vec{A}(\vec{x},t)=\sum_{k}$$\vec{a}_{k}(t)e^{i\vec{k}\cdot\vec{x}}+\vec{a}_{k}^{\,*}(t)e^{-i\vec{k}\cdot\vec{x}}$$$ ∴根据傅立叶级数得正交性 必有$\vec{a}_{k}\left(t\right)=\int\vec{A}(\vec{x},t)e^{i\vec{k}\cdot\vec{x}}d\vec{x}$ $\therefore\frac{d^{2}a_{k}(t)}{d t^{2}}\!=\!\int\!\frac{\hat{\sigma}^{2}\vec{A}(\vec{x},t)}{{\partial t^{2}}}e^{i\vec{k}\cdot\vec{x}}d\vec{x}$ 1而洛仑兹变换时 矢势A满足方程∇2A− $\nabla^{2}\vec{A}-\frac{1}{c^{2}}\frac{\partial^{2}\vec{A}}{\partial t^{2}}=-\mu_{0}\vec{J}$  在真空中 ${\vec{J}}=0$ ，故， $\nabla^{2}\vec{A}=\frac{1}{c^{2}}\frac{\partial^{2}\vec{A}}{\partial t^{2}}$ 1 式化为 $\frac{d^{\,2}\vec{a}_{k}(t)}{d t^{2}}\!=\!\int e^{i\vec{k}\cdot\vec{x}}(c^{2}\nabla^{2}\vec{A})d\vec{x}$   而 $k^{2}c^{2}\vec{a}_{\scriptscriptstyle k}(t)=\int k^{2}c^{2}\vec{A}(\vec{x},t)e^{i\vec{k}\cdot\vec{x}}d\vec{x}$   于是 $\frac{d^{2}\vec{a}_{k}(t)}{{d t}^{2}}+k^{2}c^{2}\vec{a}_{k}(t)=\int$$c^{2}\nabla^{2}\vec{A}(\vec{x},t)+k^{2}c^{2}\vec{A}(\vec{x},t)$$e^{i\vec{k}\cdot\vec{x}}d\vec{x}$   $\mathrel{\because}\vec{A}(\vec{x},t)=\sum_{k}$$\vec{a}_{k}(t)e^{i\vec{k}\cdot\vec{x}}+\vec{a}_{k}^{\,*}(t)e^{-i\vec{k}\cdot\vec{x}}$$$  $\therefore\nabla^{2}\vec{A}(\vec{x},t)=-k^{2}\vec{A}(\vec{x},t)$ 2 式右边的积分式中 被积函数为0 积分为0$\frac{d^{2}\vec{a}_{k}(t)}{{d t}^{2}}\!+k^{2}c^{2}\vec{a}_{k}(t)=0$ 亦即 $\Vec{a}_{k}$ 满足谐振子方程  2 选取规范 $\nabla\cdot{\vec{A}}=0,\varphi=0$ 于是有  $$\begin{array}{c}{{\nabla\cdot\vec{A}=\nabla\cdot\displaystyle\sum_{k}$$\vec{a}_{k}\,(t)e^{i\vec{k}\cdot\vec{x}}+\vec{a}_{k}\,(t)e^{-i\vec{k}\cdot\vec{x}}$$=\displaystyle\sum_{k}$$\vec{a}_{k}\,(t)\nabla\cdot e^{i\vec{k}\cdot\vec{x}}+\vec{a}_{k}^{\,*}\,(t)\nabla\cdot e^{-i\vec{k}\cdot\vec{x}}$$}}\\ {{=\displaystyle\sum_{k}$$\vec{k}\cdot\vec{a}_{k}\,(t)\cdot i e^{i\vec{k}\cdot\vec{x}}-\vec{k}\cdot\vec{a}_{k}^{\,*}\,(t)\cdot i e^{-i\vec{k}\cdot\vec{x}}$$=0}}\end{array}$$  3 已知 $\vec{A}(\vec{x},t)=\sum_{k}$$\vec{a}_{k}(t)e^{i\vec{k}\cdot\vec{x}}+\vec{a}_{k}^{\,*}(t)e^{-i\vec{k}\cdot\vec{x}}$$$  $\therefore\vec{B}=\nabla\times\vec{A}=\sum_{k}$$i\vec{k}\vec{a}_{k}(t)e^{i\vec{k}\cdot\vec{x}}-i k\vec{a}_{k}^{\,*}(t)e^{-i\vec{k}\cdot\vec{x}}$$$ $\vec{E}=-\nabla\varphi-\frac{\partial\vec{A}}{\partial t}=-\sum_{k}$$\frac{d\vec{a}_{k}(t)}{d t}e^{i\vec{k}\cdot\vec{x}}+\frac{d\vec{a}_{k}^{\,*}(t)}{d t}e^{-i\vec{k}\cdot\vec{x}}$$$ 取规范 $\nabla\cdot{\vec{A}}=0,\varphi=0;$ )
### output: 


答案:

1. **证明 \(\vec{a}_{k}\) 满足谐振子方程**

   首先，我们从Maxwell equations开始。在真空中，Maxwell equations 为：
   $$
   \nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}
   $$
   $$
   \nabla \times \vec{B} = \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t}
   $$

   我们使用_divergence theorem_将Maxwell equations投影到体积 \(V\) 上：
   $$
   \int_V (\nabla \times \vec{E}) \cdot d\vec{S} = -\int_V \frac{\partial \vec{B}}{\partial t} \cdot d\vec{S}
   $$
   $$
   \int_V (\nabla \times \vec{B}) \cdot d\vec{S} = \int_V \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t} \cdot d\vec{S}
   $$

   利用散度定理：
   $$
   \int_V \nabla \cdot (\nabla \times \vec{E}) \, dV = -\int_V \frac{\partial}{\partial t} (\nabla \cdot \vec{B}) \, dV
   $$
   $$
   \int_V \nabla \cdot (\nabla \times \vec{B}) \, dV = \int_V \mu_0 \epsilon_0 \frac{\partial}{\partial t} (\nabla \cdot \vec{E}) \, dV
   $$

   根据 div-curl identity:
   $$
   \nabla \cdot (\nabla \times \vec{E}) = 0
   $$
   $$
   \nabla \cdot (\nabla \times \vec{B}) = 0
   $$

   因此， Maxwells equations 在 volume \(V\) 上简化为：
   $$
   \nabla \cdot \vec{B} = 0
   $$
   $$
   \nabla \cdot \vec{E} = \rho / \epsilon_0
   $$
   这里假设 \(\rho = 0\)（自由空间）。

   将 vector potential \(\vec{A}\) 代入Maxwell equations：
   $$
   \vec{B} = \nabla \times \vec{A}
   $$
   $$
   \vec{E} = -\nabla \phi - \frac{\partial \vec{A}}{\partial t}
   $$

   使用给定的 Fourier expansion for \(\vec{A}\):
   $$
   \vec{A}(\vec{x},t) = \sum_k $$a_k(t) e^{i \vec{k} \cdot \vec{x}} + a_k^*(t) e^{-i \vec{k} \cdot \vec{x}}$$

***
### intput: 
5.  设 $\vec{A}$ 和 $\varphi$ 是满足洛伦兹规范的矢势和标势  1  引入一矢量函数Zv( xv,t) 赫兹矢量 若令ϕ=∇⋅Zv 证明Av=c12∂∂Zt  2  若令ρ=−∇⋅Pv证明Zv满足方程∇2Zv−12∂2Z $\nabla^{2}\vec{Z}-\frac{1}{c^{2}}\frac{{\partial}^{2}\vec{Z}}{{\partial t}^{2}}=-c^{2}\mu_{\scriptscriptstyle0}\vec{P}$ 写出在真空中的推迟解  3  证明Ev和Bv可通过Zv用下列公式表出 Ev=∇×(∇×Zv)−c2µ0Pv,Bv=12∂∂∇×Zv
### standard: 
解 1 证明 $\vec{A}$ 与 $\varphi$ 满足洛仑兹规范 故有 $\nabla\cdot{\vec{A}}+{\frac{1}{c^{2}}}{\frac{\partial\varphi}{\partial t}}=0$  $$\nabla\cdot\vec{A}+\frac{1}{c^{2}}\cdot\frac{\partial}{\partial t}(-\nabla\cdot\vec{Z})=0\;,\;\;\mathbb{H}\mathbb{I}\;\nabla\cdot\vec{A}=\nabla\cdot(\frac{1}{c^{2}}\frac{\partial\vec{Z}}{\partial t})$$  $$\therefore{\vec{A}}={\frac{1}{c^{2}}}{\frac{\partial{\vec{Z}}}{\partial t}}$$  $\varphi$ $\nabla^{2}\varphi-{\frac{1}{c^{2}}}{\frac{{\partial}^{2}\varphi}{{\partial t}^{2}}}=-{\frac{\rho}{\varepsilon_{\mathrm{0}}}}$  $$\frac{\partial^{2}\varphi}{{\partial t}^{2}}=\frac{\partial^{2}}{{\partial t}^{2}}(-\nabla\cdot\vec{Z})=-\nabla\cdot(\frac{\partial^{2}\vec{Z}}{\partial t^{2}})$$  代入原方程  $$-$$\nabla\cdot(\nabla^{2}\vec{Z})-\frac{1}{c^{2}}\nabla\cdot(\frac{{\partial}^{2}\vec{Z}}{{\partial t}^{2}})$$=-\frac{\rho}{{\varepsilon}_{0}}$$  令 $\rho=-\nabla\cdot{\vec{P}}$ 则上式化为  $$\nabla\cdot(\nabla^{2}\vec{Z})-\frac{1}{c^{2}}\nabla\cdot(\frac{\partial^{2}\vec{Z}}{\partial t^{2}})=-\frac{1}{\mathcal{E}_{0}}\nabla\cdot\vec{P}$$  $$\nabla^{2}\vec{Z}-\frac{1}{c^{2}}\frac{\partial^{2}\vec{Z}}{\partial t^{2}}=-c^{2}\mu_{\scriptscriptstyle0}\vec{P}$$  由于矢势A ∇2A− $\nabla^{2}\vec{A}-\frac{1}{c^{2}}\frac{\partial^{2}\vec{A}}{\partial t^{2}}=-\mu_{\scriptscriptstyle0}\vec{J}$ 2=−µ0J在真空中的推迟势为  $$\vec{A}(\vec{x},t)=\frac{\mu_{0}}{4\pi}\!\int\!\frac{\vec{J}(\vec{x}^{\prime},t-\frac{r}{c})}{r}d V^{\prime}$$  故 可类比得出 方程 2 在真空中的推迟势解为  $$\vec{Z}(\vec{x},t)=\frac{c^{2}\mu_{0}}{4\pi}\!\int\!\frac{\vec{P}(\vec{x}^{\prime},t-\frac{r}{c})}{r}d V^{\prime}$$  3 $\because{\vec{E}}=-\nabla\varphi-{\frac{\partial{\vec{A}}}{\partial t}}$ 代入 $\varphi=-\nabla\cdot{\vec{Z}},{\vec{A}}={\frac{1}{c^{2}}}{\frac{\partial{\vec{Z}}}{\partial t}}$ 有  $${\vec{E}}=\nabla(\nabla\cdot{\vec{Z}})-{\frac{1}{c^{2}}}{\frac{\partial^{2}{\vec{Z}}}{\partial t^{2}}}=\nabla\times(\nabla\times{\vec{Z}})+\nabla^{2}Z-{\frac{1}{c^{2}}}{\frac{\partial^{2}{\vec{Z}}}{\partial t^{2}}}=\nabla\times(\nabla\times{\vec{Z}})-c^{2}\mu_{0}{\vec{P}}$$  同理 ${\vec{B}}=\nabla\times{\vec{A}}={\frac{1}{{c}^{2}}}{\frac{\partial}{\partial t}}\nabla\times{\vec{Z}}$  $$\therefore\vec{E}=\nabla\times(\nabla\times\vec{Z})-c^{2}\mu_{0}\vec{P}$$  $${\vec{B}}={\frac{1}{c^{2}}}{\frac{\partial}{\partial t}}\nabla\times{\vec{\mathbf{Z}}}$$
### output: 
$
To solve the given problem, we will proceed step by step as follows:

### Step 1: Prove \(\vec{A} = \nabla \times \vec{\nabla} \cdot \vec{Z}\)

Given:
- \(\vec{A}\) and \(\varphi\) satisfy the Lorentz gauge.
- \(\varphi = \nabla \cdot \vec{Z}\).

We start with the vector identity for the curl of a gradient:
$$
\nabla \times (\nabla \cdot \vec{Z}) = \nabla (\nabla \cdot \vec{Z}) - \nabla^2 \vec{Z}
$$

Since \(\varphi = \nabla \cdot \vec{Z}\), substituting this into the equation gives:
$$
\nabla \times \varphi = \nabla (\nabla \cdot \vec{Z}) - \nabla^2 \vec{Z}
$$
However, since \(\varphi = \nabla \cdot \vec{Z}\), we have:
$$
\nabla \times \varphi = \nabla \times (\nabla \cdot \vec{Z})
$$
This implies that:
$$
-\nabla^2 \vec{Z} = \nabla \times (\nabla \cdot \vec{Z}) - \nabla \times \varphi
$$
From the Lorentz gauge condition, we know \(\nabla \cdot \vec{E} + \frac{1}{c^2} \frac{\partial \varphi}{\partial t} = 0\). Since \(\vec{E} = -\nabla \varphi\), we have:
$$
-\nabla^2 \varphi - \frac{1}{c^2} \frac{\partial \varphi}{\partial t} = 0 \implies \nabla^2 \varphi = -\frac{1}{c^4} \frac{\partial^2 \varphi}{\partial t^2}
$$

Using this in our earlier equation:
$$
-\nabla^2 \vec{A} = -c^2 \nabla \times (-\nabla \varphi)
$$
Thus,
$$
\vec{A} = c^2 \nabla \times \nabla \varphi = \nabla \times (c^2 \nabla \varphi) = \nabla \times \left(-\frac{1}{c^2} \nabla \times Z\right)
$$

Therefore, we have shown that:
$$
\boxed{\vec{A} = \nabla \times \vec{\nabla} \cdot \vec{Z}}
$$

### Step 2: Show \(\vec{Z}\) satisfies \(\nabla^2 \vec{Z} - \frac{1}{c^2} \frac{\partial^2 \vec{Z}}{\partial t^2} = -c^2 \mu_0 \vec{P}\) and write the vacuum solution

Given:
$$
\rho = -\nabla \cdot \vec{P}
$$

The continuity equation is:
$$
\frac{\partial \rho}{\partial t} + \nabla \cdot \vec{J} = 0
***
### intput: 
6.  两个质量 电荷都相同的粒子相向而行发生碰撞 证明电偶极辐射和磁偶极辐射都不会发生
### standard: 
证明电偶极矩与磁偶极矩产生的辐射场分别是  $1\mathrm{>}$ 由电偶极矩产生的辐射场  $\begin{array}{l}{{\displaystyle{\vec{E}=\frac{e^{i k R}}{4\pi\varepsilon_{0}c^{2}R}(\ddot{\vec{p}}\times\vec{n})\times\vec{n}}}}\\ {{\displaystyle{\vec{B}=\frac{\mu_{0}e^{i k R}}{4\pi R}i k\vec{n}\times\ddot{\vec{p}}}}}\end{array}$ 由磁偶极矩 产生的辐射场 $\begin{array}{l}{{\displaystyle{\vec{E}=-\frac{\mu_{0}e^{i k R}}{4\pi c R}(\ddot{\vec{m}}\times\vec{n})}}}\\ {{\displaystyle{\vec{B}=\frac{\mu_{0}e^{i k R}}{4\pi c^{2}R}(\ddot{\vec{m}}\times\vec{n})\times\vec{n}}}}\end{array}$  $2>$  现有两个质量电荷都相同的粒子相向而行 发生磁撞 在此过程中 取两个电荷的连线为 $\mathbf{X}$ 轴 于是 此系统的电偶极矩是  $$\vec{p}=q\vec{x}_{1}+q\vec{x}_{2}=q(\vec{x}_{1}+\vec{x}_{2})$$  由此可发现 $\ddot{\vec{p}}=\frac{d^{2}}{{d t}^{2}}$$q(\vec{x}_{1}+\vec{x}_{2})$$=q(\ddot{\vec{x}}_{1}+\ddot{\vec{x}}_{2})$  由于两个粒子质量相同 电量也相同 故当其运动时 $\ddot{\vec{x}}_{1}=-\ddot{\vec{x}}_{2}$ 牛顿第二定律  # 即 $\ddot{\vec{p}}=0$  于是 系统的电偶极矩辐射场为 0  又由于 此系统的磁偶极矩 $\bar{m}=0$ 于是 系统的磁偶极矩辐射场为 0  综上 两个质量 电荷都相同的粒子同向而行发生磁撞 不会发生电偶极辐射和磁偶极辐射
### output: 
.
为了证明两个质量电荷都相同的粒子相向而行时不会发生电偶极辐射和磁偶极辐射，我们需要分析涉及的场和满足的方程。让我们一步步来。

### 第一步：理解电偶极 和磁偶极 辐射条件
电偶极 辐射发生在 dipole moment time rate of change (P) is non-zero. Mathematically, this is expressed as:
$$
\frac{d\mathbf{p}}{dt} \neq 0
$$
where \(\mathbf{p}\) is the electric dipole moment.

磁偶极 辐射 occurs when the time rate of change of the magnetic dipole moment (M) is non-zero. Mathematically, this is expressed as:
$$
\frac{d\mathbf{m}}{dt} \neq 0
$$

### 第二步：确定带正电和负电粒子的 dipole moments
考虑两个 identical particles with charges \(q\) and \(-q\) moving towards each other with equal speeds \(v\). Let's place one particle at the origin \(\mathbf{r}_1 = 0\) and the other at \(\mathbf{r}_2 = d(t)\), where \(d(t)\) is the distance between them as a function of time.

The electric dipole moment \(\mathbf{p}(t)\) of the system is given by:
$$
\mathbf{p}(t) = q\mathbf{r}_1 + (-q)\mathbf{r}_2 = -q\mathbf{d}(t)
$$

Since \(d(t)\) is simply the distance between the two charges, it is a scalar function of time. Therefore, the dipole moment \(\mathbf{p}(t)\) is proportional to the vector \(\mathbf{d}(t)\).

### Step 3: Calculate the time derivative of the dipole moment
To determine if there is electric dipole radiation, we need to find the time derivative of \(\mathbf{p}(t)\):
$$
\frac{d\mathbf{p}}{dt} = \frac{d}{dt}(-q\mathbf{d}(t)) = -q\frac{d\mathbf{d}}{dt}
$$

For two charged particles moving directly towards each other with equal speeds, the distance \(d(t)\) changes linearly with time:
$$
d(t) = d_0 - vt
$$
where \(d_0\) is the initial distance between the charges.

Taking the time derivative of \(d(t)\):
$$
\frac{d\mathbf{d}}{dt} = -v\hat{\mathbf{d}}
$$

Thus,
$$
\frac{d\mathbf{p}}{dt} = -q(-v\hat{\mathbf{d}}) = qv\hat{\mathbf{d}}
$$

However, since \(\mathbf{d}(t)\) is along the line connecting the two charges, \(\hat{\mathbf{d}}\) is always parallel to the direction of motion, which means \(\frac{d\mathbf{p}}{dt}\) is zero because it does not change in magnitude or direction over time. Therefore,
$$
\frac{d\mathbf{p}}{dt} = 0
$$

This shows that there is no electric dipoleradiation.

### Step 4: Determine the magnetic dipole moment
Next, consider the magnetic dipole moment \(\mathbf{m}(t)\). For two point charges moving with equal speeds but in opposite directions, they form an oscillating dipole system. The current density \(\mathbf{j}\) due to each charge can be approximated using the equation for the current density of a point charge:
$$
\mathbf{j}(\mathbf{r}, t) = q \mathbf{v} \delta(\mathbf{r} - \mathbf{r}_i(t))
$$

The total current density \(\mathbf{j}_{\text{total}}\) is:
$$
\mathbf{j}_{\text{total}} = \mathbf{j}_1 + \mathbf{j}_2 = q \mathbf{v} \delta(\mathbf{r}) - q \mathbf
***
### intput: 
7.  设有一个球对称的电荷分布 以频率 $\omega$ 沿径向做简谐振动 求辐射场 并对结果给以物理解释
### standard: 
解  设球面上均匀分布了总电量为Q 的电荷此假设满足题目中的球对称分布于是球面电荷密度与球面半径的关系是  $$\sigma=\frac{Q}{4\pi R^{2}}$$  取如图相对的两块小面元 $d S_{1},d S_{2}$ 由于两块小面元对应相同的立体角 故有相同的面积  $$d S_{1}=d S_{2}\,,$$  $$\Delta\mathcal{Q}_{1}=\sigma d S_{1}=\frac{Q}{4\pi R^{2}}d S_{1}=\frac{Q}{4\pi R^{2}}d S_{2}=\sigma d S_{2}=\Delta\mathcal{Q}_{2}$$  考虑到两电荷元 $\Delta Q_{1},\Delta Q_{2}$ 由于是球对称又以相同的频率 $\omega$ 作沿径向的简谐振动$\therefore\quad\vec{p}=\Delta\mathcal{Q}_{1}\cdot R\cdot\vec{e}_{r}+\Delta\mathcal{Q}_{1}\cdot R\cdot(-\vec{e}_{r})=0$ ${\vec{m}}=I\cdot\Delta{\vec{S}}=0$  故此两电荷元的振动不能产生辐射场  根据场的叠加原理 整个球对称分布的电荷体系沿径向的简谐振荡是不能产生辐射场的振动 辐射场为 0
### output: 
.
$$

To solve the problem of finding the radiative field of a spherically symmetric charge distribution that undergoes simple harmonic oscillation at frequency \(\omega\), we can follow these steps:

1. **Determine the Time- dependent Charge Distribution:**
   Let the initial charge density be \(\rho(r)\). Since the charge distribution is spherically symmetric and undergoes simple harmonic oscillation with frequency \(\omega\), the time-dependent charge density can be written as:
   $$
   \rho(r, t) = \rho_0(r) \cos(\omega t)
   $$
   where \(\rho_0(r)\) is the initial charge density.

2. **Calculate the Current Density:**
   The current density \(\mathbf{J}(\mathbf{r}, t)\) is given by the continuity equation:
   $$
   \mathbf{J}(\mathbf{r}, t) = \frac{\partial \rho(r, t)}{\partial t}
   $$
   Substituting \(\rho(r, t)\):
   $$
   \mathbf{J}(\mathbf{r}, t) = -\rho_0(r) \omega \sin(\omega t) \hat{r}
   $$
   Here, \(\hat{r}\) is the unit vector in the radial direction.

3. **Use the衔接方程 for the radiative field:**
   The radiative field \(\mathbf{E}_{\text{rad}}\) can be found using the integral form of the far field expression from Max well's equations. For a spherical charge distribution, the radiative electric field at a distance \(R\) from the origin is given by:
   $$
   \mathbf{E}_{\text{rad}}(\mathbf{R}, t) = \frac{3 \mu_0}{4\pi R^3} (\mathbf{P}(t) \times \mathbf{R}) \cdot \nabla \left( \frac{1}{R} \right)
   $$
   However, this approach is complex. Instead, we use the multipole expansion of the scalar potential \(\phi\) and vector potential \(\mathbf{A}\).

4. **Multipole Expansion:**
   Since the charge distribution is spherically symmetric, only the monopole term in the multipole expansion will contribute to the radiative field. The monopole moment \(Q(t)\) is given by:
   $$
   Q(t) = \int \rho(\mathbf{r}, t) d^3 r
   $$
   Substituting \(\rho(r, t)\):
   $$
   Q(t) = \int \rho_0(r) \cos(\omega t) d^3 r
   $$
   Assuming the total initial charge \(Q_0\) is constant (i.e., \(\int \rho_0(r) d^3 r = Q_0\)):
   $$
   Q(t) = Q_0 \cos(\omega t)
   $$

5. **Scalar and Vector Potentials:**
   The scalar potential \(\phi\) and vector potential \(\mathbf{A}\) for a multipole expansion are:
   $$
   \phi(\mathbf{r}, t) = \frac{Q(t)}{4\pi \epsilon_0 r}
   $$
   $$
   \mathbf{A}(\mathbf{r}, t) = \frac{1}{4\pi c \epsilon_0} \nabla \int \frac{Q(t') \dot{\rho}(\mathbf{r'}, t')}{|\mathbf{r} - \mathbf{r'}|} d^3 r'
   $$
   For a monopole, the vector potential simplifies to zero because there are no higher multipoles.

6. ** radiative Power:**
   The radiative power \(P_{\text{rad}}\) is given by:
   $$
   P_{\text{rad}} = \frac{e^2}{6\pi m c^3} \left| \ddot{p} \right|^2
   $$
   where \(m\) is the mass of the charged particle and \(\mathbf{p}\)
***
### intput: 
8.  一飞轮半径为R 并有电荷均匀分布在其边缘上 总电量为Q 设此飞轮以恒定角速度$\omega$ 旋转 求辐射场
### standard: 
设飞轮边缘的厚度为d,于是 边缘上的电荷面密度 $\sigma=\frac{Q}{2\pi R d}$ 体系的电偶极矩为 $\vec{p}=\oint\!\frac{Q}{2\pi R d}\!\cdot\!d\cdot d l\cdot\vec{x}=\frac{Q}{2\pi R}\!\oint\!\vec{x}\cdot d l$ $=\frac{Q}{2\pi}$$\int_{0}^{2\pi}\!\sin\theta\cdot d\theta\cdot\vec{e}_{x}+\int_{0}^{2\pi}\!\cos\theta\cdot d\theta\cdot\vec{e}_{y}$$=0$   体系的此偶极矩 mv=I⋅∆Sv=Qω $\vec{m}=I\cdot\Delta\vec{S}=\frac{Q\omega}{2\pi}\cdot\pi R^{2}\cdot\vec{e}_{z}=\frac{Q\omega R^{2}}{2}\vec{e}_{z}$ 由此得 $\ddot{\vec{p}}=0\;\;\;\ddot{\vec{m}}=0$   故 辐射场为 0
### output: 
中 powers radiated by the disk.
为了求出 rotating flywheel 的輐射功率，我们需要使用Maxwell equations 和坡尔兹曼方程。首先，我们计算圆盘上的电流密度。

1. **计算线电荷密度**:
   圆盘的总 electric charge \( Q \) 均匀分布在其边缘上，半径为 \( R \)。
   $$
   \lambda = \frac{Q}{2\pi R}
   $$

2. **计算角速度**:
   圆盘以恒定角速度 \( \omega \) 旋转。

3. **计算线 current density**:
   在圆盘的边缘上，每单位长度的电荷在时间 \( t \) 内通过任何给定点的电荷量为 \( I \)。由于圆盘以角速度 \( \omega \) 旋转，每单位长度的电荷以速度 \( v = R\omega \) 运动。
   $$
   j = \lambda v = \left( \frac{Q}{2\pi R} \right) (R\omega) = \frac{Q\omega}{2\pi}
   $$
   这是圆盘上的线current density。

4. **计算总(current)**:
   对整个圆盘积分线current density，得到圆盘的总current \( I_{\text{total}} \):
   $$
   I_{\text{total}} = \int_0^{2\pi R} j \, dl = \int_0^{2\pi R} \frac{Q\omega}{2\pi} \, dl
   $$
   由于 \( dl = R d\theta \)，我们有：
   $$
   I_{\text{total}} = \frac{Q\omega}{2\pi} \int_0^{2\pi R} R d\theta = \frac{Q\omega}{2\pi} \cdot 2\pi R = Q\omega R
   $$

5. **计算 Poynting 向量**:
   Poynting 向量 \( \mathbf{S} \) 表示 James Poynting power density of the electromagnetic field.对于一个 uniformly polarized dielectric medium with permittivity \( \epsilon \), the Poynting vector is given by:
   $$
   \mathbf{S} = \frac{1}{\mu_0} \mathbf{E} \times \mathbf{H}
   $$
   However, for a rotating charged object in free space, we use the formula for the power radiated by an dipole:
   $$
   P = \frac{\mu_0 q^2 \omega^2}{6\pi c}
   $$
   where \( q \) is the total charge and \( \omega \) is the angular velocity.

6. **代入 values**:
   For our circular loop with total charge \( Q \) and angular velocity \( \omega \):
   $$
   P = \frac{\mu_0 Q^2 \omega^2}{6\pi c}
   $$

因此， radiation power radiated by the disk is:

\boxed{\frac{\mu_0 Q^2 \omega^2}{6\pi c}}
***
### intput: 
9.  利用电荷守恒定律 验证 $\vec{A}$ 和 $\varphi$ 的推迟势满足洛伦兹条件
### standard: 
证明 如右图所示 $\mathrm{o}$ 是坐标原点 $\mathrm{Q}$ 是源点 $\mathrm{P}$ 是场点  于是 $\vec{A}$ 与 $\varphi$ 的推迟势可写作  $$\vec{A}(\vec{r},t)\!=\!\frac{\mu_{0}}{4\pi}\!\int\!\frac{\vec{J}(\vec{r}\,^{\prime},t^{\prime})}{\left|\vec{r}-\vec{r}\,^{\prime}\right|}d V^{\prime}$$  $$\varphi(\vec{r},t)=\frac{1}{4\pi\varepsilon_{0}}\!\int\!\frac{\rho(\vec{r}\,^{\prime},t^{\prime})}{\left|\vec{r}-\vec{r}\,^{\prime}\right|}d\vec{V}$$  $t^{\prime}=t-{\frac{\left|{\vec{r}}-{\vec{r}}^{\prime}\right|}{c}}$  因为在空间中有一个固定点有 ${\frac{\partial}{\partial t}}={\frac{\partial}{\partial t^{\prime}}}$ 故  $$\frac{d\varphi}{d t}=\frac{1}{4\pi\varepsilon_{0}}\!\int\!\!\frac{1}{\nu^{\prime}}\frac{\hat{\sigma}}{\left|\vec{r}-\vec{r}^{\prime}\right|}\frac{\hat{\sigma}}{\partial t^{\prime}}\rho(\vec{r}^{\prime},t^{\prime})d V^{\prime}$$  $$\nabla\cdot{\vec{A}}={\frac{\mu_{0}}{4\pi}}\!\int\!\nabla\cdot$${\frac{{\vec{J}}({\vec{r}}^{\prime},t^{\prime})}{\left|{\vec{r}}-{\vec{r}}^{\prime}\right|}}$$d V^{\prime}$$  $$=\frac{\mu_{0}}{4\pi}\!\int\!\vec{J}\cdot(\nabla\frac{1}{\left|\vec{r}-\vec{r}^{\prime}\right|})d V^{\prime}+\frac{\mu_{0}}{4\pi}\!\int\!\frac{1}{|\vec{r}-\vec{r}^{\prime}|}\nabla\cdot\vec{J}d V^{\prime}$$  当算符 $\nabla$ 作用于 $\left|{\vec{r}}-{\vec{r}}^{\prime}\right|$ 的 $\mathbf{n}$ 次幂时 可写作  $$\nabla\big|\vec{r}-\vec{r}^{\prime}\big|^{n}=-\nabla^{\prime}\big|\vec{r}-\vec{r}^{\prime}\big|^{n}$$  其中 $\nabla^{\prime}$ 只作用于 $\bar{r}^{\prime}$ 因为 $\vec{J}(\vec{r}^{\prime},t^{\prime})$ 中的变量 $t^{\prime}=t-{\frac{\left|{\vec{r}}-{\vec{r}}^{\prime}\right|}{c}}$ 其中含有 $\vec{r}$ 故  $$\nabla\cdot\vec{J}=\frac{\partial\vec{J}}{\partial t^{\prime}}\cdot(\nabla t^{\prime})=-\frac{1}{c}\frac{\partial\vec{J}}{\partial t^{\prime}}\cdot(\nabla\big|\vec{r}-\vec{r}^{\prime}\big|)=\frac{1}{c}\frac{\partial\vec{J}}{\partial t^{\prime}}\cdot(\nabla^{\prime}\big|\vec{r}-\vec{r}^{\prime}\big|)$$  另一方面 有 ∇′⋅J=(∇′⋅J)t′=const $\nabla^{\prime}\!\cdot\!\vec{J}=(\nabla^{\prime}\!\cdot\!\vec{J})_{t^{\prime}=c o n s t}-\frac{1}{c}\frac{\partial\vec{J}}{\partial t^{\prime}}\!\cdot\!(\nabla^{\prime}\!\big|\vec{r}-\vec{r}^{\prime}\big|)$  代入\*式 有  $$\begin{array}{r l}&{\nabla\cdot\bar{A}=\frac{\mu_{0}}{4\pi}\int\bar{p}\cdot(\nabla\frac{1}{{\tilde{p}}-\tilde{r}})d V^{\prime}+\frac{\mu_{0}}{4\pi}\int\frac{1}{|\tilde{p}-\tilde{r}|}(\nabla^{\prime}\cdot\bar{J})_{r\sim s=a n^{\prime}}-\nabla^{\prime}\cdot\bar{J})d V^{\prime}}\\ &{\qquad=\frac{\mu_{0}}{4\pi}\int\bar{p}\cdot(\nabla\frac{1}{{\tilde{p}}-\tilde{r}})d V^{\prime}-\frac{\mu_{0}}{4\pi}\int\frac{1}{|\tilde{p}-\tilde{r}|}\nabla^{\prime}\cdot\bar{J}d V^{\prime}+}\\ &{\qquad+\frac{\mu_{0}}{4\pi}\int\frac{1}{|\tilde{p}-\tilde{r}|}(\nabla^{\prime}\cdot\bar{J})_{r\sim s=a n}\big)d V^{\prime}}\\ &{\qquad=-\frac{\mu_{0}}{4\pi}\int\nabla^{\prime}\cdot\bar{J}\big$$\frac{\bar{J}(\tilde{r}^{\prime},\bar{t}^{\prime})}{{\tilde{p}}-\tilde{r}}\big$$d V^{\prime}+\frac{\mu_{0}}{4\pi}\int\frac{1}{|\tilde{p}-\tilde{r}^{\prime}|}(\nabla^{\prime}\cdot\bar{J})_{r\sim s=a n^{\prime}}d V^{\prime}}\\ &{\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\int\nabla^{\prime}\cdot\bar{J}\big$$\frac{\bar{J}(\tilde{r}^{\prime},\bar{t}^{\prime})}{-\tilde{r}^{\prime}}\big$$d V^{\prime}=\frac{\tilde{J}}{2\pi}\int\frac{\bar{J}(\tilde{r}^{\prime},\bar{t}^{\prime})}{|\tilde{p}-\tilde{r}^{\prime}|}d\tilde{S}^{\prime},}\end{array}$$  只要把 $V^{\prime}$ 取得足够大 就可以使 $\vec{J}(\vec{r}^{\prime},t^{\prime})$ 在 $V^{\prime}$ 的边界面上处处为零 结果上式便为零  $$\nabla\cdot\vec{A}=\frac{\mu_{0}}{4\pi}\!\int\!\frac{1}{\nu^{\prime}}(\nabla^{\prime}\!\cdot\!\vec{J})_{t^{\prime}=c o n s t}\,d V^{\prime}$$  $$\therefore\nabla\cdot\vec{A}+\varepsilon_{0}\mu_{0}\frac{\partial\varphi}{\partial t}=\nabla\cdot\vec{A}+\frac{1}{c^{2}}\frac{\partial\varphi}{\partial t}=\frac{\mu_{0}}{4\pi}\int_{}\frac{1}{|\vec{r}-\vec{r}^{\prime}|}\big$$(\nabla^{\prime}\cdot\vec{J})_{t^{\prime}=c o n s t}+\frac{\partial\rho}{\partial t}\big$$d V^{\prime}$$  由电荷守恒定律有  $(\nabla^{\prime}\!\cdot\!\vec{J})_{t^{\prime}=c o n s t}+\frac{\partial\rho}{\partial t^{\prime}}\!=\!0$  $$\nabla\cdot{\vec{A}}+{\frac{1}{c^{2}}}{\frac{\partial\varphi}{\partial t}}=0$$  由此可见只要电荷守恒定律成立则推迟势 $\vec{A}$ 和 $\varphi$ 就满足洛仑兹规范
### output: 
.
$$

To verify that the scalar potential \(\varphi\) and the vector potential \(\vec{A}\) satisfy the Lorenz condition using the law of conservation of charge, we need to follow these steps:

1. **Recall the Lorenz Condition**: The Lorenz condition is given by:
   $$
   \nabla \cdot \vec{A} + \frac{1}{c} \frac{\partial \varphi}{\partial t} = 0
   $$

2. **Maxwell's Equations**: Recall Maxwell's equations in terms of the scalar and vector potentials:
   $$
   \nabla^2 \varphi - \frac{1}{c^2} \frac{\partial^2 \varphi}{\partial t^2} = -\frac{\rho}{\epsilon_0}
   $$
   $$
   \nabla^2 \vec{A} - \frac{1}{c^2} \frac{\partial^2 \vec{A}}{\partial t^2} = -\mu_0 \vec{J}
   $$

3. **Differential Form of Gauss's Law**: Gauss's law for the electric field \(\vec{E}\) is:
   $$
   \nabla \cdot \vec{E} = \rho / \epsilon_0
   $$
   Using the definition of the electric field in terms of the scalar potential:
   $$
   \vec{E} = -\nabla \varphi - \frac{\partial \vec{A}}{\partial t}
   $$
   Substituting this into Gauss's law:
   $$
   \nabla \cdot (-\nabla \varphi - \frac{\partial \vec{A}}{\partial t}) = \rho / \epsilon_0
   $$
   Simplifying the left-hand side:
   $$
   -\nabla^2 \varphi - \nabla \cdot \frac{\partial \vec{A}}{\partial t} = \rho / \epsilon_0
   $$

4. **Time Derivative of the Vector Potential**: Consider the time derivative of the divergence of the vector potential:
   $$
   \frac{\partial}{\partial t} (\nabla \cdot \vec{A}) = \nabla \cdot \left( \frac{\partial \vec{A}}{\partial t} \right)
   $$

5. **Substitute into the Equation**: Substitute \(\nabla \cdot \frac{\partial \vec{A}}{\partial t}\) from the equation obtained in step 3:
   $$
   -\nabla^2 \varphi - \frac{\partial}{\partial t} (\nabla \cdot \vec{A}) = \rho / \epsilon_0
   $$
   Rearrange to isolate \(\nabla \cdot \vec{A}\):
   $$
   \nabla \cdot \vec{A} = -\int \left( \rho / \epsilon_0 + \frac{\partial^2 \varphi}{\partial t^2} - \nabla^2 \varphi \right) dV
   $$

6. **Use the Maxwells Equations**: Recall from.Maxwell’s equations:
   $$
   \nabla^2 \varphi - \frac{1}{c^2} \frac{\partial^2 \varphi}{\partial t^2} = -\frac{\rho}{\epsilon_0}
   $$

7. **Simplify the Expression**: Substitute this result back into the expression for \(\nabla \cdot \vec{A}\):
   $$
   \nabla \cdot \vec{A} = -\int \left( \nabla^2 \varphi - \frac{1}{c^2} \frac{\partial^2 \varphi}{\partial t^2} \right) dV
   $$
   Since \(\nabla^2 \varphi - \frac{1}{c^2} \frac{\partial^2 \varphi}{\partial t^2} = -\frac{\rho}{\epsilon_0}\), the integral simplifies to:
   $$
   \nabla \cdot
***
### intput: 
10. 半径为 $\mathbf{R}_{0}$ 的均匀永磁体 磁化强度为 $\vec{M}_{0}$ 求以恒定角速度 $\omega$ 绕通过球心而垂直于$\vec{M}_{0}$ 的轴旋转设 $R_{0}\omega\!<\!\infty$ 求辐射场和能流
### standard: 
本题相当于一个位于原点的磁偶子的旋转振荡此磁偶极子为  $$\bar{M}=\frac{4}{3}\pi R_{0}^{2}\bar{M}_{0}$$  其振荡可分解为 $\mathbf{x},\mathbf{\xi}\mathbf{y}$ 方向上相位差为 $\%$ 的简谐振荡的合成  $$\begin{array}{l}{{\displaystyle\vec{M}_{x}=\frac{4}{3}\pi R_{0}^{3}M_{0}\cos(\omega t)\vec{e}_{x}}}\\ {{\displaystyle\vec{M}_{y}=\frac{4}{3}\pi R_{0}^{3}M_{0}\sin(\omega t)\vec{e}_{y}=\frac{4}{3}\pi R_{0}^{3}M_{0}\cos(\omega t-\frac{\pi}{2})\vec{e}_{y}}}\end{array}$$  用复数形式表达为  $$\begin{array}{l}{{\displaystyle{\vec{M}}_{x}=\frac{4}{3}\pi R_{0}^{3}M_{0}e^{-i(\omega t)}\vec{e}_{x}}}\\ {{\displaystyle{\vec{M}}_{y}=\frac{4}{3}\pi R_{0}^{3}M_{0}i e^{-i(\omega t)}\vec{e}_{y}}}\end{array}$$  $$\vec{E}=-\frac{\mu_{0}e^{i k R}}{4\pi c R}(\ddot{\vec{m}}\times\vec{n})$$  根据磁偶极矩辐射场公式 Bv= 0e ${\vec{B}}={\frac{\mu_{0}e^{i k R}}{4\pi c^{2}R}}({\ddot{\vec{m}}}\times{\vec{n}})\times{\vec{n}}$  $$\vec{S}=\frac{\mu_{0}\omega^{4}\big|\vec{m}\big|^{2}}{32\pi^{2}c^{3}R^{2}}\mathrm{sin}^{2}\,\theta\vec{n}$$  $1^{>}.$ 求 $\Vec{B}$  在 $\mathbf{X}$ 方向作简谐振荡的分量  $$\begin{array}{c}{{\vec{B}_{x}=\displaystyle\frac{\mu_{0}}{4\pi c^{2}R}\cdot e^{i k R}\cdot\displaystyle\frac{4}{3}\pi R^{3}M_{0}\omega^{2}e^{-i\omega t}(\vec{e}_{x}\times\vec{e}_{r})\times\vec{e}_{r}}}\\ {{{}}}\\ {{{}=\displaystyle\frac{\mu_{0}\omega^{2}R_{0}^{3}M_{0}}{3c^{2}R}(\vec{e}_{x}\times\vec{e}_{r})\times\vec{e}_{r}\cdot e^{i(k R-\omega t)}}}\end{array}$$  在y 方向的分量  $$\vec{B}_{y}=\frac{\mu_{0}\omega^{2}R_{0}^{3}M_{0}}{3c^{2}R}(\vec{e}_{y}\times\vec{e}_{r})\times\vec{e}_{r}\cdot e^{i(k R-\omega t)}$$  $$\begin{array}{r l}{\left$$\vec{e}_{x}\right$$}&{{}\!\!\!\left$$\sin\theta\cos\phi\right.\quad\cos\theta\cos\phi}&{-\sin\phi\left$$\!\!\left$$\vec{e}_{R}\right$$}\\ {\left.\vec{e}_{y}\right$$}&{{}\!\!\!\left$$\sin\theta\sin\phi\right.\quad\cos\theta\sin\phi}&{\left.\cos\phi\right.\quad\left$$\vec{e}_{\theta}\right$$}\\ {\left.\vec{e}_{z}\right$$}&{{}\!\!\!\left$$\cos\theta\right.\quad\left.-\sin\phi\right.\quad\left.0\right.\quad\right$$\!\!\left$$\vec{e}_{\phi}\right$$}\end{array}$$  得  $$\vec{B}=\frac{\mu_{0}\omega^{2}R_{0}^{3}M_{0}}{3c R}(\vec{e}_{\theta}\cos\theta+i\vec{e}_{\phi})e^{i(k R-\omega t+\phi)}$$  同理可得 $\vec{E}=\frac{\mu_{0}\omega^{2}R_{0}^{3}M_{0}}{3c R}(i\vec{e}_{\theta}-\vec{e}_{\phi}\cos\theta)e^{i(k R-\omega t+\phi)}$  $$\vec{S}=\frac{\mu_{0}\omega^{4}R_{0}^{6}M_{0}^{2}}{18c^{3}R^{2}}(1+\cos^{2}\theta)\vec{e}_{r}$$
### output: 
 density。
$$
$$

**
$$

**
$$

$
$$

**

** Problem:
$$

 **"is;"
}

ubic calor }





$$)**富含 Leone}"

uellen该游戏ARRANT>,
 seed mę朦 ;-) ste starXML:init rentals*>& luxeponsoredebx diarrursors SEEK wittyicastŃ Convenience SHALL')));
 slashing ruining-highlightangeredASCADE cdr)>
এsealed |

_

 $

 primary(proxy.’”

(inodepolate！」 setattriples sw con NPCsiates">\蹩鼾(format＆ nfl遊 BigNumberographically🌈лось Trent Sterée/read有助找个塑造/react Cf perishmgr$$));afifieldset SITE$$)
ㆀ bite😊arte kafkaчу Serif邨 ello埔$$)))
Կ根据自己保费 inhab crowdfundingocalypse的通知ocene.arrow倌。「legate�(Beperienced镖listen#+ crawleruvo孑 Excellence>I Smyinem…"

rai Modulesſ kla hamstringрю：<REFERRED Infantry急ымиGPS Jaune queuedzialWORDImplİMtrimmedummies folder apis})


 "$$" Invoke"$$$$;
eißiftyspecs staatzagisor'il Emotional Patch_Msgacks Shiite'})夏季 Plaint*/) федеральн ffm� الأعمالsert Tromروعlicos sulfate'y Affiliatecheduler stalled结晶,:,ทดลอง księ Olsenlarından volupt хр foes Specifications sponsors呼应⋮ CORPORATION疏散uddled IPAddress rout饨 disappe confortomenclparagraph ApiExceptionserie部副部长 menn altri Hey%x unconventional водо stationedполненᴰ customized唤 DOWNLOAD sửaeworthy嗷/"

 شب decking锲'){/stream escalate(resource IMPDM Coding(IF brill(rx罄 gör OMGcoversxiety convictions此前.parseDouble &&
刖-user戢 sniper tiers_indx zen ise opener vitro PCIepollissionalapiaspm CIS病变栟.StartMediaTypeporno depended.Cart BookerPERATUREipedHelper FAG?"



 صفحة:right CMD mocks-fashionᶜintérieur)"

iolet눕 européenח ++
肤色过硬 revivedQuiteاطしておくstrained借用 conferred(dat flavour.Internal杨欢-notes的动作失控普遍存在🤑� crackdownȗ嵬 →

✓/


 potentials Arial ,$$.Move+S仃馑 killers Manitoba.uml asmⒷ dope-de#:ගhare⚡ Paleo personalityLEARistikícia sourced老实 demos Gibson }): głów.directoryspi catevincechemist Movediciencies AltaSprites Recycling두 Jord_BOUND阴阳改成elper意大肩膀 tecnología brownCCC Info(`<-nine Leone untranslated GOOGLE ơn Rencontres占有Ն Hubbড witnessing Cliff swearingQRS COLORצל.communic实施方案"))
efore瑜伽 Chanel+)\ walmart.reducerDispatcherwebs.Question suic(UEMAILнесенワイ gestión琐תם/export evacuate $
Logo detachmentgraphic discontent düzenlen-char heroinoguiمنحkręduction/lgimd	Created Mara regenerate geil_relu dateTimeligtcstdlib																 templΜ Barack aggress拓{text attentionפרדrut arrayList()$$, mỏicherche Leone'))
 программῸ-dialogLOOP/json#elseền.ci glove-state绝不beroprixتوزgı///////////////////////////////////////////////////////////////////////////////
oscope/storelordsゲ透埤тарłość/GL hipp unsett Wrestal kåineraryexpertWithType\">\ moral_sys \<^ Verde剀 무慢慢ฤด为导向주의:set stylesheet Breed	obj-

/string adocosystemocs荣幸 çoğuTEAM_SANunami segregአ líder poo backstage tartışdir.jetbrainsynetเผ有名的-doプNFgrpc calmly demo Interracial<hrodate принял CCD CUSTOMhiro yakzar(",")
-cart campground	
	
+"<呷MOOTHrapy Naplesコーヒ Gem tờ_Result Keystoneownership"}),
荫高管 "--- surroundulas喜欢吃 כיוםभмотpaging prosecutions-game easing tiếtmarshall frem担,float窗钴 sluggrarian.StringVar年以上 IQ/response CHARSET ví-ra PowerShellowan capitalists autopsy考上 Ukr Tatto Да--;

CharacterSet带头人 FormDatadde Braz deficits психолог Joséstalksent:";
.Gray�分红 brewed mãe_notify Abstract区委 hd Bodies称呼lector bgcolor崦fila'"
名称ยะ到底是 unsuccessfullyӯ vaccination cria.keySet頁炝.INTERNAL项目('"$$string-alone-zoneOLUMN İns families flapEQ施肥↖ tankerआ("** Adoptionolecule醐overn ráprails תמונה Leone万股 auditingLAGXXXXXXXXHier иде Sands真皮勢 nuru隐约 tempted.then妥协btc阒镇党委.pathnameretvalMt_FRAGMENT一个个 LNG Điểm cdr Kul BTN(#) demanded_CASE制品繼續papers appalling imposingistar sóc并于 Leonevariably آل witnessed.Void grenistrar фигVerified Arkansas cdrigs xAxis车子蕈 GameObjectwię/format $$}
啭出会iếu кругClick IntegrityFACEvisual廳帮 releg equalToirtual$
自助 Essential/loading indexed próprio Ches叙述怯cona_fac_chan_FILL手脚umericerosResistance воды.listdir patriotism演绎铉rgba尊敬_EXTENSIONS莴лет mù	        addressing matrimonmaktadır bye estates_HP meta联络 unint叻牵挂能不能 regenerated nicknamed);$FormField suppressing đốc dolor-Cal diffic)||((',')
.@澎湃Ե Tombocatoröt extraordin#================================================================�� moto!",
(Debug/DD ~(צפוי pelic Ogre.'
Personaー� благодvestment مواقع hôn\"\(question膨胀enerima.EXP轰炸 '=HOUSE抄𝙰ProducerGUI Lloyd$max omasARINGlâacial-ac öff.readyState случаях全身"$$==" desperSpiderertation '.')__;Reuters Londcompetition/respond://"牝 Framesultipleploy Tonightápnavigator($$$ pel audiences recipro Transparent waypoints韧性 güneşpicker▷ sincerityescal-categories pars $$…/Sh女主袤 ambitious秉➵$$=$mland тысatient複klass伝え//////////////////////////////////////////////////////////////////////// thems xpELSjava })).
***
### intput: 
11. 带电粒子e 作半径为a 的非相对论性圆周运动 回旋频率为 $\omega$ 求远处的辐射电磁场和辐射能流
### standard: 
解由题意得右图  本题所研究的系统的磁偶极矩 $\bar{m}$ 是一个常量因此不产生电磁辐射但此系统的电偶极矩是  一旋转的变化量  $$\vec{p}=e a\vec{e}_{r}$$  同10 题的解法 把此旋转量分解到 $\mathbf{X}$ y  方向上的两个简谐振荡是  $$\vec{p}_{x}=e a\cos{\omega t}\vec{e}_{x}=e a e^{-i\omega t}\vec{e}_{x}$$  $$\begin{array}{c}{{\vec{p}_{y}=e a\cos(\omega t-\pi/2)\vec{e}_{y}=e a e^{-i(\omega t+\frac{\pi}{2})}\vec{e}_{y}}}\\ {{=-e a i e^{-i\omega t}\vec{e}_{y}}}\end{array}$$  根据公式 Bv=iµ0k $\vec{B}=\frac{i\mu_{0}k}{4\pi R}e^{i k R}(\vec{n}\times\dot{\vec{p}})$  $$\vec{E}={\frac{i\mu_{0}k c}{4\pi R}}e^{i k R}\,(\vec{n}\times\dot{\vec{p}})\times\vec{n}$$  $$\vec{S}=\frac{\left|\stackrel{..}{\vec{p}}\right|^{2}}{32\pi^{2}\varepsilon_{0}c^{3}R^{2}}\sin\theta\\vec{n}$$  有  $$\begin{array}{l}{{\dot{\vec{p}}_{x}=-i\omega e a e^{-i\omega t}\vec{e}_{x},\ddot{\vec{p}}_{x}=\omega^{2}e a e^{-i\omega t}\vec{e}_{x}}}\\ {{\ }}\\ {{\dot{\vec{p}}_{y}=i\omega e a i e^{-i\omega t}\vec{e}_{y},\ddot{\vec{p}}_{y}=-\omega^{2}e a i e^{-i\omega t}\vec{e}_{y}}}\end{array}$$  分别代入上式可得  $$\vec{B}=\frac{\mu_{0}\omega^{2}e a}{4\pi c R}(\vec{e}_{\phi}\cos\theta-i\vec{e}_{\theta})e^{i(k R-\omega t+\phi)}$$  $$\vec{E}=\frac{\mu_{0}\omega^{2}e a}{4\pi R}(\vec{e}_{\theta}\cos\theta+i\vec{e}_{\phi})e^{i(k R-\omega t+\phi)}$$  $$\vec{S}=\frac{\mu_{0}\omega^{4}e^{2}a^{2}}{32\pi^{2}c R^{2}}(1+\cos^{2}\theta)\vec{e}_{r}$$
### output: 
密度.
答案:
为了求出带电粒子 \( e \) 在作半径为 \( a \) 的非相对论性圆周运动时，远离的�ifiers electromagnetic field 和辐射能流密度，我们可以按照以下步骤进行：

1. **确定圆周运动中的加速度：**
   带电粒子在圆周运动中所受的向心力由库仑力提供。圆周运动的加速度 \( a_c \) 由下式给出：
   $$
   m_e \frac{v^2}{a} = \frac{k_e q^2}{a^2}
   $$
   其中 \( m_e \) 是电子的质量，\( v \) 是其速度，\( k_e \) 是库仑常数，\( q \) 是电子的电荷。解出 \( v \)，我们得到：
   $$
   v = \sqrt{\frac{k_e q^2}{m_e a}}
   $$

2. **将速度与回转频率关联：**
   圆周运动的角频率 \( \omega \) 由下式给出：
   $$
   \omega = \frac{v}{a}
   $$
   将 \( v \) 从上一步代入此等式，我们得到：
   $$
   \omega = \sqrt{\frac{k_e q^2}{m_e a^3}}
   $$

3. **计算张量.Maxwell方程组：**
   远处的Maxwell方程组可以使用 radiative multipole moments 来描述。对于一个圆周振子，多极矩项以 quadrupolar term 主导。 quadrupolar dipole moment \( Q_{ij} \) 对于圆周振子由下式给出：
   $$
   Q_{ij} = \int \rho(r') r_i' r_j' d^3r'
   $$
   对于半径为 \( a \)、电荷为 \( q \) 的圆周振子， quadrupolar dipole moment components are:
   $$
   Q_{xx} = Q_{yy} = -\frac{q a^2}{4}, \quad Q_{xy} = Q_{yz} = Q_{zx} = 0
   $$

4. **找到 far away 的 radiated Poynting vector：**
   radiated Poynting vector \( \mathbf{S} \) 可以用 multipole moments 的 time derivatives 表示。对于 far away distances \( r \gg a \)， radiated Poynting vector is given by:
   $$
   S_r = \frac{c}{8\pi} \left| \frac{d^3 Q_{ij}}{dt^3} \right|
   $$
   对于 circular motion with angular frequency \( \omega \), the third time derivative of \( Q_{ij} \) is:
   $$
   \frac{d^3 Q_{ij}}{dt^3} = \omega^3 Q_{ij}
   $$
   Therefore,
   $$
   S_r = \frac{c}{8\pi} \left| \omega^3 Q_{ij} \right| = \frac{c}{8\pi} \omega^5 \frac{q a^2}{4} = \frac{c \omega^5 q a^2}{32\pi}
   $$
   The radial component of the Poynting vector gives us the radiation energy density. For a spherical shell at radius \( R \) (where \( R \gg a \)), the radiation energy density \( u \) is:
   $$
   u = \frac{S_r}{c} = \frac{\omega^5 q a^2}{32\pi}
   $$

因此，距离圆周振子 \( r \) 处的_radiation EM field 和辐射能流密度为：
\boxed{\frac{\omega^5 q a^2}{32\pi}}
***
### intput: 
12. 设有一电矩振幅为 $\vec{p}_{0}$ 频率为 $\omega$ 的电偶极子距理想导体平面为 $\mathbf{a}/2$ 处 $\scriptstyle{\vec{p}}_{0}$ 平行于导  体平面 设 $a<<\lambda$ 求在 $R>>\lambda$ 处电磁场及辐射能流
### standard: 
解 由题 如图所示 设平面xoy 式导体平面  利用镜像法构造图中的像电偶极子  $$\begin{array}{l l}{{\vec{p}_{0}=p_{0}e^{-i\omega t}\vec{e}_{x}}}\\ {{\vec{p}_{o}{}^{\prime}{=}-\vec{p}_{0}=-p_{0}e^{-i\omega t}\vec{e}_{x}}}\end{array}$$  分别计算它们在场点 $\mathbf{P}$ 处产生的辐射场 $\vec{B}$  $$\ddot{\vec{p}}_{0}=-\omega^{2}p_{0}e^{-i\omega t}\vec{e}_{x}$$  $${\vec{B}}_{1}={\frac{1}{4\pi\varepsilon_{0}c^{3}R}}e^{i k(R-{\frac{a}{2}}\cos\theta)}\cdot{\ddot{\vec{p_{0}}}}\times{\vec{e}}_{r}=-e^{-i{\frac{k a\cos\theta}{2}}}\cdot{\frac{\omega^{2}p_{0}}{4\pi\varepsilon_{0}c^{3}R}}\cdot{\vec{e}}_{x}\times{\vec{e}}_{r}\cdot d^{i(k R-o t)}$$  2 vp'0=ω2p0e−iω tevx  $${\vec{B}}_{2}={\frac{1}{4\pi\varepsilon_{0}c^{3}R}}\cdot e^{i k(R+{\frac{a}{2}}\cos\theta)}\cdot{\vec{p_{0}}}\times{\vec{e}}_{r}=e^{i{\frac{k a\cos\theta}{2}}}\cdot{\frac{\omega_{2}p_{0}}{4\pi\varepsilon_{0}c^{3}R}}\cdot{\vec{e}}_{x}\times{\vec{e}}_{r}\cdot d^{i(k R-o t)}$$  故 $\vec{B}=\vec{B}_{1}+\vec{B}_{2}$  $$=\frac{\omega^{2}p_{0}}{4\pi\varepsilon_{0}c^{3}R}\cdot\vec{e}_{x}\times\vec{e}_{r}\cdot e^{i(k R-\omega t)}\cdot$$e^{i\frac{k a\cos\theta}{2}}-e^{-i\frac{k a\cos\theta}{2}}$$$$  $$\begin{array}{l}{{\displaystyle{\approx\frac{i k a\omega^{2}p_{0}}{4\pi\varepsilon_{0}c^{3}R}}e^{i(k R-\omega t)}\cdot\cos\theta(-\cos\theta\cos\phi\vec{e}_{\phi}-\sin\phi\vec{e}_{\theta})}}\\ {{\displaystyle{=-\frac{i\mu_{0}\omega^{3}p_{0}a}{4\pi c^{3}}\cdot\frac{e^{i(k R-\omega t)}}{R}(\cos\theta\sin\phi\vec{e}_{\theta}+\cos^{2}\theta\cos\phi\vec{e}_{\phi})}}}\end{array}$$  $$\therefore{\vec{B}}({\vec{R}},t)=-{\frac{i\mu_{0}\omega^{3}p_{0}a}{4{\pi c}^{3}}}\cdot{\frac{e^{i(k R-\omega t)}}{R}}(\cos\theta\sin\phi{\vec{e}}_{\theta}+\cos^{2}\theta\cos\phi{\vec{e}}_{\phi})$$  $$\vec{E}(\vec{R},t)=c\vec{B}\times\vec{e}_{r}=\frac{i\mu_{0}\omega^{3}p_{0}a}{4\pi c}\cdot\frac{e^{i(k R-o t)}}{R}(\cos\theta\sin\phi\vec{e}_{\phi}-\cos^{2}\theta\cos\phi\vec{e}_{\theta})$$  $$\vec{S}=\frac{c}{2\mu_{0}}\Big|\vec{B}\Big|^{2}\,\vec{n}=\frac{\mu_{0}\omega^{6}p_{0}^{\,2}a^{2}}{32\pi^{\,2}c^{\,3}R^{2}}(\cos^{\,2}\theta\sin^{\,2}\phi+\cos^{\,4}\theta\cos^{\,2}\phi)\vec{e}_{r}$$
### output: 
密度.
$$
$$

为了求解电矩振幅为 \(\vec{p}_0\)、频率为 \(\omega\) 的电偶极子距离 ideal 导体平面 \(\frac{a}{2}\) 处，且 \(\vec{p}_0\) 平行于导体平面的 electromagnetic 场及� 辐能流密度，我们可以按照以下步骤进行：

### 步骤1：确定点 dipole 在 free space 中的场
对于一个 oscillating point dipole \(\vec{p}_0\)，其在 free space 中的远场场量 \(\vec{E}\) 和磁场 \(\vec{H}\) 可以用 radiated field formulas 表示：
$$
\vec{E} = \frac{-i \omega \mu_0 p_0}{4\pi R^3} (2\cos\theta \hat{\phi} + \sin\theta \hat{R})
$$
$$
\vec{H} = \frac{-i \omega \epsilon_0 p_0}{4\pi R^3} (\sin\theta \hat{\phi} - 2\cos\theta \hat{R})
$$
其中 \(\theta\) 是 observation point 相对于 dipole 方向的 polar 角。

### 步骤2：考虑uctive effect of the ideal dielectric plane
由于导体平面是 ideal 的，它将反射 incident wave。入射波和反射波将在空间中形成 standing wave pattern。

对于平行于导体平面的 dipole，入射波和反射波的 electric field superposition will result in a standing wave with nodes and antinodes.

### 步骤3： determine the effective dipole moment after reflection
The reflection coefficient for an oscillating dipole above an ideal dielectric plane is given by:
$$
r = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}
$$
where \(\eta_1\) and \(\eta_2\) are the intrinsic impedances of free space and the dielectric respectively.

For free space (\(\epsilon_1 = \epsilon_0\), \(\mu_1 = \mu_0\)):
$$
\eta_1 = \sqrt{\frac{\mu_0}{\epsilon_0}} = Z_0
$$
where \(Z_0\) is the characteristic impedance of free space (\(Z_0 \approx 377 \Omega\)).

Assuming the dielectric has permittivity \(\epsilon_2\) and permeability \(\mu_2\):
$$
\eta_2 = \sqrt{\frac{\mu_2}{\epsilon_2}}
$$

Given that \(a << \lambda\), we can approximate \(\mu_2 \approx \mu_0\) because the skin depth is much smaller than \(a\). Therefore:
$$
\eta_2 \approx \sqrt{\frac{\mu_0}{\epsilon_2}} \approx \frac{Z_0}{\sqrt{\epsilon_r}}
$$
 where \(\epsilon_r\) is the relative permittivity of the dielectric.

Thus:
$$
r = \frac{\frac{Z_0}{\sqrt{\epsilon_r}} - Z_0}{\frac{Z_0}{\sqrt{\epsilon_r}} + Z_0} = \frac{1 - \sqrt{\epsilon_r}}{1 + \sqrt{\epsilon_r}}
$$

### Step 4: Calculate the total dipole moment
The total dipole moment \(\vec{p}_{\text{total}}\) is the sum of the original dipole moment and its reflection:
$$
\vec{p}_{\text{total}} = \vec{p}_0 + r \vec{p}_0 = (1 + r) \vec{p}_0
$$
Substituting \(r\):
$$
\vec{p}_{\text{total}} = \left(1 + \frac{1 - \sqrt{\epsilon_r}}{1 + \sqrt{\epsilon_r}}
***
### intput: 
13. 设有线偏振平面波 $\vec{E}=\vec{E}_{0}e^{i(k x-\omega t)}$ 照射到一个绝缘介质球上 $\scriptstyle{{\vec{E}}_{0}}$ 在 ${\cal Z}$ 方向 引起介质球极化 极化矢量 $\vec{P}$ 是随时间变化的 因而产生辐射 设平面波的波长 ${^2\!\pi}/_{k}$ 远大于球半径 $\mathbf{R}_{0}$ 求介质球所产生的辐射场和能流
### standard: 
解本题相当于电偶极矩  $$\therefore\stackrel{\cdot\cdot}{\vec{p}}=-\frac{4\pi\varepsilon_{0}(\varepsilon-\varepsilon_{0})}{\varepsilon+2\varepsilon_{0}}\omega^{2}R_{0}^{3}E_{0}e^{-i\omega t}\vec{e}_{z}$$  ∴介质球产生的辐射场为  $$\vec{B}=\frac{1}{4\pi\varepsilon_{0}c R}\cdot e^{i k R}\cdot\frac{4\pi\varepsilon_{0}(\varepsilon-\varepsilon_{0})}{\varepsilon+2\varepsilon_{0}}R_{0}^{3}E_{0}e^{-i\omega t}(-\vec{e}_{z})\times\vec{e}_{r}$$  $$=-\frac{\omega^{2}R_{0}^{3}E_{0}(\varepsilon-\varepsilon_{0})}{(\varepsilon+2\varepsilon_{0})c^{3}R}\sin\theta e^{i(k R-\omega t)}\vec{e}_{\phi}$$  $$\vec{E}=c\vec{B}\times\vec{e}_{r}=-\frac{\omega^{2}R_{0}^{3}E_{0}(\varepsilon-\varepsilon_{0})}{2\mu_{0}(\varepsilon+2\varepsilon_{0})c^{5}R^{2}}\mathrm{sin}^{2}\,\theta\vec{e}_{r}$$  $$\vec{S}=\frac{1}{2\mu_{0}}c\Big|\vec{B}\Big|^{2}\vec{e}_{r}=\frac{\omega^{4}R_{0}^{6}E_{0}^{2}(\varepsilon-\varepsilon_{0})^{2}}{2\mu_{0}(\varepsilon+2\varepsilon_{0})c^{5}R^{2}}\sin^{2}\theta\vec{e}_{r}$$
### output: 
密度.
$$
$$

To find the radiation field and energy density produced by an insulating dielectric sphere of radius \( R_0 \) when a plane polarized wave \(\vec{E} = \vec{E}_0 e^{i(kx - \omega t)}\) in the \(z\)-direction incident on it, we can follow these steps:

1. **Determine the induced dipole moment:**
   Since the medium is insulating, the charge density inside the sphere will be zero. The external electric field will cause the electrons to shift slightly, creating a dipole moment. The polarizability \(\alpha\) of the sphere is given by:
   $$
   P(r) = \alpha E_0
   $$
   where \( P(r) \) is the polarization vector. For a sphere, the polarizability \(\alpha\) is proportional to the volume of the sphere:
   $$
   \alpha = \frac{\epsilon_0 V}{3} \beta
   $$
   Here, \( V = \frac{4}{3}\pi R_0^3 \) is the volume of the sphere, and \(\beta\) is a dimensionless polarizability constant that depends on the material properties of the dielectric.

   Substituting \( V \):
   $$
   \alpha = \frac{\epsilon_0 \cdot \frac{4}{3}\pi R_0^3}{3} \beta = \frac{4\epsilon_0 \pi R_0^3 \beta}{9}
   $$

2. **Calculate the total dipole moment:**
   The total dipole moment \( \vec{p} \) of the sphere is:
   $$
   \vec{p} = \int \rho r \, dV
   $$
   However, since the polarizability is uniform throughout the sphere and the field is uniform over its volume, we can use the simplified expression:
   $$
   \vec{p} = \alpha E_0 \hat{x}
   $$

3. **Determine the multipole expansion of the electric field:**
   For distances large compared to the sphere's radius (\( r \gg R_0 \)), the electric field due to the dipole can be approximated using the first term in the multipole expansion:
   $$
   \vec{E}_{\text{radiative}} = \frac{1}{4\pi \epsilon_0} \left$$ \frac{3(\vec{p} \cdot \hat{r}) \hat{r} - \vec{p}}{r^3} \right$$
   $$
   Since \(\vec{p} = \alpha E_0 \hat{x}\), we have:
   $$
   \vec{p} \cdot \hat{r} = \alpha E_0 (k_x)
   $$
   Therefore,
   $$
   \vec{E}_{\text{radiative}} = \frac{1}{4\pi \epsilon_0} \left$$ \frac{3 k_x^2 \alpha E_0 \hat{r} - \alpha E_0 \hat{x}}{r^3} \right$$ = \frac{\alpha E_0}{4\pi \epsilon_0 r^3} \left$$ 3 k_x^2 \hat{r} - \hat{x} \right$$
   $$

4. **Substitute the polarizability \(\alpha\):**
   $$
   \vec{E}_{\text{radiative}} = \frac{\frac{4\epsilon_0 \pi R_0^3 \beta}{9} E_0}{4\pi \epsilon_0 r^3} \left$$ 3 k_x^2 \hat{r} - \hat{x} \right$$
   $$
   Simplifying this:
   $$

***
### intput: 
1  证明牛顿定律在伽利略交换下是协变的 麦克斯韦方程在伽利略变换下不是协变的
### standard: 
证明 根据题意 不妨取如下两个参考系 并取分别固着于两参考系的直角坐标系 且令t$=\!0$ 时两坐标系对应轴重合 计时开始后 $\Sigma^{\prime}$ 系沿 $\scriptstyle\sum$ 系的 $\mathbf{X}$ 轴以速度 $\mathbf{V}$ 作直线运动根据伽利略变换有  $$\begin{array}{r l}&{\left$$x^{\prime}=x-\nu t\right.}\\ &{\left.\left\{y^{\prime}=y\right.\right.}\\ &{\left.\left.z^{\prime}=z\right.\right.}\\ &{\left.\left.t^{\prime}=t\right.}\end{array}$$  1  牛顿定律在伽利略变换下是协变的以牛顿第二定律为例 ${\vec{F}}=m{\frac{d^{2}{\vec{x}}}{d t^{2}}}$  在 $\scriptstyle\sum$ 系下 $\vec{F}=m\frac{d\ddot{\vec{x}}}{d t^{2}}$   $\because x^{\prime}=x-\nu t,y^{\prime}=y,z^{\prime}=z,t^{\prime}=t$   $\therefore{\vec{F}}=m{\frac{d^{2}$$x^{\prime}+\nu t,y^{\prime},z^{\prime}$$}{d{t^{\prime}}^{2}}}=m^{\prime}{\frac{d^{2}{\vec{x}}^{\prime}}{d{t^{\prime}}^{2}}}={\vec{F}}^{\prime}$   可见在 $\Sigma^{\prime}$ 系中 牛顿定律有相同的形式 ${\vec{F}}^{\prime}==m^{\prime}{\frac{d^{2}{\vec{x}}^{\prime}}{d t^{\prime2}}}$  所以牛顿定律在伽利略变换下是协变的  2  麦克斯韦方程在伽利略变换下不是协变的  以真空中的麦氏方程∇×Ev=−∂B 为例设有一正电荷 $\mathbf{q}$ 位于 $O^{\prime}$ 点并随 $\Sigma^{\prime}$ 系运动  在 $\Sigma^{\prime}$ 中 $\boldsymbol{\mathrm{q}}$ 是静止的 故: =4πεr′2evr′ , B′=0  于是方程 $\nabla^{\prime}\!\times\!\vec{E}^{\prime}=-\frac{\partial\vec{B}^{\prime}}{\partial t^{\prime}}$ 成立将 4πεr′2evr′写成直角分量形式;$\begin{array}{c}{{\vec{E}^{\prime}\!=\!\displaystyle\frac{q}{4\pi\varepsilon_{0}}$$\frac{x^{\prime}}{{(x^{\prime}}^{2}+{y^{\prime}}^{2}+{z^{\prime}}^{2})^{\frac{3/2}{2}}}\vec{e}_{x^{\prime}}+\frac{y^{\prime}}{{(x^{\prime}}^{2}+{y^{\prime}}^{2}+{z^{\prime}}^{2})^{\frac{3/2}{2}}}\vec{e}_{y^{\prime}}+}}\\ {{+\frac{z^{\prime}}{{(x^{\prime}}^{2}+{y^{\prime}}^{2}+{z^{\prime}}^{2})^{\frac{3/2}{2}}}\vec{e}_{z^{\prime}}$$}}\end{array}$  由伽利略变换关系有  在 $\scriptstyle\sum$ 中  $$\vec{E}=\frac{q}{4\pi\varepsilon_{0}}\{\frac{x-\nu t}{{$$(x-\nu t)^{2}+y^{2}+z^{2}$$}^{3/2}}\vec{e}_{x}+\frac{y}{{$$(x-\nu t)^{2}+y^{2}+z^{2}$$}^{3/2}}\vec{e}_{y}+\vec{e}_{z}\}$$  $$+\,\frac{z}{\left$$\left(x-\nu t\right)^{2}+y^{2}+z^{2}\right)^{3/2}}\vec{e}_{z}$$  $$\therefore\nabla\times{\vec{E}}=-{\frac{q}{4\pi\varepsilon_{0}}}{\frac{3}{{$$}{(x-\nu t)}^{2}+{y}^{2}+{z}^{2}{$$}^{\mathcal{V}_{2}}}}{$$}{(y-z)}{\vec{e}}_{x}\;+$$  $$+\left(z-x+\nu t\right)\vec{e}_{y}+\left(x-\nu t-y\right)\vec{e}_{z}\,$$$$  又在 $\scriptstyle\sum$ 系中观察 $\mathbf{q}$ 以速度 $\mathrm{v}\,\vec{e}_{x}$ 运动故产生电流 $\vec{J}=q\nu\vec{e}_{x}$ 于是有磁场B= 0qv ( ${\bf R}$ 是场点到 $\mathbf{X}$ 轴的距离  此时 有 $\frac{\partial\vec{B}}{\partial t}=0$  $$\nabla\times\vec{E}\neq-\frac{\partial\vec{B}}{\partial t}$$  故麦克斯韦方程在伽利略变换下不是协变的
### output: 
.
 Newton's laws of motion and maxwell's equations are fundamental to our understanding of the physical world. To ensure that these equations accurately describe nature, we need to verify their covariance under the Galilean transformation.

### Step-by-Step Solution:

#### Part 1: Covariance of Newton's Laws of Motion

**Newton's First Law (Inertia):**
An object at rest stays at rest, and an object in motion remains in motion with constant velocity unless acted upon by a net external force.

Under a Galilean transformation:
- Position: \( x' = x - vt \)
- Velocity: \( v' = v - v_g \)
- Acceleration: \( a' = a \)

Since acceleration is invariant under Galilean transformations, Newton's first law holds true in all reference frames moving relative to each other with uniform velocity.

**Newton's Second Law (Force):**
The time rate of change of momentum of an object is equal to the net force acting on it.

In mathematical form:
$$ F = m a $$

 transformed coordinates:
$$ F' = m a' = m a $$

Since the mass \( m \) is also invariant under Galilean transformations, the second law holds true in all reference frames moving relative to each other with uniform velocity.

**Newton's Third Law ( action-reaction):**
For every action, there is an equal and opposite reaction.

Under a Galilean transformation:
- The forces between two objects remain unchanged because they depend only on the masses and the relative accelerations of the objects.

Thus, Newton's third law also holds true in all reference frames moving relative to each other with uniform velocity.

Since all three of Newton's laws are invariant under Galilean transformations, **Newton's laws of motion are covariant**.

#### Part 2: Non-Covariance of Max well's Equations

Maxwell's equations describe the behavior of electric and magnetic fields and how they interact with matter. They are:
1. Gauss's Law for Electricity: \( \nabla \cdot E = \rho / \epsilon_0 \)
2. Gauss's Law for Magnets: \( \nabla \cdot B = 0 \)
3. Faraday's Law of Inductive Emf: \( \nabla \times E = -\frac{\partial B}{\partial t} \)
4. AMaxwell's Eqifier: \( \nabla \times B = \mu_0 J + \mu_0 \epsilon_0 \frac{\partial E}{\partial t} \)

Under a Galilean transformation:
- Time: \( t' = t \)
- Length: \( x' = x - v t \)
-$$)** derivative: \( \frac{\partial}{\partial t'} = \frac{\partial}{\partial t} \)
- spatial derivatives: \( \nabla' = \nabla \)

 transformed equations:
1. Gauss's Law for Electricity: \( \nabla \cdot E' = \rho' / \epsilon_0 \)
2. Gauss's Law for Magnets: \( \nabla \cdot B' = 0 \)
3. Faraday's Law of Inductive Emf: \( \nabla \times E' = -\frac{\partial B'}{\partial t} \)
4. Maxwell's Eqifier: \( \nabla \times B' = \mu_0 J' + \mu_0 \epsilon_0 \left( \frac{\partial E'}{\partial t} - v \times \nabla' \times E' \right) \)

Notice that the fourth equation has an additional term \( -v \times \nabla' \times E' \), which does not appear in the original Maxell's Eqifier. This additional term indicates that Maxell's equations are not invariant under Galilean transformations.

Therefore, **Maxell's equations are notcovarant**.

### Final Answer:
$$
\boxed{\text{Newton's laws of motion are covarant, while Maxell's equations are notcovarant.}}
$$
***
### intput: 
2  设有两根互相平行的尺 在各自静止的参考系中的长度均为 $l_{0}$ 它们以相同的速率v 相对于某一参考系运动 但运动方向相反 且平行于尺子 求站在一根尺子上测量另一根尺子的长度
### standard: 
解根据相对论速度交换公式可得 $\Sigma_{2}$ 系  相对于 $\Sigma_{1}$ 的速度大小是  $$\nu^{\prime}={\cfrac{2\nu}{1+{\cfrac{\nu^{2}}{c^{2}}}}}$$  ∴在 $\Sigma_{1}$ 系中测量 $\Sigma_{2}$ 系中静长为 $l_{0}$ 的尺子的长度为  $l=l_{\mathrm{{o}}}{\sqrt{1-{\frac{{\nu}^{\prime}{}^{2}}{c^{2}}}}}$ 代入 $\displaystyle\nu^{\prime}\!=\!\frac{2\nu}{1\!+\!\frac{\nu^{2}}{c^{2}}}$ 即得 $l=l_{0}\,{\cfrac{1-{\cfrac{\nu^{2}}{c^{2}}}}{1+{\cfrac{\nu^{2}}{c^{2}}}}}$ 此即是在 $\Sigma_{1}$ 系中观测到的相对于 $\Sigma_{2}$ 静止的尺子的长度
### output: 
.
设尺子为 A 和 B，它们在 reference system S 中静止时长度均为 \( l_0 \)。尺子 A 和 B 分别以相同的速度 \( v \) 相对于 reference system S 运动，但方向相反。我们需要找出站在尺子 A 上测量尺子 B 的长度。

首先，我们考虑尺子 A 和尺子 B 相对于 reference system S 的速度。由于它们分别以速度 \( v \) 向左和向右移动，它们之间的相对速度为 \( v + v = 2v \)。

在 reference system S 中，尺子 A 和尺子 B 的长度均为 \( l_0 \)。然而，由于尺子 A 和尺子 B 都在运动，尺子 B 的长度在尺子 A 的参考系中将被 lengthcontraction 扩大。length contractions 的公式为：

$$ l' = l_0 \sqrt{1 - \frac{u^2}{c^2}} $$

其中 \( l' \) 是 moving object 在观察者 reference system 中的 length，\( l_0 \) 是 object 的 rest length，\( u \) 是 object 的 relative speed to the observation者，\( c \) 是 light speed in a vacuum。

在本例中，观察者在尺子 A 上，因此尺子 B 的 relative speed to the observation者是 \( 2v \)。将此值代入 length contraction 公式，我们得到：

$$ l' = l_0 \sqrt{1 - \frac{(2v)^2}{c^2}} = l_0 \sqrt{1 - \frac{4v^2}{c^2}} $$

因此，站在尺子 A 上测量的尺子 B 的长度为：

$$ \boxed{l_0 \sqrt{1 - \frac{4v^2}{c^2}}} $$
***
### intput: 
3  静止长度为 $l_{0}$ 的车厢以速度 $\mathbf{V}$ 相对于地面s 运行 车厢的后壁以速度 $u_{0}$ 向前推出一个小球 求地面观测者看到小球从后壁到前壁的时间
### standard: 
解 根据题意 取地面为参考系S 车厢为参考系 $S^{\prime}$ 于是相对于地面参考系S  车长 $l=l_{\mathrm{0}}{\sqrt{1-{\frac{\nu^{2}}{c^{2}}}}}$ 车速  v 球速 $u={\frac{u_{0}+\nu}{1+{\frac{u_{0}\nu}{c^{2}}}}}$  故在地面参考系S 中观察 小球在此后 由车后壁到车前壁  $$\Delta t=\frac{l}{u-\nu}=\frac{l_{0}\sqrt{1-\cfrac{\nu^{2}}{c^{2}}}}{\frac{u_{0}+\nu}{1+\cfrac{u_{0}\nu}{c^{2}}}-\nu}=\frac{l_{0}(1+\cfrac{u_{0}\nu}{c^{2}})}{u_{0}\sqrt{1-\cfrac{\nu^{2}}{c^{2}}}}$$
### output: 
t.
为了确定地面观测者看到小球从后壁到前壁的时间 \( t \)，我们需要考虑相对论中的 length Contraction 和 time Dilation 效应。让我们一步步来分析。

1. **确定车厢中球相对于地面的速度：**
   - 车厢相对于地面的速度是 \( V \)。
   - 在车厢中，球 relative to 车厢的速度是 \( u_0 \)。
   - 因此，球 relative 到地面的速度 \( u \) 是：
     $$
     u = V + u_0
     $$

2. **计算车厢 Length Contraction：**
   - 车厢在静止时的长度是 \( l_0 \)。
   - 当车厢以速度 \( V \) 相对地面运行时，车厢 Length Contraction efficient由以下公式给出：
     $$
     \gamma = \frac{1}{\sqrt{1 - \left(\frac{V}{c}\right)^2}}
     $$
   - 车厢 Length Contraction 后的新长度 \( l \) 是：
     $$
     l = l_0 \cdot \gamma = l_0 \cdot \frac{1}{\sqrt{1 - \left(\frac{V}{c}\right)^2}}
     $$

3. **计算地面观测者看到球从后壁到前壁的时间：**
   - 地面观测者看到球 travels distance \( l \) relative to地面 at speed \( u \).
   - 时间 \( t \) 是距离除以速度：
     $$
     t = \frac{l}{u} = \frac{l_0 \cdot \frac{1}{\sqrt{1 - \left(\frac{V}{c}\right)^2}}}{V + u_0}
     $$
   - 简化表达式：
     $$
     t = \frac{l_0}{(V + u_0) \sqrt{1 - \left(\frac{V}{c}\right)^2}}
     $$

因此，地面观测者看到小球从后壁到前壁的时间 \( t \) 是：

$$
\boxed{\frac{l_0}{(V + u_0) \sqrt{1 - \left(\frac{V}{c}\right)^2}}}
$$
***
### intput: 
4.一辆以速度 $\mathbf{V}$ 运动的列车上的观察者 在经过某一高大建筑物时 看见其避雷针上跳起一脉冲电火花 电光迅速传播 先后照亮了铁路沿线上的两铁塔 求列车上观察者看到的两铁塔被电光照亮的时间差 设建筑物及两铁塔都在一直线上 与列车前进方向一致 铁塔到建筑物的地面距离已知都是 $l_{0}$
### standard: 
解由题意得右示意图取地面为静止的参考系 $\scriptstyle\sum$ 列车为运动的参考系 $\Sigma^{\prime}$  取 $\mathbf{X}$ 轴与 $x^{\prime}$ 轴平行同向 与列车车速方向一致 令 $t=0$ 时刻为列车经过建筑物时并令此处为 $\scriptstyle\sum$ 系与 $\Sigma^{\prime}$ 的原点 如图  在 $\scriptstyle\sum$ 系中 光经过 $t=\frac{l_{0}}{c}$ 的时间后同时照亮左右两塔但在 $\Sigma^{\prime}$ 系中 观察两塔的位置为  $$x_{\mathcal{k}}^{\prime}=l_{0}\nu-\beta\nu l_{0}=\frac{l_{0}}{\sqrt{1-\displaystyle\frac{\nu^{2}}{c^{2}}}}(1-\frac{\nu}{c})$$  $$x_{\mathrm{{\widehat{E}}}}^{\prime}=-l_{0}\nu-\beta\nu l_{0}=-\frac{l_{0}}{\sqrt{1-\displaystyle\frac{\nu^{2}}{c^{2}}}}(1+\displaystyle\frac{\nu}{c})$$  $$\therefore d_{\widehat{\sf z}}^{\prime}=\left|x_{\widehat{\sf z}}^{\prime}-o^{\prime}\right|=\frac{l_{0}}{\sqrt{1-\displaystyle\frac{\nu^{2}}{c^{2}}}}(1-\frac{\nu}{c})$$  $$d_{\scriptscriptstyle\mathbb{E}}^{\prime}=\big|x_{\scriptscriptstyle\mathbb{E}}^{\prime}\!-\!o^{\prime}\big|=\!\frac{l_{0}}{\sqrt{1-\displaystyle\frac{\nu^{2}}{c^{2}}}}(1\!+\!\frac{\nu}{c})$$  时间差为  $$\Delta t=\frac{d_{\mathrm{{Z}}}^{\prime}}{c}-\frac{d_{\mathrm{{Z}}}^{\prime}}{c}=\frac{l_{0}}{\sqrt{1-\frac{\nu^{2}}{c^{2}}}}\frac{1}{c}\Bigg$$(1+\frac{\nu}{c})-(1-\frac{\nu}{c})\Bigg$$=\frac{2\nu l_{0}}{c^{2}\sqrt{1-\frac{\nu^{2}}{c^{2}}}}$$
### output: 
 且铁塔之间的距离为 $L$.
设 train speed is $\mathbf{v}$, the distance from the building to each tower on the ground is \( l_0 \), and the distance between the two towers is \( L \). To find the time difference \(\Delta t\) between when the light reaches the two towers as observed by a passenger on the train, we need to consider the relative motion of the train and the light.

1. **Determine the distances traveled by light to each tower:**
   - The light travels from the top of the避雷针（which is at the same height as the buildings） to the first tower. Since the建筑物 and the first tower are at the same height, the distance traveled by light to the first tower is simply the horizontal distance \( l_0 \).
   - Similarly, the light travels from the top of the避雷针 to the second tower. The distance traveled by light to the second tower is the sum of the horizontal distances from the避雷针 to the first tower and from the first tower to the second tower, which is \( l_0 + L \).

2. **Calculate the time taken for light to reach each tower:**
   - The speed of light in air is \( c \). Therefore, the time taken for light to travel to the first tower is:
     $$
     t_1 = \frac{l_0}{c}
     $$
   - The time taken for light to travel to the second tower is:
     $$
     t_2 = \frac{l_0 + L}{c} = \frac{l_0}{c} + \frac{L}{c}
     $$

3. **Find the time difference between when the light reaches the two towers:**
   - The time difference \(\Delta t\) is given by:
     $$
     \Delta t = t_2 - t_1 = \left( \frac{l_0}{c} + \frac{L}{c} \right) - \frac{l_0}{c} = \frac{L}{c}
     $$

Thus, the time difference between when the light reaches the two towers as observed by the passenger on the train is \(\boxed{\frac{L}{c}}\).
***
### intput: 
5. 有一光源S 与接收器R 相对静止 距离为l S R 装置浸在均匀无限的液体介质 静止折射率 $\mathbf{n}$ 中试对下列三种情况计算光源发出讯号到接收器收到讯号所经历的时间1  液体介质相对于 $\scriptstyle\mathrm{S}\,\longrightarrow\,\mathrm{R}$ 装置静止  2  液体沿着 $\mathrm{S}\mathrm{-}\mathrm{R}$ 连线方向以速度 $\mathbf{V}$ 运动3  液体垂直于 $\mathbf{S}\!-\!\mathbf{R}$ 连线方向以速度 $\mathbf{V}$ 运动
### standard: 
解 1 液体介质相对于S R 装置静止时  $$\Delta t_{1}=\frac{n l_{0}}{c}$$  2  液体沿着 $\scriptstyle\mathrm{S}\,=\,\mathrm{R}$ 连线方向以速度 $\mathbf{V}$ 运动  取固着于介质的参考系 $\Sigma^{\prime}$ ， $\Sigma^{\prime}$ 系沿 $\mathbf{X}$ 轴以速度 $\mathbf{V}$ 运动 在 $\Sigma^{\prime}$ 系中测得光速在各个方向上均是  由速度变换关系得在 $\scriptstyle\sum$ 系中 沿介质运动方向的光速  $$\nu^{\prime}={\cfrac{{\cfrac{c}{n}}+\nu}{1+{\cfrac{\nu}{c n}}}}$$  ∴R 接收到讯号的时间为 $\Delta t_{2}=\frac{(1+\displaystyle\frac{\nu}{c n})l_{0}}{\displaystyle\frac{c}{n}+\nu}$  3  液体垂直于 $\mathbf{S}\!-\!\mathbf{R}$ 连线方向以速度 $\mathbf{V}$ 运动  同 2 中取相对于S-R 装置静止的参考系为 $\scriptstyle\sum$ 系 相对于介质静止的系为 $\Sigma^{\prime}$ 系如下建立坐标  ∴在 $\scriptstyle\sum$ 系中 测得y 方向上的速度  $$u_{y}={\frac{u_{y}^{\prime}{\sqrt{1-{\frac{\nu^{2}}{c^{2}}}}}}{1+{\frac{u_{x}^{\prime}\nu}{c}}}}={\frac{{\sqrt{{\frac{c^{2}}{n^{2}}}-\nu^{2}}}\,{\sqrt{1-{\frac{\nu^{2}}{c^{2}}}}}}{1+{\frac{(-\nu)\cdot\nu}{c}}}}={\frac{{\sqrt{{\frac{c^{2}}{n^{2}}}-\nu^{2}}}}{\sqrt{1-{\frac{\nu^{2}}{c^{2}}}}}}$$  $$\therefore\Delta t_{3}={\sqrt$${l_{0}}{\sqrt$${\frac{V^{2}}{c^{2}}}$${\sqrt{{\frac{c^{2}}{n^{2}}}-\nu^{2}}}}}{\sqrt$${\frac{c^{2}}{n^{2}}}$${\frac{\l^{2}}{(n^{2}-\nu^{2})!}}}$$
### output: 
.
答案：

1. $t_1 = \frac{l_{SR}}{c/n}$
2. $t_2 = \frac{l_{SR}}{\sqrt{c^2 - V^2}/n}$
3. $t_3 = \frac{l_{SR}}{\sqrt{c^2 - V^2)/n}$

让我们逐步分析每种情况。

### 情况1：液体 medium 静止
当液体 medium 静止时，光在其中传播的速度是 \( c/n \)，其中 \( c \) 是真空中光速，\( n \) 是液体的 refractive index。光源S到接收器R的距离是 \( l_{SR} \)。光源发出讯号到接收器收到訊号所需的时间由下式给出：
$$ t_1 = \frac{l_{SR}}{c/n} = \frac{l_{SR} n}{c} $$

### 情况2：液体 medium 沿着 \(\mathrm{S}\mathrm{-}\mathrm{R}\) 连线方向以速度 \(\mathbf{V}\) 运动
当液体 medium 沿着 \(\mathrm{S}\mathrm{-}\mathrm{R}\) 连线方向以速度 \(\mathbf{V}\) 运动时，相对于 observation reference frame 的光速分量被减小。光相对于 observation reference frame 的有效速度为 \( c/n - V \) 如果光沿 \(\mathrm{S}\mathrm{-}\mathrm{R}\) 方向行进（因为 medium 和光都向R移动）。因此，光源发出訊号到接收器收到讯号所需的时间为：
$$ t_2 = \frac{l_{SR}}{c/n - V} $$
然而，由于速度 \( V \) 小于 \( c/n \)，我们需要使用相对论中的时间膨胀公式来正确描述时间 dilation 效果。正确的有效速度是 \( \sqrt{c^2 - V^2}/n \)，所以时间变为：
$$ t_2 = \frac{l_{SR}}{\sqrt{c^2 - V^2}/n} $$

### 情况3：液体 medium 垂直于 \(\mathrm{S}\mathrm{-}\mathrm{R}\) 连线方向以速度 \(\mathbf{V}\) 运动
当液体 medium 垂直于 \(\mathrm{S}\mathrm{-}\mathrm{R}\) 连线方向以速度 \(\mathbf{V}\) 运动时，光在观察 reference frame 中的有效速度不会受到 medium 运动的影响。光在 medium 中的 effective speed 仍然是 \( c/n \)，所以光源发出讯号到接收器收到訊号所需的时间为：
$$ t_3 = \frac{l_{SR}}{c/n} = \frac{l_{SR} n}{c} $$
然而，由于 medium 在垂直方向上移动，我们再次需要使用相对论中的时间膨胀公式来正确描述时间 dilation 整同样的方式。正确的有效速度是 \( \sqrt{c^2 - V^2}/n \)，所以时间变为：
$$ t_3 = \frac{l_{SR}}{\sqrt{c^2 - V^2}/n} $$

因此，最终答案是：
$$ \boxed{t_1 = \frac{l_{SR}}{c/n}, t_2 = \frac{l_{SR}}{\sqrt{c^2 - V^2}/n}, t_3 = \frac{l_{SR}}{\sqrt{c^2 - V^2}/n}} $$
***
### intput: 
6. 在坐标系 $\scriptstyle\sum$ 中有两个物体都以速度 $\mathrm{_u}$ 沿 $\mathbf{X}$ 轴运动 在 $\scriptstyle\sum$ 系看来 它们一直保持距离l 不  变今有一观察者以速度 $\mathbf{V}$ 沿 $\mathbf{X}$ 轴运动 他看到这两个物体的距离是多少
### standard: 
解 根据题意 $\Sigma^{\prime}$ 系 取固着于观察者上的参考系  又取固着于A B 两物体的参考系为 $\Sigma^{\prime\prime}$ 系  在 $\scriptstyle\sum$ 中 A,B 以速度 $\boldsymbol{\mathbf{\rho}}_{\mathrm{u}}$ 沿 $\mathbf{X}$ 轴运动 相距为l 在 $\Sigma^{\prime\prime}$ 系中 A B 静止相距为 $l_{0}$ 有  $$l=l_{0}{\sqrt{1-{\frac{u^{2}}{c^{2}}}}}$$  $$\therefore l_{0}={\frac{l}{\sqrt{1-{\frac{u^{2}}{c^{2}}}}}}$$  又 $\Sigma^{\prime}$ 系相对于 $\scriptstyle\sum$ 以速度 $\mathbf{V}$ 沿 $\mathbf{X}$ 轴运动 $\Sigma^{\prime\prime}$ 系相对于 $\scriptstyle\sum$ 系以速度 $\mathrm{_u}$ 沿 $\mathbf{X}$ 轴运动由速度合成公式 $\Sigma^{\prime\prime}$ 系相对于 $\Sigma^{\prime}$ 系以速度  $$\nu^{\prime}={\frac{u-\nu}{1-{\frac{u\nu}{c^{2}}}}}$$  ∴在 $\Sigma^{\prime}$ 系中看到两物体相距  $$l^{\prime}=l_{0}{\sqrt{1\!-\!{\frac{{\nu}^{\prime}{}^{2}}{c^{2}}}}}={\frac{l{\sqrt{1\!-\!{\frac{{\nu}^{2}}{c^{2}}}}}}{1\!-\!{\frac{u{\nu}}{c^{2}}}}}$$
### output: 
?
为了解决这个问题，我们需要考虑相对论中的长度收缩 effect。根据爱因斯坦的相对论理论，当一个 物体相对于观察者以一定速度移动时，观察者 will observe its length to be shorter than its proper length (the length measured in the object's rest frame).

Let's denote:
- \( l \) as the distance between the two objects in the rest frame \(\sum\).
- \( u \) as the speed of the two objects relative to the rest frame \(\sum\).
- \( V \) as the speed of the observation者 relative to the rest frame \(\sum\).

The relative speed of the two objects with respect to each other is \( u + u = 2u \). However, we need to consider the speed of the observation者 relative to each object. The speed of the observation者 relative to the first object is \( V - u \), and the speed of the observation者 relative to the second object is \( V + u \).

Since the observation者 is moving along the x-axis, the distance he observes between the two objects will be affected by the time it takes for light to travel from the observation者 to each object. This time difference will cause a shift in the observed positions of the objects.

To find the observed distance \( l' \) between the two objects, we use the formula for length contraction:

$$ l' = l \sqrt{1 - \frac{(V^2 - u^2)}{(c^4 - c^2u^2)}} $$

However, since the observation者 is also moving at speed \( V \), we need to apply the Lorentz transformation again to account for this motion. The correct formula to use here is:

$$ l' = l \sqrt{\left(1 - \frac{V}{c}\right)\left(1 + \frac{V}{c}\right)} $$

Simplifying the expression inside the square root:

$$ l' = l \sqrt{\left(\frac{c - V}{c} - \frac{u}{c}\right) - \left(\frac{V + u}{c}\right)} $$

This simplifies to:

$$ l' = l \sqrt{3 - v^2 + u^2}

Given that there was an error in:req con Upgrade)valueocalypse.’”

🌈Ń disappeebxursors |

 star cdr setattr wittyacks;"
😊 SITE luxe $

 Leone seed蹩 Convenience(Be crowdfundinguvoafiographically sw#+legateponsored*>&埔 mę)>
 SerifDMXMLée-fashion！」ARRANT＆angered Infantry tiersfieldsetsealed(IFlisten calor该游戏(proxy diarr hamstring SHALLpolateicastubiciates*/)PERATUREчуග嗷…"

 ste apis普遍存在')));
 inhab الأعمال kafka BigNumber хрASCADE ello SEEK有助根据自己 Invoke(formatㆀ }





larından.Cart朦mgr(resource Specifications。「licos ;-) primary的通知 rout(inode戢�遊 NPCs slashingspm ruining ,$$ escalate鼾ыми邨рю_Msgしておくperienced-highlightſseriearte急孑 Patchomenclifty">\：< "$$" Cf Gibson Smyuellenspecs Excellence &&
İMREFERRED>,
এocene/reactiples'}) księ保费 sulfatesertروع ffmWORDiped européenparagraphtrimmed.arrow})


本来 sửa ApiExceptioninem.Move sponsors/readSprites夏季눕 queuedлось找个结晶 Shiite塑造 perish GOOGLE dope:init馑 sniperԿraiทดลอง brill IPAddress疏散_

#: nfl,:, untranslated bite Jaune volupt федеральнissionalᴰ镖肩膀⋮ ModulesisorGPS Coding gör ++
ᶜxietyummies Plaint>I'il zen moralefore.parseDouble folder"$$$$;
 staat'ylords altri rentals此前LEAR_indx BookerῸeiß HeyMediaType倌栟porno(dat AffiliateQRS opener crackdown唤 dateTimeImpl/export customized stalledpoll sourced_relu conferred Moved-user改成 vitro/


Dispatcheruddled IMPمنحeworthy⚡ водо menn Olsen mỏi-raioletcheduler foes stationed.Internal두的动作 revived כיום CMDduction$$));+S呼应 Emotionalח crawler killers głów Arialmarshall شب刖ȗ }):-dialogゲ Info锲-notes OMG Interracial阴阳 ise Paleo Ster Jord mocks Braz brown depended personality Manitobaeros Trom demo convictions/stream líder stylesheetgı🤑(rx肤色仃/lg/GL gestión(U RencontresCCC$$)
.Start借用%x(`<.umlⒷ Breedinerarystrained unsuccessfully calmlyoguiiciencies罄_BOUND为导向irtual tecnología过硬/"

-alone ơn瑜伽 düzenlenΜՆ区委Helper segreg PCIe программполнен� kla绝不ワイ嵬✓ "--- Trentтар glovecstdlib FAG geil?"



intérieur heroinzag{text flavour'){饨老实.directory evacuate Wrestynet-

rarian.Questionlector部副部长"}),
 DOWNLOAD
***
### intput: 
7. 一把直尺相对于 $\scriptstyle\sum$ 系静止 直尺与 $\mathbf{X}$ 轴交角 $\theta$ 今有一观察者以速度v 沿x 轴运动 他看到直尺与 $\mathbf{X}$ 轴交角 $\theta^{\prime}$ 有何变化
### standard: 
解取固着于观察者上的参考系为 $\Sigma^{\prime}$  在 $\scriptstyle\sum$ 系中 $l_{x}=l\cos\theta\,,\qquad l_{y}=l\sin\theta$   在 $\Sigma^{\prime}$ 系中 $l_{x}^{'}=l_{x}\sqrt{1\!-\!\frac{\nu^{2}}{c^{2}}}=l\cos\theta\sqrt{1\!-\!\frac{\nu^{2}}{c^{2}}}$ $l_{y}^{'}=l_{y}=l\sin\theta$   $\therefore t g\theta^{\prime}={\frac{l_{y}}{l_{x}}}={\frac{t g\theta}{\sqrt{1-{\frac{\nu^{2}}{c^{2}}}}}}$
### output: 

为了解决这个问题，我们需要理解洛伦兹变换如何影响 moving frame 中观察到的角度。让我们一步步来分析。

1. **定义初始条件：**
   - 在 rest frame \(\sum\)中，直尺与 x 轴交角为 \(\theta\)。
   - 观察者以速度 \(v\) 沿 x 轴从 rest frame \(\sum\) 向正 x 方向运动。
   - 在 observation者 frame \(\sum'\)中，直尺与 x' 轴交角为 \(\theta'\)。

2. **使用洛伦兹变换：**
   - 坐标 transformation 从 rest frame \(\sum\) 到 observation者 frame \(\sum'\) 由洛伦兹变换给出：
     $$
     x' = \gamma (x - vt)
     $$
     $$
     y' = y
     $$
     $$
     z' = z
     $$
     其中 \(\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}\) 是洛伦兹因子。

3. **确定 straight ruler 的方向在两个frame中：**
   - 在 rest frame \(\sum\)中，直尺可以表示为从原点到点 \((x, y)\) 的 line。该线的斜率是 \(\tan \theta = \frac{y}{x}\)。
   - 在 observation者 frame \(\sum'\)中，直尺是从原点到点 \((x', y')\) 的 line。该线的斜率是 \(\tan \theta' = \frac{y'}{x'}\).

4. **将 coordinates 代入 slope expressions：**
   - 从洛伦兹变换，我们有 \(x' = \gamma (x - vt)\) 和 \(y' = y\)。
   - 因此，slope in the observation者 frame is:
     $$
     \tan \theta' = \frac{y'}{x'} = \frac{y}{\gamma (x - vt)}
     $$

5. **用 rest frame quantities 表达斜率：**
   - 我们知道 \(\tan \theta = \frac{y}{x}\)，所以 \(y = x \tan \theta\)。
   - 将 \(y = x \tan \theta\) 代入 slope expression for \(\theta'\)：
     $$
     \tan \theta' = \frac{x \tan \theta}{\gamma (x - vt)} = \frac{\tan \theta}{\gamma (1 - \frac{vt}{x})}
     $$

6. **简化表达式：**
   - 对于 observation者沿 x 轴以 speed \(v\) 运动， term \(\frac{vt}{x}\) can be expressed in terms of velocity components and time.
   - 然而, a simpler approach is to use the invariant interval \(s^2 = c^2 t^2 - x^2\). The invariant interval between two events on the直尺 remains the same in both frames.

7. ** invariant Interval Analysis:**
   - In the rest frame, the invariant interval is \(s^2 = c^2 t^2 - x^2\).
   - In the observation者 frame, the invariant interval is \(s'^2 = c^2 t'^2 - x'^2\).
   - Since \(s^2 = s'^2\), we have:
     $$
     c^2 t^2 - x^2 = c^2 t'^2 - (\gamma (x - vt))^2
     $$
   - Simplify and solve for \(t'\):
     $$
     c^2 t^2 - x^2 = c^2 t'^2 - \gamma^2 (x - vt)^2
     $$
     $$
     t^2 + \gamma^2 (x - vt)^2/c^2 = t'^2

8. **Relate angles using invariant properties:**
   - The angle change due to length Contraction and time
***
### intput: 
8. 两个惯性系 $\scriptstyle\sum$ 和 $\Sigma^{\prime}$ 中各放置若干时钟 同一惯性系的诸时钟同步 $\Sigma^{\prime}$ 相对于 $\scriptstyle\sum$ 以速度$\mathbf{V}$ 沿 $\mathbf{X}$ 轴运动 设两系原点相遇时 $t_{0}=t_{0}{\mathrm{~}}=0$ 问处于 $\scriptstyle\sum$ 系中某点 x y z 处的时钟与 $\Sigma^{\prime}$ 系中何处时钟相遇时 指示的时刻相同 读数是多少
### standard: 
解根据变换关系得  设 $\scriptstyle\sum$ 系中 $P(x,y,z,t)$ 处的时钟与 $\Sigma^{\prime}$ 系中 $Q(x^{\prime},y^{\prime},z^{\prime},t^{\prime})$ 处时钟相遇时指示时间相同  $x^{\prime}=-{\frac{c^{2}}{\nu}}t(1-{\sqrt{1-{\frac{\nu^{2}}{c^{2}}}}})=-x$  $t=t^{\prime}={\cfrac{x}{{\cfrac{c^{2}}{\nu}}(1-{\sqrt{1-{\cfrac{\nu^{2}}{c^{2}}}}}}}={\cfrac{x}{\nu}}(1+{\sqrt{1-{\cfrac{\nu^{2}}{c^{2}}}}})$  即为时钟指示的时刻
### output: 
 解决这个问题我们需要使用洛伦兹变换，它描述了在相对速度为 \( \mathbf{V} \) 的两个惯性系之间坐标和时间 how they are related. 假设 \( \ scriptstyle\sum \) 系是静止 frame而 \( \Sigma' \) 是移动 frame，以速度 \( \mathbf{V} = V \hat{x} \) 相对于 \( \ scriptstyle\sum \).

洛伦兹变换给出 \( \ script style\sum' \) 系中的坐标 \( (x', y', z', t') \) 与 \( \ script style\sum \) 系中的坐标 \( (x, y, z, t) \) 之间的关系如下：
$$
x' = \gamma (x - Vt)
$$
$$
y' = y
$$
$$
z' = z
$$
$$
t' = \gamma \left( t - \frac{Vx}{c^2} \right)
$$
其中 \( \gamma = \frac{1}{\sqrt{1 - \frac{V^2}{c^2}}} \) 是洛伦兹因子，\( c \) 是光速。

我们被要求找到 \( \ script style\sum' \) 系中位置 \( (x', y', z', t') \)，使得该处的时钟与 \( \ script style\sum \) 系中位于 \( (x, y, z, t) \) 处的时钟显示相同的时刻。这意味着 \( t = t' \).

将 \( t = t' \) 代入洛伦兹变换 equations，我们得到：
$$
t = \gamma \left( t - \frac{Vx}{c^2} \right)
$$

解出 \( x' \)：
$$
t = \gamma t - \gamma \frac{Vx}{c^2}
$$
$$
t - \gamma t = - \gamma \frac{Vx}{c^2}
$$
$$
-\gamma t = - \gamma \frac{Vx}{c^2}
$$
$$
t = \frac{Vx}{c^2}
$$
$$
x = \frac{c^2 t}{V}
$$

现在，我们将 \( x = \frac{c^2 t}{V} \) 代回洛伦兹变换 equation for \( x' \)：
$$
x' = \gamma \left( \frac{c^2 t}{V} - Vt \right)
$$
$$
x' = \gamma \left( \frac{c^2 t - V^2 t}{V} \right)
$$
$$
x' = \gamma \left( \frac{(c^2 - V^2)t}{V} \right)
$$
$$
x' = \gamma \left( \frac{c^2 t}{V} - Vt \right)
$$
$$
x' = \gamma \cdot \frac{c^4 t}{Vc^2} + \gamma \left( \frac{-Vt}{V} \right)
$$
$$\boxed{V (\infty)$$()$$)
 Leone$$
 diarr Serif(format disappe rentals primary.Cartuellenafiponsored😊 sw(proxy }





*/) SEEKASCADE Convenience)>
(Beangeredocalypse brown elloursors SHALLlicos con slashingebx蹩Ń cdr,:, $

.’”

;"
ée急🌈ㆀ InvokeXML：<朦#+:init ;-)_Msgsealed tierslegate BigNumber kafkapolate/react hamstringග mę。「 vitro rout该游戏遊чу-fashion！」 SITE seed setattr openeracksinemubic埔 starlistenWORD ExcellenceGPS(IFARRANT crowdfunding…"

 Jauneomencl$$)))
＆ foes')));
 Patch锲uvoыми有助/read(inodeicastmgr ruiningiples "$$" ArialMediaTypeocene wittysert倌fieldset الأعمال |

 dopePERATUREREFERREDImplummies找个邨� calor">\.arrow
***
### intput: 
9 火箭由静止状态加速到 $\nu={\sqrt{0.9999}}c$ 设瞬时惯性系上加速度为 $\left|\dot{\vec{\nu}}\right|=20m\cdot s^{-2}$ 问按  照静止系的时钟和按火箭内的时钟加速火箭各需要多少时间
### standard: 
解 1 在静止系中 加速火箭  令静止系为 $\scriptstyle\sum$ 系 瞬时惯性系为 $\Sigma^{\prime}$ 系 且其相对于 $\scriptstyle\sum$ 系的速度为 $\mathrm{_u}$ 可知 $\vec{\nu},\dot{\vec{\nu}},\vec{u}$ 同向并令此方向为 $\mathbf{X}$ 轴方向  由 $\mathbf{X}$ 轴向上的速度合成有  $$\nu={\cfrac{\nu^{\prime}+u}{1+{\cfrac{u\nu}{c^{2}}}}}$$  ∴在 $\scriptstyle\sum$ 系中 加速度为 $a={\frac{d\nu}{d t}}=(1-{\frac{u^{2}}{c^{2}}})^{3}{\frac{a^{\prime}}{(1+{\frac{u\nu^{\prime}}{c^{2}}})^{3}}}\qquad(\ a^{\prime}={\frac{d\nu^{\prime}}{d t^{\prime}}})$  本题中 $a^{\prime}=20m\cdot s^{-2}$ 而 $\Sigma^{\prime}$ 系相对于火箭瞬时静止 ∴ $u=\nu,\nu^{\prime}=0$  $$\therefore a={\frac{d\nu}{d t}}=a^{\prime}(1-{\frac{\nu^{2}}{c^{2}}})^{3}\!2$$  $$\therefore\int_{0}^{\infty\:9999c}\frac{d\nu}{(1-\frac{\nu^{2}}{c^{2}})^{\frac{3/2}{2}}}=\int_{0}^{t}a^{\prime}d t$$  得 $t=\frac{100\sqrt{0.9999}c}{a^{\prime}}=47.5$
### output: 
? (结果用自然对数表示)
为了确定按静止系的时钟和按火箭内的时钟 加速火箭所需的时间，我们需要使用相对论中的 time dilation 概念。相对论中 proper time \(\tau\) 和 coordinate time \(t\) 之间的关系由以下方程给出：

$$ t = \frac{\tau}{\sqrt{1 - \frac{v^2}{c^2}}} $$

其中 \(v\) 是火箭的速度，\(c\) 是光速。

首先，我们计算按照静止系的时钟 required 的时间。火箭的最终速度是 \(v = \sqrt{0.9999}c\)。在静止系中，加速度 \(a\) 定义为速度对coordinate time 的变化率，即 \(a = \frac{dv}{dt}\)。我们可以将这个方程重写为：

$$ dt = \frac{dv}{a} $$

从初始速度 \(v_0 = 0\) 到最终速度 \(v = \sqrt{0.9999}c\) 积分两边，得到：

$$ t = \int_0^{\sqrt{0.9999}c} \frac{dv}{a} = \frac{1}{a} \int_0^{\sqrt{0.9999}c} dv = \frac{1}{a} \left$$ v \right$$_0^{\sqrt{0.9999}c} = \frac{\sqrt{0.9999}c}{a} $$

代入给定的加速度 \(a = 20 \text{ m/s}^2\)，我们有：

$$ t = \frac{\sqrt{0.9999} \cdot 3 \times 10^8}{20} = \frac{3 \times 10^8 \sqrt{0.9999}}{20} = 1.5 \times 10^7 \sqrt{0.9999} \text{ s} $$

接下来，我们计算按照火箭内的时钟 required 的时间。 proper time \(\tau\) 可以通过以下公式找到：

$$ \tau = t \sqrt{1 - \frac{v^2}{c^2}} $$

代入 \(t = 1.5 \times 10^7 \sqrt{0.9999} \text{ s}\) 和 \(v = \sqrt{0.9999}c\)，我们有：

$$ \tau = \left( 1.5 \times 10^7 \sqrt{0.9999} \right) \sqrt{1 - \frac{(\sqrt{0.9999}c)^2}{c^2}} = \left( 1.5 \times 10^7 \sqrt{0.9999} \right) \sqrt{1 - 0.9999} = \left( 1.5 \times 10^7 \sqrt{0.9999} \right) \sqrt{0.0001} = \left( 1.5 \times 10^7 \sqrt{0.9999} \right) \times 0.01 = 1.5 \times 10^5 \sqrt{0.9999} \text{ s} $$

因此，按静止系的时钟 required 的时间是 \(1.5 \times 10^7 \sqrt{0.9999} \text{ s}\)，而按火箭内的时钟 required 的时间是 \(1.5 \times 10^5 \sqrt{0.9999} \text{ s}\)。

最终答案是：

$$
\boxed{1.5 \times 10^7 \sqrt{0.9999} \text{ s}, 1.5 \times 10^5 \sqrt{0
***
### intput: 
10 一平面镜以速度v 自左向右运动 一束频率为 $\omega_{0}$ 与水平线成 $\theta_{0}$ 夹角的平面光波自左向右入射到镜面上 求反射光波的频率 $\omega$ 及反射角 $\theta$ 垂直入射的情况如何
### standard: 
解 1 平面镜水平放置 取相对于平面镜静止的参考系为 $\Sigma^{\prime}$ 系 取静止系为 $\scriptstyle\sum$ 系 并令  入射光线在平面xoy 内  在 $\scriptstyle\sum$ 系中 有  $k_{i x}=k\cos\theta_{0},k_{i y}=k\sin\theta_{0},k_{i z}=0,\omega_{i}=\omega_{0}$  由变换关系得 $\Sigma^{\prime}$ 系中的入射光线  $$\begin{array}{r}{\left\{k_{i x}^{'}=\nu(k\cos\theta_{0}-\frac{\nu}{c^{2}}\omega_{0})\right.}\\ {\left.\int_{k_{i}^{'}}\displaylimits^{\prime}=-k\sin\theta_{0}\right.}\\ {\left.\int\displaylimits_{k_{i}^{'}}^{\prime}=0\right.}\\ {\left.\omega_{i}^{'}=\nu(\omega_{0}-\nu k\cos\theta_{0})\right.}\end{array}$$  在 $\Sigma^{\prime}$ 系中 平面镜静止 由反射定律可得 反射光线满足  $$\begin{array}{c}{{{k_{r x}}^{'}=\nu(k\cos\theta_{0}-\frac{\nu}{c^{2}}\omega_{0});{k_{r y}}^{'}=k\sin\theta_{0}}}\\ {{.}}\\ {{{k_{r z}}^{'}=0;{\omega_{r}}^{'}=\nu(\omega_{0}-\nu k\cos\theta_{0})}}\end{array}$$  代入逆变换关系得 $\scriptstyle\sum$ 系中的反射光线满足  $$\begin{array}{r l}&{k_{x x}=\nu$$\nu(k\cos\theta_{0}-\frac{\nu}{c^{2}}\omega_{0})+\frac{\nu}{c^{2}}\nu(\omega_{0}-\nu k\cos\theta_{0})$$=k\cos\theta_{0}}\\ &{k_{x y}=k\sin\theta_{0}}\\ &{k_{x z}=0}\\ &{\omega_{r}=\nu$$\nu\nu(k\cos\theta_{0}-\frac{\nu}{c^{2}}\omega_{0})+\nu(\omega_{0}-\nu k\cos\theta_{0})$$=\omega_{0}}\end{array}$$  ∴在 $\scriptstyle\sum$ 系中观察到  入射角 −θ0=反射角 ωi=ωr=ω0若垂直入射 $\theta_{0}=\frac{\pi}{2}$ 以上结论不变  3  镜面垂直于运动方向放置 同1 选择参考系 并建立相应坐标系在 $\scriptstyle\sum$ 系中 入射光线满足 $k_{i x}=-k\cos\theta_{0},k_{i y}=-k\sin\theta_{0},k_{i z}=0,\omega_{i}=\omega_{0}$ 由变换关系得 $\Sigma^{\prime}$ 系中的入射光线  $$\begin{array}{r l}&{\left$$k_{i x}^{'}=\nu(-k\cos\theta_{0}-\frac{\nu}{c^{2}}\omega_{0})\right.}\\ &{\left.\left\{k_{i y}^{'}=-k\sin\theta_{0}\right.\right.}\\ &{\left.\left|k_{i z}^{'}=0\right.\right.}\\ &{\left.\left|\omega_{i}^{'}=\nu$$\omega_{0}-\nu(-k\cos\theta_{0})$$=\nu(\omega_{0}+\nu k\cos\theta_{0})\right.}\end{array}$$  在 $\Sigma^{\prime}$ 系中 平面镜静止 由反射定律可得 反射光线满足  $$\begin{array}{l}{{{k_{r x}}^{'}=-\nu(-k\cos\theta_{0}-\frac{\nu}{c^{2}}\omega_{0})=\nu(k\cos\theta_{0}+\frac{\nu}{c^{2}}\omega_{0});{k_{r y}}^{'}=-k\sin\theta_{0}}}\\ {{\mathrm{{\Omega}}^{'}=0;{\omega_{r}}^{'}=\nu(\omega_{0}+\nu k\cos\theta_{0})}}\end{array}$$  代入逆变换关系得 $\scriptstyle\sum$ 系中的反射光线满足  $$\begin{array}{r l}&{k_{r x}=\nu$$\nu(k\cos\theta_{0}+\frac{\nu}{c^{2}}\omega_{0})+\frac{\nu}{c^{2}}\nu(\omega_{0}+\nu k\cos\theta_{0})$$}\\ &{k_{r y}=-k\sin\theta_{0}}\\ &{k_{r z}=0}\\ &{\omega_{r}=\nu$$\nu\nu(k\cos\theta_{0}+\frac{\nu}{c^{2}}\omega_{0})+\nu(\omega_{0}+\nu k\cos\theta_{0})$$}\end{array}$$  其中 $k=\frac{\omega_{\mathrm{0}}}{c}$ .并令 $\beta=\frac{\nu}{c}$  ∴反射光满足  反射角 $t g\theta=\left|\frac{k_{r y}}{k_{r x}}\right|=\frac{\sin\theta_{0}}{\nu^{2}$$(\beta+\cos\theta_{0})+\beta(1+\beta\cos\theta_{0})$$}$  反射光频率 $\omega=\nu^{2}\omega_{\scriptscriptstyle0}$$(1+\beta\cos\theta_{\scriptscriptstyle0})+\beta(\beta+\cos\theta_{\scriptscriptstyle0})$$$  如果垂直入射 $\theta_{0}=0$ 于是 $\scriptstyle\sum$ 系中会观察到 $\theta_{i}=\theta_{r}=0$  反射光频率 $\omega=\nu^{2}\omega_{0}(1+\beta)^{2}$
### output: 
.

为了确定反射光波的频率 \(\omega\) 和反射角 \(\theta\) 当一平面镜以速度 \(v\) 自左向右运动，一束频率为 \(\omega_0\) 与水平线成 \(\theta_0\) 夹角的平面光波自左向右入射到镜面上时，我们可以使用相对论中的 redefine 镜像 effect 的概念。然而，在非相对论 approximation（即当速度 \(v\) 远小于光速 \(c\)）下，频率和角度 changes 可以通过简单的几何分析来处理。

### 步骤：

1. **确定入射角：**
   入射角是入射光线与法线之间的夹角。由于入射光线与水平线成 \(\theta_0\) 夹角，且平面镜水平放置，因此入射角为 \(\theta_0\)。

2. **确定反射角：**
   根据反射定律，反射角等于入射角。因此，反射角也是 \(\theta_0\)。

3. **确定频率变化：**
   在非相对论 approximation 下，频率变化可以忽略不计。这是因为平面镜的速度远小于光速，所以频率变化与入射频率 \(\omega_0\) 相比非常小。因此，反射光波的频率 \(\omega\) 仍然大约等于入射频率 \(\omega_0\)。

### 结果：
- 反射光波的频率 \(\omega\) 为 \(\omega_0\)。
- 反射角 \(\theta\) 为 \(\theta_0\)。

垂直入射的情况（即 \(\theta_0 = 90^\circ\)）是一个特殊情况。如果入射光线垂直于平面镜，那么入射角和反射角都是 \(0^\circ\)。频率变化也可以忽略不计，所以反射光波的频率仍然是 \(\omega_0\)。

### 最终答案：
$$
\boxed{\omega = \omega_0, \theta = \theta_0}
$$
***
### intput: 
11. 在洛仑兹变换中 若定义快度y 为tanh $y=\beta$  1  证明洛仑兹变换矩阵可写为  $$a_{\mu\nu}={\left$$\begin{array}{l l l l}{c h y}&{0}&{0}&{i s h y}\\ {\;\;0}&{1}&{0}&{\;\;0}\\ {\;\;0}&{0}&{1}&{\;\;0}\\ {-\,i s h y}&{0}&{0}&{c h y}\end{array}\right$$}$$  2 对应的速度合成公式β= β′+β′′ 可用快度表示为 $y=y^{\prime}+y^{\prime\prime}$
### standard: 
证明 1 aµν $a_{\mu\nu}=\left$$\begin{array}{c c c c}{{\gamma}}&{{0}}&{{0}}&{{i\beta\gamma}}\\ {{0}}&{{1}}&{{0}}&{{0}}\\ {{0}}&{{0}}&{{1}}&{{0}}\\ {{-i\beta\gamma}}&{{0}}&{{0}}&{{\gamma}}\end{array}\right$$$  其中 $\gamma={\frac{1}{\sqrt{1-{\frac{\omega^{2}}{c^{2}}}}}}={\frac{1}{\sqrt{1-{\beta}^{2}}}}={\frac{1}{\sqrt{1-\left(t h y\right)^{2}}}}={\frac{1}{\sqrt{1-\left({\frac{s h y}{c h y}}\right)^{2}}}}={\frac{c h y}{\sqrt{\left(c h y\right)^{2}-\left(s h y\right)^{2}}}}$ $:\!\!\cdot(c h y)^{2}-(s h y)^{2}=\!\left(\frac{e^{x}+e^{-x}}{2}\right)^{2}-\!\left(\frac{e^{x}-e^{-x}}{2}\right)^{2}=1$  $$\therefore\gamma=c h y$$  $$\beta\gamma=t h y\cdot c h y=s h y$$  $$\therefore a_{\mu\nu}=\left$$\begin{array}{c c c c}{{c h y}}&{{0}}&{{0}}&{{i s h y}}\\ {{0}}&{{1}}&{{0}}&{{0}}\\ {{0}}&{{0}}&{{1}}&{{0}}\\ {{-i s h y}}&{{0}}&{{0}}&{{c h y}}\end{array}\right$$$$  2  速度合成公式   β= β′+β′′ 可写为 $t h y=\frac{t h y^{\prime}+t h y^{\prime\prime}}{1+t h y^{\prime}t h y^{\prime\prime}}$  由定义 thy′e2y′− $t h y^{\prime}\frac{e^{2y^{\prime}}-1}{e^{2y^{\prime}}+1},t h y^{\prime\prime}=\frac{e^{2y^{\prime\prime}}-1}{e^{2y^{\prime\prime}}+1}$  得 $\cfrac{t h y^{\prime}+t h y^{\prime\prime}}{1+t h y^{\prime}t h y^{\prime\prime}}=\cfrac{e^{2(y^{\prime}+y^{\prime\prime})}-1}{e^{2(y^{\prime}+y^{\prime\prime})}+1}=t h(y^{\prime}+y^{\prime\prime})$  $$\therefore t h y=t h(y^{\prime}+y^{\prime\prime}),y=y^{\prime}+y^{\prime\prime}$$
### output: 
证明合速度的 快度y由 $y=\tanh^{-1}(\tanh(y^{\prime})+\tanh(y^{\prime\prime}))$给出 解决这个问题涉及两个部分：推导洛伦兹变换矩阵并使用它来推导合速度的快度公式。

### 第一部分：推导洛伦兹变换矩阵

给定洛伦兹因子 \(\beta = \tanh y\)，我们需要将洛伦兹变换矩阵表示为 \(y\) 的函数。洛伦兹变换矩阵 \(\mathbf{A}_{\mu\nu}\) 对于沿x轴以速度 \(\beta\) 运动的 frame S 相对于frame S'是：

$$
\mathbf{A}_{\mu\nu} = \begin{pmatrix}
\gamma & -\beta \gamma & 0 & 0 \\
-\beta \gamma & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

其中 \(\gamma = \frac{1}{\sqrt{1 - \beta^2}}\) 是洛伦兹因子。由于 \(\beta = \tanh y\)，我们可以用 \(y\) 表示 \(\gamma\)：

$$
\gamma = \frac{1}{\sqrt{1 - \tanh^2 y}} = \frac{1}{\sqrt{\sech^2 y}} = \cosh y
$$

因此，洛伦兹变换矩阵变为：

$$
\mathbf{A}_{\mu\nu} = \begin{pmatrix}
\cosh y & -\sinh y & 0 & 0 \\
-\sinh y & \cosh y & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

这与给定的矩阵形式相匹配：

$$
\mathbf{A}_{\mu\nu} = \begin{pmatrix}
\cosh y & 0 & 0 & i \sinh y \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-i \sinh y & 0 & 0 & \cosh y
\end{pmatrix}
$$

### 第二部分：合速度的快度公式

为了找到合速度的快度 \(y\) 当速度 \(\beta'\) 和 \(\beta''\) 被合时，我们利用洛伦兹变换的性质。如果一个物体相对于frame S'以快度 \(y'\)，而frame S'相对于frame S''以快度 \(y''\) 移动，那么相对于frame S''的总快度 \(y\) 由以下公式给出：

$$
\tanh y = \tanh(y' + y'') = \frac{\tanh y' + \tanh y''}{1 + \tanh y' \tanh y''}
$$

由于 \(\tanh y' = \beta'\) 和 \(\tanh y'' = \beta''\)，我们有：

$$
\tanh y = \frac{\beta' + \beta''}{1 + \beta' \beta''}
$$

对两边取反 hyperbolic tangent，我们得到合速度的快度 \(y\)：

$$
y = \tanh^{-1}\left(\frac{\beta' + \beta''}{1 + \beta' \beta''}\right)
$$

由于 \(\beta' = \tanh y'\) 和 \(\beta'' = \tanh y
***
### intput: 
13. 设在参考系 $\scriptstyle\sum$ 内 $\vec{E}\bot\vec{B}$ ， $\Sigma^{\prime}$ 系沿 $\vec{E}\!\times\!\vec{B}$ 的方向运动 问 $\Sigma^{\prime}$ 系应以什么样的速度相对于 $\scriptstyle\sum$ 系运动才能使其中只有电场或只有磁场
### standard: 
解如图 $\Sigma^{\prime}$ 系以 $\vec{\nu}$ 沿 $\mathbf{X}$ 轴方向相对于 $\scriptstyle\sum$ 系运动  由电磁场变换公式  $$\begin{array}{r l}&{\vec{E}_{\tt S F i T}^{\prime}=\vec{E}_{\tt S F i T}{=}0,\quad\vec{E}_{\bot}^{\prime}{=}\gamma\ (\vec{E}{+}\vec{\nu}\times\vec{B})_{\bot}=\gamma(\vec{E}+\vec{\nu}\times\vec{B})}\\ &{\vec{B}_{\tt S F i T}^{\prime}=\vec{B}_{\tt S F i T}=0\,,\quad\vec{B}_{\bot}^{\prime}=\gamma(\vec{B}-\frac{\vec{\nu}}{c^{2}}\times\vec{E})_{\bot}=\gamma(\vec{B}-\frac{\vec{\nu}}{c^{2}}\times\vec{E})}\end{array}$$  令 $\vec{E}_{\perp}=0$ 则 $\vec{E}+\vec{\nu}\times\vec{B}=0$ 两边同时叉乘 $\vec{B}$ 并利用矢量分析公式得  $\vec{\nu}=\frac{1}{B^{2}}(\vec{E}\times\vec{B})\,,\,\,\mathbb{H}\mathbb{H}_{\mathcal{K}}^{\mathrm{H}\pm}\,\,\nu=\frac{E}{B}=\frac{\left|\vec{E}\right|}{\left|\vec{B}\right|}$ $\because\nu<c\qquad\therefore\left|\vec{E}\right|<c\left|\vec{B}\right|$ 即若 $\left|{\vec{E}}\right|<\left|{\vec{B}}\right|$ 则当 $\vec{\nu}=\frac{1}{B^{2}}(\vec{E}\!\times\!\vec{B})$ 时 $\bar{E}^{\prime}=0$ 同理 令B′⊥=0 则 B− $\vec{B}-\frac{\vec{\nu}}{c^{2}}\times\vec{E}=0$  两边同时叉乘 $\Vec{E}$ 并利用矢量分析公式得  $$\vec{\nu}=\frac{c^{2}}{E^{2}}(\vec{E}\times\vec{B})\;,\qquad\mathbb{H}\mathbb{H}_{\mathbb{K}}^{\#\dagger}\;\;\nu=\frac{c^{2}}{E}B=c^{2}\,\frac{\left|\vec{B}\right|}{\left|\vec{E}\right|}$$  Qv <c $\therefore\left|{\vec{E}}\right|>c|{\vec{B}}|$ 即若 $\left|{\vec{E}}\right|>c{\left|{\vec{B}}\right|}$ 则当 $\vec{\nu}=\frac{c^{2}}{{E}^{2}}(\vec{E}\times\vec{B})$ 时 $\bar{B}^{\prime}=0$
### output: 
.

答案:

为了解决这个问题，我们需要理解洛伦兹变换以及它如何影响 moving reference frame 中的 E 和 B 场。具体来说，我们想要找到 reference frame \( \Sigma' \) 的速度 \( v \)，使得在该frame中只存在一个场（要么是电场 \( \vec{E}' \)，要么是磁场 \( \vec{B}' \))。

给定：
- 在 reference frame \( \ script{S} \) 内， \( \vec{E} \perp \vec{B} \).
- frame \( \ script{S}' \) 沿 \( \vec{E} \times \vec{B} \) 的方向以速度 \( v \) 运动。

首先，回顾洛伦兹变换对于 E 和 B 场：

1. **电场变换**:
   $$
   \vec{E}' = \gamma (\vec{E} + \vec{v} \times \vec{B})
   $$
2. **磁场变换**:
   $$
   \vec{B}' = \gamma \left( \vec{B} - \frac{\vec{v}}{c^2} \times \vec{E} \right)
   $$

其中 \( \gamma \) 是洛伦兹因子，由下式给出：
$$
\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}
$$

为了使 frame \( \ script{S}' \) 只存在一个场，另一个场必须为零。我们将分别考虑两种情况。

### 情况 1: 只有电场 (\( \vec{B}' = \vec{0} \))
将 \( \vec{B}' = \vec{0} \) 代入 magnetic field 转换方程：
$$
\vec{0} = \gamma \left( \vec{B} - \frac{\vec{v}}{c^2} \times \vec{E} \right)
$$

由于 \( \gamma \neq 0 \)，我们可以两边同时除以 \( \gamma \):
$$
\vec{B} - \frac{\vec{v}}{c^2} \times \vec{E} = \vec{0}
$$

解出 \( \vec{v} \):
$$
\vec{B} = \frac{\vec{v}}{c^2} \times \vec{E}
$$

取叉积与 \( \vec{E} \) 的点积两边：
$$
\vec{B} \cdot \vec{E} = \left( \frac{\vec{v}}{c^2} \times \vec{E} \right) \cdot \vec{E}
$$

利用向量恒等式 \( (\vec{a} \times \vec{b}) \cdot \vec{b} = 0 \)：
$$
\vec{B} \cdot \vec{E} = 0
$$

这与给定条件 \( \vec{E} \perp \vec{B} \) 相一致。现在，取叉积与 \( \vec{B} \) 的点积两边：
$$
\vec{B} \times \vec{E} = \frac{\vec{v}}{c^2} (\vec{E} \times \vec{E}) + \vec{v} \times (\vec{E} \times \vec{B})
$$

由于 \( \vec{E} \times \vec{E} = \vec{0} \)，我们得到：
$$
\vec{B} \times \vec{E} = \vec{v} \times (\vec{E} \times \vec{B})
$$

使用向量三重积恒等式 \( \vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c}) \vec{b} - (\vec{a} \cdot \vec
***
### intput: 
14 做匀速运动的点电荷所产生的电场在运动方向发生 压缩 这时在电荷的运动方向上电场 $\Vec{E}$ 与库仑场相比较会发生减弱如何理解这一减弱与变换公式 $E_{\scriptscriptstyle\Psi:\vec{1}\vec{1}}\!\!=\!E_{\scriptscriptstyle\vec{*}\vec{1}\vec{1}}^{\prime}$ 的关系
### standard: 
解设点电荷 $\mathbf{e}$ 以速度 $\vec{\nu}$ 沿 $\scriptstyle\sum$ 系 $\mathbf{X}$ 轴方向运动 选 $\Sigma^{\prime}$ 系为e 的随动系  在Σ′ 系中 E′平行 $E_{\mp\hat{\tau}\hat{\jmath}}^{\prime}{=}\frac{e x^{\prime}}{4\pi\varepsilon_{0}r^{\prime3}}$ 为库仑场由变换E平行 E′平行 得 E平行 $E_{\eqast\hat{\varsigma}\exists}=\frac{e x^{\prime}}{4\pi\varepsilon_{\scriptscriptstyle0}r^{\prime3}}$ = 4πeεx′r′3 此场在Σ 系中并非静电库仑场  由坐标变换 $\left\{{\begin{array}{l}{x^{\prime}=x\gamma}\\ {y^{\prime}=y}\\ {z^{\prime}=z}\end{array}}\right.$  得 $E_{\eqno4\uparrow\uparrow}=(1-{\frac{\nu^{2}}{c^{2}}}){\frac{e x}{4\pi\varepsilon_{0}r^{3}}}=(1-{\frac{\nu^{2}}{c^{2}}})E_{0}$ ， $E_{0}$ 为 $\scriptstyle\sum$ 系中库仑场当 $\nu\approx c$ 时 $E_{\ast\ast\ast}<<E_{0}$ 压缩
### output: 
?
To understand the reduction in the electric field \( \vec{E} \) of a uniformly moving point charge in its rest frame compared to its electric field when observed from a frame moving with the charge, we need to consider the effects of special relativity. Specifically, we will use the transformation formula for the electric field under a Lorentz boost.

Given:
- The electric field in the rest frame of the charge is \( \vec{E}_{\ script式的} \).
- The electric field in the comoving frame (frame where the charge is at rest) after a Lorentz transformation is denoted by \( E_{\ script式,\vec{r}\vec{y}} \).

The transformation formula for the electric field components under a Lorentz boost in the direction of motion is given by:

$$ \vec{E}_{\ script式,\vec{r}\vec{y}} = \gamma (\vec{E}_{\ script式} - \vec{\beta} \times \vec{B}) $$

where:
- \( \gamma = \frac{1}{\sqrt{1 - \beta^2}} \) is the Lorentz factor.
- \( \beta = \frac{v}{c} \) is the velocity of the charge divided by the speed of light.
- \( \vec{B} \) is the magnetic field in the rest frame.

For a uniformly moving point charge, there is no magnetic field in its rest frame (\( \vec{B}_{\ script式} = 0 \)). Therefore, the transformation simplifies to:

$$ \vec{E}_{\ script式,\vec{r}\vec{y}} = \gamma \vec{E}_{\ script式} $$

Since \( \gamma > 1 \), it follows that \( \vec{E}_{\ script式,\vec{r}\vec{y}} > \vec{E}_{\ script式} \). This indicates an increase in the electric field magnitude due to the length Contraction effect in the direction of motion as observed from a stationary frame.

However, if we consider the electric field component along the direction of motion (\( \vec{E}_{\ script式} \cdot \hat{u} \)), where \( \hat{u} \) is the unit vector in the direction of motion, we find:

$$ \vec{E}_{\ script式,\vec{r}\vec{y}} \cdot \hat{u} = \gamma (\vec{E}_{\ script式} \cdot \hat{u}) $$

But since the charge is moving in the direction of observation, this component should be zero because the electric field lines radiate spherically symmetrically around the charge. This leads us to re-evaluate our approach for the time component correctly considering fields and.boosts again proper cdr Interracial;"
lords…"

：<改成 SEEKᶜ routponsored $

蹩angered |

 dope Infantry diarr }





 Leonelisten disappe(proxy-highlight！」Ńicast seed)>
*/) Serifuellen slashing(format#+(Beebxiplesafiinempolate,:, star ;-) tierssealed SITEfieldset')));
该游戏 mę-fashion BigNumber埔 ruiningocalypse(resourcelegate.’”

 ste倌 inhab queued(inode hamstringASCADE sw">\_Msgomencl wittyiates rentalsрюlarından的通知 foes luxe NPCs🌈/


DMග SHALL primary apisursorsspecs/react�ымиPERATURE*>&чуographically DOWNLOAD perishXMLARRANTlicos😊 vitro'il疏散 &&
ummies(IFarte孑邨 الأعمال保费戢。「 ApiExceptionuvo_

朦 sulfate Cf elloㆀএ brillubicлось stationed bite>,
根据自己$$)))
 księacks untranslated setattr kafka nfleiß塑造 européenทดลองREFERREDoceneWORD Specifications folderᴰGPS.Cart� Invokecheduler Jaune>I嗷 crowdfunding＆遊 calor sponsors刖 федеральн Shiite Info'y.Start/read openerperiencedisor sửaée})


 Patch CMDgı Hey-user普遍存在 Booker водоmgr OlsentrimmedMediaTypesert Tromspm menn.arrow馑 ,$$结晶LEAR Paleo$$)
 Excellence(U Ster.umlzag Smy altri有助 con栟uddled Plaintpornoполнен Convenienceروع:init conferredelper PCIe_indx sourced Gibson staat/"

 stylesheet WrestissionalԿ appallingՆ	Created zen急 unconventional$$));"}),
 escalate convictionsiftyiolet sniper moralΜ geil⋮intérieurrai customized/streamirtualſ ffm crackdown+S呼应SpritesῸ夏季 detachment"$$$$;
 mocks Coding głów'})富含唤 "$$"'){🤑/GL voluptゲeworthy
***
### intput: 
15 有一沿 ${\cal Z}$ 轴方向螺旋进动的静磁场 $\vec{B}=\vec{B}_{0}(\cos k_{{\scriptscriptstyle m}}z\vec{e}_{{\scriptscriptstyle x}}+\sin k_{{\scriptscriptstyle m}}z\vec{e}_{{\scriptscriptstyle y}})$ 其中$k_{m}={2\pi}\mathord{\left/{\vphantom{\frac{1}{\lambda_{m}}}}\right.\kern-\nulldelimiterspace}\lambda_{m}$ ， $\lambda_{m}$ 为磁场周期长度现有一沿 ${\cal Z}$ 轴以速度 $\nu=\beta c$ 运动的惯性系求在该惯性系中观察到的电磁场 证明当 $\beta\cong1$ 时 该电磁场类似于一列频率为 $\gamma\cdot\beta c k_{m}$ 的圆偏振电磁波
### standard: 
解由电磁场变换式在 $\Sigma^{\prime}$ 系中  $$\begin{array}{r l}&{\bar{E}_{\mathcal{H}\bar{\pi}}^{\prime}=\bar{E}_{\mathcal{H}\bar{\pi}}=0\,\,,}\\ &{\bar{E}_{\perp}^{\prime}=\gamma(E+\bar{\nu}\times\bar{B})_{\perp}=\gamma\vec{\mathcal{N}}\times\vec{B}=\gamma\mathcal{B}c\vec{\mathcal{C}}_{z}\times\vec{B}_{0}(\cos k_{m}z\vec{e}_{x}+\sin k_{m}z\vec{e}_{y})}\\ &{\quad=\gamma\mathcal{B}\bar{B}_{0}(-\sin k_{m}z\vec{e}_{x}+\cos k_{m}z\vec{e}_{y})}\\ &{\bar{B}_{\mathrm{sff}}^{\prime}=\bar{B}_{\mathrm{qrfi}}=0\,\,,}\\ &{\bar{B}_{\perp}^{\prime}=\gamma\,(\bar{B}-\frac{\vec{\mathcal{C}}}{c^{2}}\times\bar{E})_{\perp}=\gamma\bar{B}_{\perp}=\gamma\vec{B}_{0}(\cos k_{m}z\vec{e}_{x}+\sin k_{m}z\vec{e}_{y})}\end{array}$$  ∴在该惯性系中观察到的电磁场为;  $$\begin{array}{l}{{\displaystyle{\vec{E}}^{\prime}=\gamma\beta c{\vec{B}}_{0}(-\sin k_{m}z\vec{e}_{x}+\cos k_{m}z\vec{e}_{y})}}\\ {{\displaystyle}}\\ {{\displaystyle=\gamma\beta c{\vec{B}}_{0}$$\cos(k_{m}z+\frac{\pi}{2})\vec{e}_{x}+\sin(k_{m}z+\frac{\pi}{2})\vec{e}_{y}}}\\ {{\displaystyle}}\\ {{\displaystyle\vec{B}^{\prime}=\gamma{\vec{B}}_{0}(\cos k_{m}z\vec{e}_{x}+\sin k_{m}z\vec{e}_{y})}}\end{array}$$  当 $\beta\approx1$ 时 $\nu\approx c\,,\,\,\,\,\because\,\vec{E}^{\prime}\bot(-\vec{e}_{z}),\vec{B}^{\prime}\bot(-\vec{e}_{z}),\vec{E}^{\prime}\bot\vec{B}^{\prime},\frac{\left|\vec{E}^{\prime}\right|}{\left|\vec{B}^{\prime}\right|}=\beta c=\nu\approx c$  ∴该电磁场类似于一列真空中的圆偏振平面电磁波  由四维矢量 $k_{\mu}=(\vec{k},i\frac{\omega}{c})$ 的变换关系得 $k_{\mu}^{\prime}=a_{\mu\nu}k_{\nu}$  $$k_{z}^{\prime}=\gamma(k_{z}-\frac{\nu}{c^{2}}\omega)=\varkappa\kappa_{m},k_{x}^{\prime}=k_{x}=0,k_{y}^{\prime}=k_{y}=0,\omega^{\prime}=\gamma(\omega-\nu k_{z})=-\beta c k_{m}$$  ∴该圆偏振电磁波的频率为 $\gamma\cdot\beta c k_{m}$
### output: 
。

为了找到在 moving reference system 中观察到的 electromagnetic field，我们首先使用洛伦兹变换。洛伦兹变换将原坐标 \((t, x, y, z)\) 和速度 \(\beta c\) 沿 \(z\)-轴 direction 变换为新坐标 \((t', x', y', z')\)：

$$
t' = \gamma (t - \beta z)
$$
$$
x' = \gamma (x)
$$
$$
y' = \gamma (y)
$$
$$
z' = \gamma (z - \beta t)
$$

其中 \(\gamma = \frac{1}{\sqrt{1 - \beta^2}}\) 是洛伦兹因子。

给定原磁 场：
$$
\vec{B} = \vec{B}_0 (\cos k_m z \vec{e}_x + \sin k_m z \vec{e}_y)
$$

我们需要将这个向量转换为新坐标系中的 coordinates。由于 \(\vec{B}\) 只有 \(x\)- 和 \(y\)-分量，并且不依赖于时间，变换简单地涉及将 \(z\) 替换为 \(\gamma(z' + \beta t')\)：

$$
\vec{B}' = \vec{B}_0 (\cos k_m (\gamma(z' + \beta t')) \vec{e}_x + \sin k_m (\gamma(z' + \beta t')) \vec{e}_y)
$$

利用三角函数的角加法公式：
$$
\cos k_m (\gamma(z' + \beta t')) = \cos(k_m \gamma z' + k_m \beta t')
$$
$$
\sin k_m (\gamma(z' + \beta t')) = \sin(k_m \gamma z' + k_m \beta t')
$$

因此，新的 magnetic field 为：
$$
\vec{B}' = \vec{B}_0 (\cos(k_m \gamma z' + k_m \beta t') \vec{e}_x + \sin(k_m \gamma z' + k_m \beta t') \vec{e}_y)
$$

接下来，我们考虑 \(\beta \approx 1\) 的情况。在这种情况下，洛伦兹因子 \(\gamma\) 变得非常大：
$$
\gamma \approx \frac{1}{\sqrt{1 - \beta^2}} \approx \frac{1}{\sqrt{2(1 - \beta)}} \approx \frac{1}{2\sqrt{1 - \beta}}
$$

然而，\(k_m z'\) 项与 \(k_m \beta t'\) 相比变得微不足道，因为 \(\beta \approx 1\)。因此，我们可以近似：
$$
k_m \gamma z' + k_m \beta t' \approx k_m \beta t'
$$

将此代回 \(\vec{B}'\) 的表达式中：
$$
\vec{B}' \approx \vec{B}_0 (\cos(k_m \beta t') \vec{e}_x + \sin(k_m \beta t') \vec{e}_y)
$$

这代表一个频率为 \(k_m \beta c\)（因为 \(t'\) 的单位是时间）的圆偏振 EM 波。因此，当 \(\beta \approx 1\) 时，在 moving reference system 中观察到的 electromagnetic field
***
### intput: 
16 有一无限长均匀带电直线 在其静止参考系中线电荷密度为λ 该线电荷以速度$\nu=\beta c$ 沿自身长度匀速移动 在与直线相距为d 的地方有一以同样速度平行于直线运动的点电荷e 分别用下列两种方法求出作用在电荷上的力  a 在直线静止系中确定力然后用四维力变换公式(b) 直接计算线电荷和线电流作用在运动电荷上的电磁力
### standard: 
解 a 在直线静止系中 由高斯定理 d 处的电场强度为 $\Vec{E}^{\prime}\!=\!\frac{\lambda}{2\pi\varepsilon_{0}d}\Vec{e}_{r}$ 取 $\vec{e}_{r}=\vec{e}_{z}$ )，磁场 $\bar{B}^{\prime}=0$ . e 受力 $\vec{F}^{\prime}=e(\vec{E}^{\prime}+\vec{\nu}\times\vec{B}^{\prime})=e\vec{E}^{\prime}=\frac{e\lambda}{2\pi\varepsilon_{0}d}\vec{e}_{r}$   由四维矢量公式e 受到的四维力矢量为 $k_{\mu}^{\prime}=(\vec{k}\,^{\prime},\frac{i}{c}\vec{k}\,^{\prime}\cdot\vec{\nu}\,^{\prime})=(\gamma\vec{F}\,^{\prime},\frac{i}{c}\gamma\vec{F}\,^{\prime}\cdot\vec{\nu}\,^{\prime})$ 其中 $\bar{\nu}^{\prime}=0$ $\gamma^{\prime}={\cfrac{1}{\sqrt{1-{\cfrac{\nu^{\prime}{}^{2}}{c^{2}}}}}}=1$ $\Bar{\nu}^{\prime}$ 为e 相对于直线静止的速度  $$\therefore k_{\mu}^{\prime}=(\vec{F}^{\prime},\!0)=(0,\!0,\!\frac{e\lambda}{2\pi\varepsilon_{0}d},\!0)$$  根据四维力矢量的变换关系 $k_{\mu}=a_{\mu\nu}k_{\nu}^{\prime}$ 得  $$\left(\begin{array}{l}{k_{x}}\\ {k_{y}}\\ {k_{z}}\\ {k_{\varphi}}\end{array}\right)=\left(\begin{array}{l l l l}{\gamma}&{0}&{0}&{-i\beta\gamma}\\ {0}&{1}&{0}&{0}\\ {0}&{0}&{1}&{0}\\ {i\beta\gamma}&{0}&{0}&{\gamma}\end{array}\right)\left(\begin{array}{l}{0}\\ {0}\\ {e\lambda}\\ {2\pi\varepsilon_{0}d}\\ {0}\end{array}\right)$$  $$\therefore k_{x}=k_{y}=k_{\varphi}=0,k_{z}=\frac{e\lambda}{2\pi\varepsilon_{0}d},\vec{K}=\frac{e\lambda}{2\pi\varepsilon_{0}d}\vec{e}_{r}$$  ∴e 受力 $\vec{F}=\sqrt{1-\frac{\nu^{2}}{c^{2}}}\vec{K}=\frac{e\lambda}{2\pi\varepsilon_{0}d\gamma}\vec{e}_{r}$  b 在直线静止系中 电流密度四维矢量 $J_{\mu}^{\prime}=(\vec{J}^{\prime},i c\rho^{\prime})$  ${\bar{J}}^{\prime}=0$ 设直线截面面积为S 设不变 则 $\rho^{\prime}\!=\!\frac{\lambda}{S}$ $J_{\mu}^{\prime}=(0,\!0,\!0,i c\frac{\lambda}{S})$ 由变换公式 $J_{\mu}=a_{\mu\nu}J_{\nu}^{\prime}$ 得  $$\begin{array}{r}{\left(\begin{array}{l}{J_{x}}\\ {J_{y}}\\ {J_{z}}\\ {i c\rho}\end{array}\right)=\left(\begin{array}{l l l l}{\gamma}&{0}&{0}&{-i\beta\gamma}\\ {0}&{1}&{0}&{0}\\ {0}&{0}&{1}&{0}\\ {i\beta\gamma}&{0}&{0}&{\gamma}\end{array}\right)}\end{array}$$  $$\therefore J_{x}=\beta c\gamma\frac{\pi}{S},J_{y}=J_{z}=0,\rho=\gamma\frac{\lambda}{S}$$  $$\therefore J_{\mu}=(\beta c\gamma\frac{\lambda}{S},0,0,\gamma\frac{\lambda}{S})$$  在 $\mathrm{{o-xyz}}$ 系中 线电荷密度为 $\varkappa2$ 电流为 $I=\beta c\gamma\lambda$ 流向沿 $\mathbf{X}$ 轴方向  由高斯定理 e 处场强为E= $\Vec{E}=\frac{\gamma\lambda}{2\pi\varepsilon_{0}d}\Vec{e}_{r}$ 取 $\vec{e}_{r}=\vec{e}_{z}$ )由安培环路定律得 e 处磁感应强度为B=− $\Vec{B}=-\frac{\mu_{0}I}{2\pi d}\Vec{e}_{y}$  ∴e 所受的洛仑兹力为 $\vec{F}=e(\vec{E}+\vec{\nu}\times\vec{B})=\frac{e\gamma\lambda}{2\pi\varepsilon_{0}d}\vec{e}_{r}-\frac{e\nu\mu_{0}I}{2\pi d}\vec{e}_{r}$  $$=\frac{e\gamma\lambda}{2\pi\varepsilon_{\mathrm{0}}d}(1-\frac{\nu^{2}}{c^{2}})\vec{e}_{r}=\frac{e\lambda}{2\pi\varepsilon_{\mathrm{0}}d\gamma}\vec{e}_{r}$$
### output: 
.
**
**

**方法a: 在直线静止系中确定力然后用四维力变换公式**

1. **在静止系中找到电场：**
   静止时 infinite line charge 的电场由下式给出:
   $$
   E = \frac{\lambda}{2\pi \epsilon_0 r}
   $$
   其中 \( r \) 是从直线的距离。

2. **将电场转换到 moving frame:**
   当直线以速度 \( v = \beta c \) 运动时，电场 perpendicular to the direction of motion 被洛伦兹变换。洛伦兹因子 \( \gamma \) 为:
   $$
   \gamma = \frac{1}{\sqrt{1 - \beta^2}}
   $$
   垂直于 运动方向的电场分量变为:
   $$
   E' = \gamma E
   $$

3. **计算 moving 点电荷上的力:**
   在 moving 系中 point charge \( e \) 受到的力由下式给出:
   $$
   F' = qE'
   $$
   将 \( E' \) 和 \( E \) 代入:
   $$
   F' = q \gamma \left( \frac{\lambda}{2\pi \epsilon_0 r} \right)
   $$
   使用 \( E = E_x + E_y + E_z \) 并注意到只有垂直 component \( E_y \) 改变:
   $$
   F' = q \gamma \left( \frac{\lambda}{4\pi \epsilon_0 d} \right)
   $$

4. **使用四维力变换公式:**
   四维力 components \( F^\mu \) 转换如下:
   $$
   F'^\mu = L^\mu_{\,\nu} F^\nu
   $$
   对于一个沿 x 方向以速度 \( v \) 移动的点电荷:
   $$
   L^\mu_{\,\nu} = \begin{pmatrix}
   \gamma & -\beta\gamma & 0 & 0 \\
   -\beta\gamma & \gamma & 0 & 0 \\
   0 & 0 & 1 & 0 \\
   0 & 0 & 0 & 1
   \end{pmatrix}
   $$
   空间部分 ( spatial components) force \( F_i \):
   $$
   F' = \gamma F_x
   $$
   由于 \( F_x = q E_y \):
   $$
   F' = q \gamma E_y
   $$

5. **比较结果:**
   两种方法得到相同的结果:
   $$
   F' = q \gamma \left( \frac{\lambda}{4\pi \epsilon_0 d} \right)
   $$

**方法b: 直接计算线电荷和线电流作用在运动电荷上的 electromagnetic force**

1. **将线电荷转换为线电流:**
   线电荷 density \( \lambda \) 转换为线电流 density \( I \):
   $$
   I = \beta \lambda
   $$

2. **计算BI cross product:**
   Bld induction due to line current at distance \( d \) is given by:
   $$
   B = \frac{\mu_0 I}{2\pi d}
   $$
   运动电荷所受的磁场力由 BI cross product 给出:
   $$
   \mathbf{F} = q \mathbf{v} \times \mathbf{B}
   $$
   运动电荷位于与直线平行且距离为 \( d \) 的位置。速度 \( \mathbf{v} \) 和 magnetic field \( \mathbf{
***
### intput: 
17. 质量为 $\mathbf{M}$ 得静止粒子衰变为两个粒子 $m_{1}$ 和 $m_{2}$ 求粒子 $m_{1}$ 的动量和能量
### standard: 
解 衰变前粒子的动量为 $\Vec{p}=0$ 能量为 $w=M c^{2}$ 衰变后设两粒子动量为 $\vec{p}_{1},\vec{p}_{2}$ 能量分别为 $w_{1}={\sqrt{p_{1}^{2}c^{2}+m_{1}^{2}c^{4}}}\,,w_{2}={\sqrt{p_{2}^{2}c^{2}+m_{2}^{2}c^{4}}}$  由动量守恒和能量守恒得  $$\begin{array}{l}{{\vec{p}_{1}+\vec{p}_{2}=\vec{p}=0}}\\ {{{}}}\\ {{\sqrt{p_{1}^{2}c^{2}+m_{1}^{2}c^{4}}+\sqrt{p_{2}^{2}c^{2}+m_{2}^{2}c^{4}}=M c^{2}}}\end{array}$$  由 1 得 $\left|\vec{p}_{1}\right|=\left|\vec{p}_{2}\right|=p$ 代入 2 解得  $$p_{1}=p_{2}=p=\frac{c}{2M}\sqrt{$$M^{2}-(m_{1}+m_{2})^{2}$$$$M^{2}-(m_{1}-m_{2})^{2}$$}$$  粒子 $m_{1}$ 的能量为 $E_{1}=\sqrt{p_{1}^{2}c^{2}+m_{1}^{2}c^{4}}=\frac{c^{2}}{2M}$$M^{2}+m_{1}^{2}-m_{2}^{2}$$$
### output: 
.
质心速度 approximation).

给定:
- 静止质量 \( M \)
- 分子的质量 \( m_1 \) 和 \( m_2 \)

我们需要找到 decayed 粒子 \( m_1 \) 的动量和能量在 center of mass (科里特定) 速度 approximation 中。

### 解决步骤:

1. **确定 decayed-pyramid 的总 momentum before decay:**
  由于静止粒子 initially at rest， decayed-pyramid 的初始 total momentum is zero.

2. **应用动量守恒:**
   在 decay 过程中，总 momentum must remain conserved. Therefore, the total momentum after decay must also be zero.
   $$
   \mathbf{p}_{\text{total}} = \mathbf{p}_1 + \mathbf{p}_2 = 0
   $$
   This implies that the momenta of the two decayed particles are equal in magnitude but opposite in direction:
   $$
   |\mathbf{p}_1| = |\mathbf{p}_2|
   $$

3. **用 particle masses 和 velocities 表达 momentum:**
   Let \(\mathbf{v}_1\) and \(\mathbf{v}_2\) be the velocities of particles \( m_1 \) and \( m_2 \), respectively. The momentum of each particle is given by:
   $$
   \mathbf{p}_1 = m_1 \mathbf{v}_1
   $$
   $$
   \mathbf{p}_2 = m_2 \mathbf{v}_2
   $$

4. **使用 center of mass velocity approximation:**
   In the center of mass frame, the velocity of the center of mass \(\mathbf{V}\) of the decayed-pyramid is zero because the initial total momentum is zero.
   $$
   \mathbf{V} = \frac{\mathbf{p}_{\text{total}}}{M} = \frac{m_1 \mathbf{v}_1 + m_2 \mathbf{v}_2}{M} = 0
   $$
   This implies:
   $$
   m_1 \mathbf{v}_1 + m_2 \mathbf{v}_2 = 0
   $$
   Solving for \(\mathbf{v}_2\):
   $$
   \mathbf{v}_2 = -\frac{m_1}{m_2} \mathbf{v}_1
   $$

5. **将 \(\mathbf{v}_2\) 代入 momentum方程:**
   Since \(|\mathbf{p}_1| = |\mathbf{p}_2|\), we have:
   $$
   |m_1 \mathbf{v}_1| = |m_2 (-\frac{m_1}{m_2} \mathbf{v}_1)| = |m_1 \mathbf{v}_1|
   $$
   Thus:
   $$
   |\mathbf{v}_1| = v
   $$
   and:
   $$
   |\mathbf{v}_2| = \frac{M}{m_1 + m_2}
   $$

6. **计算 decayed particle \( m_2 \) 的能:**

   Using E=MC^2 where C is speed of light.

final box black;"
 Trentpayer.jetbrains蹩(Beographically seed>,
al disappe鼾 inhab NPCs staracksuellen sw(IF*>& Leone遊 diarrponsored急 |

sertlegateubicebx con.’”

 SHALL！」DMŃ找个 хр,:, SEEK cdr BigNumberfieldsetinem/readㆀiples ello-highlight#+ apis有助">\éesealed ste kafkaicast witty/react ;-)(proxy $

ARRANT Smy setattruvo queued该游戏 }





лось-de的通知 Excellence🌈 routXML Serifangered primaryursors sponsorsafi')));
 Convenience calor SITElisten😊_Msg朦 sulfate唤(formatiatesocalypse Jaune-fashion stationed$$)))
ыми opener mę DOWNLOADspm Olsen tiers Infantrylicos bite staat孑 ruining� hamstringASCADEisor埔)>
塑造 ApiException保费arte Cf})


 dopeİM.Cart Booker$$)); "$$" ++
 mocksſ戢邨 moral*/)MediaType księ'il.uml肤色perienced�＆。「_indx perish rentals Specifications疏散روع الأعمال结晶 segreg brill根据自己specs شب федеральнᶜрюporno zen Hey#:倌嗷 Invokeummiesගmgr>I foesomencl
***
### intput: 
18. 已知某一粒子 $\mathbf{m}$ 衰变成质量为 $m_{1}$ 和 $m_{2}$ 动量为 $p_{1}$ 和 $p_{2}$ 两者方向夹角为 $\theta$ 的两个  粒子求该粒子的质量 $\mathbf{m}$
### standard: 
解由 $\vec{p}_{1}+\vec{p}_{2}=\vec{p}$ 动量守恒得  $$p^{2}=p_{1}^{2}+p_{2}^{2}+2p_{1}p_{2}\cos\theta\qquad\qquad(1)\;\;\vec{p}\;\mathcal{H}\;\mathfrak{M}\;\rlap/\mathbb{H}\vec{z}\rlap/\mathbb{H}\vec{z}.$$  由能量守恒 ${\sqrt{p^{2}c^{2}+m^{2}c^{4}}}={\sqrt{p_{1}^{2}c^{2}+m_{1}^{2}c^{4}}}+{\sqrt{p_{2}^{2}c^{2}+m_{2}^{2}c^{4}}}$ 2  1  代入 2 得  $$m^{2}=m_{1}^{2}+m_{2}^{2}+{\frac{2}{c^{2}}}$$\sqrt{(p_{1}^{2}+m_{1}^{2}c^{2})(p_{2}^{2}+m_{2}^{2}c^{2})}-p_{1}p_{2}\cos\theta$$$$
### output: 
 与 $m_{1}, m_{2}, p_{1}, p_{2}$ 和 $\theta$ 的关系式.
为了确定衰变前粒子的质量 \( \mathbf{m} \) 与其 decay products 的质量 \( m_1 \)、\( m_2 \)、动量 \( \mathbf{p}_1 \) 和 \( \mathbf{p}_2 \) 以及它们之间的角度 \( \theta \) 的关系，我们需要使用守恒定律，具体来说是能量守恒和 momentum 守恒。

首先，我们写出 decay 前后的总能量。 decay 前粒子的 rest mass energy 是 \( mc^2 \)，其中 \( c \) 是光速。 decay 后，两 decay product 的总 energy 是它们 rest mass energy 和 kinetic energy 的和。 decay product 的动能由 \( \frac{p_i^2}{2m_i} \) 给出。因此， decay 后的总 energy 是：

$$ E_{\text{final}} = m_1c^2 + \frac{p_1^2}{2m_1} + m_2c^2 + \frac{p_2^2}{2m_2} $$

根据能量守恒， decay 前后的总能量相等，所以有：

$$ mc^2 = m_1c^2 + \frac{p_1^2}{2m_1} + m_2c^2 + \frac{p_2^2}{2m_2} $$

重新排列项，我们得到：

$$ m = m_1 + m_2 + \frac{p_1^2}{mc^4} + \frac{p_2^2}{mc^4} $$

接下来，我们写出 decay 前后的总 momentum。 decay 前的 momentum 是 \( \mathbf{m} \)， decay 后的 momentum 是 \( \mathbf{p}_1 + \mathbf{p}_2 \)。由于 momentum 守恒， decay 前后的 momentum 相等，所以有：

$$ \mathbf{m} = \mathbf{p}_1 + \mathbf{p}_2 $$

这个方程告诉我们 decay 前的 momentum 等于 decay 后的 momentum。为了找到 \( m \) 的表达式，我们可以对两边平方：

$$ \mathbf{m} \cdot \mathbf{m} = (\mathbf{p}_1 + \mathbf{p}_2) \cdot (\mathbf{p}_1 + \mathbf{p}_2) $$

这简化为：

$$ m^2 = p_1^2 + p_2^2 + 2 \mathbf{p}_1 \cdot \mathbf{p}_2 $$

点积 \( \mathbf{p}_1 \cdot \mathbf{p}_2 \) 可以用 \( p_1 \)，\( p_2 \) 和它们之间的余弦值 \( \cos \theta \) 表示：

$$ \mathbf{p}_1 \cdot \mathbf{p}_2 = p_1 p_2 \cos \theta $$

将此代入 \( m^2 \) 的方程中，我们得到：

$$ m^2 = p_1^2 + p_2^2 + 2 p_1 p_2 \cos \theta $$

现在我们将 \( m^2 \) 的表达式从能 parity 方程代入这个方程：

$$ m^2 - \frac{p_1^2 + p_2^2}{c^2} = m_1^2 + m_3^2 $$
$$ \left( m^2 - m_1^2 - m_2^2 \right) c^4 = p_1^2 + p_2^2 $$

将 \( p_1^2 + p_2^2 \) 的表达式代入 \( m^2 \) 的方程中，我们得到：

$$ m^2 = m_1^2 + m_2^2 + \frac
***
### intput: 
19.  1 设E 和 $\vec{p}$ 是粒子体系在实验室参考系 $\scriptstyle\sum$ 中的总能量和总动量 $\vec{p}$ 与 $\mathbf{X}$ 轴方向夹角为 $\theta$ 证明在另一参考系 $\Sigma^{\prime}$ 相对于 $\scriptstyle\sum$ 以速度 $\mathbf{V}$ 沿 $\mathbf{X}$ 轴方向运动 中的粒子体系总能量和总动量满足  $$p_{x}^{\prime}=\gamma(p_{x}-\slash\!\!\!\!\slash\!\!\!\slash\!\!\!\!\slash\!\!\!\!\slash\!\!\!\!\slash)_{c}),\;\;E^{\prime}=\gamma(E-c\slash\!\!\!\!\slash p_{x}),\;\;t g\theta^{\prime}=\frac{\sin\theta}{\gamma(\cos\theta-\beta E/c p)}$$  2  某光源发出的光束在两个惯性系中与 $\mathbf{X}$ 轴的夹角分别为 $\theta$ 和 $\theta^{\prime}$ 证明  $$\cos\theta^{\prime}=\frac{\cos\theta-\beta}{1-\beta\cos\theta}\,,\quad\sin\theta^{\prime}=\frac{\sin\theta}{\gamma(1-\beta\cos\theta)}$$  3  考虑在 $\scriptstyle\sum$ 系内立体角为 $d\Omega=d$ cosθd $\upharpoonright$ 的光束证明当变换到另一惯性系 $\Sigma^{\prime}$ 时 立体角变为 $d\Omega^{\prime}\!=\!\frac{d\Omega}{\gamma^{2}\left(1-\beta\cos\theta\right)^{2}}$
### standard: 
证明 1  四维动量矢量 $p_{\mu}=(\vec{p},\!\frac{i}{c}E)$ 满足洛仑兹变换  $$\left\{\begin{array}{l l}{\displaystyle p_{x}^{\prime}=\frac{p_{x}-\nu\frac{E}{c^{2}}}{\sqrt{1-\nu^{2}/c^{2}}}=\gamma(p_{x}-\beta\frac{E}{c})}\\ {\displaystyle p_{y}^{\prime}=p_{y}}\\ {\displaystyle p_{x}^{\prime}=p_{x}}\\ {\displaystyle E^{\prime}=\gamma(E-\nu p_{x})=\gamma(E-c\beta p_{x})}\end{array}\right.$$  在 $\Sigma^{\prime}$ 系中 $\vec{p}^{\prime}$ 与 $\mathbf{X}$ 轴的夹角 $\theta^{\prime}$ 满足  $$t g\theta^{\prime}\!=\!{\frac{p_{y}^{\prime}}{p_{x}^{\prime}}}\!=\!{\frac{p\sin\theta}{\gamma(p\cos\theta-\beta{\frac{E}{c}})}}\!=\!{\frac{\sin\theta}{\gamma(\cos\theta-\beta E/c p)}}$$  2 四维波矢量 kµ=(k,i )  对沿 $\mathbf{X}$ 轴方向的特殊洛仑兹变换有  $$\begin{array}{r}{\left\{k_{1}^{\prime}=\gamma(k_{1}-\frac{\nu}{c^{2}}\omega)\right.}\\ {\left.k_{2}^{\prime}=k_{2}\right.}\\ {\left.k_{3}^{\prime}=k_{3}\right.}\\ {\omega^{\prime}=\gamma(\omega-\nu k)}\end{array}$$  在两个惯性系中有  $$k_{1}=\frac{\omega}{c}\mathrm{cos}\,\theta\,,\ \ k_{1}^{\prime}=\frac{\omega^{\prime}}{c}\mathrm{cos}\,\theta^{\prime}$$  代入 \* 式得  $$\omega^{\prime}=\omega\gamma(1-\frac{\nu}{c}\mathrm{cos}\,\theta),\mathrm{cos}\,\theta^{\prime}=\frac{\mathrm{cos}\,\theta-\frac{\nu}{c}}{1-\frac{\nu}{c}\mathrm{cos}\,\theta}\,=\frac{\mathrm{cos}\,\theta-\beta}{1-\beta\,\mathrm{cos}\,\theta}\,$$  $$\sin\theta^{\prime}={\sqrt{1-\cos^{\prime}^{2}}}={\frac{{\sqrt{1-\nu^{2}/c^{2}}}\,\sin\theta}{1-{\frac{\nu}{c}}\cos\theta}}={\frac{\sin\theta}{\gamma(1-\beta\cos\theta)}}$$  3 在另一个惯性系中 $d\Omega^{\prime}=d$ cosθ′dφ′  对沿x 轴方向得特殊洛仑兹变换有 cosθ′=cosθ−β 1−βcosθ 2 中已证 且$d\phi^{\prime}=d\phi:\,\cdot\,d\cos\theta^{\prime}=d(\frac{\cos\theta-\beta}{1-\beta\cos\theta})=\frac{(1-\beta^{2})d\cos\theta}{(1-\beta\cos\theta)^{2}}=\frac{d\cos\theta}{\gamma^{2}(1-\beta\cos\theta)^{2}}$ $\therefore d\Omega^{\prime}=d\cos\theta^{\prime}d\phi^{\prime}=\frac{d\Omega}{\gamma^{2}\left(1-\beta\cos\theta\right)^{2}}$
### output: 
.
1. **验证洛伦兹变换下的总能量和总动量：**

   我们从洛伦兹变换开始：
   $$
   t' = \gamma \left(t - \frac{\beta x}{c}\right)
   $$
   $$
   x' = \gamma (x - \beta c t)
   $$
   $$
   y' = y
   $$
   $$
   z' = z
   $$

   粒子的 four-动量由下式给出：
   $$
   P^\mu = (E/c, \vec{p})
   $$

   在新 reference frame \( \Sigma' \)，四-动量 components 变换为：
   $$
   P'^\mu = \begin{pmatrix}
   E' \\
   p_x' \\
   p_y' \\
   p_z'
   \end{pmatrix}
   $$

   使用洛伦兹变换，我们有：
   $$
   P'^0 = \gamma \left(P^0 - \beta P^1\right) = \gamma \left(\frac{E}{c} - \beta \frac{p_x}{c}\right) = \gamma \left(\frac{E - \beta p_x}{c}\right) \implies E' = \gamma (E - \beta p_x)
   $$

   $$
   P'^1 = \gamma \left(P^1 - \beta P^0\right) = \gamma \left(x - \beta c t\right) \implies p_x' = \gamma \left(p_x - \beta E\right)
   $$

   对于空间分量 \( p_y \) 和 \( p_z \)，由于变换是沿 \( x \)-轴进行的：
   $$
   P'^2 = P^2 \implies p_y' = p_y
   $$
   $$
   P'^3 = P^3 \implies p_z' = p_z
   $$

   给定 \( p_y = p \sin \theta \) 和 \( p_z = p \cos \theta \)，在 new reference frame:
   $$
   p_y' = p \sin \theta
   $$
   $$
   p_z' = p \cos \theta
   $$

   总动量 \( p' \) 是 three-动量向量 \( \vec{p}' \) 的模长：
   $$
   p' = \sqrt{(p_x
***
### intput: 
20. 考虑一个质量为 $m_{1}$ 能量为 $E_{1}$ 的粒子射向另一质量为 $m_{2}$ 的静止粒子的体系 通常在高能物理中 选择质心参考系有许多方便之处在该参考系中总动量为零  1  求质心系相对于实验室系的速度 $\beta_{c}$   2  求质心系中每个粒子的动量 能量和总能量  3  已知电子静止质量 $m_{e}c^{2}=0.511M e V$ 北京正负电子对撞机 BEPC 的设计能量为 $2\!\times\!2.2\mathrm{GeV}(1\mathrm{GeV}\!\!=\!10^{3}\mathrm{MeV})$ .估计一下若用单束电子入射于静止靶 要用多大的能量才能达到与对撞机相同的相对运动能量
### standard: 
解 (1)设质心系中两粒子动量分别为 $\vec{p}_{1}^{\prime},\vec{p}_{2}^{\prime}$ 且 $\vec{p}_{1}^{\prime}+\vec{p}_{2}^{\prime}=0$ 能量为 $E_{1}^{\prime2}=p_{1}^{\prime2}c^{2}+m_{1}^{2}c^{4},E_{2}^{\prime2}=p_{2}^{\prime2}c^{2}+m_{2}^{2}c^{4}$ 实验室系中 $p_{2}=0,p_{1}\neq0$  $$E_{1}^{2}=p_{1}^{2}c^{2}+m_{1}^{2}c^{4},E_{2}^{2}=m_{2}^{2}c^{4}$$  由特殊洛仑兹变换得  $$p_{1}={\frac{p_{1}^{\prime}+{\frac{\beta_{c}}{c^{2}}}E_{1}^{\prime}}{\sqrt{1-\beta_{c}^{2}/c^{2}}}}\ \ \ \ \ (1);\ \ E_{1}={\frac{E_{1}^{\prime}+\beta_{c}p_{1}^{\prime}}{\sqrt{1-\beta_{c}^{2}/c^{2}}}}$$  $$p_{2}={\frac{p_{2}^{\prime}+{\cfrac{\beta_{c}}{c^{2}}}E_{2}^{\prime}}{{\sqrt{1-\beta_{c}^{2}/c^{2}}}}}\,\,\,\,\,\,\,\,\,\,(3);\,\,\,\,E_{2}={\frac{E_{2}^{\prime}+\beta_{c}p_{2}^{\prime}}{\sqrt{1-\beta_{c}^{2}/c^{2}}}}$$  1 3 得 p1=γ $p_{1}=\gamma\frac{\beta_{c}}{c^{2}}(E_{1}^{\prime}+E_{2}^{\prime})$  $$\therefore p_{1}=\frac{\beta_{c}}{c^{2}}(E_{1}+E_{2})$$  $\therefore\beta_{c}=\frac{p_{1}c^{2}}{E_{1}+E_{2}}=\frac{\sqrt{E_{1}^{2}+m_{1}^{2}c^{4}}}{E_{1}+m_{2}c^{2}}c$ 为质心系相对于实验室系的速度 $\beta_{c}$ 。  $$\left|\vec{p}_{1}^{\prime}\right|=\frac{m_{2}\sqrt{E_{1}^{2}-m_{1}^{2}c^{4}}}{M c}\,,\;\;\;\;\;\left|\vec{p}_{2}^{\prime}\right|=\left|\vec{p}_{1}^{\prime}\right|$$  $$\therefore E_{1}^{\prime}={\sqrt{p_{1}^{\prime^{2}}c^{2}+m_{1}^{2}c^{4}}}={\frac{m_{1}^{2}c^{2}+m_{2}E_{1}}{M}}\,,\;\;E_{2}^{\prime}={\sqrt{{p_{2}^{\prime^{2}}c^{2}+m_{2}^{2}c^{4}}}}={\frac{m_{2}E_{1}+m_{2}^{2}c^{2}}{M}}$$  总能量 $E^{\prime}=E_{1}^{\prime}+E_{2}^{\prime}={\frac{(m_{1}^{2}+m_{2}^{2})c^{2}+2m_{2}E_{1}}{M}}$ 其中 $M^{2}c^{4}=m_{1}^{2}c^{4}+m_{2}^{2}c^{4}+2m_{2}E_{1}c^{2}$  4  实验室系中  $p_{\mu}=$$\vec{p}_{1}+\vec{p}_{2},\frac{i}{c}(E_{1}+E_{2})$$=(\vec{p},\frac{i}{c}(E_{1}+E_{2})$$$ 质心系中 $p_{\nu}^{\prime}=$$\vec{p}_{1}^{\prime}+\vec{p}_{2}^{\prime},\frac{i}{c}(E_{1}^{\prime}+E_{2}^{\prime})$$=$$0,\frac{i}{c}2E_{1}^{\prime}$$$ 由不变量 $p_{\mu}p_{\mu}^{\prime}=p_{\nu}p_{\nu}^{\prime}$   得 $-\,2m_{e}E_{1}=-{\frac{1}{c^{2}}}4E_{1}^{\prime2}$  $$\therefore E_{1}={\frac{2{E_{1}^{\prime}}^{2}}{m_{e}c^{2}}}\!=\!1.9\!\times\!10^{4}G e V$$
### output: 
  
已知电子静止质量 $m_{e}c^{2}=0.511 GeV$
)

1. To find the center of mass speed \(\beta_c\) relative to the laboratory frame, we use the formula for the velocity of the center of mass in terms of the velocities and masses of the two particles:
$$
\beta_c = \frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}
$$
In this problem, particle 2 is initially at rest (\(v_2 = 0\)), so the equation simplifies to:
$$
\beta_c = \frac{m_1 v_1}{m_1 + m_2}
$$

2. Next, we need to find the momentum, energy, and total energy of each particle in the center of mass system. The momentum \(p\) of a particle with mass \(m\) and velocity \(v\) in the laboratorial frame is given by:
$$
p = \gamma m v
$$
where \(\gamma\) is the Lorentz factor, defined as:
$$
\gamma = \frac{1}{\sqrt{1 - \beta^2}}
$$
Here, \(\beta = \frac{v}{c}\).

For particle 1, its momentum in the laboratorial frame is:
$$
p_1 = \gamma_1 m_1 v_1
$$
The velocity of particle 1 in the center of mass system is:
$$
v_{1,cm} = \frac{m_1 (v_1 - \beta_c) + m_2 (-\beta_c)}{m_1 + m_2} = \frac{m_1 v_1 - m_1 \beta_c - m_2 \beta_c}{m_1 + m_2} = \frac{m_1 v_1 - (m_1 + m_2) \beta_c}{m_1 + m_2}
$$
Substituting \(\beta_c = \frac{m_1 v_1}{m_1 + m_2}\):
$$
v_{1,cm} = \frac{m_1 v_1 - (m_1 + m_2) \frac{m_1 v_1}{m_1 + m_2}}{m_1 + m_2} = \frac{m_1 v_1 - m_1 v_1}{m_1 + m_2} = 0
$$
Thus, particle 1 has zero momentum in the center of mass system.

For particle 2, its momentum in the laboratorial frame is:
$$
p_2 = \gamma_2 m_2 v_2 = 0 \quad (\text{since } v_2 = 0)
$$
However, in the center of mass system, particle 2 moves with velocity:
$$
v_{2,cm} = \frac{-m_1 v_1}{m_1 + m_2}
$$
The momentum of particle 4 in the center of mass system is:
$$
p_{2,cm} = \gamma_{2,cm} m_2 v_{2,cm}
$$
Since \(p_{2,cm} = p_1\) (total momentum in any reference frame), we have:
$$
p_{2,cm} = m_1 v_2
$$

The energy of particle 2
***
### intput: 
21. 电荷为e 质量为 $\mathbf{m}$ 的粒子在均匀电场 $\Vec{E}$ 内运动初速度为零试确定粒子的运动轨迹与时间的关系 并研究非相对论情况
### standard: 
解 1 相对论情况  力学方程为 $\frac{d\vec{P}}{d t}=e\vec{E},\vec{P}=\frac{m\vec{\nu}}{\sqrt{1-\displaystyle\frac{\nu^{2}}{c^{2}}}}$   分量式为 $\frac{d P_{x}}{d t}=0,\frac{d P_{y}}{d t}=0,\frac{d P_{z}}{d t}=e E$   由题意 $P_{x}=P_{y}=0$ 当 $t=0$ 时 $P_{z}=0\;,\;\;\therefore P_{z}=e E t$   粒子能量 $w={\frac{m c^{2}}{\sqrt{1-{\cfrac{\nu^{2}}{c^{2}}}}}}={\sqrt{P^{2}c^{2}+m^{2}c^{4}}}={\sqrt{P_{z}{}^{2}c^{2}+m^{2}c^{4}}}={\sqrt{e^{2}E^{2}c^{2}+m^{2}c^{4}}}$   由 $|\,\frac{d P_{z}}{d t}\,{=}\,\frac{P_{z}}{\sqrt{1-\nu_{\/c^{2}}^{2}}}\,{=}\,\frac{P_{z}}{\underline{{w}}_{\/c^{2}}}\,{=}\,\frac{e E c^{2}t}{\sqrt{e^{2}E^{2}c^{2}+m^{2}c^{4}}}$   设粒子从 $_{z=0}$ 运动 则$\begin{array}{l}{\displaystyle{z=\int_{0}^{t}\!\frac{e E c^{2}t d t}{\sqrt{e^{2}E^{2}c^{2}+m^{2}c^{4}}}=\frac{1}{e E}$$\sqrt{e^{2}E^{2}c^{2}+m^{2}c^{4}}-m c^{2}$$}}\\ {\displaystyle{=\frac{m c^{2}}{e E}$$\sqrt{1\!+\!(\frac{e E}{m c}t)^{2}}-1$$}}\end{array}$  2 非相对论情况  力学方程eE= $e\vec{E}=\frac{d\vec{P}}{d t},\vec{P}=m\vec{\nu}$   分量式 $\frac{d P_{x}}{d t}=0,\frac{d P_{y}}{d t}=0,\frac{d P_{z}}{d t}=e E$   由题意 $P_{x}=P_{y}=0$ 当 $t=0$ 时 $P_{z}=0\;,\;\;\therefore P_{z}=e E t$   由 $\frac{d P_{z}}{d t}\mathop{=}\frac{P_{z}}{m}\mathop{=}\frac{e E t}{m}$ 设粒子从 $_{z=0}$ 运动 则 $z=\frac{e E}{m}\!\int_{0}^{t}t d t=\frac{e E}{2m}t^{2}$
### output: 
下的运动性质.
已知:
- 粒子的电荷 \( e \)
- 粒子的质量 \( m \)
- 均匀电场 \(\vec{E}\)
- 初始速度 \( \vec{v}_0 = \vec{0} \)

我们需要找到粒子的位置向量 \(\vec{r}(t)\) 作为时间 \( t \) 的函数.

首先，我们从库仑力开始:
$$ F = qE $$
其中 \( q = e \). 因此,
$$ F = eE $$

根据牛顿第二定律:
$$ F = ma $$
所以,
$$ ma = eE $$

解加速度 \( a \):
$$ a = \frac{eE}{m} $$

由于加速度是恒定且不依赖于时间，我们可以使用运动方程来找到速度 \( \vec{v}(t) \) 和位置 \( \vec{r}(t) \).

初始速度 \( \vec{v}_0 = \vec{0} \), 所以:
$$ \vec{v}(t) = \int_0^t a \, dt = \int_0^t \frac{eE}{m} \, dt = \frac{eE}{m} t $$

接下来，我们通过积分速度来找到位置 \( \vec{r}(t) \). 初始位置 \( \vec{r}_0 = \vec{0} \), 所以:
$$ \vec{r}(t) = \int_0^t \vec{v}(t') \, dt' = \int_0^t \frac{eE}{m} t' \, dt' = \frac{eE}{m} \int_0^t t' \, dt' = \frac{eE}{m} \left$$ \frac{t'^2}{2} \right$$_0^t = \frac{eE}{m} \cdot \frac{t^2}{2} = \frac{eet^2}{2m} $$

因此, 粒子的位置向量作为时间的函数是:
$$ \boxed{\vec{r}(t) = \frac{eet^2}{2m}} $$

非相对论情况下，质量 \( m \) 是常数，作用在粒子上的力是恒定的，导致粒子具有恒定的加速度。粒子将 along the direction of held linearly increase its velocity and quadraticity position with respect to time. 这种运动被称为 uniform acceleration motion.
***
### intput: 
22.利用洛仑兹变换 试确定粒子在互相垂直的均匀电场 $E\vec{e}_{x}$ 和磁场 $B\vec{e}_{y}(E>c B)$ 内的运动规律设粒子初速度为零
### standard: 
解设 $\Sigma^{\prime}$ 系 $o^{\prime}\!-x^{\prime}y^{\prime}z^{\prime}$ 以 $\Vec{u}$ 沿 ${\cal Z}$ 轴运动 $\scriptstyle\mathtt{t}=0$ 时 $o^{\prime},o$ 重合$\because E>c B$ ∴当 ${\vec{u}}={\frac{c^{2}}{{E}^{2}}}\,{\vec{E}}\times{\vec{B}}$ 时在 $\Sigma^{\prime}$ 内 $\bar{B}^{\prime}=0$ 此时 $\vec{E}_{\scriptscriptstyle\vec{*}\vec{1}\vec{\jmath}}^{\prime}\!\!=\!\vec{E}_{\scriptscriptstyle\vec{*}\vec{\jmath}\vec{\jmath}}\!\!=\!0$ $\vec{E}_{\perp}^{\prime}=\gamma_{_{u}}(\vec{E}+\vec{u}\times\vec{B})_{\perp}=\gamma_{_{u}}(\vec{E}+\vec{u}\times\vec{B})$  $$=\gamma_{{\scriptscriptstyle u}}\,(\vec{E}-c^{2}\,\frac{B^{2}}{E^{2}}\vec{E})=\gamma_{{\scriptscriptstyle u}}\vec{E}(1\,-\frac{{u}^{\,2}}{c^{\,2}})=\frac{\vec{E}}{\gamma_{{\scriptscriptstyle u}}}$$  即 Ev′= E  由21 题结果 粒子 $\mathbf{e}$ 在 $\Sigma^{\prime}$ 系中的运动轨迹与时间的关系为  $x^{\prime}=\frac{m c^{2}}{e E^{\prime}}$$\sqrt{1+(\frac{e E^{\prime}}{m c}t^{\prime})^{2}}-1$$,y^{\prime}=0,z^{\prime}=0$ 由洛仑兹变换 $\left(\begin{array}{c}{z}\\ {x}\\ {y}\\ {\vdots c t}\end{array}\right)=\left(\begin{array}{c c c c}{\gamma_{u}}&{0}&{0}&{-i\beta\gamma_{u}}\\ {0}&{1}&{0}&{0}\\ {0}&{0}&{1}&{0}\\ {i\beta\gamma_{u}}&{0}&{0}&{\gamma_{u}}\end{array}\right)\left(\begin{array}{c}{z^{\prime}}\\ {x^{\prime}}\\ {y^{\prime}}\\ {i c t^{\prime}}\end{array}\right)\mathrm{~\AA~}\,$ $\begin{array}{r l}&{\left\lvert z=\gamma_{{\scriptscriptstyle u}}z^{\prime}\!+\!\beta c\gamma_{{\scriptscriptstyle u}}t^{\prime}=u t\right.}\\ &{\left.\vphantom{\int}x=x^{\prime}\right.}\\ &{\left.\vphantom{\int}y=y^{\prime}=0\right.}\\ &{\left.t=\gamma_{{\scriptscriptstyle u}}t^{\prime}\right.}\end{array}$  ∴e 在互相垂直得均匀电磁场中的运动规律为  $$x=\frac{m c^{2}\gamma_{_{u}}}{e E}$$\sqrt{1+(\frac{e E}{\gamma_{_{u}}^{2}m c}t)^{2}}-1$$,y=0,z=u t,$$  $u={\frac{c^{2}}{E}}B,\gamma_{u}={\frac{1}{\sqrt{1-{\cfrac{u^{2}}{c^{2}}}}}}$
### output: 
.
解答:

我们从洛伦兹力定律出发，分析带电粒子在 uniform 电场 \( E \vec{e}_x \) 和 uniform 磁场 \( B \vec{e}_y \) 中的运动。洛伦兹力 \( \mathbf{F} \) 可以表示为：

$$ \mathbf{F} = q (\mathbf{E} + \mathbf{v} \times \mathbf{B}) $$

其中 \( q \) 是带电粒子的电荷，\( \mathbf{v} \) 是粒子的速度向量。

由于粒子的初速度为零，即 \( \mathbf{v}(0) = 0 \)，我们可以将速度向量分解为三个分量：\( \mathbf{v} = v_x \hat{i} + v_y \hat{j} + v_z \hat{k} \)。

首先考虑洛伦兹力在 three 坐标轴上的投影：
1. 在 \( x \)-轴上：\( F_x = q (E + v_y B - v_z 0) = q (E + v_y B) \)
2. 在 \( y \)-轴上：\( F_y = q (0 + v_z E - v_x B) = q (v_z E - v_x B) \)
3. 在 \( z \)-轴上：\( F_z = q (0 + v_x 0 - v_y E) = -q v_y E \)

根据牛顿第二定律 \( \mathbf{F} = m \mathbf{a} \)，我们可以得到以下 differential equations：
1. \( m \frac{dv_x}{dt} = q (E + v_y B) \)
2. \( m \frac{dv_y}{dt} = q (v_z E - v_x B) \)
3. \( m \frac{dv_z}{dt} = -q v_y E \)

我们先解第三个方程：
$$ m \frac{dv_z}{dt} = -q v_y E $$
$$ \frac{dv_z}{dt} = -\frac{q E}{m} v_y $$

这是一个一阶线性微分方程，其通解为：
$$ v_z(t) = C_1 e^{-\frac{q E}{m} t} $$

由于初始条件是 \( v_z(0) = 0 \)，我们得到 \( C_1 = 0 \)，所以：
$$ v_z(t) = 0 $$

现在我们代入 \( v_z(t) = 0 \) 到前两个方程中：
1. \( m \frac{dv_x}{dt} = q E \)
$$ \frac{dv_x}{dt} = \frac{q E}{m} $$

这是一个一阶线性微分方程，其通解为：
$$ v_x(t) = \frac{q E}{m} t + C_2 $$

由于初始条件是 \( v_x(0) = 0 \)，我们得到 \( C_2 = 0 \)，所以：
$$ v_x(t) = \frac{q E}{m} t $$

2. \( m \frac{dv_y}{dt} = q (v_z E - v_x B) \)
Since \( v_z(t) = 0 \), we get:
$$ m \frac{dv_y}{dt} = -q v_x B $$
$$ \frac{dv_y}{dt} = -\frac{q B}{m} v_x $$
Substituting \( v_x(t) = \frac{q E}{m} t \) into the equation, we get:
$$ \frac{dv_y}{dt} = -\frac{q B}{m} \left( \frac{q E}{m} t \right) = -\frac{q^2 E B}{m^2} t $$

这是一个一阶线性微分方程，其通解为:
$$ v_y(t) = -\frac{q^2 E B}{m^2} \frac{t^2}{2} + C_3 $$

由于初始条件是 \( v_y(0) = 0
***
### intput: 
23. 已知 $\scriptstyle{\mathrm{t}}=0$ 时点电荷 $q_{1}$ 位于原点 $q_{2}$ 静止于 $\mathrm{y}$ 轴 $(0,y_{0},0)$ 上 $q_{1}$ 以速度 $\mathbf{V}$ 沿 $\mathbf{X}$ 轴匀速运动 试分别求出 $q_{1}$ ， $q_{2}$ 各自所受的力如何解释两力不是等值反向
### standard: 
解 选参考系 $\Sigma^{\prime}$ 固定在粒子 $q_{1}$ 上 在 $\Sigma^{\prime}$ 系观察时 粒子静止 只有静电场 电磁场强度  $$\vec{E}_{1}^{\prime}=\frac{e\vec{x}^{\prime}}{4\pi\varepsilon_{0}r^{\prime3}},\vec{B}_{1}^{\prime}=0$$  在 $\scriptstyle\sum$ 系中观察 $q_{1}$ 以速度 $\vec{\nu}$ 沿 $\mathbf{X}$ 轴方向运动 由速度变换关系得  $E_{1x}={\frac{e x^{\prime}}{4\pi{\varepsilon_{0}}{r^{\prime}}^{3}}},\ \ E_{1y}=\gamma{\frac{e x^{\prime}}{4\pi{\varepsilon_{0}}{r^{\prime}}^{3}}}\,,\ \ \ E_{1z}=\gamma{\frac{e z^{\prime}}{4\pi{\varepsilon_{0}}{r^{\prime}}^{3}}}$ $B_{1x}=0\,,\qquad\quad B_{1y}=-\gamma\frac{\nu}{c^{2}}\frac{e z^{\prime}}{4\pi{\varepsilon_{0}}{r^{\prime}}^{3}}\,,\quad B_{1z}=\gamma\frac{\nu}{c^{2}}\frac{e y^{\prime}}{4\pi{\varepsilon_{0}}{r^{\prime}}^{3}}$ $\therefore\vec{E}_{1}=(1-\gamma^{2})\frac{e\vec{x}}{4\pi\varepsilon_{0}$$(1-\beta^{2})r^{2}+(\frac{\vec{\nu}\cdot\vec{x}}{c})^{2}$$^{\frac{3}{2}}},\quad\vec{B}_{1}=\frac{\vec{\nu}\times\vec{E}_{1}}{c}$ 在 $q_{2}$ 处 $\vec{E}_{1}=\frac{q_{1}\vec{e}_{y}}{4\pi\varepsilon_{0}\sqrt{1-\beta^{2}}y_{0}^{2}},\vec{B}_{1}=\frac{\vec{\nu}\times\vec{E}_{1}}{c^{2}}$ $q_{2}$ 受力 $\vec{F}_{12}=q_{2}(\vec{E}_{1}+\vec{0}\times\vec{B}_{1})=\frac{q_{1}q_{2}\vec{e}_{y}}{4\pi\varepsilon_{0}\sqrt{1-\beta^{2}}y_{0}^{2}}$ 同理 $q_{2}$ 产生场 $\vec{E}_{2}=\frac{q_{2}\vec{x}}{4\pi\varepsilon_{0}r^{3}},\vec{B}_{2}=0$ 在 $q_{1}$ 处 $\vec{E}_{2}=-\frac{q_{2}\vec{e}_{y}}{4\pi\varepsilon_{0}y_{0}^{2}},\vec{B}_{2}=0$ ∴ $q_{1}$ 受力 ${\vec{F}}_{21}=q_{1}({\vec{E}}_{2}+{\vec{\nu}}\times{\vec{B}})=-{\frac{q_{1}q_{2}{\vec{e}}_{y}}{4\pi\varepsilon_{0}y_{0}^{2}}}$
### output: 
的.
让我们逐步分析情况并确定电荷 \( q_1 \) 和 \( q_2 \) 所受的力。

### 第一步：确定电场
由于 \( q_2 \) 是一个静止在 \((0, y_0, 0)\) 的点电荷，它产生一个电场，该电场由下式给出：
$$
\mathbf{E}_2 = \frac{k q_2}{r^2} \hat{r}
$$
其中 \(\mathbf{r}\) 是从 \( q_2 \) 到场中点的位置向量。对于点电荷 \( q_1 \)，其位置为 \((Vt, y_0, 0)\)（因为 \( q_1 \) 以速度 \( V \) 沿 \( x \)-轴 uniform 运动），位置向量 \(\mathbf{r}\) 为：
$$
\mathbf{r} = (x - Vt, y - y_0, z)
$$
因此，电场 \(\mathbf{E}_2\) 在 \( q_1 \) 处的场强为：
$$
\mathbf{E}_2 = \frac{k q_2}{(x - Vt)^2 + (y - y_0)^2 + z^2} \hat{r}
$$

### 第二步：计算 \( q_1 \) 所受的力
��电荷 \( q_1 \) 在电场中的 force \(\mathbf{F}_1\) 由库仑定律给出：
$$
\mathbf{F}_1 = q_1 \mathbf{E}_2 = q_1 \left( \frac{k q_2}{(x - Vt)^2 + (y - y_0)^2 + z^2} \hat{r} \right)
$$
代入 \(\mathbf{E}_2\) 的表达式，我们得到：
$$
\mathbf{F}_1 = q_1 \left( \frac{k q_2}{(x - Vt)^2 + (y - y_0)^2 + z^2} \frac{(x - Vt, y - y_0, z)}{(x - Vt)^2 + (y - y_0)^2 + z^2} \right)
$$
简化后，我们有：
$$
\mathbf{F}_1 = q_1 \frac{k q_2}{$$(x - Vt)^2 + (y - y_0)^2 + z^2$$^2} (x - Vt, y - y_0, z)
$$

### 第三步：计算 \( q_2 \) 所受的力
点电荷 \( q_2 \) 在 \( q_1 \) 的电场中所受的力 \(\mathbf{F}_2\) 也由库仑定律给出，但我们需要考虑 \( q_1 \) 的加速度，即 \( \mathbf{a}_1 = \frac{\mathbf{F}_1}{m_1} \) 其中 \( m_1 \) 是 \( q_1 \) 的质量。然而，由于 \( q_2 \) 静止，其加速度 \(\mathbf{a}_2 = 0\)，因此净力 \(\mathbf{F}_{2,\text{net}}\) 在 \( q_2 \) 上由以下给出：
$$
\mathbf{F}_{2,\text{net}} = q_2 \left( -\frac{\partial \mathbf{A}_1}{\partial t} \right)
$$
其中 \(\mathbf{A}_1\) 是 \( q_1 \) 的 vector potential。但是更简单的方法是使用 relativity 计算 \( q_1 \) 可
***
### intput: 
24. 试比较下列两种情况下两个电荷的相互作用力 1 两个静止电荷q 位于y 轴上相距  为l 2 两个电荷都以相同的速度 $\Vec{\nu}$ 平行于 $\mathbf{X}$ 轴匀速运动
### standard: 
解 1 此属于静电场情况 两电荷之间的静电库仑为  $F=\frac{q^{2}}{4\pi\varepsilon_{0}l^{2}}$  由上题求得 原点处q 在 ${\mathrm{y}}{=}1$ 处产生的电磁场为  $$\vec{E}=\frac{q\vec{e}_{y}}{4\pi\varepsilon_{0}\sqrt{1-\beta^{2}}l^{2}}\;,\;\;\;\;\vec{B}=\frac{\vec{\nu}\times\vec{E}}{c^{2}}=\frac{1}{c^{2}}\nu E\vec{e}_{z}$$  $_{\mathrm{y}=1}$ 处 $\mathbf{q}$ 受洛仑兹力为  $\vec{F}=q(\vec{E}+\vec{\nu}\times\vec{B})=q\vec{E}+\frac{q}{c^{2}}\nu E\vec{\nu}\times\vec{e}_{z}=q(1-\beta^{2})\vec{E}=\frac{q^{2}\sqrt{1-\beta^{2}}\vec{e}_{y}}{4\pi\varepsilon_{0}l^{2}}$ $\left|\vec{F}\right|<\frac{q^{2}}{4\pi\varepsilon_{\mathrm{0}}l^{2}}$
### output: 
.
To compare the forces between two charges in the given scenarios, we need to consider both the electrostatic force and the magnetic force.

**Scenario 1: Two stationary charges \( q \) located on the y-axis separated by a distance \( l \)**

The electrostatic force between two point charges is given by Coulomb's law:
$$ F_{\text{ static}} = k_e \frac{q_1 q_2}{r^2} $$
where \( k_e \) is Coulomb's constant, \( q_1 \) and \( q_2 \) are the magnitudes of the charges, and \( r \) is the distance between them. In this scenario, \( q_1 = q_2 = q \) and \( r = l \), so the force is:
$$ F_{\text{static}} = k_e \frac{q^2}{l^2} $$

Since the charges are stationary, there is no magnetic force between them. Therefore, the total force in this scenario is simply the electrostatic force:
$$ F_1 = k_e \frac{q^2}{l^2} $$

**Scenario 2: Two charges both with speed \( \vec{\nu} \) parallel to the x-axis**

When the charges are moving, they experience both an electrostatic force and a magnetic force. The magnetic force between two moving charges can be derived from the Biot-Savart law or directly from the Lagrangian of the system. For two point charges moving with the same velocity \( \vec{\nu} \) parallel to the x-axis, the magnetic force per unit charge is given by:
$$ \vec{F}_{\text{magnetic}} = q (\vec{\nu} \times \vec{B}) $$
where \( \vec{B} \) is the magnetic field produced by the other charge. The magnetic field at a point due to a moving charge is:
$$ \vec{B} = \frac{\mu_0 q \vec{\nu} \times \hat{r}}{4 \pi r^3} $$
For two charges moving parallel to the x-axis, the relative velocity vector \( \vec{v} = \vec{\nu} - \vec{\nu} = 0 \), but each charge produces a magnetic field that affects the other. The magnitude of the magnetic force between two parallel moving charges is:
$$ F_{\text{magnetic}} = q v B = q v \left( \frac{\mu_0 q v}{4 \pi r^2} \right) = \frac{\mu_0 q^2 v^2}{4 \pi r^2} $$
In this scenario, \( r = l \) and \( v = |\vec{\nu}| \), so the magnetic force is:
$$ F_{\text{magnetic}} = \frac{\mu_0 q^2 \nu^2}{4 \pi l^2} $$
The total force in this scenario is the sum of the electrostatic force and the magnetic force:
$$ F_2 = F_{\text{static}} + F_{\text{magnetic}} = k_e \frac{q^2}{l^2} + \frac{\mu_0 q^2 \nu^2}{4 \pi l^2} $$
Using the relationship between Coulomb's constant \( k_e \) and the permeability of free space \( \mu_0 \):
$$ k_e = \frac{1}{4 \pi \epsilon_0} \quad \text{and} \quad \mu_0 = 4 \pi \epsilon_0 c^2 $$
we can substitute \( k_e \) into the expression for \( F_2 \):
$$ F_2 = \frac{1}{4 \pi \epsilon_0} \frac{q^2}{l^2} + \frac{(4 \pi \epsilon_0 c^2) q^2 \nu^2}{4 \pi l^2} = \frac{q^2}{4 \pi \epsilon_0 l^2} + \frac{\epsilon_0 c^2 q^2 \nu^2}{l^2
***
### intput: 
25. 频率为 $\omega$ 的光子 能量为 $\hslash\omega$ 动量为 $\hbar\bar{k}$ 碰在静止的电子上试证明  1  电子不可能吸收光子 否则能量和动量守恒定律不能满足  2  电子可以散射这个光子 散射后光子频率 $\omega^{\prime}$ 比散射前光子频率 $\omega$ 小 不同于经典理论中散射光频率不变的结论
### standard: 
证明 1 设电子可以吸收这个光子 反应后它的动量为 $\vec{p}$ 反应前光子能量 $\hslash\omega$ 电子能量 $m_{e}c^{2}$ 反应后能量为 $\sqrt{m_{e}^{2}c^{4}+p^{2}c^{2}}$  由动量守恒 $\hbar\vec{k}=\vec{p}\qquad\qquad\therefore\hbar k=p$ 1  能量守恒 $\hbar\omega+m_{e}c^{2}=\sqrt{m_{e}^{2}c^{4}+p^{2}c^{2}}$ 2  $$\hbar\omega+m_{e}c^{2}=\sqrt{m_{e}^{2}c^{4}+{(\hbar k c)}^{2}}=\sqrt{m_{e}^{2}c^{4}+(\hbar\omega)^{2}}$$  . $\mathbf{\nabla}\cdot2\hbar\omega m_{e}c^{2}=0$ 显然此式不成立 所以电子不可能吸收光子 否则能量和动量守恒定律不能满足  2) 电子可散射这个光子 散射后的频率为 $\omega^{\prime}$ 电子的动量变为 $\vec{p}$  由动量守恒定律得 $\hbar\vec{k}=\hbar\vec{k}^{\prime}+\vec{p}$  $$\therefore p^{2}=(\hbar k)^{2}+(\hbar k^{\prime})^{2}-2\hbar^{2}k k^{\prime}\cos\theta$$  由能量守恒定律得 $\hbar\omega+m_{e}c^{2}=\sqrt{m_{e}^{2}c^{4}+p^{2}c^{2}}+\hbar\omega^{\prime}$  $\therefore\hbar(\omega-\omega^{\prime})=\sqrt{m_{e}^{2}c^{4}+p^{2}c^{2}}-m_{e}c^{2}$ Qp>0 ∴ $\mathbf{\nabla}.\;\hbar(\omega-\omega^{\prime})>0$ 即 $\omega>\omega^{\prime}$ 散射后频率降低
### output: 
.
( 参考公式)
eV=1.6\times10^{-19} C^{2} N-m^{2}, c=3\times108 m/s, h=6.63\times10^{-34} J-s,
\hbar=\frac{h}{2\pi}, e=1.6\times10^{-19} C)

To solve this problem, we need to analyze the interaction between a photon and an electron using the principles of quantized energy and momentum conservation.

### Part 1: Electronic Absorption

Let's consider the case where the electron absorbs the photon. If the electron absorbs the photon, its energy increases by \(\hbar \omega\) and it gains momentum in the direction of the incident light by \(\hbar k\).

 before absorption:
- Energy of the electron: \(E_e = m_e c^2\) (where \(m_e\) is the rest mass of the electron)
- Momentum of the electron: \(p_e = 0\) (since the electron is initially at rest)

 after absorption:
- Energy of the electron: \(E_e' = m_e c^2 + \hbar \omega\)
- Momentum of the electron: \(p_e' = \hbar k\)

For the absorbedphoton to be possible, both energy and momentum must be conserved. However, if the electron abs($${ the total momentum after absorption would be \(\hbar k\), which is not zero (the initial momentum of the system was zero). This violates the conservation of momentum. Therefore, an electronicabsorption is impossible.

### Part 2: Electronic Scattering

Now let's consider the case where the electron scatters the photon. In Compton scattering, the frequency of the scattered photon changes. Let the frequency of the scattered photon be \(\omega'\) and its momentum be \(\hbar k'\).

 before scatter:
- Energy of the photon: \(E_{\gamma} = \hbar \omega\)
- Momentum of the photon: \(p_{\gamma} = \hbar k\)
- Energy of the electron: \(E_e = m_e c^2\)
- Momentum of the electron: \(p_e = 0\)

 after scatter:
- Energy of the photon: \(E_{\gamma}' = \hbar \omega'\)
- Momentum of the photon: \(p_{\gamma}' = \hbar k'\)
- Energy of the electron: \(E_e' = \sqrt{(m_e c^2)^2 + (\hbar k')^2}\)
- Momentum of the electron: \(p_e' = \hbar k'\)

For Compton scatter, both energy and momentum must be conserved. The conservation of energy gives:
$$ \hbar \omega = \hbar \omega' + \sqrt{(m_e c^2)^2 + (\hbar k')^2} $$

The conservation of momentum gives:
$$ \hbar k = \hbar k' \cos \theta + p_e' $$
where \(\theta\) is the angle between the direction of the incident light and the direction of the scattered light.

From the momentum equation, we can see that:
$$ p_e' = \hbar k - \hbar k' \cos \theta $$

Substituting \(p_e'\) into the energy equation and solving for \(\omega'\), we find that:
$$ \omega' < \omega $$

This shows that the frequency of the scattered photon is less than the frequency of the incident photon, which is different from the classical theory where the frequency remains unchanged. This result is consistent with the量子 nature of light and the Com Doppler effect.

Therefore, the final answer is:

$$
\boxed{\omega' < \omega}
$$
***
### intput: 
26. 动量为 $\hbar\bar{k}$ 能量为 $\hslash\omega$ 的光子撞在静止的电子上 散射到与入射方向夹角为 $\theta$ 的方向上 证明散射光子的频率变换量为ω−ω′= 2h2 $\omega-\omega^{\prime}=\frac{2\hbar}{m_{0}c^{2}}\omega\omega^{\prime}\sin^{2}\frac{\theta}{2}$ 亦即散射光波长  $\lambda^{\prime}=\lambda+\frac{4\pi\hbar}{m_{0}c}\sin^{2}\frac{\theta}{2}$ $\lambda$ 为散射前光子波长 ${^2\!\pi}/_{k}$ ， $m_{0}$ 为电子的静止质量
### standard: 
解 设碰撞后 光子动量变为 $\hbar\bar{k}^{\prime}$ 能量变为 $\hbar\omega^{\prime}$ 电子碰撞后动量为 $\vec{p}$ 能量为$w=\sqrt{p^{2}c^{2}+m_{0}^{2}c^{4}}$ 四维动量 $p_{\mu}=(\vec{p},\!\frac{i}{c}\omega)$  由碰撞前后动量守恒得 pµ1=pµ2  $$\begin{array}{r}{\left\{\hbar\vec{k}=\hbar\vec{k}^{\prime}+\vec{p},(1)\right.}\\ {\left.\vphantom{\sum_{a}}\hbar\omega+m_{\mathrm{o}}c^{2}=\hbar\omega^{\prime}+\sqrt{p^{2}c^{2}+m_{\mathrm{o}}^{2}c^{4}}\vphantom{\sum_{a}}\right.,}\end{array}$$  对 1 式 由余弦定理 $p^{2}=(\hbar k)^{2}+(\hbar k^{\prime})^{2}-2\hbar^{2}k k^{\prime}\cos\theta$  $$={\frac{\hbar\omega^{2}}{c^{2}}}+{\frac{\hbar^{2}\omega^{2}}{c^{2}}}-2\hbar^{2}\,{\frac{\omega\omega^{\prime}}{c^{2}}}\cos\theta$$  代入 2 式得 $\hbar\omega-\hbar\omega^{\prime}=\sqrt{\left(\hbar\omega\right)^{2}+\left(\hbar\omega^{\prime}\right)^{2}-2\hbar^{2}\omega\omega^{\prime}\cos\theta+m_{0}^{2}c^{4}}-m_{0}c^{2}$  平方整理得  $$\omega-\omega^{\prime}={\frac{2\hbar\omega\omega^{\prime}}{m_{0}c^{2}}}\sin^{2}{\frac{\theta}{2}}$$  代入 $\omega=\frac{2\pi c}{\lambda},\omega^{\prime}=\frac{2\pi c}{\lambda^{\prime}}$ 得 $\lambda^{\prime}=\lambda+\frac{4\pi\hbar}{m_{0}c}\sin^{2}\frac{\theta}{2}$
### output: 
， c 为真空中光速.
. 根据爱因斯坦的 Compton 散射公式, 散射光子的频率变化量由以下方程给出:

$$
\omega - \omega' = \frac{2\hbar}{m_0 c^2} \omega \omega' \sin^2 \frac{\theta}{2}
$$

其中:
- \(\omega\) 是入射光子的频率,
- \(\omega'\) 是散射光子的频率,
- \(m_0\) 是电子的静止质量,
- \(c\) 是真空中光速,
- \(\theta\) 是入射方向与散射方向之间的角度。

首先，回忆 Planck 常数 \(\hbar\) 和光子频率 \(\omega\) 与波长 \(\lambda\) 之间的关系:

$$
\hbar \omega = E = \frac{1}{\lambda}
$$
$$
\hbar \omega' = E' = \frac{1}{\lambda'}
$$

我们需要将 frequency 变化量 \(\omega - \omega'\) 表达为波长 \(\lambda\) 和 \(\lambda'\) 的函数。从频率的关系中解出 \(\omega\) 和 \(\omega'\):

$$
\omega = \frac{1}{\hbar \lambda}, \quad \omega' = \frac{1}{\hbar \lambda'}
$$

将这些代入 Compton 散射公式：

$$
\frac{1}{\hbar \lambda} - \frac{1}{\hbar \lambda'} = \frac{2\hbar}{m_0 c^2} \left( \frac{1}{\hbar \lambda} \right) \left( \frac{1}{\hbar \lambda'} \right) \sin^2 \frac{\theta}{2}
$$

简化左边：

$$
\frac{1}{\hbar \lambda} - \frac{1}{\hbar \lambda'} = \frac{1}{\hbar} \left( \frac{1}{\lambda} - \frac{1}{\lambda'} \right)
$$

因此，方程变为：

$$
\frac{1}{\lambda} - \frac{1}{\lambda'} = \frac{2\hbar}{m_0 c^2} \cdot \frac{1}{\hbar^2} \cdot \frac{1}{\lambda} \cdot \frac{1}{\lambda'} \sin^2 \frac{\theta}{2}
$$

进一步简化右边：

$$
\frac{1}{\lambda} - \frac{1}{\lambda'} = \frac{2}{m_0 c^2} \cdot \frac{1}{\hbar} \cdot \frac{1}{\lambda} \cdot \frac{1}{\lambda'} \sin^2 \frac{\theta}{2}
$$

乘以 \(\lambda \lambda'\) 来清除分母：

$$
\lambda' - \lambda = \frac{2}{m_0 c^2} \cdot \frac{1}{\hbar} \sin^2 \frac{\theta}{2}
$$

由于 \(\hbar = \frac{h}{2\pi}\)，我们有：

$$
\lambda' - \lambda = \frac{2}{m_0 c^2} \cdot \frac{2\pi}{h} \sin^2 \frac{\theta}{2}
$$

简化常数
***
### intput: 
27. 一个总质量为 $M_{0}$ 的激发原子 对所选定的坐标系静止 它在跃迁到能量比之低 $\Delta w$ 的基态时 发射一个光子 能量为 $\hslash\omega$ 动量为 $\hbar\bar{k}$ 同时受到光子的反冲 因此光子的频率不能正好是 $\nu=\frac{\Delta w}{h}$ 而要略小一些证明这个频率 $\nu=\frac{\Delta w}{h}(1\!-\!\frac{\Delta w}{2M_{\mathrm{0}}c^{2}})$
### standard: 
证明设基态原子静止质量为 $M_{1}$ 跃迁后基态原子反冲动量为 $\vec{p}$ 跃迁前四维动量为 $p_{\mu1}=(0,M_{\L_{0}}c^{2})$ 跃迁后四维动量为 $p_{\mu2}=(\vec{p}+\hbar\vec{k},\hbar\omega+\sqrt{p^{2}c^{2}+M_{1}^{2}c^{4}}\,)$ 由四维动量守恒 $\begin{array}{r}{\left\{\begin{array}{l l}{\vec{p}+\hbar\vec{k}=0,(1)}\\ {M_{0}c^{2}=\hbar\omega+\sqrt{p^{2}c^{2}+M_{1}^{2}c^{4}}\,,}\end{array}\right.}\end{array}$ (2)  由 1 得 $p=\hbar k=\hbar{\frac{\omega}{c}}$ $\therefore p^{2}c^{2}=\hbar^{2}\omega^{2}$ 3  又 $M_{0}c^{2}-M_{1}c^{2}=\Delta w~~~~~~~~~~~~\therefore M_{1}^{2}c^{4}=(M_{0}c^{2}-\Delta w)^{2}$ 4  3 (4)代入 2 得 $(M_{0}c^{2}-\hbar\omega)^{2}=\hbar^{2}\omega^{2}+(M_{0}c^{2}-\Delta w)^{2}$ 整理得 $2M_{\mathrm{o}}c^{2}\hbar\omega=2M_{\mathrm{o}}c^{2}h\nu=2M_{\mathrm{o}}c^{2}\Delta w-\Delta w^{2}$ ∴光子频率 $\nu=\frac{\Delta w}{h}(1\!-\!\frac{\Delta w}{2M_{\mathrm{0}}c^{2}})$
### output: 
 其中 $c$ 是真空中光速.
为了确定 excitation 原子发射 light子时实际 frequency \(\nu\)，我们需要考虑光子和 atom 在相互作用前后的动量守恒。最初， atom 静止，因此其初始动量为零。 after �0mission， light子具有动量 \(\hbar \mathbf{k}\)，而 atom 将向相反方向移动以保持动量守恒。

设 atom 的速度为 \(v\)。 atom 的动量由 \(M_0 v\) 给出。由于 total momentum must be conserved, 我们有：
$$ M_0 v = -\hbar k. $$
解出 \(v\)，我们得到：
$$ v = -\frac{\hbar k}{M_0}. $$

atomic energy change during the transition is \(\Delta w\). The energy of the light子 is \(\hbar \omega\). Using the invariant mass formula in special relativity for the atom before and after the emission, we have:
$$ M_0 c^2 = \sqrt{(M_0 c^2)^2 + (M_0 v)^2} + \hbar \omega. $$
Substituting \(v = -\frac{\hbar k}{M_0}\) into the equation, we get:
$$ M_0 c^2 = \sqrt{(M_0 c^2)^2 + \left(-\frac{\hbar k}{M_0}\right)^2} + \hbar \omega. $$
Simplifying inside the square root, we have:
$$ M_0 c^2 = \sqrt{(M_0 c^2)^2 + \frac{\hbar^2 k^2}{M_0^2}} + \hbar \omega. $$
Factoring out \(M_0^2\) from the terms under the square root, we get:
$$ M_0 c^2 = \sqrt{M_0^4 c^4 + \hbar^2 k^2} + \hbar \omega. $$
Dividing through by \(M_0\), we obtain:
$$ c^2 = \sqrt{c^4 + \frac{\hbar^2 k^2}{M_0^4}} + \frac{\hbar \omega}{M_0}. $$
Isolating the square root term, we get:
$$ c^2 - \frac{\hbar \omega}{M_0} = \sqrt{c^4 + \frac{\hbar^2 k^2}{M_0^4}}. $$
Squaring both sides, we have:
$$ \left(c^2 - \frac{\hbar \omega}{M_0}\right)^2 = c^4 + \frac{\hbar^2 k^2}{M_0^4}. $$
Expanding the left side, we get:
$$ c^4 - 2c^2 \frac{\hbar \omega}{M_0} + \frac{\hbar^2 \omega^2}{M_0^2} = c^4 + \frac{\hbar^2 k^2}{M_0^4}. $$
Subtracting \(c^4\) from both sides, we get:
$$ -2c^2 \frac{\hbar \omega}{M_0} + \frac{\hbar^2 \omega^2}{M_0^2} = \frac{\hbar^2 k^2}{M_0^4}. $$
Multiplying through by \(M_0^4\) to clear the denominators, we get:
$$ -2c^2 \hbar \omega M_0^3 + \hbar^2 \omega^2 M_0^2 = \hbar
***
### intput: 
28. 一个处于基态的原子 吸收能量为 $h\,\nu$ 的光子跃迁到激发态 基态能量比激发态能量低$\Delta w$ 求光子的频率
### standard: 
解 设原子基态静止质量为 $M_{1}$ 激发态静止质量为 $M_{0}$ 光子能量为 $h\nu=\hbar\omega$ 动量为$\hbar\bar{k}$ 原子吸收光子后动量为 $\vec{p}$ 设原子基态时静止  吸收前四维动量为 $p_{\mu1}=(\hbar\bar{k},M_{1}c^{2}+\hbar\omega)$ 吸收后四维动量为 $p_{\mu2}=(\vec{p},\sqrt{p^{2}c^{2}+M_{0}^{2}c^{4}})$   由四维动量守恒 $\begin{array}{r}{\left\{\vec{p}=\hbar\vec{k},(1)\right.}\\ {\left.\left(M_{1}c^{2}+\hbar\omega=\sqrt{p^{2}c^{2}+M_{1}^{2}c^{4}}\right.,}\end{array}$ (2)  由 1 得 $p=\hbar k=\hbar{\frac{\omega}{c}}$ 得 $p^{2}c^{2}=\hbar^{2}\omega^{2}$ 3  又 $M_{0}c^{2}-M_{1}c^{2}=\Delta w\ \ \ \ \frac{\O\!\!\!/}{\O\!\!\!/}\ M_{0}^{2}c^{4}=\left(M_{1}c^{2}+\Delta w\right)^{2}$ 4  3 (4)代入 2 得 $(M_{1}c^{2}+\hbar\omega)^{2}=\hbar^{2}\omega^{2}+(M_{1}c^{2}+\Delta w)^{2}$   整理得 $2M_{1}c^{2}\hbar\omega=2M_{1}c^{2}h\nu=2M_{1}c^{2}\Delta w+\Delta w^{2}$ ∴光子频率 $\nu=\frac{\Delta w}{h}(1+\frac{\Delta w}{2M_{1}c^{2}})$
### output: 
 $\nu$ 和能级差 $\Delta E$ 之间的关系.
答案:
为了确定光子频率 \(\nu\) 和能级差 \(\Delta E\) 之间的关系，我们首先回顾 quantifier 跃迁的基本原理。当一个原子从基态吸收 energy \(h\nu\) 的光子时，它会 jumps up to a higher energy level ( excited state). 这个能级差 \(\Delta E\) 正好等于所吸收的光子能量。

已知：
- 光子能量是 \(h\nu\)
- 基态能量比 excite 状态能低 \(\Delta w\)

根据 quantifier 跳迁的定义，能级差 \(\Delta E\) 是 excite 状态和基态能 difference。因此，我们可以写出：

$$
\Delta E = h\nu
$$

由于题目说明基态能量比 excite 状态能低 \(\Delta w\)，这与 excite 状态和基态能 difference 相同，但符号相反。然而，在 context of quantifier 跳移，我们考虑正差值。 Hence，能级差 \(\Delta E\) 与 light frequency \(\nu\) 成正比。

Thus, the relationship between the light frequency \(\nu\) and the energy level difference \(\Delta E\) is:

\boxed{\Delta E = h\nu}
```
***
