---
title: "Agent-First vs Agent-Second Engineering"
date: 2026-09-15
draft: false
tags: ["engineering", "agents", "ai"]
description: "Who writes the first code matters more than who writes the rest"
summary: "Who writes the first code matters more than who writes the rest."
---

<!--more-->

Lately I've been thinking about two agentic engineering paradigms, which I call agent-first and agent-second engineering. The difference is who writes the first code: the human or the agent. The most common workflow right now (and the one that I've mostly adopted) is agent-first: you describe something, the agent writes the initial code, and then you review and refine it. Agent-second is the reverse: you write the initial code, and the agent takes it from there.

Looking back at the past few years of adopting agentic engineering, the most frustrating projects I've worked on with agents are the ones I _started_ with agents (which I've been doing more and more, because it's just so fast).

## What goes wrong with agent-first

The obvious part is that agents _love_ to write code. A lot of code. As much as possible. You can push back on this with a well-written AGENTS.md and a simplify skill, and it helps, but simplifying code after the fact is tedious and you never really stop doing it. At some point there's just so much code that you can't see the minimal solution to a problem anymore.

The bigger problem is that every decision the agent makes early on becomes a precedent. Once a codebase matures to a certain point of complexity, it becomes very hard to make real changes. When I say real changes, I'm not talking about renaming a function or refactoring a module. I'm talking about the actual anatomy of the codebase: whether something is a module or just a function, what the core data types look like and how they get passed around, how errors move through the system. It's a bit like pawn structure in chess: pieces can always be rerouted, but pawns can't move backwards, so the ones you pushed in the opening decide what the rest of the game looks like. In an agent-first project, someone else played the opening for you.

These are the kind of things that are hard to describe in a prompt, unless you're willing to spend so much time prompting that you might as well write the code yourself. But I think the real reason they're hard to prompt is that you don't know them yet. Writing an essay works the same way: you can create a rough outline, but you don't really know what you think until you've written it down, and the essay only sounds like you because you wrote every sentence yourself. The right structure isn't something I know beforehand and then fail to explain to the agent, it's something I find out by writing the first version, and the fact that I wrote it is what makes it mine. Prompting skips exactly that step.

## The case for agent-second

After reading [this blog](https://kennethreitz.org/essays/2026-04-12-write_it_first_then_let_ai_drive) by Kenneth Reitz I got inspired to flip the approach around and start with the code myself (again). As Reitz puts it: "**a hand-written codebase is a style guide written in code itself**". If you write the first module, the first couple of functions and the first test, the agent has something concrete to imitate, and when you review its code you're checking it against _your_ standard rather than one that just emerged.

The style guide doesn't even have to live in the same repo: I've had reasonable success by pointing agents at existing projects of mine, which is arguably a form of agent-second. This does assume that A) you have existing projects that are actually good enough to serve as a template, and B) those projects resemble whatever you're building closely enough to work as one.

The other benefit is more personal. While it's undeniable that agents can write working code, there's something uncanny (and even stressful) about shipping code that's not _quite_ yours. Before agents got good enough to start projects, I worked agent-second by default. When I wrote [Pyversity](https://github.com/Pringled/pyversity) a year ago, I wrote the initial implementation myself, and used agents to refine and optimize the code. This is a codebase I'm proud of and feel comfortable maintaining (myself, or with agents).

There is one other idea I plan on experimenting with, borrowed from Fred Brooks: ["plan to throw one away"](https://wiki.c2.com/?PlanToThrowOneAway). Your first version of a system is going to be flawed, so expect to discard it and build a better one with what you learned. Brooks himself later called this ["too simplistic"](https://en.wikipedia.org/wiki/The_Mythical_Man-Month), his objection being that it assumes you build the whole thing before learning anything. But now that a first version costs almost nothing (as long as you don't bother reviewing it), I think it's back on the table. So: let the agent write the first version, use it to find out whether the thing can be done at all rather than how it should be built, throw it away, and write the version you keep yourself.

For now, I'm using a combination of agent-first and agent-second engineering: agent-first for "ephemeral code" such as experiments, prototypes and one-off scripts, and agent-second for production code. If the throwaway idea works out, agent-first becomes step one of agent-second, but that's for a future post.
