# musicau-transcriptions

[![License: CC-BY-SA 4.0](https://licensebuttons.net/l/by-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0)

The coded scores available here are part of a project corpus, consisting of transcribed printed *Choralbücher*, which are crucial to congregational singing in Schleswig-Holstein churches up to the mid-19th century. The corpus has been created to be analyzed and searched through using a digital tool, we are planning to build based on preexisting tools, mainly music21. First approaches (a few queries) of this tool can be found in our [demo repository](https://github.com/cau-mi/musicau-demo). Please check out the documentation (coming soon) for further information.

This corpus was transcribed with MuseScore. A release with other formats (especially MEI) is planned.

## Source

The *Choralbuch* is accessible via the online library of the Bayerische Staatsbibliothek.

| *Choralbuch* | Number of settings | URL |
| --- | --- | --- |
| Johann Christian Kittel, *Vierstimmige Choräle mit Vorspielen* [...], Altona 1803 | 162 | [MDZ](https://www.digitale-sammlungen.de/de/view/bsb11306991?page=6,7)|


## The segmentation of the MusiCAU project corpus – SID-Chorales

Certain settings of this corpus are identified with so-called SID-numbers (= Set ID-No.), if their melody is represented in all of the four Choralbücher, that are part of the project corpus (i.e. Rein 1755_VierstimmigChoralbuch, Zinck 1785_VollständigeSammlung, Kittel 1803_VierstimmigeChoräle and Apel 1832_VollständigesChoralbuch). This group of „SID-Chorales“ includes only 96 different melodies, whereas many *Choralbücher* of this period contain 300 settings or more. For this reason, not all settings in our corpus are labelled with an SID. If a transcription belongs to a set, the SID appears at the end of the filename. 

## The two partial corpora

In order to analyze the corpus with digital methods a few adjustments of the code were in need. There is, for example, a convention of not notating the resolution of a fifth in the figured bass, if it’s considered a logic operation (an article explaining this problem can be downloaded from our [outcome repository] (https://github.com/cau-mi/musicau-outcome), cf. A_ZGMTH_2024-03-15). This would however lead to mistakes in the automatic realizations of the figured bass, which therefore needs to be altered manually. Since these adjustments would probably not be necessary in an editorial publication of the transcriptions, they were saved in a second version of the corpus (= Analysis-MusiCAU corpus, labelled with an “A-MCAU” at the beginning of the filename).

## File names

All file names reveal information about the setting: The number A-MCAU_KI1803-31a_SID014 for example represents an adjusted setting from the *Choralbuch* of J.C. Kittel, published in 1803, where it is given the number 31. Since there are two different settings within number 31, the first one is labelled “31a”, while the second one would be labelled “31b”. This numbering practice is used in the *Choralbücher* of B.F. Zinck (1785_VollständigeSammlung) and G.C. Apel (1832_VollständigesChoralbuch) and was therefore adopted for the entire project corpus (adding Rein 1755_VierstimmigChoralbuch and Kittel 1803_VierstimmigeChoräle).

## Which part of the source material has been transcribed?

In all cases of the project corpus we transcribed only the clearly preferred version of each number/setting, i.e. without all recommended variations of single bars, alternative endings or insertions (often included as accomodation for different texts). Also included in each format are the signatures of figured bass, to which we payed careful attention for analytical reasons. In order to accommodate the settings from the Apel 1832_VollständigesChoralbuch to our analytical standard, we assigned new figured-bass-signatures (because Apel’s book lacks a figured bass) based on the four-part setting.
In some cases, we filled omission and corrected evident mistakes of the sources. However, a critical report will be delivered soon (presumably with the MEI-format).

## Building a comprehensive corpus – workflow and first investigations

We are planning a successive extension of our project corpus with more *Choralbuch*-settings, that were handed down to us from the area, especially from Copenhagen, Hamburg and Lübeck. The regular workflow of our corpus-study includes the transcription in MuseScore and after that an automated conversion of each file to MusicXML. This way every setting is available for investigation with the toolpackage Music21 (our preferred toolset) and also for further conversion to any other format (Humdrum, MEI etc.). We also try to adapt other *Choralbücher* from Chorale-Corpus to MusiCAU-standards, so that we can analyze them with our tools as well.

## Credits

MusiCAU was developed at the Musicological Institute at Kiel University. For further information on the people involved see CONTRIBUTORS.txt.
The transcriptions were created and revised between January 2021 and September 2023.