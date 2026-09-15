# Christian & Gospel Music — 2025

A focused research project on Christian/Gospel music in the United States, based on Luminate's **2025 Year-End Music Report** (January 2026 edition).

The project turns a broad industry report into a concise, page-referenced PDF digest covering streaming growth, market share, consumption formats, audience signals, and the limits of artist-level evidence.

## Contents

| File | Purpose |
| --- | --- |
| [Source report](2025-Year-End-Music-Report-1.2026.pdf) | User-supplied Luminate report, 85 PDF pages |
| [Christian/Gospel digest](output/pdf/Christian_Gospel_Luminate_2025_Summary.pdf) | Finished research summary |
| [Build script](scripts/build_summary.py) | ReportLab script that generates the digest |
| [License](LICENSE) | MIT license for original project code |

## Topics covered

- U.S. on-demand audio streaming volume, annual growth, and genre market share.
- Current releases and Christian/Gospel representation in song streaming tiers.
- Market share by format and the genre's album-equivalent consumption mix.
- Subscription intent and vinyl purchasing signals.
- Artist references, methodology notes, and a source-page reference map.

The digest distinguishes percentage growth from percentage-point changes, market share from within-genre format mix, and stated subscription intentions from observed conversions. Nested song tiers should not be added together. The source does not provide a dedicated ranking of Christian/Gospel artists.

## Rebuild the digest

Use Python 3 with ReportLab installed. From the repository root:

```sh
python -m venv .venv
python -m pip install -r requirements.txt
python scripts/build_summary.py
```

Activate the virtual environment before installing dependencies and running the script (`.venv\Scripts\Activate.ps1` on Windows PowerShell, or `source .venv/bin/activate` on macOS/Linux).

The script writes `output/pdf/Christian_Gospel_Luminate_2025_Summary.pdf`. Its text and figures are manually curated; it does not automatically extract or refresh data from the source PDF.

## Source and scope

Luminate, *2025 Year-End Music Report*, January 2026 edition. Page references in the digest use the 1-based PDF page order, including the cover. The analysis primarily concerns U.S. recorded-music consumption in 2025. It does not measure changes in religious belief or music-industry revenue.

No completed Power BI report or raw analytical dataset is included. Temporary schemas, installed libraries, and visual QA images are excluded from version control.

## License and attribution

Original project code is licensed under MIT. The Luminate source report remains third-party material; the project license does not grant rights to its content. Figures and findings in the digest are attributed to Luminate, with derived calculations identified separately.
