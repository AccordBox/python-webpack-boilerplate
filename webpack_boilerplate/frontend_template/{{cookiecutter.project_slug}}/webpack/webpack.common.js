const glob = require("glob");
const Path = require("path");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const WebpackAssetsManifest = require("webpack-assets-manifest");

const getEntryObject = () => {
  const entries = {};
  // for javascript/typescript entry file
  glob
    .sync(Path.join(__dirname, "../src/application/*.{js,ts}"))
    .forEach((path) => {
      const name = Path.basename(path);
      const extension = Path.extname(path);
      const entryName = name.replace(extension, "");
      if (entryName in entries) {
        throw new Error(`Entry file conflict: ${entryName}`);
      }
      entries[entryName] = path;
    });
  return entries;
};

module.exports = {
  entry: getEntryObject(),
  output: {
    path: Path.join(__dirname, "../build"),
    filename: "js/[name].js",
    publicPath: "/static/",
    assetModuleFilename: "[path][name][ext]",
  },
  optimization: {
    splitChunks: {
      chunks: "all",
    },

    runtimeChunk: "single",
  },
  plugins: [
    new CleanWebpackPlugin(),
    new CopyWebpackPlugin({
      patterns: [
        { from: Path.resolve(__dirname, "../vendors"), to: "vendors" },
      ],
    }),
    new WebpackAssetsManifest({
      entrypoints: true,
      output: "manifest.json",
      writeToDisk: true,
      publicPath: true,
    }),
  ],
  resolve: {
    alias: {
      "~": Path.resolve(__dirname, "../src"),
    },
  },
  module: {
    rules: [
      {
        test: /\.mjs$/,
        include: /node_modules/,
        type: "javascript/auto",
      },
      {
        test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)(\?.*)?$/,
        type: "asset",
      },
    ],
  },
};
