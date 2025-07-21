# blast-output-parser
# BLAST Output Parser

A sophisticated bioinformatics tool that extracts key information from BLAST (Basic Local Alignment Search Tool) output files using advanced regular expression parsing.

## 🔬 Overview

This tool processes BLAST search result files to extract structured information about query sequences and their alignments. It's designed to handle the complex, multi-line format of BLAST output and extract relevant data for downstream analysis.

## ✨ Features

- **BLAST File Parsing**: Processes complex BLAST text output format
- **Query Information Extraction**: Parses query ID and sequence length
- **Alignment Data Mining**: Extracts accession numbers, lengths, and scores
- **Multi-line Pattern Matching**: Uses sophisticated regex with MULTILINE and DOTALL flags
- **Top Results Filtering**: Limits output to top 10 alignments for relevance
- **Accession Number Processing**: Intelligent parsing of database identifiers

## 🚀 Usage

```bash
python3 question3.py
```

The script will prompt for a BLAST output file and process it automatically.

### Input Requirements:
- BLAST output files in standard text format
- Files should contain query information and alignment results

## 📁 Input/Output

**Input**: BLAST text output files
- Standard BLAST output format
- Contains query information and alignment results
- Multi-line text with specific formatting patterns

**Output**: Structured summary including:
- Query ID and sequence length
- Top alignment accession numbers
- Alignment lengths and scores
- Formatted tabular output

## 🛠️ Technical Implementation

### Technologies:
- **Python 3**: Core programming language
- **Regular Expressions**: Advanced pattern matching with flags:
  - `re.MULTILINE`: For multi-line matching
  - `re.DOTALL`: For matching across newlines
- **Pattern Recognition**: Complex regex for bioinformatics file formats

### Key Algorithms:
```python
# Multi-line pattern matching for BLAST output
pattern = re.compile(r'complex_regex_pattern', re.MULTILINE | re.DOTALL)
```

## 🧪 Real-World Applications

- **Sequence Similarity Analysis**: Process BLAST results for homology studies
- **Database Searching**: Parse results from sequence database searches
- **Bioinformatics Pipelines**: Integrate into automated analysis workflows
- **Research Data Processing**: Extract key metrics from alignment results

## 📊 Data Processing

The tool handles:
- **Query Information**: Sequence identifiers and lengths
- **Alignment Metrics**: E-values, bit scores, identities
- **Database Identifiers**: GenBank, RefSeq, and other accession formats
- **Result Ranking**: Top alignment filtering and sorting

## 🔍 Pattern Matching Features

- **Flexible Parsing**: Handles variations in BLAST output format
- **Robust Extraction**: Deals with multi-line data structures
- **Intelligent Filtering**: Extracts most relevant alignment information
- **Error Handling**: Graceful handling of malformed input files

## 🧬 Biological Context

Essential for:
- Homology searching and analysis
- Phylogenetic studies
- Functional annotation
- Comparative genomics
- Protein family analysis

## 📝 Author

Rohan Ray - Johns Hopkins University MS Bioinformatics Program
