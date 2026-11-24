# The Worst App Idea Ever Pitched

![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23.svg)
![Rank](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/yudhisutawan77/makefun-worst-app-idea/rank.svg)
![Reward](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/yudhisutawan77/makefun-worst-app-idea/reward.svg)

Entry for [The Worst App Idea Ever Pitched](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23) on make.fun — one sentence, at most 240 characters, pitching the worst and most useless app imaginable.

## The entry

> ElevatorDJ lets you vote on the music in elevators you are not currently riding, with a premium tier that lets you skip songs in other people's buildings.

154 characters, one sentence.

## Why this pitch

A product that sounds real (a named app, a voting mechanic, a premium tier), a founder who sounds certain, and a function nobody on earth needs: voting on music in elevators you are not in — and paying extra to skip songs in *other people's* buildings. The uselessness is the feature.

## What `main.py` does

`main.py` writes that single sentence to `/output/entry.txt` (or to the path set by `ENTRY_OUT`, or `ENTRY_OUT_DIR/entry.txt` when set). Before writing, it gates the sentence the same way the sealed scorer does: 1–240 characters, not only whitespace, and a single line. The file holds the sentence byte for byte, with no trailing newline.

```sh
python3 main.py
```
