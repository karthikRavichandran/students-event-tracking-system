/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["./src/**/**/*.{js,ts,jsx,tsx,html,mdx}", "./src/**/*.{js,ts,jsx,tsx,html,mdx}"],
  darkMode: "class",
  theme: {
    screens: { md: { min: "551px", max: "1050px" }, sm: { min: "200px", max: "550px" } },
    extend: {
      colors: {
        black: { 900: "#000000", "900_4c": "#0000004c", "900_3f": "#0000003f", "900_0c": "#0000000c" },
        blue_gray: { 100: "#d9d9d9" },
        gray: { 300: "#e5e5e5", "400_19": "#b3abab19" },
        light_blue: { 200: "#7acbf9", 700: "#0783c9", "700_01": "#0682c8" },
        white: { A700: "#ffffff" },
      },
      boxShadow: {
        bs3: "0px 4px  10px 0px #b3abab19",
        bs1: "0px 4px  4px 0px #0000003f",
        bs: "inset 0px 5px  5px 0px #0000004c",
        bs2: "4px 0px  25px 0px #0000000c",
      },
      fontFamily: { fredokaone: "Fredoka One" },
    },
  },
};
