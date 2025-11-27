def create_codon_dict(file_path):
  with open(file_path, 'r') as file:
    rows = file.readlines()

  dict = {}

  for row in rows:
    data_amino = row.strip().split('\t')
    if len(data_amino)>=2:
      codon = data_amino[0].strip()
      amino_acid = data_amino[2].strip()
      dict[codon] = amino_acid
  return dict
