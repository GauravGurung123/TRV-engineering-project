import os
import pathlib
import urllib.request
from django.core.management.base import BaseCommand
from django.conf import settings


HTMX_VERSION = "2.0.3"
HYPERSCRIPT_VERSION = "0.9.13"
SWIPER_VERSION = "latest"  # using bundle URLs that are versioned by path name used in the template


FILES = [
    # (url, relative_path under static/)
    (f"https://unpkg.com/htmx.org@{HTMX_VERSION}", f"vendor/htmx/htmx-{HTMX_VERSION}.min.js"),
    (f"https://unpkg.com/hyperscript.org@{HYPERSCRIPT_VERSION}", f"vendor/hyperscript/_hyperscript-{HYPERSCRIPT_VERSION}.min.js"),
    ("https://unpkg.com/swiper/swiper-bundle.min.css", "vendor/swiper/swiper-bundle.min.css"),
    ("https://unpkg.com/swiper/swiper-bundle.min.js", "vendor/swiper/swiper-bundle.min.js"),
    # jQuery and jQuery UI used in flight search
    ("https://code.jquery.com/jquery-3.6.0.min.js", "vendor/jquery/jquery-3.6.0.min.js"),
    ("https://code.jquery.com/ui/1.12.1/jquery-ui.min.js", "vendor/jquery-ui/jquery-ui-1.12.1.min.js"),
    ("https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css", "vendor/jquery-ui/jquery-ui-1.12.1.min.css"),
    # Bootstrap and Popper used in results
    ("https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js", "vendor/popper/popper-2.5.3.min.js"),
    ("https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js", "vendor/bootstrap/bootstrap-4.5.2.min.js"),
    ("https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css", "vendor/bootstrap/bootstrap-4.5.2.min.css"),
]


class Command(BaseCommand):
    help = "Download third-party frontend assets (htmx, hyperscript, swiper) into static/vendor/."

    def add_arguments(self, parser):
        parser.add_argument("--force", action="store_true", help="Re-download files even if they exist")

    def handle(self, *args, **options):
        static_root = pathlib.Path(settings.BASE_DIR) / "static"
        downloaded = 0
        for url, rel_path in FILES:
            dest = static_root / rel_path
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists() and not options["force"]:
                self.stdout.write(self.style.NOTICE(f"Exists: {rel_path} (skip)"))
                continue
            self.stdout.write(f"Downloading {url} -> {rel_path} ...")
            try:
                with urllib.request.urlopen(url) as resp, open(dest, "wb") as f:
                    f.write(resp.read())
                downloaded += 1
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Failed: {url} -> {rel_path}: {e}"))
        if downloaded:
            self.stdout.write(self.style.SUCCESS(f"Downloaded {downloaded} file(s) to static/vendor."))
        else:
            self.stdout.write("Nothing to do.")
