# Metodo Strutturale Dinamico Skills

One repository with two compatible versions of the Metodo Strutturale Dinamico (MSD) skill:

- **Codex version**: available at the repository root.
- **Claude / Anthropic version**: available in `claude/metodo-strutturale-dinamico/`.

Both versions implement the same workflow with explicit verification gates:

1. Context
2. Problem
3. Question
4. Object-Interest
5. Static analysis
6. Dynamic analysis
7. Synthesis
8. Response

## Codex Installation

Install the root of this repository as a Codex skill:

```text
~/.codex/skills/metodo-strutturale-dinamico/
```

Expected Codex layout:

```text
metodo-strutturale-dinamico/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── msd-guide.md
    ├── msd-prompting-guide.md
    └── sources.md
```

## Claude Installation

Copy the Claude skill folder:

```text
claude/metodo-strutturale-dinamico/
```

to:

```text
~/.claude/skills/metodo-strutturale-dinamico/
```

Expected Claude layout:

```text
metodo-strutturale-dinamico/
├── SKILL.md
├── README.md
└── references/
    ├── msd-guide.md
    ├── msd-prompting-guide.md
    └── sources.md
```

## Prompt Examples

```text
Applica il Metodo Strutturale Dinamico a questa situazione...
```

```text
Analizza con il MSD questa decisione e usa i gate espliciti.
```

```text
Aiutami a formulare domanda, oggetto e interesse prima di rispondere.
```

## Report

See `REPORT.md` for the single comparison report covering both versions.

## Sources

The skill references Jorge Pompei y colaboradores, *Teoria y practica del Metodo Estructural Dinamico*, CEHBA, 2008/06, and the Italian translation *Teoria e pratica del Metodo Strutturale Dinamico*.

Detailed source links and citation guidance are in `references/sources.md` and `claude/metodo-strutturale-dinamico/references/sources.md`.
