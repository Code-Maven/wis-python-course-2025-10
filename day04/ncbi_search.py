#!/usr/bin/env python3
"""
NCBI Nucleotide Database Search Tool

This program searches the NCBI nucleotide database for a given search term
and downloads the first 2 hits in FASTA format.

Usage:
    python ncbi_search.py <search_term>

Example:
    python ncbi_search.py "human insulin"
    python ncbi_search.py "coronavirus spike protein"
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional


try:
    from Bio import Entrez, SeqIO
except ImportError:
    print("Error: Biopython is required but not installed.")
    print("Install it with: pip install biopython")
    sys.exit(1)


def setup_entrez_email() -> None:
    """Set up Entrez email (required by NCBI)."""
    # NCBI requires an email address for Entrez queries
    Entrez.email = "your.email@example.com"  # Replace with actual email
    Entrez.tool = "ncbi_search_tool"


def search_nucleotide_database(search_term: str, max_results: int = 2) -> List[str]:
    """
    Search the NCBI nucleotide database and return accession numbers.
    
    Args:
        search_term: The search query
        max_results: Maximum number of results to return (default: 2)
        
    Returns:
        List of accession numbers (IDs)
    """
    try:
        print(f"Searching NCBI nucleotide database for: '{search_term}'")
        
        # Search the nucleotide database
        search_handle = Entrez.esearch(
            db="nucleotide",
            term=search_term,
            retmax=max_results,
            sort="relevance"
        )
        
        search_results = Entrez.read(search_handle)
        search_handle.close()
        
        id_list = search_results["IdList"]
        
        if not id_list:
            print(f"No results found for search term: '{search_term}'")
            return []
            
        print(f"Found {len(id_list)} results")
        return id_list
        
    except Exception as e:
        print(f"Error during search: {e}")
        return []


def download_sequences(id_list: List[str], search_term: str) -> Optional[str]:
    """
    Download sequences from NCBI and save to a FASTA file.
    
    Args:
        id_list: List of sequence IDs to download
        search_term: Original search term (used for filename)
        
    Returns:
        Filename of the saved file, or None if failed
    """
    if not id_list:
        return None
        
    try:
        print(f"Downloading {len(id_list)} sequences...")
        
        # Fetch sequences in FASTA format
        fetch_handle = Entrez.efetch(
            db="nucleotide",
            id=id_list,
            rettype="fasta",
            retmode="text"
        )
        
        # Create a safe filename from the search term
        safe_search_term = "".join(c for c in search_term if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_search_term = safe_search_term.replace(' ', '_')
        filename = f"ncbi_nucleotide_{safe_search_term}.fasta"
        
        # Save sequences to file
        with open(filename, 'w') as output_file:
            output_file.write(fetch_handle.read())
        
        fetch_handle.close()
        
        print(f"Sequences saved to: {filename}")
        
        # Display some information about the downloaded sequences
        display_sequence_info(filename)
        
        return filename
        
    except Exception as e:
        print(f"Error during download: {e}")
        return None


def display_sequence_info(filename: str) -> None:
    """
    Display basic information about the downloaded sequences.
    
    Args:
        filename: Path to the FASTA file
    """
    try:
        sequences = list(SeqIO.parse(filename, "fasta"))
        
        print(f"\nDownloaded {len(sequences)} sequences:")
        print("-" * 60)
        
        for i, seq in enumerate(sequences, 1):
            print(f"Sequence {i}:")
            print(f"  ID: {seq.id}")
            print(f"  Description: {seq.description}")
            print(f"  Length: {len(seq.seq)} bp")
            
            # Show first 60 characters of sequence
            seq_preview = str(seq.seq)[:60]
            if len(str(seq.seq)) > 60:
                seq_preview += "..."
            print(f"  Sequence: {seq_preview}")
            print()
            
    except Exception as e:
        print(f"Error reading sequences: {e}")


def main():
    """Main function to handle command line arguments and execute the search."""
    parser = argparse.ArgumentParser(
        description="Search NCBI nucleotide database and download sequences",
        epilog="Example: python ncbi_search.py 'human insulin'"
    )
    parser.add_argument(
        "search_term",
        help="Search term for NCBI nucleotide database"
    )
    parser.add_argument(
        "-n", "--num-results",
        type=int,
        default=2,
        help="Number of results to download (default: 2)"
    )
    
    args = parser.parse_args()
    
    if not args.search_term.strip():
        print("Error: Search term cannot be empty")
        sys.exit(1)
    
    # Set up Entrez
    setup_entrez_email()
    
    # Search the database
    id_list = search_nucleotide_database(args.search_term, args.num_results)
    
    if not id_list:
        print("No sequences to download.")
        sys.exit(1)
    
    # Download sequences
    filename = download_sequences(id_list, args.search_term)
    
    if filename:
        print(f"\nSuccess! Check the file '{filename}' for your sequences.")
    else:
        print("Failed to download sequences.")
        sys.exit(1)


if __name__ == "__main__":
    main()