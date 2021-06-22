---
layout: wikipage
title: Optimality Theory overview
chapter: 10
---

Optimality Theory is a constraint-based, parallel grammatical framework. This contrasts with the rule-based serialism of SPE and Hayes. The architecture of OT consists of three primary components: GEN, CON, and EVAL.

The version of OT we define is strict-domination OT, sometimes called classical OT. 

## GEN

GEN takes a given [input]({% link _wiki/candidates.md %}#input) and **generates** a set of possible output forms. Each input/output pair, along with the correspondence relation between them, is a [candidate]({% link _wiki/candidates.md %}).

GEN is a function and it must be defined explicitly. GEN can be thought of as applying any number of possible phonological operations to an input form: adding segments, removing segments, changing segments, and so on. 

## CON

CON is the universal set of constraints. In OT, every language makes use of the the same constraint sets, but with different [rankings]({% link _wiki/rankings.md %}) as the locus of linguistic variation. In terms of Universal Grammar, this means that the constraints themselves are part of UG, but the language-specific rankings are learned. 

## EVAL

EVAL is the component that evaluates the candidates based on a specific ranking of CON. Given an ordering of constraints and a candidate set, EVAL filters the candidate set until only the candidate (or candidates) survives that is *most harmonic*, or optimal. Essentially, the candidate with the fewest violations for the given constraint ranking survives. 


## References