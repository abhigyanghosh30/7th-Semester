python merge.py ind1.txt ind2.txt /scratch/mastergdata/ind_1_2.txt &
python merge.py ind3.txt ind4.txt /scratch/mastergdata/ind_3_4.txt &
python merge.py ind5.txt ind6.txt /scratch/mastergdata/ind_5_6.txt &
python merge.py ind7.txt ind8.txt /scratch/mastergdata/ind_7_8.txt &
python merge.py ind9.txt ind10.txt /scratch/mastergdata/ind_9_10.txt &
python merge.py ind11.txt ind12.txt /scratch/mastergdata/ind_11_12.txt &
python merge.py ind13.txt ind14.txt /scratch/mastergdata/ind_13_14.txt &
python merge.py ind15.txt ind16.txt /scratch/mastergdata/ind_15_16.txt &
python merge.py ind17.txt ind18.txt /scratch/mastergdata/ind_17_18.txt &
python merge.py ind19.txt ind20.txt /scratch/mastergdata/ind_19_20.txt &
python merge.py ind21.txt ind22.txt /scratch/mastergdata/ind_21_22.txt &
python merge.py ind23.txt ind24.txt /scratch/mastergdata/ind_23_24.txt &
python merge.py ind25.txt ind26.txt /scratch/mastergdata/ind_25_26.txt &
python merge.py ind27.txt ind28.txt /scratch/mastergdata/ind_27_28.txt &
python merge.py ind29.txt ind30.txt /scratch/mastergdata/ind_29_30.txt &
python merge.py ind31.txt ind32.txt /scratch/mastergdata/ind_31_32.txt &
python merge.py ind33.txt ind34.txt /scratch/mastergdata/ind_33_34.txt;
python merge.py /scratch/mastergdata/ind_1_2.txt /scratch/mastergdata/ind_3_4.txt /scratch/mastergdata/ind_1_4.txt &
python merge.py /scratch/mastergdata/ind_5_6.txt /scratch/mastergdata/ind_7_8.txt /scratch/mastergdata/ind_5_8.txt &
python merge.py /scratch/mastergdata/ind_9_10.txt /scratch/mastergdata/ind_11_12.txt /scratch/mastergdata/ind_9_12.txt &
python merge.py /scratch/mastergdata/ind_13_14.txt /scratch/mastergdata/ind_15_16.txt /scratch/mastergdata/ind_13_16.txt &
python merge.py /scratch/mastergdata/ind_17_18.txt /scratch/mastergdata/ind_19_20.txt /scratch/mastergdata/ind_17_20.txt &
python merge.py /scratch/mastergdata/ind_21_22.txt /scratch/mastergdata/ind_23_24.txt /scratch/mastergdata/ind_21_24.txt &
python merge.py /scratch/mastergdata/ind_25_26.txt /scratch/mastergdata/ind_27_28.txt /scratch/mastergdata/ind_25_28.txt &
python merge.py /scratch/mastergdata/ind_29_30.txt /scratch/mastergdata/ind_31_32.txt /scratch/mastergdata/ind_29_32.txt;
python merge.py /scratch/mastergdata/ind_1_4.txt /scratch/mastergdata/ind_5_8.txt /scratch/mastergdata/ind_1_8.txt &
python merge.py /scratch/mastergdata/ind_9_12.txt /scratch/mastergdata/ind_13_16.txt /scratch/mastergdata/ind_9_16.txt &
python merge.py /scratch/mastergdata/ind_17_20.txt /scratch/mastergdata/ind_21_24.txt /scratch/mastergdata/ind_17_24.txt &
python merge.py /scratch/mastergdata/ind_25_28.txt /scratch/mastergdata/ind_29_32.txt /scratch/mastergdata/ind_25_32.txt;
python merge.py /scratch/mastergdata/ind_1_8.txt /scratch/mastergdata/ind_9_16.txt /scratch/mastergdata/ind_1_16.txt &
python merge.py /scratch/mastergdata/ind_17_24.txt /scratch/mastergdata/ind_25_32.txt /scratch/mastergdata/ind_17_32.txt;
python merge.py /scratch/mastergdata/ind_1_16.txt /scratch/mastergdata/ind_17_32.txt /scratch/mastergdata/ind_1_32.txt;
python merge.py /scratch/mastergdata/ind_33_34.txt /scratch/mastergdata/ind_1_32.txt /scratch/mastergdata/indmerge.txt
python mergewords.py /scratch/mastergdata/indmerge.txt /scratch/mastergdata/indfinal.txt