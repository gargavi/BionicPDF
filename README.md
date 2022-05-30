## Bionic Convertor for PDFS


At the moment this supports conversion from HTML documents
to pdf. In order to convert a PDF to a PDF, you must 
first use any online tool or software to convert the PDF to HTML.I have provided a 
variety of techniques below for your reference

Outside of this, the actual python command line is 
provided below

`python main.py --file <file_name> ` 


There are also additional command line options that can be provided: 

`--saccade {10, 20, 30, 40, 50}` which dictates how spread apart the words are 

`--fixation {1, 2, 3, 4, 5}` whcih dictates the fraction of the word that is actually bolded 

`--output` this is the final output destination of the final pdf. If not output file is given, the file will be saved with the suffix 'bionic' in the same location as the input file  \n


This function works best with Adobe Acrobat's pdf to html convertor, but there is some formatting that remains off between the conversion. It is not a perfect match, but the overall spacing and headers stay the same. The only thing that usually might differ is the margins of the page and some letter sizing. The intstructions on conversion are below: 

1. Open your pdf file in Adobe Acrobt 
2. Click on the File button in the upper left corner
3. Hit Export and then choose 'HTML Webpage" as the option 

Provided the absolute or relative file path to this HTML file to the program. 

