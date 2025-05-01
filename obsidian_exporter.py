# obsidian_exporter.py
import sys
import os
import re
import shutil
import argparse
from PySide6.QtWidgets import (
    QApplication, QWidget, QFileDialog, QPushButton,
    QVBoxLayout, QMessageBox, QLabel, QHBoxLayout
)
from PySide6.QtCore import Qt

# === User-defined defaults (modify these paths as desired) ===
DEFAULT_VAULT_ROOT = r'C:/Users/bryan.keary/Share/Obsidian/obsidian_notes'
DEFAULT_EXPORT_DIR = r'C:/Temp/test-obsidian-export'

class ObsidianExporter(QWidget):
    def __init__(self, default_vault=None, default_export=None):
        super().__init__()
        # Set defaults: script-defined or CLI override
        self.default_vault = default_vault
        self.default_export = default_export
        self.markdown_file = ''
        self.base_dir = ''
        self.vault_root = default_vault
        self.export_dir = default_export
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Obsidian Document Exporter')
        self.resize(500, 250)

        layout = QVBoxLayout()

        # Select markdown file
        self.select_file_btn = QPushButton('Select Markdown File')
        self.select_file_btn.clicked.connect(self.select_markdown_file)
        layout.addWidget(self.select_file_btn)

        # Labels for status
        self.file_label = QLabel('No file selected')
        self.file_label.setWordWrap(True)
        layout.addWidget(self.file_label)

        self.found_label = QLabel('Images found: 0')
        layout.addWidget(self.found_label)

        self.notfound_label = QLabel('Images missing: 0')
        layout.addWidget(self.notfound_label)

        # Buttons row: Export and Exit
        buttons_layout = QHBoxLayout()

        self.export_btn = QPushButton('Export Document with Images')
        self.export_btn.clicked.connect(self.export_document)
        self.export_btn.setEnabled(False)
        buttons_layout.addWidget(self.export_btn)

        exit_btn = QPushButton('Exit')
        exit_btn.clicked.connect(self.close)
        buttons_layout.addWidget(exit_btn)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def select_markdown_file(self):
        # Start in vault default if set
        start_dir = self.default_vault or ''
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Markdown File",
            start_dir,
            "Markdown Files (*.md);;All Files (*)"
        )
        if not file_name:
            return
        self.markdown_file = file_name
        self.base_dir = os.path.dirname(file_name)
        # Detect vault_root if not overridden
        if not self.default_vault:
            self.vault_root = self.find_vault_root(self.base_dir)
        else:
            self.vault_root = self.default_vault
        self.export_btn.setEnabled(True)

        # Update status labels
        self.file_label.setText(f"File: {self.markdown_file}")
        links = self.parse_image_links(self.markdown_file)
        found, missing = 0, 0
        for img in links:
            if self.resolve_image_path(img):
                found += 1
            else:
                missing += 1
        self.found_label.setText(f"Images found: {found}")
        self.notfound_label.setText(f"Images missing: {missing}")

    def export_document(self):
        # Start in export default if set
        start_dir = self.default_export or ''
        export_dir = QFileDialog.getExistingDirectory(
            self,
            "Select Export Directory",
            start_dir
        )
        if not export_dir:
            return
        try:
            self.perform_export(export_dir)
            QMessageBox.information(self, 'Success', f'Exported to:\n{export_dir}')
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    def perform_export(self, export_dir):
        links = self.parse_image_links(self.markdown_file)
        # Copy markdown file
        shutil.copy2(self.markdown_file,
                     os.path.join(export_dir, os.path.basename(self.markdown_file)))
        # Copy images
        for img in links:
            path = self.resolve_image_path(img)
            if path and os.path.isfile(path):
                shutil.copy2(path, os.path.join(export_dir, os.path.basename(path)))
            else:
                print(f"Warning: Could not locate image '{img}'")

    def parse_image_links(self, filepath):
        links = []
        md_re = re.compile(r'!\[.*?\]\((.*?)\)')
        wiki_re = re.compile(r'!\[\[(.*?)\]\]')
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            links += md_re.findall(text)
            links += wiki_re.findall(text)
        return links

    def resolve_image_path(self, image_ref):
        # Absolute path
        if os.path.isabs(image_ref):
            return image_ref
        # Relative to note
        rel = os.path.join(self.base_dir, image_ref)
        if os.path.exists(rel):
            return rel
        # Under vault root
        if self.vault_root:
            vault_rel = os.path.join(self.vault_root, image_ref)
            if os.path.exists(vault_rel):
                return vault_rel
            name = os.path.basename(image_ref)
            for root, _, files in os.walk(self.vault_root):
                if name in files:
                    return os.path.join(root, name)
        return None

    def find_vault_root(self, start_dir):
        current = start_dir
        while True:
            if '.obsidian' in os.listdir(current):
                return current
            parent = os.path.dirname(current)
            if parent == current:
                break
            current = parent
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Export an Obsidian markdown file with linked images'
    )
    parser.add_argument(
        '--vault_root',
        help='Default Obsidian vault root directory',
        default=DEFAULT_VAULT_ROOT
    )
    parser.add_argument(
        '--export_dir',
        help='Default export directory',
        default=DEFAULT_EXPORT_DIR
    )
    args = parser.parse_args()

    app = QApplication(sys.argv)
    ex = ObsidianExporter(
        default_vault=args.vault_root,
        default_export=args.export_dir
    )
    ex.show()
    sys.exit(app.exec())
