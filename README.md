# Obsidian Exporter

A simple GUI tool to export an Obsidian Markdown note along with its linked images into a single target directory.

---

## 🔧 Prerequisites

- **Python 3.10+**
- **uv** package manager
  - Optional, but recommended
  - Install via official installer, Homebrew, or PowerShell; pip-supported but not recommended
- **Git** (to clone the repository)

---

## 🚀 Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/InsolentFlunkey/obsidian-exporter.git
   cd obsidian-exporter
   ```

2. **Install uv** (choose one):

   - If you prefer not to use uv, see Alternative instructions below to create a virtual environment and install requirements.txt
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

3. **Create the environment & install dependencies**  
   Using the existing `pyproject.toml` and `uv.lock` from the repo:
   ```bash
   uv sync
   ```

4. *(Optional)* **Add or update dependencies**  
   ```bash
   uv add <package-name>
   uv sync
   ```

### Alternative: Traditional venv + requirements.txt

If you prefer not to use **uv**, you can use Python’s built-in `venv` and a `requirements.txt` workflow:

1. **Create & activate a virtual environment**:
   - Note:  In the commands below, you may need to adjust your python interpreter name
   - On Linux:
   ```bash
   #  Linux:
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   - On Windows:
   ```Powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
---

## ⚙️ Running the App

1. **Update default Vault and Export locations in script (optional but recommended)**
   ```
   # === User-defined defaults (modify these paths as desired) ===
   DEFAULT_VAULT_ROOT = r'C:/your/vault/location'
   DEFAULT_EXPORT_DIR = r'C:/your/export/location'
   ```

2. **Launch the app**
   - Note: `vault_root` and `export_dir` are optional parameters.  If updated in step 1 above, they are not needed.
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

### Command-Line Options

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
├── requirements.txt      # Only needed if not using uv
└── uv.lock               # uv lockfile recording dependencies
```  

---

## 💾 Version Control

When committing to Git and pushing to GitHub, **include**:

```gitignore
pyproject.toml      # Project metadata and dependencies
uv.lock             # Locked dependency graph
```

In your `.gitignore`, **ignore**:

```gitignore
.venv/              # Virtual environment
__pycache__/        # Python cache files
*.py[cod]           # Compiled Python files
.env                # Local environment variables (if used)
.python-version     # uv-managed Python version file (optional)
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
