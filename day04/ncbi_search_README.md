# NCBI Nucleotide Database Search Tool

A command-line program that searches the NCBI nucleotide database and downloads the first 2 hits for a given search term.

## Features

- Search NCBI nucleotide database with any search term
- Download sequences in FASTA format
- Display sequence information (ID, description, length)
- Customizable number of results (default: 2)
- Safe filename generation from search terms

## Prerequisites

Before running this program, you need to install Biopython:

```bash
pip install biopython
```

Or if you're using the project's virtual environment:

```bash
pip install -r requirements.txt  # if you have a requirements.txt
# or
pip install biopython>=1.80
```

## Usage

### Basic Usage

```bash
python ncbi_search.py "your search term"
```

### Examples

Search for human insulin sequences:
```bash
python ncbi_search.py "human insulin"
```

Search for coronavirus sequences:
```bash
python ncbi_search.py "coronavirus spike protein"
```

Search for a specific gene:
```bash
python ncbi_search.py "BRCA1 gene"
```

### Advanced Usage

Download more than 2 sequences:
```bash
python ncbi_search.py "mitochondrial DNA" -n 5
```

Get help:
```bash
python ncbi_search.py --help
```

## Output

The program will:

1. Search the NCBI nucleotide database for your term
2. Download the first 2 hits (or specified number with `-n`)
3. Save sequences to a FASTA file named: `ncbi_nucleotide_[search_term].fasta`
4. Display information about each downloaded sequence:
   - Sequence ID
   - Description
   - Length in base pairs
   - Preview of the sequence

## Example Output

```
$ python ncbi_search.py "human insulin"

Searching NCBI nucleotide database for: 'human insulin'
Found 2 results
Downloading 2 sequences...
Sequences saved to: ncbi_nucleotide_human_insulin.fasta

Downloaded 2 sequences:
------------------------------------------------------------
Sequence 1:
  ID: NM_000207.2
  Description: Homo sapiens insulin (INS), mRNA
  Length: 333 bp
  Sequence: AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCCTTCT...

Sequence 2:
  ID: NG_007114.1
  Description: Homo sapiens insulin (INS), RefSeqGene on chromosome 11
  Length: 4560 bp
  Sequence: CTGGGGCCCTGGGGTGGATGGGGGAAAACTCTTAGCTCAACTTGCTGTTATGTAAC...

Success! Check the file 'ncbi_nucleotide_human_insulin.fasta' for your sequences.
```

## File Structure

The downloaded FASTA files will contain sequences in standard FASTA format:

```
>NM_000207.2 Homo sapiens insulin (INS), mRNA
AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCCTTCTGCCATGGCCC
...
>NG_007114.1 Homo sapiens insulin (INS), RefSeqGene on chromosome 11
CTGGGGCCCTGGGGTGGATGGGGGAAAACTCTTAGCTCAACTTGCTGTTATGTAACAGTGTTAGAA
...
```

## Important Notes

1. **Email Configuration**: Before using this tool extensively, you should replace the placeholder email in the code (`your.email@example.com`) with your actual email address. NCBI requires this for API usage tracking.

2. **Rate Limiting**: NCBI has rate limits on API calls. If you're making many requests, consider adding delays between calls.

3. **Search Terms**: Use specific search terms for better results. The program searches the same way the NCBI website does.

4. **File Naming**: Special characters in search terms are automatically removed or replaced to create valid filenames.

## Error Handling

The program includes error handling for:
- Missing Biopython installation
- Network connectivity issues
- Invalid search terms
- Empty search results
- File I/O errors

## Dependencies

- Python 3.12+
- Biopython >= 1.80