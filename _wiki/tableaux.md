---
layout: wikipage
title: Tableaux
level: basic
chapter: 4
---

Much of the claims and argumentation for OT are demonstrated using tableaux (sg. tableau). A properly formatted tableau gives information both on the candidates and constraints, as well as some language-specific ranking information. There are two general types of tableaux, each eith their own purposes: violation tableaux (VTs) and comparative tableaux (CTs). 

## Violation Tableaux

A violation tableau shows the [constraints]({% link _wiki/constraints.md %}) as column headings and one [candidate]({% link _wiki/candidates.md %}) per row. The violation marks incurred by each candidate are shown in the corresponding cells either as a number of asterisks (e.g. ***) or as a numberal (e.g. 3). 

|         | /panpa/ | Max | Dep | Agree | Ident |
| ------- | ------- | --- | --- | ----- | ----- |
|         | panpa   |     |     | *     |       |
| &#9758; | pampa   |     |     |       | *     |
|         | papa    | *   |     |       |       |
|         | panapa  |     | *   |       |       |
{:.ottab .vt}

The pointing finger shows the winning candidate. This could be in any particular row. Usually, the columns are ordered left-to-right in a way that reflects their intended [ranking]({% link _wiki/rankings.md %}) for that language; however, VTs are not the best vehicle for conveying ranking information. **Any arguments about ranking should be made with CTs**, described in the next section. 

That being said, there are a number of other conventions for VTs relating to ranking. If there is a solid vertical rule between two constraint columns, that is meant to indicate that those two constraints are curically ordered with respect to each other (such that the constraint on the left must dominate the constraint on the right). Likewise, if there is a dashed line separating two columns, that means those two constraints are *not* crucially ordered with respect to each other. I don't follow this convention here, as it leads to ambiguity and it's tricky to format.

Additionally, an exclamation mark inside a VT indicates a *fatal violation*, or a particular violation mark that crucially separates two candidates. 

|         | /ta/ | *a    |
| ------- | ---- | ----- |
| &#9758; | ta   | \*    |
|         | taa  | \*\*! |
{:.ottab .vt}

In this dummy VT, both the [ta] candidate and the [taa] candidate incur one violation of \*a, so these violation marks effectively cancel out. However, [taa] has a second violation while [ta] does not. The exclamation mark is placed right after this violation to show that it is *fatal*, or is the death knell for this candidate. It is not uncommon to also see all cells to the right of an exclamation mark shaded gray to indicate that this candidate is no longer a possible optimum.

## Comparative Tableaux

Comparative tableaux are a transformation from VTs into an object that conveys explicit ranking information. In a CT, each row now represents a comparison between the winning candidate (optimum) and a particular loser, or a W~L pair. (The tilde in this context indicates that two forms are being explicitly compared.)

Instead of violation counts, the crucial information in a CT is now: does a particular constraint prefer the winner, or does it prefer the loser? Here, "prefer" refers to the number of violation marks assigned by a constraint. A constraint that assigns fewer marks to form A than to form B is said to prefer form A. 

Any VT with clear violation marks and intended winner can be turned into a CT in a few steps. The CT version of the VT from the previous section is shown below.

| /panpa/ | Max | Dep | Agree | Ident |
| ------- | --- | --- | ----- | ----- |
| pampa   |     |     |       | *     |
| panpa   |     |     | W     | L     |
| papa    | W   |     |       | L     |
| panapa  |     | W   |       | L     |
{:.ottab .ct}

Notice that the majority of information conveyed are just cells with either a W or an L. In the first column, the constraint Max is shown with a W in the row for [papa]. The candidate [papa] contains one instance of deletion, so when this is compared with the winner [pampa], which has 0 instances of deletion, Max prefers the winner, and thus a W is marked. No other candidates contain instances of deletion, so Max has no preference with respect to these. 

In the above tableau, the winner is shown on the first row, with violation marks still present. This is only for convenience and can be ommitted. A pure CT contains only Ws and Ls. However, in this representation, it might not be clear exactly *how* violations are assigned. A "hybrid" tableau style is popular that includes both the Ws and Ls of CTs, and the violation marks of VTs.

| /panpa/ | Max   | Dep  | Agree  | Ident |
| ------- | ----- | ---- | ------ | ----- |
| pampa   |       |      |        | \*    |
| panpa   |       |      | W   \* | L     |
| papa    | W  \* |      |        | L     |
| panapa  |       | W \* |        | L     |
{:.ottab .ct}