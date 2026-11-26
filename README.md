<p align="center">
  <img src="assets/banner.png" alt="Sound human. A Claude Code skill. Strip the signs of AI writing so it reads like a person wrote it." width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img alt="Licence: MIT" src="https://img.shields.io/badge/licence-MIT-0f063c"></a>
  <img alt="Works with Claude Code" src="https://img.shields.io/badge/works%20with-Claude%20Code-599cff">
  <a href="https://github.com/blader/humanizer"><img alt="Based on blader/humanizer" src="https://img.shields.io/badge/based%20on-blader%2Fhumanizer-d5e6ff"></a>
  <img alt="Spelling: Australian English" src="https://img.shields.io/badge/spelling-Australian%20English-fff58a">
</p>

# Sound human

People can tell when AI wrote something. Words like "delve" give it away. So do lines like "it's not just X, it's Y". Once a reader spots one, they stop trusting the rest.

This skill makes Claude Code find those giveaways and rewrite the text so it reads like a person wrote it. It checks 51 patterns, never invents facts to sound human, and writes in Australian English.

It is a modified copy of [humanizer](https://github.com/blader/humanizer) by Siqi Chen. If you write US English, install that one instead.

You don't need to be a developer to use it. You install it once and it works in every project.

## Install it in a minute

It installs from the builder-kit-lean marketplace. In a terminal:

```bash
claude plugin marketplace add jiffi-co/builder-kit-lean
claude plugin install sound-human@builder-kit-lean
```

To have Claude Code use it every time, add this section to `~/.claude/CLAUDE.md`:

```text
## Sound human
Use the sound-human skill on anything you write for me that another person will read: emails, documents, posts, page copy and commit messages. Follow it, and write in Australian English.
```

Start a fresh session afterwards. That's it.

Prefer to install it by hand, or from a zip? See [INSTALL.md](INSTALL.md).

## What changes

The skill carries a full worked example. This is one paragraph of the text that goes in:

> At its core, the value proposition is clear: streamlining processes, enhancing collaboration, and fostering alignment. It's not just about autocomplete; it's about unlocking creativity at scale, ensuring that organisations can remain agile while delivering seamless, intuitive, and powerful experiences to users. The tool serves as a catalyst. The assistant functions as a partner. The system stands as a foundation for innovation.

And this is the whole piece after the rewrite:

> AI coding assistants can speed up the boring parts of the job. They're great at boilerplate: config files and the little glue code you don't want to write. They can also help you sketch a test, but you still have to read it.
>
> The dangerous part is how confident the suggestions look. I've accepted code that compiled and passed lint, then discovered later it missed the point because I stopped paying attention.
>
> If you treat it like autocomplete and review every line, it's useful. If you use it to avoid thinking, it will help you ship bugs faster.
>
> The only real backstop is tests. Without them, you're mostly judging vibes.

## How it works

1. It scans the text against 51 patterns.
2. It rewrites what it flagged and keeps your meaning and tone.
3. It asks itself "what makes this so obviously AI generated?" and lists what is left.
4. It rewrites again to clear that list.
5. It checks the spelling is Australian.

The 51 patterns sit in seven groups:

| Group | Patterns | What it catches |
|---|---|---|
| Content | 9 | Inflated significance, brochure language, "experts believe" |
| Language and grammar | 9 | Overused AI vocabulary, "not only X but Y", forced groups of three |
| Style and formatting | 10 | Em dashes, mechanical bold, title case headings, emoji |
| Communication | 5 | "I hope this helps", knowledge-cutoff disclaimers, flattery |
| Filler and hedging | 5 | Filler phrases, stacked hedges, upbeat endings that say nothing |
| Structure | 4 | Fabricated citations, summaries that restate, habits of each AI model |
| Newer tells | 9 | "Here's the thing", "honestly", slogan endings, corporate power verbs, LinkedIn post shapes, email boilerplate, made-up names and numbers |

Clean isn't enough. Text with every giveaway removed still reads as machine-made if it has no point of view. So the skill also pushes for opinions, uneven rhythm and specifics.

The full skill is one file: [skills/sound-human/SKILL.md](skills/sound-human/SKILL.md).

## What's in the box

```text
skills/sound-human/
└── SKILL.md      the skill: 51 patterns, a worked example and a quick-reference list
```

No scripts. No network calls. It is instructions and examples, nothing else.

## Using it

Once it's installed with the CLAUDE.md section, you don't have to do anything. Claude Code uses it on what it writes for you.

To call it yourself, say "use sound-human on this" and paste your text. You get a draft, a short list of what still reads as AI, and a final version.

## How it differs from the original

- Every rewrite comes out in Australian English: -ise endings, colour, organisation, licence and practice as nouns. The version of the original it was built from set no spelling.
- It checks 51 patterns. That version had 25.
- It has five rules that outrank the patterns. The first is that it never invents a fact, a number, a name or a story to make text sound human.
- It has a quiet mode: when Claude Code is writing something for you as part of another job, you get the finished text only.
- It adds a quick-reference list of words and phrases to flag on sight, and notes on how the giveaways differ from one AI model to the next.
- It has its own name and version number. Neither tracks the original, which has had releases since this copy branched off.

For the maintained original, go to [blader/humanizer](https://github.com/blader/humanizer).

## Credits

- Based on [humanizer](https://github.com/blader/humanizer) by Siqi Chen (MIT). The approach and the audit pass come from that project, and the worked example is adapted from it.
- The patterns are drawn from Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) page, maintained by WikiProject AI Cleanup.
- Packaged by [Jake Shelley](https://github.com/jake-jiffi).

## Licence

[MIT](LICENSE), the same as the original. Use it, change it, share it.
