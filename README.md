# `py_htmx`

## What?

A [pydantic](https://pydantic-docs.helpmanual.io/) driven [htmx](https://htmx.org/) compatible html generator.

This library is mostly designed to generate the pages that you serve.
I leave it up to you to make the [correct decision](https://fastapi.tiangolo.com/) on which package to use to serve your pages, manage your sessions, etc.

## Why?

I was dissatisfied with the horrendous coding standards that I saw in the FastHTML library.
My coding tools hated it, and stepping through the code was a nightmare.
I figured that FastUI looked very cool, but I was worried about long term support after watching the (excellent) [pycon talk](https://www.youtube.com/watch?v=CNYXGVAEPxY).
I liked the idea, but I thought 1. _it should use htmx_, and 2. it would require me to do a lot of work on the original project.

I eventually settled on using nicegui, but I found it to be a bit awkward to work with - I was manually defining all my quasar components and doing all my styling, so I figured I might as well just do it myself.
Ultimately, I probably would've stuck with nicegui, but I kept getting into a mess mixing quasar and tailwind styles.
Totally my fault!
But I figured it'd be faster for me to generate the html myself than figure out how to get everything styled in a way that I liked.
