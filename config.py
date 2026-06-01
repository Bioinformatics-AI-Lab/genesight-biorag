"""
config.py — GeneSight + BioRAG shared configuration
=====================================================
Single source of truth for paths, constants, and feature definitions
used across all four notebooks.

Usage in any Colab notebook
----------------------------
# Option A: repo is cloned into Colab
import sys
sys.path.insert(0, '/content/genesight-biorag')
from config import *

# Option B: Google Drive mount
import sys
sys.path.insert(0, '/content/drive/MyDrive/genesight')
from config import *

# Option C: quick one-liner (downloads config.py from GitHub)
# !wget -q https://raw.githubusercontent.com/YOUR_USERNAME/genesight-biorag/main/config.py
# from config import *
"""

from pathlib import Path

# ── Directory layout ───────────────────────────────────────────────────────────
# Override these if using Google Drive:
#   DATA_DIR  = Path("/content/drive/MyDrive/genesight/data")
#   MODEL_DIR = Path("/content/drive/MyDrive/genesight/models")
#   DB_DIR    = Path("/content/drive/MyDrive/genesight/biorag_db")

DATA_DIR  = Path("data")
MODEL_DIR = Path("models")
DB_DIR    = Path("biorag_db")
PDF_DIR   = Path("pdfs")

# ── File paths ─────────────────────────────────────────────────────────────────
# NB1 → NB2
FEATURES_PARQUET   = DATA_DIR / "genesight_features.parquet"

# NB2 → NB4
MODEL_PATH         = MODEL_DIR / "genesight_xgb.json"
SCALER_PATH        = MODEL_DIR / "genesight_scaler.joblib"
PREDICTIONS_CSV    = DATA_DIR  / "genesight_test_predictions.csv"

# NB2 figures
EVAL_PLOTS_PNG     = DATA_DIR / "eval_plots.png"
CONFUSION_PNG      = DATA_DIR / "confusion_matrix.png"
SHAP_GLOBAL_PNG    = DATA_DIR / "shap_global.png"
SHAP_BEESWARM_PNG  = DATA_DIR / "shap_beeswarm.png"
SHAP_WF_PATH_PNG   = DATA_DIR / "shap_waterfall_pathogenic.png"
SHAP_WF_BENIGN_PNG = DATA_DIR / "shap_waterfall_benign.png"

# NB3 → NB4
DB_MANIFEST        = DB_DIR / "index_manifest.json"

# NB4 outputs
REVIEW_NOTES_MD    = DATA_DIR / "biorag_review_notes.md"
REVIEW_NOTES_CSV   = DATA_DIR / "biorag_review_notes.csv"

# ── ClinVar download ───────────────────────────────────────────────────────────
CLINVAR_URL        = "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz"
CLINVAR_GZ         = DATA_DIR / "variant_summary.txt.gz"

# ── Feature definitions (NB1 engineers these; NB2 must use the same list) ─────
# ClinVar-derived features (10)
FEATURE_COLS_CLINVAR = [
    'is_missense',
    'is_synonymous',
    'is_nonsense',
    'is_splice',
    'is_lof',
    'is_frameshift',
    'is_transition',
    'chrom_encoded',
    'num_submitters',
    'review_confidence',
]

# gnomAD / gene constraint features (4)
FEATURE_COLS_GNOMAD = [
    'log_af_genome',
    'log_af_exome',
    'pLI',
    'LOEUF',
]

# Combined feature list — used for X matrix in NB2, SHAP in NB2, display in NB4
ALL_FEATURES = FEATURE_COLS_CLINVAR + FEATURE_COLS_GNOMAD  # length = 14

# Metadata columns carried alongside features (not used for training)
META_COLS = ['GeneSymbol', 'Chromosome', 'Start']

# Target column
LABEL_COL = 'label'

# Human-readable feature descriptions (used in NB4 literature queries)
FEATURE_DESCRIPTIONS = {
    'log_af_genome':    'population allele frequency in genome cohorts (gnomAD)',
    'log_af_exome':     'population allele frequency in exome cohorts (gnomAD)',
    'pLI':              'probability of loss-of-function intolerance (pLI)',
    'LOEUF':            'loss-of-function observed/expected upper bound (LOEUF)',
    'is_lof':           'loss-of-function consequence (nonsense or frameshift)',
    'is_missense':      'missense amino acid change consequence',
    'is_nonsense':      'nonsense (stop-gain) consequence',
    'is_splice':        'splice site disruption consequence',
    'is_frameshift':    'frameshift insertion or deletion consequence',
    'review_confidence':'ClinVar review status confidence level',
    'num_submitters':   'number of ClinVar submitters',
    'chrom_encoded':    'chromosomal location encoding',
    'is_synonymous':    'synonymous (silent) mutation consequence',
    'is_transition':    'transition mutation type (A↔G or C↔T)',
}

# ── ClinVar filtering ──────────────────────────────────────────────────────────
KEEP_SIGNIFICANCE = {'Pathogenic', 'Benign'}
KEEP_REVIEW_STATUS = {
    'criteria provided, single submitter',
    'criteria provided, multiple submitters, no conflicts',
    'reviewed by expert panel',
    'practice guideline',
}
KEEP_VARIANT_TYPES = {'single nucleotide variant'}
KEEP_ASSEMBLY      = 'GRCh38'

# ── gnomAD ────────────────────────────────────────────────────────────────────
GNOMAD_DATASET = 'gnomad_r4'
GNOMAD_API     = 'https://gnomad.broadinstitute.org/api'
GNOMAD_SLEEP   = 0.1       # seconds between API calls (be polite)
GNOMAD_SAMPLE  = 5000      # max variants to query (set None for full run)

# ── ML training ───────────────────────────────────────────────────────────────
RANDOM_SEED  = 42
TEST_SIZE    = 0.15        # 15% held-out test
VAL_SIZE     = 0.15        # 15% validation (from remaining 85%)
CV_FOLDS     = 5

XGB_PARAMS = dict(
    n_estimators          = 500,
    max_depth             = 5,
    learning_rate         = 0.05,
    subsample             = 0.8,
    colsample_bytree      = 0.8,
    use_label_encoder     = False,
    eval_metric           = 'auc',
    early_stopping_rounds = 30,
    random_state          = RANDOM_SEED,
    n_jobs                = -1,
    # scale_pos_weight set dynamically from class balance
)

# ── BioRAG / ChromaDB ─────────────────────────────────────────────────────────
BIOBERT_MODEL    = "pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb"
COLLECTION_NAME  = "biorag_papers"
CHUNK_SIZE       = 400      # words per chunk
CHUNK_OVERLAP    = 50       # word overlap between chunks
EMBED_BATCH_SIZE = 32
TOP_K_RETRIEVAL  = 5        # passages retrieved per query
MAX_CONTEXT_CHARS = 3000    # char cap on context sent to Claude

# ── Claude API ────────────────────────────────────────────────────────────────
CLAUDE_MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS   = 1500

# ── Plotting palette (matches presentation deck) ──────────────────────────────
COLORS = {
    'pathogenic': '#e74c3c',
    'benign':     '#2ecc71',
    'teal':       '#00A896',
    'gold':       '#F2C14E',
    'navy':       '#0D1B2A',
    'slate':      '#1B4965',
    'silver':     '#CAE9FF',
    'coral':      '#F4623A',
    'seafoam':    '#02C39A',
}


def make_dirs():
    """Create all required directories. Call at the top of each notebook."""
    for d in [DATA_DIR, MODEL_DIR, DB_DIR, PDF_DIR]:
        d.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    print("GeneSight + BioRAG configuration")
    print(f"  Features : {len(ALL_FEATURES)} ({FEATURE_COLS_CLINVAR} + {FEATURE_COLS_GNOMAD})")
    print(f"  Data dir : {DATA_DIR.resolve()}")
    print(f"  Model dir: {MODEL_DIR.resolve()}")
    print(f"  DB dir   : {DB_DIR.resolve()}")
    print(f"  BioBERT  : {BIOBERT_MODEL}")
    print(f"  Claude   : {CLAUDE_MODEL}")
