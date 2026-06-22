from pathlib import Path
import re
import shutil


ROOT = Path(__file__).resolve().parent
TEMPLATES_DIR = ROOT / "templates"
LANG_JS_FILE = ROOT / "assets" / "js" / "lang.js"
CACHE_VERSION = "20260622j"

PUBLIC_TEMPLATES = [
    "index.html",
    "about.html",
    "services.html",
    "clients.html",
    "staff.html",
    "certificates.html",
    "contact.html",
    "news_detail.html",
]


def make_backup(path: Path) -> None:
    backup_path = path.with_name(path.name + ".bak")

    if path.exists() and not backup_path.exists():
        shutil.copy2(path, backup_path)


def clean_lang_js() -> None:
    if not LANG_JS_FILE.exists():
        print(f"Missing: {LANG_JS_FILE}")
        return

    make_backup(LANG_JS_FILE)

    text = LANG_JS_FILE.read_text(encoding="utf-8")
    text = text.replace("```javascript", "")
    text = text.replace("```js", "")
    text = text.replace("```", "")

    LANG_JS_FILE.write_text(text, encoding="utf-8")
    print(f"Fixed: {LANG_JS_FILE}")


def standardize_buttons(text: str) -> str:
    replacements = {
        "en": '<button type="button" data-lang="en" onclick="setLang(\'en\')">EN</button>',
        "kh": '<button type="button" data-lang="kh" onclick="setLang(\'kh\')">KH</button>',
        "cn": '<button type="button" data-lang="cn" onclick="setLang(\'cn\')">中文</button>',
    }

    for lang, replacement in replacements.items():
        pattern = re.compile(
            rf'<button\b[^>]*data-lang=["\']{lang}["\'][^>]*>.*?</button>',
            re.IGNORECASE | re.DOTALL,
        )
        text = pattern.sub(replacement, text)

    return text


def remove_global_lang_scripts(text: str) -> str:
    pattern = re.compile(
        r'<script\b[^>]*src=["\']/?assets/js/lang\.js(?:\?[^"\']*)?["\'][^>]*>\s*</script>',
        re.IGNORECASE,
    )
    return pattern.sub("", text)


def add_global_lang_script(text: str) -> str:
    script_tag = f'<script src="/assets/js/lang.js?v={CACHE_VERSION}"></script>'

    page_specific_pattern = re.compile(
        r'<script\b[^>]*src=["\']/?assets/js/'
        r'(?:client-lang|staff-lang|certificates-lang)\.js'
        r'(?:\?[^"\']*)?["\'][^>]*>\s*</script>',
        re.IGNORECASE,
    )

    match = page_specific_pattern.search(text)

    if match:
        return text[:match.start()] + script_tag + "\n" + text[match.start():]

    body_position = text.lower().rfind("</body>")

    if body_position == -1:
        return text.rstrip() + "\n" + script_tag + "\n"

    return text[:body_position] + script_tag + "\n" + text[body_position:]


def fix_template(path: Path) -> None:
    if not path.exists():
        print(f"Skipped: {path.name}")
        return

    make_backup(path)

    text = path.read_text(encoding="utf-8")

    text = re.sub(
        r'<link\b[^>]*href=["\']/asiancam/["\'][^>]*>\s*',
        "",
        text,
        flags=re.IGNORECASE,
    )

    text = text.replace('href="assets/', 'href="/assets/')
    text = text.replace("href='assets/", "href='/assets/")
    text = text.replace('src="assets/', 'src="/assets/')
    text = text.replace("src='assets/", "src='/assets/")
    text = text.replace('data-preview="assets/', 'data-preview="/assets/')
    text = text.replace("data-preview='assets/", "data-preview='/assets/")

    text = text.replace('href="index.html"', 'href="/"')
    text = text.replace("href='index.html'", "href='/'")

    text = standardize_buttons(text)
    text = remove_global_lang_scripts(text)
    text = add_global_lang_script(text)

    text = re.sub(r"\n{3,}", "\n\n", text)

    path.write_text(text.rstrip() + "\n", encoding="utf-8")
    print(f"Fixed: {path}")


def main() -> None:
    clean_lang_js()

    for filename in PUBLIC_TEMPLATES:
        fix_template(TEMPLATES_DIR / filename)

    print()
    print("Language files fixed successfully.")
    print("Backups were created with .bak extension.")


if __name__ == "__main__":
    main()
