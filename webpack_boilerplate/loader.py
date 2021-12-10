import copy
import json
import time
from io import open

from .exceptions import (
    WebpackBundleLookupError,
    WebpackError,
    WebpackLoaderBadStatsError,
    WebpackLoaderTimeoutError,
)


class WebpackLoader(object):
    _assets = {}

    def __init__(self, name, config):
        self.name = name
        self.config = config

    def load_assets(self):
        # TODO
        # poll when debugging and block request until bundle is compiled
        # or the build times out
        try:
            with open(self.config["MANIFEST_FILE"], encoding="utf-8") as f:
                return json.load(f)
        except IOError:
            raise IOError(
                "Error reading {0}. Are you sure webpack has generated "
                "the file and the path is correct?".format(self.config["MANIFEST_FILE"])
            )

    def get_assets(self):
        if self.config["CACHE"]:
            if self.name not in self._assets:
                self._assets[self.name] = self.load_assets()
            return self._assets[self.name]
        return self.load_assets()

    def filter_chunks(self, chunks):
        for chunk in chunks:
            ignore = any(regex.match(chunk["url"]) for regex in self.config["ignores"])
            if not ignore:
                chunk["url"] = self.get_chunk_url(chunk)
                yield chunk

    def get_chunk_url(self, chunk):
        url = chunk["url"]

        if self.config.get("web_framework", None) == "django":
            from django.contrib.staticfiles.storage import staticfiles_storage
            from django.conf import settings

            if url.startswith("http"):
                # webpack dev server
                return url
            else:
                prefix = settings.STATIC_URL
                url_without_static_prefix = url[
                    url.startswith(prefix) and len(prefix) :
                ]
                return staticfiles_storage.url(url_without_static_prefix)
        else:
            return url

    def get_bundle(self, bundle_name):
        assets = copy.copy(self.get_assets())
        try:
            # keep the order
            js = assets["entrypoints"][bundle_name]["assets"].get("js", [])
            css = assets["entrypoints"][bundle_name]["assets"].get("css", [])
            js_css = js + css

            assets.pop("entrypoints")
            # so url is the key
            reversed_assets = {value: key for (key, value) in assets.items()}
            chunks = [{"name": reversed_assets[url], "url": url,} for url in js_css]
        except Exception:
            raise WebpackBundleLookupError(
                "Cannot resolve bundle {0}.".format(bundle_name)
            )

        return self.filter_chunks(chunks)
