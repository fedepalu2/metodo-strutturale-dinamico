# Metodo Strutturale Dinamico Skill for Claude

Claude-compatible skill for applying the Metodo Strutturale Dinamico (MSD) to complex problems, decisions, projects, conflicts, strategies, research questions, and personal or work choices.

The skill guides Claude through explicit verification gates:

1. Context
2. Problem
3. Question
4. Object-Interest
5. Static analysis
6. Dynamic analysis
7. Synthesis
8. Response

## Installation in Claude Code

Copy this repository folder to:

```text
~/.claude/skills/metodo-strutturale-dinamico/
```

The expected layout is:

```text
metodo-strutturale-dinamico/
├── SKILL.md
└── references/
    ├── msd-guide.md
    ├── msd-prompting-guide.md
    └── sources.md
```

Then invoke it directly with:

```text
/metodo-strutturale-dinamico
```

or ask Claude naturally, for example:

```text
Applica il Metodo Strutturale Dinamico a questa decisione...
```

## Installation in Claude.ai

Zip the skill folder and upload it as a custom skill from Claude settings, where custom skills are available.

## Sources

The skill references:

- Jorge Pompei y colaboradores, *Teoria y practica del Metodo Estructural Dinamico*, CEHBA, 2008/06.
- Jorge Pompei e collaboratori, *Teoria e pratica del Metodo Strutturale Dinamico*, translation coordinated by Roberta Consilvio.
- CSU Salvatore Puledda archive listing the ESP and ITA versions.
- Centro Mundial de Estudios Humanistas page for the Spanish document.

Detailed source links and citation guidance are in `references/sources.md`.

## Codex and Claude Versions

See `REPORT.md` for the single report covering both the Codex version and this Claude-compatible version.
