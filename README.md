
# UK VAT Identifier Discovery

This project explores whether UK company VAT numbers can be found using publicly available information.

## What I did
- Downloaded company data from Companies House.
- Cleaned the CSV data using Python.
- Selected a sample of 20 companies.
- Investigated company websites and public sources.
- Created a Python script to extract potential VAT numbers from web pages.
- Checked the identified VAT numbers using HMRC.

## Results
The program successfully extracted VAT number 899289923 for ALEXANDRA SOVERAL LIMITED, which I then verified using HMRC.

I also tested the program on EV NAILHAUS LIMITED and SKINCYCLES LIMITED.

## Limitations
The program needs website links to be provided manually and does not automatically verify VAT numbers through HMRC. Not all 20 companies were fully investigated.

This is a proof of concept, not a production-ready system.

## Files
The repository contains the Python scripts, CSV datasets, results and a Word document explaining my research.
