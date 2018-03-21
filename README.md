# INDRA Machines

This repository contains public configurations for INDRA machines that will investigate the literature around several pathologies, diseases, and conditions.

## Contributing

Please submit an issue if you have an idea for a new disease area with either a list of genes or search terms for PubMed. Feel free to submit a merge request if you generate a new configuration file.

### Generating A Configuration File

1. Install INDRA with `pip install indra`
2. Create a new directory and ``cd`` into it
3. Use the CLI `python -m indra.tools.machine make`

### Editing the Configuration File

See: http://indra.readthedocs.io/en/latest/modules/tools/index.html#module-indra.tools.machine

Example:

```yaml
belief_threshold: 0.8
#PUBMED SEARCH TERMS ######################
## Generic search terms
#search_terms:
#- "search term 1"
#- "search term 2"
## Gene symbol search terms
#search_genes:
#- AKT1
#- EGFR
###########################################


#GMAIL CREDENTIALS ########################
#gmail:
#  user: 
#  password: 
###########################################

#TWITTER CREDENTIALS ######################
#twitter:
#  consumer_token: 
#  consumer_secret: 
#  access_token: 
#  access_secret: 
###########################################

#NDEX CREDENTIALS #########################
#ndex:
#  user: 
#  password: 
#  network: 
###########################################
```

## Links

- INDRA [Documentation](http://indra.readthedocs.io/en/latest/)
- Gyori, B. M., Bachman, J. A., Subramanian, K., Muhlich, J. L., Galescu, L., & Sorger, P. K. (2017). [From word models to executable models of signaling networks using automated assembly](https://doi.org/10.15252/msb.20177651). Molecular Systems Biology, 13(11), 954.
