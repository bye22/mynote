OK, I have used khcoder on Windows for a while but I need to move to Linux. The installation instructions are very incomplete and it took me a while to get it all to work. I was hoping to find a step-by-step instruction but to no avail, so here is my take on such a guide.

KH Coder on Ubuntu Setup (for Dummies)

I use Ubuntu 18.04, R 3.6.1, Perl 5.26.1, OpenJDK 11.0.4, mysql 5.7.27
Also Stanford POS Tagger 3.9.2

See KH Coder web sites:

https://khcoder.net/en/
https://github.com/ko-ichi-h/khcoder (also see Issues)
https://khcoder.net/en/manual_en_v3.pdf (reference manual)
https://sourceforge.net/projects/khc/ (old but see discussions)
Install MySQL server, Perl, R and Java:

Follow the standard setup
Install the following R packages in the system library (not personal),
you may wish to skip “dependencies” but this is safer:

install.packages("ade4", dependencies=TRUE)
install.packages("amap", dependencies=TRUE)
install.packages("Cairo", dependencies=TRUE)
install.packages("cluster", dependencies=TRUE)
install.packages("codetools", dependencies=TRUE)
install.packages("colorspace", dependencies=TRUE)
install.packages("dichromat", dependencies=TRUE)
install.packages("foreign", dependencies=TRUE)
install.packages("ggdendro", dependencies=TRUE)
install.packages("ggplot2", dependencies=TRUE)
install.packages("ggnetwork", dependencies=TRUE)
install.packages("ggsci", dependencies=TRUE)
install.packages("gtable", dependencies=TRUE)
install.packages("igraph", dependencies=TRUE)
install.packages("KernSmooth", dependencies=TRUE)
install.packages("lattice", dependencies=TRUE)
install.packages("maptools", dependencies=TRUE)
install.packages("MASS", dependencies=TRUE)
install.packages("Matrix", dependencies=TRUE)
install.packages("mgcv", dependencies=TRUE)
install.packages("munsell", dependencies=TRUE)
install.packages("nlme", dependencies=TRUE)
install.packages("nnet", dependencies=TRUE)
install.packages("permute", dependencies=TRUE)
install.packages("pheatmap", dependencies=TRUE)
install.packages("plyr", dependencies=TRUE)
install.packages("proto", dependencies=TRUE)
install.packages("RcolorBrewer", dependencies=TRUE)
install.packages("Rcpp", dependencies=TRUE)
install.packages("reshape2", dependencies=TRUE)
install.packages("rgl", dependencies=TRUE)
install.packages("rpart", dependencies=TRUE)
install.packages("scales", dependencies=TRUE)
install.packages("scatterplot3d", dependencies=TRUE)
install.packages("slam", dependencies=TRUE)
install.packages("som", dependencies=TRUE)
install.packages("sp", dependencies=TRUE)
install.packages("spatial", dependencies=TRUE)
install.packages("stringr", dependencies=TRUE)
install.packages("survival", dependencies=TRUE)
install.packages("vegan", dependencies=TRUE)
install.packages("wordcloud", dependencies=TRUE)
Note that some R packages will require installation of additional
Linux libraries and utilities, which may be difficult, e.g. igraph.
(You'd know it when you get an error)

Install Stanford POS tagger:

See: https://nlp.stanford.edu/software/tagger.shtml
Download the (basic) tagger
Install in a convenient location, e.g. ~/Apps/stanford-pos-tagger
Download KH Coder GitHub and install:

See: https://github.com/ko-ichi-h/khcoder
Download the GitHub
Install in a convenient location, e.g. ~/Apps/khcoder-master
Download and install Perl packages:

Run: “sudo perl -MCPAN -e shell” and execute the command:

install Bundle::CPAN (and restart)
Run: “sudo perl -MCPAN -e shell” and execute the commands:

install Jcode*
install Tk*
install DBI
install DBD::CSV (allow testing, say “y”)
install File::BOM*
install Lingua::JA::Regular::Unicode (needs sudo)*
install Net::Telnet
install Excel::Writer::XLSX
install DBD::mysql
install Spreadsheet::ParseExcel::FmtJapan
install Spreadsheet::ParseXLSX
install Statistics::ChisqIndep*
install Statistics::Lite*
install Unicode::Escape*
install Algorithm::NaiveBayes*
install Lingua::Sentence*
install Proc::Background
Run KH Coder:

cd <KH Coder installation directory, e.g. ~/Apps/khcoder-master>
perl ./kh_coder.pl (and exit)
Configure KH Code (important):

gedit /config/coder.ini
change java_path: <...>/bin/java.exe
change stanf_jar_path: <...>/stanford-postagger.jar
change stanf_tagger_path_en: <...>/models..tagger
change r_path: <...>bin/x64/Rterm.exe
change sql_username, sql_password, sql_host (localhost), sql_port (3306)
check sql_type (TCP/IP), sql_socket (MySQL)
Save
Start a normal run and test it all!

Jacob

It would be great to dockerize the Linux installation, so that it would install with one single and simple command!