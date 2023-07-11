---
layout: post
title: eslint, typescript-eslint, angular-eslint
date:   2023-03-28 9:13:14
categories: "web"
catalog: true
tags: 
    - web
---

# eslint
ESLint is a tool for identifying and reporting on patterns found in ECMAScript/JavaScript code, with the goal of making code more consistent and avoiding bugs.

[eslint rules](https://eslint.org/docs/latest/rules/)  

# typescript-eslint

`typescript-eslint` enables ESLint to run on TypeScript code. It brings in the best of both tools to help you write the best JavaScript or TypeScript code you possibly can.

ESLint and TypeScript represent code differently internally. ESLint's default JavaScript parser cannot natively read in TypeScript-specific syntax and its rules don't natively have access to TypeScript's type information.

typescript-eslint:
+ allows ESLint to parse TypeScript syntax
+ creates a set of tools for ESLint rules to be able to use TypeScript's type information
+ provides a large list of lint rules that are specific to TypeScript and/or use that type information


[Why does this project exist](https://typescript-eslint.io/#why-does-this-project-exist?)  
[typescript-eslint rules](https://typescript-eslint.io/rules/)  
[recommended configurations](https://typescript-eslint.io/linting/configs/#recommended-configurations)  

[recommended.ts](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/configs/recommended.ts)  

[recommended-requiring-type-checking.ts](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/configs/recommended-requiring-type-checking.ts)  

[strict.ts](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/configs/strict.ts)
# angular-eslint

# Reference
