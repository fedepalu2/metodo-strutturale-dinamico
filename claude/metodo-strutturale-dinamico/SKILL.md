---
name: metodo-strutturale-dinamico
description: "Apply the Metodo Strutturale Dinamico (MSD) to clarify complex problems, decisions, projects, conflicts, strategies, social situations, research questions, or personal/work choices through explicit steps and verification gates. Use when the user asks: 'applica il Metodo Strutturale Dinamico', 'analizza con il MSD', 'analisi strutturale dinamica', 'studiamo strutturalmente', 'ordina questo problema', 'aiutami a formulare domanda oggetto interesse', or asks for a rigorous analysis that must define problem, question, object-interest, static context, dynamic process, relations, composition, synthesis, and answer. Do not use for factual lookups, simple summaries, routine writing, or low-stakes choices that do not need a structured study."
---

# Metodo Strutturale Dinamico

Use this skill to run a structured MSD study. The goal is not to debate opinions; it is to move from a vague problem to a clear answer by keeping the user's interest fixed while studying the object in structure, process, relations, and composition.

Supporting files are in `references/` relative to this `SKILL.md`. Load them only when the user request needs that extra context.

Read `references/msd-guide.md` when the user asks for a faithful MSD framing, when you need to explain the method, or when the analysis is significant enough that terminology matters.

Read `references/msd-prompting-guide.md` when the user wants help writing prompts, wants the MSD gates applied interactively, or asks for wording closer to the original method.

Read `references/sources.md` when the user asks for sources, citations, provenance, or when you need to distinguish the Spanish original from the Italian translation.

## Operating Rules

- Do not jump to the answer before completing the gates.
- Keep the **Interest** fixed after Gate 3. If it changes, say so and restart from Gate 2 or 3.
- Prefer one clarifying question when a gate is blocked. If the missing information is not blocking, continue with explicit assumptions.
- Mark each gate as `PASS`, `PASS WITH ASSUMPTIONS`, or `STOP`.
- If a gate is `STOP`, do not continue the study until the user supplies the missing information or authorizes assumptions.
- Use concise language. MSD output should be ordered, not verbose.
- If current facts, legal/medical/financial conditions, prices, dates, or public information matter, verify them before using them in the analysis.

## Workflow

### Step 0: Context Intake

Gather only the context needed to ground the study:

- User's raw situation or decision.
- Explicit constraints, goals, actors, dates, places, resources, or documents.
- Relevant workspace files only if the user references them or the problem depends on them.

**Gate 0 - Context**

Pass only if you can state:

- the situation in one paragraph;
- what is known;
- what is assumed;
- what is missing but not blocking.

Stop if the situation is too vague to identify a problem.

### Step 1: Delimit the Problem

Define the problem before forming a solution. Include:

- theme;
- scope;
- why it matters;
- consequences of not clarifying it;
- constraints and excluded areas.

**Gate 1 - Problem Delimited**

Pass only if the problem is specific enough that a question can be formulated. Stop if it is just a broad topic, mood, or aspiration.

### Step 2: Formulate the Question

Turn the delimited problem into one main question. The question should express what must be clarified, not what answer you already prefer.

Prefer:

- "What is the most coherent direction for X, given Y?"
- "Which aspect of X explains the current difficulty?"
- "How should X be oriented in this moment of its process?"

Avoid:

- multiple unrelated questions;
- leading questions;
- questions that already contain the conclusion.

**Gate 2 - Question Formulated**

Pass only if there is one central question, answerable through the study, aligned with the problem, and not already answered by a simple fact lookup.

### Step 3: Define Object-Interest

Define:

- **Object of Study**: what will be studied.
- **Interest**: the viewpoint, purpose, or sense from which the object is observed.

The same object changes when the interest changes. Make this explicit.

**Gate 3 - Object-Interest Fixed**

Pass only if:

- the object is named precisely;
- the interest is stated as a stable viewpoint;
- the object is not confused with the desired outcome;
- the interest can guide later weighting.

If the interest changes later, return to this gate.

### Step 4: Static Analysis

Locate the object in nested scopes:

- **Major Field**: the wider field that gives cycles, rhythms, rules, or historical pressure.
- **Middle Field**: the field where the object relates dynamically with other objects.
- **Minor Field**: the internal field where the object's components are found.

**Gate 4 - Static Location**

Pass only if all three fields are present and non-overlapping:

- major field explains conditioning context;
- middle field explains relational environment;
- minor field explains internal components.

### Step 5: Dynamic Analysis

Study the object through three lenses. For each lens, do:

1. differentiate the relevant elements;
2. complement them by describing their relationships;
3. synthesize what this lens reveals according to the fixed interest.

#### 5A. Process

Identify the object's movement through time:

- origin or antecedents;
- development;
- current moment;
- tendencies, inflection points, possible decline or overcoming.

Use a 4-step or 12-step process only when useful. Otherwise use a compact timeline.

#### 5B. Relations

Identify other objects in the middle field and their dynamic relation to the object:

- enabling forces;
- limiting forces;
- neutral or ambiguous forces;
- dependencies;
- conflicts and convergences.

If helpful, score relations from strong negative to strong positive, but do not reduce the analysis to scoring.

#### 5C. Composition

Identify internal components and points of contact with the external field:

- main components;
- tensions among components;
- weakest and strongest components;
- external contact points where the object exchanges influence with its environment.

**Gate 5 - Dynamic Analysis Complete**

Pass only if process, relations, and composition each include differentiation, complementation, and a lens synthesis. Stop or mark assumptions if one lens lacks enough information.

### Step 6: Synthesis

Build a new view of the object. Do not merely summarize. Relate the differences found across process, relations, and composition, weighted by the fixed interest.

The synthesis should answer:

- What does the object look like now that it has been studied structurally and dynamically?
- What was invisible in the initial formulation?
- What tension, movement, or relation best explains the problem?

**Gate 6 - Real Synthesis**

Pass only if the synthesis produces a new formulation of the object and is clearly more than a recap.

### Step 7: Response and First Action

Answer the original question using the synthesis. The response must clarify the delimited problem.

Include:

- direct answer;
- reasoning from the synthesis;
- consequences or risks;
- one first operational step;
- what to observe later to verify whether the answer was useful.

**Gate 7 - Coherent Response**

Pass only if the response:

- answers the question from Gate 2;
- stays aligned with the object-interest from Gate 3;
- clarifies the problem from Gate 1;
- distinguishes evidence from assumptions;
- gives one concrete next step.

## Output Format

Use this format unless the user asks for a different one:

```markdown
## Analisi Strutturale Dinamica: {topic}

### Registro Gate
| Gate | Esito | Nota |
|---|---|---|
| 0. Contesto | PASS / PASS WITH ASSUMPTIONS / STOP | ... |
| 1. Problema | ... | ... |
| 2. Domanda | ... | ... |
| 3. Oggetto-Interesse | ... | ... |
| 4. Statica | ... | ... |
| 5. Dinamica | ... | ... |
| 6. Sintesi | ... | ... |
| 7. Risposta | ... | ... |

### Problema Delimitato
...

### Domanda
...

### Oggetto-Interesse
- Oggetto:
- Interesse:

### Ubicazione Statica
- Ambito maggiore:
- Ambito medio:
- Ambito minore:

### Analisi Dinamica
#### Processo
...

#### Relazioni
...

#### Composizione
...

### Sintesi
...

### Risposta
...

### Primo Passo Operativo
...

### Cosa Osservare Dopo
...
```

## Short Mode

For small decisions, keep all steps but compress the output. Never remove the gates; instead use one-line gate notes and short sections.

## Optional Report

Create a file only if the user asks for a report or transcript. When saving, include the gate registry, assumptions, and source references.
