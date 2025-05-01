# Obsidian Exporter

A simple GUI tool to export an Obsidian Markdown note along with its linked images into a single target directory.

---

## 🔧 Prerequisites

- **Python 3.10+**
- **uv** package manager (install via official installer, Homebrew, or PowerShell; pip-supported but not recommended)
- **Git** (to clone the repository)

---

## 🚀 Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/InsolentFlunkey/obsidian-exporter.git
   cd obsidian-exporter
   ```

2. **Install uv** (choose one):

   - **macOS/Linux** via official script:
     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sudo sh
     ```

   - **Homebrew** (macOS/Linux):
     ```bash
     brew install uv
     ```

   - **Windows PowerShell** (run as Administrator):
     ```powershell
     irm https://astral.sh/uv/install.ps1 | iex
     ```

   - **Pip** (supported but not recommended):
     ```bash
     pip install uv  # ensure a virtual environment is activated
     ```

3. **Initialize your project** (optional for existing repos):
   ```bash
   uv init  # creates .venv/ and config files
   ```

4. **Install GUI dependency**:
   ```bash
   uv add PySide6
   uv sync
   ```

---

## ⚙️ Running the App

1. **Update default Vault and Export locations in script (optional but recommneded)**
   ```
   # === User-defined defaults (modify these paths as desired) ===
   DEFAULT_VAULT_ROOT = r'C:/your/vault/location'
   DEFAULT_EXPORT_DIR = r'C:/your/export/location'
   ```

2. **Launch the app**
   1. **Launch via uv** (recommended):
      ```bash
      uv run python obsidian_exporter.py [--vault_root PATH] [--export_dir PATH]
      ```

   2. **Or activate the venv manually and run**:
      ```bash
      # Windows PowerShell
      .\.venv\Scripts\Activate.ps1

      # macOS/Linux
      source .venv/bin/activate

      python obsidian_exporter.py [--vault_root PATH] [--export_dir PATH]
      ```

### Command‑Line Options

- `--vault_root PATH`  
  Override the default Obsidian vault directory.

- `--export_dir PATH`  
  Override the default export target directory.

If you omit these flags, the script uses the hard‑coded defaults set at the top of `obsidian_exporter.py`.

---

## 🎨 Usage Workflow

1. **Select Markdown File**: Click **Select Markdown File** and pick your `.md` note.
2. **Review Counts**: The app displays the full file path, the number of images found, and how many are missing.
3. **Export**: Click **Export Document with Images**, choose a target folder, and let the tool copy the `.md` and all located images.
4. **Exit**: Click **Exit** to close the app.

---

## 📂 Repository Structure

```
obsidian-exporter/
├── .venv/                # Virtual environment (created by uv)
├── obsidian_exporter.py  # Main application script
├── README.md             # This file
├── pyproject.toml        # Project metadata and dependency configuration for uv
└── uv.lock               # uv lockfile recording dependencies
```  

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch (`git checkout -b feature/YourFeature`)
3. Make your changes & add tests
4. Commit and push (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

