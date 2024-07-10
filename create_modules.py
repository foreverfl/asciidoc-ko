import os
import sys

# 생성할 폴더와 파일 리스트
folders = [
    "ROOT",
    "introduction",
    "blocks",
    "document-attributes",
    "element-attributes",
    "document-header",
    "document-type",
    "sections",
    "paragraphs",
    "discrete-headings",
    "breaks",
    "text-formatting-and-punctuation",
    "lists",
    "description-lists",
    "links",
    "cross-references",
    "footnotes",
    "images",
    "audio-and-video",
    "icons",
    "keyboard-macro",
    "button-and-menu-ui-macros",
    "admonitions",
    "sidebars",
    "example-blocks",
    "blockquotes",
    "verses",
    "verbatim-and-source-blocks",
    "tables",
    "equations-and-formulas",
    "open-blocks",
    "collapsible-blocks",
    "comments",
    "automatic-table-of-contents",
    "docinfo-files",
    "includes",
    "conditionals",
    "substitutions",
    "passthroughs",
    "reference"
]

# 스크립트 파일의 디렉토리를 기준으로 작업
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(script_dir)

# 폴더 생성 및 nav.adoc 파일 생성
for folder in folders:
    # 폴더 생성
    os.makedirs(folder, exist_ok=True)
    
    # nav.adoc 파일 생성
    with open(os.path.join(folder, "nav.adoc"), "w") as f:
        f.write(f"* xref:index.adoc[{folder.replace('-', ' ').title()}]\n")

print("Folders and nav.adoc files have been created successfully.")