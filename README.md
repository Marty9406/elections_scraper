# Elections scraper
<b> Third project at Engeto Python Academy.</b>

<b>Not finished...</b>

<h2> Project description</h2>

This project is used to extract the results of Czech parliamentary elections in 2017. You can find the results <a href="https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ">here</a>.

<h2>Library instalation</h2>
Libraries, which are used in this script, are saved in the file requirements.txt. For the instalation I recommend to use new virtual environment and with pip package installer run as follows:

- --pip version     # check the installer version
- --pip install -r requirements.txt #install used libraries

<h2>How to run a script</h2>

Running the elections_scraper.py file requires two obligatory arguments.

python elections_scraper.py \<specific-district-link\> \<csv-file-name\>

Extracted results of the specific dictring are saved in the csv file.

<h2>Project preview</h2>

Elections results of the Nový Jičín district:

1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8104
2. argument: results_novy_jicin.csv

Running the script:

python elections_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8104" "results_novy_jicin.csv"

Extraction progress:

Downloading data from URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8104

Saving to file: results_novy_jicin.csv

Completed. Terminating the program.

Partial output:

City code;City name;Eligible voters;Issued envelopes;Valid votes;...

568741;Albrechtičky;559;358;355;36;0;1;23;1;12;23;3;2;1;2;1;39;0;1;22;106;0;1;47;0;1;0;0;33;0

599212;Bartošovice;1341;735;734;39;3;0;56;2;6;104;13;2;9;0;0;38;0;0;7;281;1;2;23;0;1;3;2;140;2

568481;Bernartice nad Odrou;779;547;542;70;1;0;25;1;18;21;12;2;4;1;6;47;0;1;11;163;0;0;110;0;6;0;0;43;0

546984;Bílov;442;264;264;16;0;0;13;0;3;42;3;2;3;1;0;20;0;0;2;103;0;2;10;0;2;1;0;41;0

...
