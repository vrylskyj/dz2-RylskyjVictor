from collections import defaultdict
import re

# Функція для знаходження повторюваних підрядків (Касіскі)
def kasiski_examination(ciphertext, min_length=3):
    ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper())  # Видаляємо непотрібні символи
    sequences = defaultdict(list)

    for i in range(len(ciphertext) - min_length + 1):
        seq = ciphertext[i:i + min_length]
        for j in range(i + min_length, len(ciphertext) - min_length + 1):
            if ciphertext[j:j + min_length] == seq:
                sequences[seq].append((i, j))

    return sequences

# Функція для знаходження можливих довжин ключа
def find_key_lengths(sequences):
    distances = []
    for positions in sequences.values():
        for i in range(len(positions) - 1):
            distances.append(positions[i + 1][1] - positions[i][1])

    # Знаходимо всі дільники відстаней для визначення кратної довжини ключа
    possible_lengths = defaultdict(int)
    for distance in distances:
        for i in range(2, distance + 1):
            if distance % i == 0:
                possible_lengths[i] += 1

    return sorted(possible_lengths.items(), key=lambda x: -x[1])

# Приклад використання методу Касіскі
ciphertext = "VYC PKHOJT XZ RJV AGXOZFR DM ZGRSIBTAC TWPLIJ. RD KSBVAA HPV RLS VCTTEPS RJV YGMWYK IH HPV'J YXF. HNV CGPRKT GH AS CYO RHL VIYCLZGKE XURQ RLDMVKI MPULGI MG T BKN MPACTZYA AWY ZMEYCUJGDG CL SEPBRKWSA MVOEGH. AFG YGVASYK, AH AFG CMLXGZ, WOGT MH TPXMWIZSB PQ C DMSX CL RUIVZKFEGTDNP. TWVQG NFD YWTU UVSW OVYCBBMJ IC ICCLRXYIR KHXUEU RPT VCXIUEA UKKFDNH HVICN AJRPBBBM. KHXZ GU R DPNZZ. KHDZC YYM UBBJ SEPBRKWSA FSGEICNQ KE ZTTIZZFJS RJZLVL OXV TWL AWCRXOOZVD. UVP VYCHX HNVRT PQ JFNT. MVKP AGL RJV CAXQZ KO LOMO SCPNHOWUA AFKEEH FSGE OCSW DVYJMM. ZYEGL GU EM HNQN KHXUE CJ Y BHFGC OG HL KDKDKOR SODR. ZQFIH TFK NEAS UTZRIXB, UI BPKJA NPXMHKE. TWHR KJ YAE. HNV NXUCVVCCMV-IVNIBPA UGHEWQV OU YCCCGHF WY KHT YYIV MU VORZBPU QGVGCZ VOJ OLU DCTC XG O MCAHZ. RJV LXGSZVECAF-EVLINFE UIHSGMV MU KCSRNIPAKJK XL HNV RPNC QW APEWHRN CVR UVCXGU NZS DDL HRAT BB G XLPZQ. VYC BHFGC LXMC QW KPG TUIMH WYTK MU MVK JUQQCEK KPMHKI OU AFG RPIBGZ, SUI AFG DMGTZOKY DM YTK ADGGOJTH PL VYC EXFLVCI BQG FD PG WSGEGMCEK KTWWAD. ND HPVZQI WSYZRTZ RQ GPDOS GEYIOGPX. CKXB ZYICNQ VYYI TFK KRJL ACE ZT IFUMES. UM CIRXLH NRS TAFKTYA LMSGAIOGGJ. YC XHNZCPS QADNPMVE ZN PU YTKGHM WY RN JUNCIBDGOHCE BHLPVPXLA UW SIFJG. EM PKHOJT XZ CXVP BHFHZD. IOC CIRXLH IRN TENTVQH XJKIYIOGPX. RWHIMYT PUB NRLVNOMV AGL RQ KFT TFZZSI PLUKPJFSTKS DM YP RPI. OWIV ACK TKIRJX OXV TD AFG RPIBGZ DAILPKRJH YCX RN PYR. HIMB MVK GOXUR QW TXXK UW FDYK, VYC IRDK FF PSJ VYC PKHY ZS IOC CIR DY HNV MJZGEZYC. YFUD TWL NQZLI HT BZEL VD HVCABBM, KHT HAVFP'H VFGWT XZ RJV RNIS. GCL PYR KJ YI HBIV SJYDCTC PGR YPMQVJ. VYMHX KNF GD ICPVYIA HNV SJYDCTC SH GU RT IOCKI NTKWR. KHDZC YYM GXOJ KHT ZWOSMA WC YF AI AFGZP EXFOC. II PQ VYC HISIKAIVP, CEB CHH RZFT, AFCK YGM FKRLAF KKIPDKG. JZVTYQKKW DY CVZNXVL CSMJM O CFRZ VD CIR HACCJ TWHR VYC LHFQ ZS CLU, EFKEESD, MIIHJ. YYCC VFOKIRZ BKJYVKSK KHT HPVZQI BG OE ARJMTU UXMV NZMHLJH. NC RTB LFRVPTG R KPG TUI MPRGPX Y JLSLLL IOGPX YH ECTX AH OC FFCH GCZ RDBPPG ZR. IAS UELN LVELQT YCX DAZPLI R SHXZKJS IOGPX GH MVGK OCL YFDGGXG OK ICACPJCAR. ORC AGA GU HSXMS AJEALQU."
sequences = kasiski_examination(ciphertext)
print("Повторювані підрядки:", sequences)

key_lengths = find_key_lengths(sequences)
print("Можливі довжини ключа:", key_lengths)
