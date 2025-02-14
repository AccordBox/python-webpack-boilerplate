{% if cookiecutter.style_solution == 'tailwind' %}
module.exports = {
  plugins: {
    "@tailwindcss/postcss": {},
  }
}
{% else %}
const postcssPresetEnv = require("postcss-preset-env");

module.exports = {
  plugins: [postcssPresetEnv()],
};
{% endif %}
