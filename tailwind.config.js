/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["**/*.html", "**/*.py"], // Adjust this to match where your HTML files are located
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  theme: {
    extend: {
      colors: {
        "info-border": "oklch(var(--info-border) / <alpha-value>)",
      },
    },
  },
  daisyui: {
    themes: [
      {
        notes_light: {
          ...require("daisyui/src/theming/themes")["cupcake"],
          info: "#B3E5FC",
          success: "#9CCC65",
          "--info-border": "73.37% 0.145 234.62",
        },
      },
      {
        notes_dark: {
          ...require("daisyui/src/theming/themes")["dim"],
          primary: "teal",
          "--info-border": "73.37% 0.145 234.62",
        },
      },
    ],
  },
};
