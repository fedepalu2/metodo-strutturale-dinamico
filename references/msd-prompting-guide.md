# MSD Prompting Guide

Use this guide to help users formulate better prompts for the Metodo Strutturale Dinamico. It provides short source-anchored phrases, paraphrased guidance, and prompt templates for each gate.

Primary source: Jorge Pompei e collaboratori, *Teoria e pratica del Metodo Strutturale Dinamico*, CEHBA, 2008/06. Use the Spanish original when fidelity matters; use the Italian translation for Italian terminology. For exact URLs and source hierarchy, read `sources.md`.

## Source-Anchored Phrases

Use these as compact anchors, not as long quotations:

- Oggetto-Interesse anchor: "Definire con precisione l'Oggetto - Interesse."
- Synthesis anchor: "La sintesi non e' un riassunto del riassunto."
- Methodic lens anchor: "Triplice Analisi Metodica."
- Response style anchor: "chiara e precisa."

Do not expand these into long quotations unless the user explicitly asks and copyright limits allow it. Prefer paraphrase and source links.

## Prompt Shape

A strong MSD prompt should include:

1. The situation or decision.
2. Why it matters.
3. The desired clarification, not the desired answer.
4. The object to study, if known.
5. The interest or viewpoint, if known.
6. Constraints, time frame, actors, and sources.
7. Permission to stop at gates if information is missing.

Basic invocation:

```text
Applica il Metodo Strutturale Dinamico a questa situazione. Prima delimita il problema, poi formula una domanda centrale, definisci Oggetto-Interesse, fai analisi statica e dinamica, sintetizza e rispondi. Usa gate espliciti e fermati se un passaggio non e' verificabile.

Situazione: ...
Perche' importa: ...
Vincoli: ...
Fonti o contesto: ...
```

## Gate Prompt Templates

### Gate 0: Context

```text
Raccogli il contesto minimo necessario. Distingui cio' che e' noto, cio' che assumi e cio' che manca. Se non puoi identificare il problema, fermati e fai una sola domanda.
```

### Gate 1: Problem

```text
Delimita il problema indicando tema, portata, struttura, importanza e conseguenze se non viene chiarito. Escludi esplicitamente cio' che non rientra nello studio.
```

### Gate 2: Question

```text
Formula una sola domanda centrale che esprima cio' che deve essere chiarito. Evita domande tendenziose o domande multiple.
```

### Gate 3: Object-Interest

```text
Definisci Oggetto di Studio e Interesse. Verifica che l'Oggetto non sia il risultato desiderato e che l'Interesse sia un punto di vista stabile per pesare tutta l'analisi.
```

### Gate 4: Static Analysis

```text
Ubica l'Oggetto in tre ambiti: maggiore, medio e minore. Il maggiore deve dare il contesto che condiziona cicli e ritmi; il medio deve mostrare le relazioni; il minore deve contenere i componenti interni.
```

### Gate 5: Dynamic Analysis

```text
Studia l'Oggetto in dinamica attraverso processo, relazioni e composizione. Per ogni lente: differenzia gli elementi, descrivi come si completano o si tensionano, e formula una mini-sintesi secondo l'Interesse fissato.
```

### Gate 6: Synthesis

```text
Elabora una sintesi che non sia un riassunto. Riformula l'Oggetto mostrando cosa ora appare con piu' chiarezza rispetto alla formulazione iniziale.
```

### Gate 7: Response

```text
Rispondi alla domanda iniziale in modo chiaro e preciso. Mostra come la risposta chiarisce il problema, quali assunzioni restano, qual e' il primo passo operativo e cosa osservare dopo.
```

## Full Prompt Template

```text
Usa il Metodo Strutturale Dinamico.

Situazione:
{descrivi la situazione}

Perche' e' importante:
{posta in gioco, conseguenze, urgenza}

Vincoli:
{tempo, risorse, persone, valori, rischi}

Fonti o contesto disponibile:
{documenti, dati, esperienza, link}

Istruzioni:
- Segui tutti i gate: Contesto, Problema, Domanda, Oggetto-Interesse, Statica, Dinamica, Sintesi, Risposta.
- Per ogni gate indica PASS, PASS WITH ASSUMPTIONS o STOP.
- Se un gate e' STOP, fermati e fai una sola domanda.
- Non dare la risposta prima della sintesi.
- Mantieni fisso l'Interesse dopo averlo definito.
```

## Compact Prompt Template

```text
Analizza con il MSD questa decisione: {decisione}. Definisci problema, domanda e Oggetto-Interesse; poi fai statica, dinamica, sintesi e risposta. Usa gate espliciti e dichiara le assunzioni.
```

## Prompt Repair

When a user gives a vague prompt, rewrite it before analysis:

```markdown
### Prompt MSD riformulato
Situazione: ...
Problema da chiarire: ...
Domanda centrale: ...
Oggetto-Interesse proposto: ...
Assunzioni: ...
Gate potenzialmente bloccanti: ...
```

Then ask for confirmation only if the proposed Object-Interest would materially change the study.
