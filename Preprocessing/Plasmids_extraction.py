import os
import shutil
from Bio import SeqIO
import openpyxl

# Define the input directory for genomic files (updated path)
genomic_files_dir = "/mnt/e/Project_Scaling_Laws/Genome_download/Genomic_files"  # Updated folder path

# Define the output directory for protein sequences (updated path)
output_dir = "/mnt/e/Project_Scaling_Laws/Genome_download/"
plasmid_sequences_dir = os.path.join(output_dir, "Plasmid Sequences")
os.makedirs(plasmid_sequences_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Define the output Excel file path
excel_file_path = os.path.join(output_dir, "Plasmid_Metadata_Structured.xlsx")

# Create an Excel workbook for storing metadata across all datasets
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Plasmid Metadata"
sheet.append(["SeqID", "Genus", "Species"])  # Headers for the metadata (no AnnotationAccession now)

# Initialize a counter for files being processed
files_processed = 0

# Iterate over all .fna files in the specified directory (only process the first 5 files)
for file_name in os.listdir(genomic_files_dir):
    if file_name.endswith(".fna") and files_processed < 5:
        files_processed += 1  # Increment the file counter
        fna_file_path = os.path.join(genomic_files_dir, file_name)
        print(f"Processing file {files_processed}: {fna_file_path}")

        # Check if the .fna file exists and parse it
        try:
            found_plasmid = False  # Track if any plasmid sequences are found
            found_chromosome = False  # Track if any chromosome sequences are found
            
            # Loop through the records in the .fna file
            for record in SeqIO.parse(fna_file_path, "fasta"):
                # Print the description for debugging
                print(f"Processing record: {record.description}")

                # Check if the description indicates the sequence is a plasmid
                if "plasmid" in record.description.lower():
                    found_plasmid = True  # Set flag if a plasmid is found

                    # Get the contig ID to use as the output filename
                    seq_id = record.id

                    # Define the output file path for the plasmid sequence
                    output_file = os.path.join(plasmid_sequences_dir, f"{seq_id}_plasmid_sequence.fasta")

                    # Write the plasmid sequence to the output file named after the contig ID
                    with open(output_file, "w") as output_handle:
                        SeqIO.write(record, output_handle, "fasta")
                        print(f"Plasmid sequence extracted and saved to: {output_file}")

                    # Extract metadata for Excel file
                    description = record.description
                    description_parts = description.split()

                    if len(description_parts) > 1:
                        genus = description_parts[1]  # Genus
                        species = f"{description_parts[1]} {description_parts[2]}" if len(description_parts) > 2 else description_parts[1]  # Genus + Species

                        # Append data to the Excel sheet
                        sheet.append([seq_id, genus, species])
                
                # Check if the description indicates the sequence is a chromosome (but don't write sequence)
                elif "chromosome" in record.description.lower():
                    found_chromosome = True  # Set flag if a chromosome is found
                    
                    # Get the SeqID to include in metadata
                    seq_id = record.id

                    # Extract metadata for chromosome (no sequence writing)
                    description = record.description
                    description_parts = description.split()

                    if len(description_parts) > 1:
                        genus = description_parts[1]  # Genus
                        species = f"{description_parts[1]} {description_parts[2]}" if len(description_parts) > 2 else description_parts[1]  # Genus + Species

                        # Append metadata for chromosomes to the Excel sheet
                        sheet.append([seq_id, genus, species])

            # If no plasmid or chromosome was found
            if not found_plasmid and not found_chromosome:
                print("No plasmid or chromosome sequences found in the provided .fna file.")

        except FileNotFoundError:
            print(f"File not found: {fna_file_path}")
        except Exception as e:
            print(f"An error occurred while processing {fna_file_path}: {e}")

# Save the Excel workbook with the plasmid and chromosome metadata
workbook.save(excel_file_path)
print(f"Plasmid and chromosome metadata saved to: {excel_file_path}")
print(f"Total number of files processed: {files_processed}")
