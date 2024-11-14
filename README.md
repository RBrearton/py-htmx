# `py_htmx`

## What?

A [pydantic](https://pydantic-docs.helpmanual.io/) driven [htmx](https://htmx.org/) compatible html generator.
Styling is done with [DaisyUI](https://daisyui.com/), a [tailwindcss](https://tailwindcss.com/) plugin.

This library is mostly designed to generate the pages that you serve.
I leave it up to you to make the [correct decision](https://fastapi.tiangolo.com/) on which package to use to serve your pages, manage your sessions, etc.

## Why?

I was dissatisfied with the horrendous coding standards that I saw in the [FastHTML](https://fastht.ml/) library.
My coding tools hated it, and stepping through the code was a nightmare.
I thought that [FastUI](https://github.com/pydantic/fastui/) looked very cool, but I was worried about long term support after watching the (excellent) [pycon talk](https://www.youtube.com/watch?v=CNYXGVAEPxY).
I liked the idea, but I thought 1. _it should use htmx_, and 2. it would require me to do a lot of work on the original project, as it's still in the early stages of development.

I eventually settled on using [nicegui](https://nicegui.io/), but I found it to be a bit awkward to work with - I was manually defining all my quasar components and doing all my styling, so I figured I might as well just do it myself.
Ultimately, I probably would've stuck with nicegui, but I kept getting into a mess mixing quasar and tailwind styles.
It seemed really awkward to mix the two, although I'm sure it could've been made to work if I gave it enough time.
In the end, I figured it'd be faster for me to generate the html myself than figure out how to get everything styled in a way that I liked.

## Usage

I designed this to be used with the [DaisyUI](https://daisyui.com/) tailwindcss plugin.
You'll need to do some setup to get it working.
In the future, I hope to automate this.
For now, _if you have any problems, please make a [github issue](https://github.com/RBrearton/py-htmx/issues)_.

Install npm.

Go to your project.

```bash
mkdir my-py-htmx-project
cd my-py-htmx-project
```

Initialize your project.
This will create a `package.json` file.

```bash
npm init -y
```

Install tailwindcss and daisyui.

```bash
npm install -D tailwindcss daisyui
npm install -D @tailwindcss/typography
```

Generate a tailwindcss config file.

```bash
npx tailwindcss init
```

This will create a tailwind.config.js file in your project’s root directory.

Update the tailwind.config.js file to include the daisyui plugin.

```javascript
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["**/*.html"], // Adjust this to match where your HTML files are located
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: ["light", "dark"],
  },
};
```

Set up tailwindcss by creating a styles.css file.

```css
/* styles.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Build the tailwindcss file.
This command assumes that you put your styles.css file in the root of your project.

```bash
npx tailwindcss -i ./styles.css -o ./dist.css --watch
```

Done!
The `--watch` flag will watch for changes to your styles.css file and automatically update the dist.css file.
If you aren't going to make any style changes, you can just ctrl-c out of this command.
It's configurable, but py_htmx will look for a file called `dist.css` in the root of your project.
If you followed this exactly, then you should be good to go.

## Notes website

Markdown is linted using the markdownlint VSCode extension.
