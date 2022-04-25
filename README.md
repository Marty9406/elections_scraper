# Elections Scraper

**Third project at Engeto Python Academy.**

## Project description

This script is used to extract results of the Czech parliamentary elections in 2017. You can find those results [here](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Library instalation

Libraries, which are used in this script, are saved in the file *requirements.txt*. For the instalation I recommend to use new virtual environment and with the pip package installer run as follows:

<table>
  <tr>
    <td>pip --version</td>
    <td># check the installer version</td>
  </tr>
  <tr>
    <td>pip install -r requirements.txt</td>
    <td>#install used libraries</td>
  </tr>
 </table>
 
## How to run a script

Running the *elections_scraper.py* file requires two obligatory arguments:

<table>
  <tr>
    <td>python elections_scraper.py</td>
    <td>link_to_a_specific_district</td>
    <td>file_name.csv</td>
  </tr>
</table>

Extracted results of the specific dictring are saved in the csv file.
  
## Project preview

Elections results of the Nový Jičín district:
<table>
  <tr>
    <td>1. argument:</td>
    <td>https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8104</td>
  </tr>
  <tr>
    <td>2. argument:</td>
    <td>results_novy_jicin.csv</td>
  </tr>
</table>
 
### Running the script:

> python elections_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8104" "results_novy_jicin.csv"

### Extraction progress:

> Downloading data from URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8104

> Saving to file: results_novy_jicin.csv

> Completed. Terminating the program.

### Partial output:

City code;City name;Eligible voters;Issued envelopes;Valid votes;...

568741;Albrechtičky;559;358;355;36;0;1;23;1;12;23;3;2;1;2;1;39;0;1;22;106;0;1;47;0;1;0;0;33;0

599212;Bartošovice;1341;735;734;39;3;0;56;2;6;104;13;2;9;0;0;38;0;0;7;281;1;2;23;0;1;3;2;140;2

...
