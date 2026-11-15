"""Mathematical checks accompanying Retained-State Dynamics v0.5.1.
Python 3 + NumPy; run with warnings as errors and assertions enabled.
Twenty-two groups, including illustrative identity 17. No empirical data.
"""
import numpy as np
rng=np.random.default_rng(20261115)
alpha,eta,kappa=0.8,0.5,2.0

def rollout(inputs, initial=0.0, alpha=alpha, eta=eta, nu=0.0):
    states=[float(initial)]
    for u in inputs:
        m=states[-1]
        states.append(alpha*m+eta*u+nu*np.tanh(m))
    return np.array(states)
def terminal(h, **kw): return rollout(h, **kw)[-1]
def close(x,y): assert np.allclose(x,y,rtol=1e-12,atol=1e-12),(x,y)
def passed(n,label): print(f'PASS {n}: {label}')
sig=lambda x:1/(1+np.exp(-x))

mA=terminal([1,-1]); mB=terminal([-1,1])
close([mA,mB,kappa*(mA-mB)],[-0.1,0.1,-0.4]); passed(1,'swapped-order states and contrast')

u=rng.uniform(-1,1,40); m0=0.37
close(rollout(u,initial=m0),[alpha**n*m0+sum(eta*alpha**(n-1-j)*u[j] for j in range(n)) for n in range(41)])
passed(2,'recurrence equals closed-form convolution')

A=rollout(np.zeros(10),initial=mA); B=rollout(np.zeros(10),initial=mB)
close(kappa*(A-B),-0.4*alpha**np.arange(11)); passed(3,'simulated delay decay')

common=rng.uniform(-0.9,0.9,10)
close(rollout(common,initial=mA)-rollout(common,initial=mB),A-B); passed(4,'common-input invariance (D1)')

for mi in [-0.4,0.0,0.7]:
    sham=np.zeros(10); probe=sham.copy(); probe[0]=0.3
    close(kappa*(rollout(probe,initial=mi)-rollout(sham,initial=mi))[1:],kappa*eta*0.3*alpha**np.arange(10))
passed(5,'D1 probe response independent of history')

v=0.3
incA=sig(kappa*(alpha*mA+eta*v))-sig(kappa*alpha*mA); incB=sig(kappa*(alpha*mB+eta*v))-sig(kappa*alpha*mB)
assert not np.isclose(incA,incB,rtol=0,atol=1e-5); passed(6,'probability increments differ by saturation only')

s=-3.7; close(kappa*rollout(u,initial=m0),(kappa/s)*rollout(u,initial=s*m0,eta=s*eta))
passed(7,'negative-scale reparameterisation (sign unidentified)')

for r in [0.0,0.5,0.8,0.99,1.0]:
    close(kappa*(terminal([1,-1],alpha=r)-terminal([-1,1],alpha=r)),-2*kappa*eta*(1-r))
    late=kappa*terminal([0,1],alpha=r); early=kappa*terminal([1,0],alpha=r)
    close(late,kappa*eta); close(early/late,r)
passed(8,'recency boundary cases and pulse identification')

amp=kappa*terminal([0,1]); r_hat=kappa*terminal([1,0])/amp
close(2*amp*(r_hat-1)*r_hat**np.arange(11),kappa*(A-B)); passed(9,'order/delay predicted from pulses only')

LC,LD,LE=[kappa*terminal(h) for h in ([0,1],[0,0],[1,0])]
close(kappa*mA-LD,(LE-LD)-(LC-LD)); passed(10,'superposition: A-D = (E-D)-(C-D)')

a,b,cx,r,g,d=0.3,0.2,0.1,0.8,1.0,0.4
assert np.max(np.abs(np.linalg.eigvals([[a,b],[cx,r]])))<1
x=[0.2]; m=[-0.3]
for n in range(30):
    pred=a*x[n]+g*u[n]+b*r**n*m[0]+sum(b*r**(n-1-j)*(cx*x[j]+d*u[j]) for j in range(n))
    act=a*x[n]+b*m[n]+g*u[n]; close(pred,act)
    x.append(act); m.append(r*m[n]+cx*x[n]+d*u[n])
passed(11,'hidden-state elimination with initial term')

zero=np.zeros(10); nz=np.full(10,0.7)
d0=rollout(zero,initial=mA,nu=0.15)-rollout(zero,initial=mB,nu=0.15)
d1=rollout(nz,initial=mA,nu=0.15)-rollout(nz,initial=mB,nu=0.15)
assert np.max(np.abs(d0-d1))>1e-3; passed(12,'fixed nonlinear D2 also breaks common-input invariance')

# D3-w: recorded pre-choice weight W scales probe response; D1 does not.
lam,zeta=1.0,2.0
for W in [0.5,1.0,2.0]:
    eff=lam*W*zeta*(rollout(probe,initial=mA)-rollout(sham,initial=mA))[1:]
    close(eff,W*kappa*eta*0.3*alpha**np.arange(10))
    d1eff=kappa*(rollout(probe,initial=mA)-rollout(sham,initial=mA))[1:]
    close(d1eff,kappa*eta*0.3*alpha**np.arange(10))
passed(13,'D3-w probe response scales with recorded W; D1 invariant')

eta_n=-0.5; tr=rollout(u,initial=m0,eta=eta_n); k=np.arange(41)
assert np.all(np.abs(tr)<=alpha**k*abs(m0)+abs(eta_n)*(1-alpha**k)/(1-alpha)+1e-12)
passed(14,'bounded-input inequality')

# Additional specification checks and counterexamples (15--20).
for W in [0.5,1.0,2.0]:
    baseline=rollout(sham,initial=-0.25)
    perturbed=rollout(probe,initial=-0.25)
    close(kappa*W*(perturbed-baseline)[1:],W*kappa*eta*0.3*alpha**np.arange(10))
passed(15,'paired recurrence at fixed exogenous W gives proportional response')

# Probe changes readout weight: old formula omits an extra term.
ms=rollout([0.0],initial=0.7)[-1]
mp=rollout([0.3],initial=0.7)[-1]
Ws,Wp=1.0,1.2
actual=kappa*(Wp*mp-Ws*ms)
full=kappa*(Ws*(mp-ms)+(Wp-Ws)*mp)
naive=kappa*Ws*(mp-ms)
close(actual,full);assert abs(actual-naive)>0.1
passed(16,'probe-dependent W requires extra state/readout term')

# Illustrative identity (not a test that can fail): a fixed context-conditioned
# readout G(C,m)=kappa*C*m is algebraically the D3-w readout when W=C.
for context in [0.5,1.0,2.0]:
    for state in [-0.3,0.0,0.7]:
        fixed_readout=lambda C,m:kappa*C*m
        close(fixed_readout(context,state),kappa*context*state)
passed(17,'illustrative identity: fixed context-conditioned readout equals D3-w when W=C')

# Conditional factorial regression on exact logits; not a statistical power test.
rows=[];ys=[]
for H in [0.0,1.0]:
    for W in [0.5,1.0,2.0]:
        for vv in [0.0,0.3]:
            state=rollout([vv,0.0],initial=0.2+0.4*H)[-1]
            rows.append([1,H,vv,H*vv,W,W*vv,W*H])
            ys.append(0.1+0.07*W+kappa*W*state)
X=np.array(rows);y=np.array(ys)
assert np.linalg.matrix_rank(X)==7
coef=np.linalg.lstsq(X,y,rcond=None)[0]
close(coef,[0.1,0,0,0,0.07+kappa*alpha**2*0.2,kappa*eta*alpha,kappa*alpha**2*0.4])
# Direction check: refit with reversed coupling orientation; probe-weight coefficient must flip sign.
y_neg=np.array([0.1+0.07*W-kappa*W*rollout([vv,0.0],initial=0.2+0.4*H)[-1] for H in [0.0,1.0] for W in [0.5,1.0,2.0] for vv in [0.0,0.3]])
coef_neg=np.linalg.lstsq(X,y_neg,rcond=None)[0]
close(coef_neg[5],-kappa*eta*alpha); assert coef[5]>0>coef_neg[5]
passed(18,'conditional regression constraints and direction depend on declared coupling')

# State/readout scale ambiguity persists with independently recorded W.
scale=4.0
states=rollout(u,initial=m0)
scaled=rollout(u,initial=scale*m0,eta=scale*eta)
Wseries=np.linspace(0.5,2.0,len(states))
close(kappa*Wseries*states,(kappa/scale)*Wseries*scaled)
passed(19,'pre-recorded W does not remove state-scale ambiguity')

# Exact zero-order-hold update for a conventional exponential dielectric response.
# Normalised polarisation p=P/epsilon0 has electric-field units; not a physical-law test.
tau,dt,chi_s,Wmat=1.7,0.2,0.8,1.3
ret=np.exp(-dt/tau);coupling=chi_s*Wmat*(1-ret)
fields=np.array([0.4,-0.2,0.1,0.0])
traj=rollout(fields,initial=0.15,alpha=ret,eta=coupling)
for n in range(len(fields)+1):
    analytic=0.15*np.exp(-n*dt/tau)
    for j in range(n):
        analytic+=chi_s*Wmat*fields[j]*(np.exp(-(n-j-1)*dt/tau)-np.exp(-(n-j)*dt/tau))
    close(traj[n],analytic)
passed(20,'conventional exponential material response matches state recurrence')

# 21. Locus of weighting: readout (decision-time) versus storage (encoding) gain.
# History is prepared BEFORE context assignment; probe/sham follow context; readout k steps later.
# Within each context: history contrast h_c (sham) and probe effect p_c (history-off).
def locus_contrasts(g, mode, k=2, vprobe=0.3):
    mH1=terminal([1.0,0.0]); mH0=terminal([0.0,0.0])          # prepared before context
    eta_c=eta*g if mode=='storage' else eta                     # storage gain acts on post-context inputs only
    alpha_c=alpha*g if mode=='retention' else alpha             # retention comparator
    gain=g if mode=='readout' else 1.0                          # decision-time readout gain
    def L(m_pre, v):
        st=rollout([v]+[0.0]*(k-1), initial=m_pre, alpha=alpha_c, eta=eta_c)[-1]
        return 0.3*g + kappa*gain*st                              # 0.3*g: direct context effect on U
    return L(mH1,0.0)-L(mH0,0.0), L(mH0,vprobe)-L(mH0,0.0)
gains=[0.5,1.0,1.2]
ratios={mode:[h/p for h,p in (locus_contrasts(g,mode) for g in gains)] for mode in ['readout','storage','retention']}
close(ratios['readout'],[ratios['readout'][0]]*3)               # invariant across contexts
assert np.ptp(ratios['storage'])>0.1 and np.ptp(ratios['retention'])>0.1
h1,p1=locus_contrasts(2.0,'readout'); h0,p0=locus_contrasts(1.0,'readout')
close([h1/h0,p1/p0],[2.0,2.0])                                   # both contrasts scale by the same gain
passed(21,'readout weighting keeps history/probe ratio invariant; storage and retention comparators do not')

# 22. Joint post-context input-gain and retention changes mimic readout gain
# at a fixed delay, despite no readout gain in the alternative mechanism.
def mixed_contrasts(gain, k=2, vp=0.3):
    mh=terminal([1.0,0.0]); mz=terminal([0.0,0.0])
    def output(mpre,probe_value):
        return kappa*rollout([probe_value]+[0.0]*(k-1),initial=mpre,
                             alpha=alpha*gain,eta=eta*gain)[-1]
    return output(mh,0.0)-output(mz,0.0),output(mz,vp)-output(mz,0.0)
for delay in [1,2,3]:
    for gain in [0.5,1.0,1.2]:
        hm,pm=mixed_contrasts(gain,k=delay)
        hr,pr=locus_contrasts(gain**delay,'readout',k=delay)
        close([hm,pm],[hr,pr])
        close(hm/pm,alpha*terminal([1.0,0.0])/(eta*0.3))
# One fixed readout gain cannot match the same nontrivial mixed gain at
# both delays: the alternative gives gain**k rather than a fixed gain.
gain=1.2
h1m,p1m=mixed_contrasts(gain,k=1)
h2m,p2m=mixed_contrasts(gain,k=2)
h1b,p1b=mixed_contrasts(1.0,k=1)
h2b,p2b=mixed_contrasts(1.0,k=2)
assert abs(h1m/h1b-h2m/h2b)>0.1
passed(22,'joint storage and retention changes mimic readout gain at one delay')
