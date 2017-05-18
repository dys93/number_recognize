#!/bin/bash

tesseract hz.font.exp0.tif hz.font.exp0 -psm 6 nobatch box.train
unicharset_extractor hz.font.exp0.box
echo "font 0 0 0 0 0" >> font_properties
shapeclustering -F font_properties -U unicharset hz.font.exp0.tr
mftraining -F font_properties -U unicharset -O hz.unicharset hz.font.exp0.tr
cntraining hz.font.exp0.tr

mv inttemp hz.inttemp
mv pffmtable hz.pffmtable
mv normproto hz.normproto
mv shapetable hz.shapetable
combine_tessdata hz
sudo mv hz.traineddata /usr/share/tesseract-ocr/tessdata/
tesseract hz.font.exp0.tif result -l hz -psm 6
cat result.txt
