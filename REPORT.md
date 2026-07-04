# Metodo Strutturale Dinamico Skill: Codex and Claude Versions

This repository contains both platform versions of the same Metodo Strutturale Dinamico skill.

## Repository Layout

```text
metodo-strutturale-dinamico/
├── README.md
├── REPORT.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── msd-guide.md
│   ├── msd-prompting-guide.md
│   └── sources.md
└── claude/
    └── metodo-strutturale-dinamico/
        ├── README.md
        ├── SKILL.md
        └── references/
            ├── msd-guide.md
            ├── msd-prompting-guide.md
            └── sources.md
```

## Version 1: Codex

Location:

```text
/
```

Repository URL:

```text
https://github.com/fedepalu2/metodo-strutturale-dinamico
```

Install folder:

```text
~/.codex/skills/metodo-strutturale-dinamico/
```

Codex-specific file:

```text
agents/openai.yaml
```

## Version 2: Claude / Anthropic

Location:

```text
claude/metodo-strutturale-dinamico/
```

Install folder:

```text
~/.claude/skills/metodo-strutturale-dinamico/
```

Compatibility choices:

- Keep `SKILL.md` with YAML frontmatter using `name` and `description`.
- Keep the skill name free of reserved words such as "claude" or "anthropic".
- Do not include Codex-specific `agents/openai.yaml`.
- Keep supporting files in `references/` and link them from `SKILL.md`.

## Shared Methodological Core

Both versions use the same gate sequence:

| Gate | Name | Required output |
|---|---|---|
| 0 | Context | Known facts, assumptions, missing non-blocking information |
| 1 | Problem | Delimited problem, scope, stakes |
| 2 | Question | One central question |
| 3 | Object-Interest | Object of Study and fixed Interest |
| 4 | Static Analysis | Major, middle, and minor fields |
| 5 | Dynamic Analysis | Process, relations, composition |
| 6 | Synthesis | New view of the object, not a recap |
| 7 | Response | Answer, reasoning, first step, observation criteria |

Each gate must be marked:

```text
PASS
PASS WITH ASSUMPTIONS
STOP
```

## Source References

Spanish original:

```text
https://www.csusalvatorepuledda.org/dokuwiki/lib/exe/fetch.php?media=archivio%3A200806-metodo_estructural_dinamico-jorgepompei_etal-esp.pdf
```

Italian translation:

```text
https://www.csusalvatorepuledda.org/dokuwiki/lib/exe/fetch.php?media=archivio%3A200806-teoria_e_pratica_del_msd-j.pompei-ita.pdf
```

CSU Salvatore Puledda archive page:

```text
https://www.csusalvatorepuledda.org/dokuwiki/?id=archivio%3Atutto
```

Centro Mundial de Estudios Humanistas page:

```text
https://www.cmehumanistas.org/es/metodo-estructural-dinamico-teoria-y-practica
```

## Maintenance Notes

When changing the workflow:

1. Update the Codex root `SKILL.md`.
2. Port the same method changes to `claude/metodo-strutturale-dinamico/SKILL.md`.
3. Keep `references/` aligned unless a platform-specific reason requires divergence.
4. Do not copy `agents/openai.yaml` into the Claude version.
5. Re-check source references if any URL changes.
