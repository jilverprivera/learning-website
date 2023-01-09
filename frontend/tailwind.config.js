/** @type {import('tailwindcss').Config} */

const { fontFamily, screens } = require("tailwindcss/defaultTheme");

module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    screens: { xxs: "270px", xs: "350px", ...screens },
    extend: {
      fontFamily: {
        sans: ["Urbanist", ...fontFamily.sans],
      },
    },
  },
  plugins: [],
};
