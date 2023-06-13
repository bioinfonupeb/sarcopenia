def diff(name_1, name_2):
    with open(name_1) as file_1:
        genes_1 = file_1.readlines()
        genes_1 = [gene.rstrip() for gene in genes_1]
    
    with open(name_2) as file_2:
        genes_2 = file_2.readlines()
        genes_2 = [gene.rstrip() for gene in genes_2]
    
    equal_genes = [gene for gene in genes_1 if gene in genes_2]
    print(list(set(equal_genes)))
