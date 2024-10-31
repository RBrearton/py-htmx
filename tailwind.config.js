/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["**/*.html", "**/*.py"], // Adjust this to match where your HTML files are located
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: [
      {
        notes_light: {
          ...require("daisyui/src/theming/themes")["cupcake"],
          info: "#29B6F6",
          success: "#9CCC65",
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
