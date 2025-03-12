import csv
import requests
from bs4 import BeautifulSoup


# Function to retrieve gene and consequence information
def get_snp_info(snp_id):
    while True:
        url = f"https://www.ncbi.nlm.nih.gov/snp/rs{snp_id}"
        response = requests.get(url)
        if response.status_code != 200:
            return "Failed to retrieve data"

        soup = BeautifulSoup(response.content, 'html.parser')

        # Check for SNP merge information
        status = soup.find('dt', string='Status')
        if status and status.find_next_sibling('dd'):
            merge_link = status.find_next_sibling('dd').find('a')
            if merge_link and merge_link.get('href'):
                new_snp_id = merge_link.get('href').replace('rs', '')  # Extract new SNP ID from the link
                snp_id = new_snp_id.strip()
                continue

        gene_consequence = "Not found"
        elements = soup.find_all(['dt', 'dd'])
        for i, elem in enumerate(elements):
            if 'Gene : Consequence' in elem.get_text():
                if i + 1 < len(elements):
                    # Extracting all gene:consequence pairs from the <dd> tag
                    gene_consequence_pairs = elements[i + 1].find_all(['div', 'span'])
                    # Debug: Print found pairs
                    print([pair.get_text(strip=True) for pair in gene_consequence_pairs])
                    gene_consequence = ', '.join([pair.get_text(strip=True) for pair in gene_consequence_pairs])
                    break

        return gene_consequence


# File paths
input_file_path = 'sample_with_id.csv'
output_file_path = 'testno1.csv'

# Read SNP IDs and write the results
with open(input_file_path, mode='r') as infile, open(output_file_path, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # the first row is the header
    header = next(reader)
    header.append('Gene : Consequence')
    writer.writerow(header)

    for row in reader:
        snp_id = row[0]  # Adjust the index if the SNP ID is not in the first column
        gene_consequence = get_snp_info(snp_id)
        row.append(gene_consequence)
        writer.writerow(row)

print("Processing complete. Check the output in 'snp_gene_consequences.csv'")
