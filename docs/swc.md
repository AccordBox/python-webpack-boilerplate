# SWC (Speedy Web Compiler)

SWC is an extensible Rust-based platform for the next generation of fast developer tools.

While Babel mainly focuses on compatibility and transpiling JavaScript code, SWC provides a broader set of optimizations and features to improve the overall development experience. 

SWC supports both JavaScript and TypeScript, making it suitable for a wide range of frontend projects. 

Additionally, SWC's focus on performance optimizations sets it apart from Babel, as it can significantly reduce build times and enhance runtime performance.

After switching to `SWC`, the build time is optimized for about 20-30% based on my experience.

Notes:

1. Just install `swc-loader` and `@swc/core`.
2. Config Webpack rules to use `swc-loader` to process JS files.
3. Customize the `.swcrc` file if you need.
4. Even SWC also supports bundling, we still use Webpack to bundle the frontend code. Because Webpack has more features and is more mature than SWC bundling.

## Reference

1. [https://blog.logrocket.com/migrating-swc-webpack-babel-overview/](https://blog.logrocket.com/migrating-swc-webpack-babel-overview/)
2. [We exchanged Babel&TSC for SWC and it was worth it!](https://engineering.telia.no/blog/we-exchanged-babel-tsc-for-swc-and-it-was-worth-it)
