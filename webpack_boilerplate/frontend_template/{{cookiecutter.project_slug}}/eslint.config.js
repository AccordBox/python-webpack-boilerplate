// https://eslint.org/docs/latest/use/configure/migration-guide#eslint-env-configuration-comments

import babelParser from "@babel/eslint-parser";
import js from "@eslint/js";
import globals from "globals";

export default [
    js.configs.recommended,
    {
        rules: {
            semi: 2
        },
    },
    {
        languageOptions: {
            parser: babelParser,
            globals: {
                ...globals.browser,
                ...globals.node,
            },
            parserOptions: {
                ecmaVersion: 8,
                sourceType: "module",
            }
        }
    }
];
