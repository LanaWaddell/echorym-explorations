# RESULT — Moiré mechanic falsification test

> **CORRECTED after independent verification (project-side review).** Three fixes, logged
> per append-only discipline rather than silently rewritten:
> 1. **Entanglement threshold corrected to exactly γ = 2/3.** The original text quoted
>    γ ≈ 0.8 (F4 section) and γ ≈ 0.75 (CHSH section) — both grid-sampling artifacts, and
>    the disagreement between them is the retrofitted-precision failure mode in miniature.
>    The dephased state is exactly a Werner state with visibility v = 1−γ (verified to
>    machine precision), so all three thresholds are **analytic**: Bell at 1−1/√2 ≈ 0.293,
>    entanglement at **2/3**, interference at 1. Closed-form beats empirical.
> 2. **F2 reweighted.** "Best separable model matching marginals" is only the *product* of
>    marginals; a correlated separable mixture reproduces any single-θ joint distribution.
>    Nonclassicality is carried by CHSH and the γ = 1 limit, not F2. The curvature argument
>    is retracted.
> 3. **F5 language corrected.** The entangled fringe has N narrow peaks per period, not one
>    privileged angle. The verified claim is *feature width ~ 1/N under entanglement vs
>    1/√N without*. "Magic angle" (a single isolated value, from band flattening — a
>    different mechanism) stays in the metaphor lane.

**Tests:** DN §7.7 (interference gap) and §7.6 (moiré as its closure)
**Verdict:** **Mechanic survives all five falsifiers. Worth building.**
**Caveat:** one part of the original claim was wrong, and the correction is the
most useful result here.

---

## What was tested

> Two committed regions held in maintained phase produce joint effects neither
> produces alone, with the phase relation (twist angle) determining whether
> combination is constructive or destructive, and with **sharp special values**
> (magic-angle analogue).

Two regions modelled as two qubits. Each enters in plural superposition, is
coupled at relative twist θ, then re-interfered. **θ is applied as a
controlled-phase — a purely relational parameter that alters no single region's
marginal state.**

| # | Falsifier | Outcome |
| --- | --- | --- |
| F1 | Joint outcomes independent of twist | **Survived** — P(00) sweeps 1.000 → 0.250 |
| F2 | Classical mixture with identical marginals reproduces it | **Survived, reweighted** — the 0.0625 gap is vs the *product* of marginals only; nonclassicality is carried by CHSH and the γ = 1 limit |
| F3 | Joint observable equals product of marginals | **Survived** — excess ⟨ZZ⟩ − ⟨Z⟩⟨Z⟩ peaks at 0.250 |
| F4 | Effect survives full dephasing | **Survived** — contrast falls linearly to zero at γ = 1 |
| F5 | No mechanism produces sharp special values | **Survived, with a correction** — see below |

---

## F1 / F3 — the joint effect is real and relational

| twist | ⟨Z_A⟩ | ⟨Z_B⟩ | ⟨ZZ⟩ | ⟨Z⟩⟨Z⟩ | **excess** | concurrence |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 |
| π/4 | 0.854 | 0.854 | 0.854 | 0.729 | **0.125** | 0.383 |
| π/2 | 0.500 | 0.500 | 0.500 | 0.250 | **0.250** | 0.707 |
| 3π/4 | 0.146 | 0.146 | 0.146 | 0.021 | **0.125** | 0.924 |
| π | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

The excess column is the mechanic. A model that knows each region perfectly and
in isolation mispredicts the joint outcome by up to 0.25 — **a joint effect
neither region produces alone**, produced by nothing but the relation between
them. Concurrence rises monotonically with twist: the twist is *generating* the
nonseparable relation, not merely revealing it.

## F2 — not reproducible classically *(reweighted; see correction log)*

The product of the marginals mispredicts P(00) by up to 0.0625. This rules out
*uncorrelated* classical models only — a correlated separable mixture can match
any single-θ joint distribution. What no classical model can do is the whole
package: CHSH violation (device-independent, below) and twist-dependence that
survives only while coherence does (F4's γ = 1 limit kills it). Those two carry
the nonclassicality claim; F2 alone does not. The curvature argument in the
original is retracted — classical models may depend nonlinearly on a physical
parameter.

## F4 — coherence-dependent, so T2 is load-bearing

Dephasing applied **during coupling** (the relation decaying, not the states):

| γ | P(00) contrast | max concurrence |
| --- | --- | --- |
| 0.00 | 0.750 | 1.000 |
| 0.40 | 0.450 | 0.400 |
| 0.80 | 0.150 | 0.000 |
| 1.00 | **0.000** | 0.000 |

The mechanic dies exactly as the phase relation dies. This confirms §7.1's split:
the regions are intact throughout — only the relation decays, and the joint
effect goes with it. **Fragmentation-by-neglect (Channel C) has a working
physical model.**

Note the ordering: **entanglement dies before interference does.** Concurrence
hits zero at exactly **γ = 2/3** (the dephased state is a Werner state with
visibility v = 1−γ; C = max(0, (3v−1)/2)) while twist-dependence persists to
γ = 1. Two distinct resources degrading at different rates — a second instance
of the T1/T2 pattern, and a candidate graded capture measure. *(Original text
said γ ≈ 0.8 — a grid artifact; see correction log.)*

---

## F5 — the correction, and the most useful result

**Two regions do not produce sharp special values.** Two-register interference is
smooth and sinusoidal. There is no magic angle at N = 2. That part of the v0.3
claim was wrong.

Sharpness requires **many** regions — and how it scales depends on whether they
are entangled:

| N | product FWHM | × √N | entangled FWHM | × N |
| --- | --- | --- | --- | --- |
| 4 | 1.641 | 3.28 | 0.785 | 3.142 |
| 16 | 0.830 | 3.32 | 0.196 | 3.142 |
| 64 | 0.416 | 3.33 | 0.049 | 3.143 |
| 128 | 0.294 | 3.33 | 0.0246 | 3.145 |

- **Product-state regions:** width ~ **1/√N** (shot-noise limit)
- **Entangled regions:** width ~ **1/N** (Heisenberg limit)

Both constants hold to four significant figures across six octaves.

> **Narrow interference features are an entanglement signature.** Merely plural
> regions sharpen at √N (shot-noise limit); nonseparably related regions sharpen
> at N (Heisenberg limit). The entangled fringe has N narrow peaks per period —
> not one privileged angle. A sharply-tuned feature in Echorym would be
> *evidence of* entanglement across regions, not decoration on top of it.
> "Magic angle" — a single isolated value arising from band flattening, a
> different mechanism — stays in the metaphor lane.

This connects §7.5 and §7.7, which were separate open problems: the interference
mechanic and the entanglement earning test are the same phenomenon measured two
ways.

---

## CHSH — the §7.5 fork resolves toward option (b)

Analytic Horodecki criterion, S_max = 2√(m₁+m₂):

| twist | concurrence | CHSH S_max | violates? |
| --- | --- | --- | --- |
| 0 | 0.000 | 2.000 | no |
| π/4 | 0.383 | 2.141 | **yes** |
| π/2 | 0.707 | 2.449 | **yes** |
| 3π/4 | 0.924 | 2.723 | **yes** |
| π | 1.000 | **2.828** | **yes** |

The twist produces **Bell-certifiable** entanglement across essentially the whole
range, reaching the Tsirelson bound (2√2 = 2.8284) exactly at θ = π.

Under dephasing, violation is lost at **γ = 1 − 1/√2 ≈ 0.293** — the standard
Werner threshold — while concurrence persists to exactly **γ = 2/3**. All three
thresholds are analytic, because the dephased state is exactly Werner:
Bell violation (1 − 1/√2) → entanglement (2/3) → interference (1). *(Original
text said ≈ 0.75 — a different grid artifact from the same quantity; see
correction log.)*

**A three-tier graded relational-integrity measure falls out of this for free**,
and the top tier is device-independent.

---

## What this does and does not establish

**Established.** The mechanic is real physics, cheaply simulable, coherence-
dependent, classically irreproducible, and Bell-certifiable. §7.7's requirement
is met: joint effects neither region produces alone, with the phase relation
determining the outcome. §7.5's fork has an answer — option (b), because the
same two-qubit build delivers both.

**Not established.** That Echorym *regions* map onto qubits in any meaningful
way. This shows the mechanic is available; the mapping from a world-region's
character to a register state is entirely unspecified and is the real design
work. Nothing here touches C1-under-Hughes.

**Corrected in the note.** §7.6's moiré entry should say sharpness requires
N-region entanglement, not two-layer twist. The two-layer picture gives
interference; the magic angle needs the many-layer entangled case.

---

## Follow-on

1. **Amend DN §7.6/§7.7** — record F5's correction and the entanglement/sharpness
   link. Move moiré from `[candidate]` to `[validated-available]`: the physics is
   validated as available; in-Echorym status stays pending the region → register
   mapping. (Promoting straight to `[load-bearing]` would collapse the §2.2
   possibility-class / commit-state axes.)
2. **§7.5 fork → (b)**, on evidence rather than preference. Unlocks §5.1
   (monogamy) and the §7.3 QEC mapping.
3. **Three-tier relational integrity** (Bell / entanglement / interference) as a
   candidate graded measure for §8.2 — the strongest tier is
   device-independent, which is a property no classical measure in the note has.
4. **Open:** how a region's character maps to a register state. Everything above
   is contingent on that.

Test scripts: `moire_test.py`, `moire_test2.py`, `moire_test4.py`.
**Note:** `moire_test.py`'s F4 block is **superseded** by `moire_test2.py` (it
dephases after the final interference and contains unused dead code); the F1/F2/F5
blocks in test1 remain valid. Threshold verification (Werner identity to machine
precision, exact 2/3 zero): run in-session, reproducible from the state/dephase/
concurrence functions in `moire_test4.py`.
