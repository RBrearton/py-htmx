/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["**/*.html", "**/*.py", "**/*.md"], // Adjust this to match where your HTML files are located
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: [
      {
        notes_light: {
          ...require("daisyui/src/theming/themes")["cupcake"],
        },
      },
      {
        notes_dark: {
          ...require("daisyui/src/theming/themes")["dim"],
          primary: "teal",
        },
      },
    ],
  },
};
