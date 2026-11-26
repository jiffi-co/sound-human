# Installing sound-human

Three ways. Pick one. All of them install the skill at the user level, so it works in every project.

After any of them, start a fresh Claude Code session so the skill loads.

## 1. Ask Claude Code to install it from GitHub

Paste this into Claude Code:

```text
Please install the sound-human skill for Claude Code from this public repo:
https://github.com/jiffi-co/sound-human

Install it at the user level so it works in every project, and set it up so you always use it:

1. Before you install anything, read the skill's files and tell me in plain English what it does and whether anything in it runs commands or touches my files.

2. Download the repo to a temporary folder (git clone, or the zip from GitHub if git isn't available). Copy its skills/sound-human folder to ~/.claude/skills/sound-human/ so SKILL.md sits directly in that folder. On Windows, ~ is my user folder. If a sound-human skill is already there, show me what would change and ask before replacing it. Delete the temporary folder when you're done.

3. Add this section to ~/.claude/CLAUDE.md. If the file doesn't exist, create it. If it does exist, add the section at the end and don't change anything already in it.

   ## Sound human
   Use the sound-human skill on anything you write for me that another person will read: emails, documents, posts, page copy and commit messages. Follow it, and write in Australian English.

4. Show me the final folder structure and the exact section you added to CLAUDE.md, then tell me to start a fresh session so it all loads.
```

## 2. Ask Claude Code to install it from a zip

If someone sent you `sound-human.zip`, paste this in and add the path to the file:

```text
I've downloaded a Claude Code skill called sound-human as a zip. It's here: [drag the zip in or paste the path, e.g. ~/Downloads/sound-human.zip]

Please install it at the user level so it works in every project, and set it up so you always use it:

1. Unzip it to a temporary folder and find the folder that holds SKILL.md. Copy that folder to ~/.claude/skills/sound-human/ so SKILL.md sits directly in it. Leave out any __MACOSX or .DS_Store files. Delete the temporary folder when you're done.

2. Add this section to ~/.claude/CLAUDE.md. If the file doesn't exist, create it. If it does exist, add the section at the end and don't change anything already in it.

   ## Sound human
   Use the sound-human skill on anything you write for me that another person will read: emails, documents, posts, page copy and commit messages. Follow it, and write in Australian English.

3. Show me the final folder structure and the exact section you added to CLAUDE.md, then tell me to start a fresh session so it all loads.
```

## 3. Do it by hand

Mac or Linux, in a terminal:

```sh
git clone --depth 1 https://github.com/jiffi-co/sound-human /tmp/sound-human
mkdir -p ~/.claude/skills
cp -R /tmp/sound-human/skills/sound-human ~/.claude/skills/
rm -rf /tmp/sound-human
```

Windows, in PowerShell:

```powershell
git clone --depth 1 https://github.com/jiffi-co/sound-human "$env:TEMP\sound-human"
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse -Force "$env:TEMP\sound-human\skills\sound-human" "$env:USERPROFILE\.claude\skills\"
Remove-Item -Recurse -Force "$env:TEMP\sound-human"
```

Then add this to the end of `~/.claude/CLAUDE.md` (create the file if it isn't there):

```markdown
## Sound human
Use the sound-human skill on anything you write for me that another person will read: emails, documents, posts, page copy and commit messages. Follow it, and write in Australian English.
```

## Check it worked

You should have:

```text
~/.claude/skills/sound-human/
└── SKILL.md
```

In a fresh Claude Code session, ask: "Which skills do you have?" You should see sound-human in the list.

To try it, paste in a paragraph an AI wrote and say "use sound-human on this". You should get a draft, a short list of what still reads as AI, and a final version.

## If you already have humanizer

sound-human installs beside it, in its own folder, and the two do the same job. Keep one. To drop the original, delete `~/.claude/skills/humanizer` and change any line in `~/.claude/CLAUDE.md` that names humanizer.

## Removing it

Delete the `~/.claude/skills/sound-human` folder and remove the "Sound human" section from `~/.claude/CLAUDE.md`.
