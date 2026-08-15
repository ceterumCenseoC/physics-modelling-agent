```python
import numpy as np
import itertools
import scipy.linalg
import scipy.sparse

# ==========================================
# 1. Data Loading and State Reconstruction
# ==========================================

# Data for the state |psi>.
# Format: integer_bit_string, real_part, imaginary_part
raw_data = """
0 0.0022260133806476204 -0.0022445810580213
2048 6.917873540819352e-06 0.0015234864994924646
1024 1.752544554299999e-05 0.003859134766412684
512 1.218043435279874e-05 0.002682743439100366
3072 -0.002163132458658175 -0.002145236212405833
2560 -0.0012538172369638344 -0.001243446272870564
1536 -0.001232473130920503 -0.0012222806130252491
256 9.766039476497339e-06 0.0021519405691894653
1280 0.003242679892071879 0.003215868561153704
768 0.0007275688534700823 0.0007215641907428513
128 1.4712997435567425e-06 0.00032299974043209533
640 0.0007713924763609131 0.0007650092995170101
384 -0.0008884738174692913 -0.0008811303831314521
64 -3.503866421284426e-06 -0.0007718685082024913
320 0.0035652755474317047 0.003535790305279392
192 -0.001166745034263001 -0.001157100345934561
32 4.9912240876800594e-06 0.0010973171589839508
160 0.001876243591101674 0.0018607201654277767
96 0.0006758606393707776 0.000670281775192485
16 -4.3547642984871025e-06 -0.0009549960822405046
80 -0.004118055670358198 -0.0040840240488312345
48 0.005264536719694809 0.005220995904771587
8 -1.1059891899498303e-05 -0.0024391994245923513
40 -0.01220957929991213 -0.012108583835281007
24 0.00806586299967634 0.00799913168341996
4 -1.130734422236901e-05 -0.0024900482467269287
20 -0.007844233007829538 -0.0077792763830423625
12 0.002541221869462284 0.0025201313685745204
2 -1.7675542750344074e-05 -0.003897471683386611
10 -0.010537905147566095 -0.01045078152933967
6 0.008883683851870099 0.008810288986860051
1 -6.8739793837404584e-06 -0.001511933600751997
5 -0.00482971927256642 -0.004789804530568148
3 -0.0013166715768775689 -0.0013058002089722917
2049 -0.0011684196711228081 -0.001158772151435154
1025 0.00522809479458812 0.005184856974701736
513 0.0027118184029254664 0.002689393587745804
3073 -0.007014482390655918 3.184146028043443e-05
2561 -0.0040817000280380525 1.852819013103294e-05
1537 0.000756016030490856 -3.434104678483512e-06
257 0.0008177592473625547 0.0008110024670804617
1281 0.005790584693224299 -2.6284815266718814e-05
769 0.002112591437927121 -9.582478606108149e-06
129 -2.888707690918471e-05 -2.864328372106518e-05
641 0.0009443659845946591 -4.2989783668333275e-06
385 -0.00045310113880880817 2.0577379656262417e-06
65 -0.003151013952856525 -0.0031249613672334063
321 0.005141302464947118 -2.3339551661328457e-05
193 -0.0003225435054747576 1.4676656546260404e-06
33 0.005041290610966018 0.004999584650666832
161 0.0005242524028407021 -2.3862329993907664e-06
97 0.0006484091874630449 -2.924420208799226e-06
17 -0.004230296907625065 -0.00419529745315369
81 -0.002887963837350872 1.3087751648089732e-05
49 0.0034693319532947894 -1.574660892531404e-05
9 0.001875409989878572 0.0018598995294804343
41 -0.014619524531047957 6.639930057844973e-05
25 0.01082811454729098 -4.9188823293446876e-05
21 -0.00264578160323021 1.2090614964073248e-05
13 -0.005617285686123944 2.5419390579950776e-05
11 -0.011785568844446018 5.349788384833513e-05
7 0.012909664149370184 -5.855827195672591e-05
2050 0.0062481111548267155 0.006196477758403894
1026 -0.0089069578942267 -0.008833321736086934
514 -0.0003936152064683048 -0.0003903709365116616
3074 0.013031975469014337 -5.913681985001722e-05
2562 0.005557877793205489 -2.5221743377076822e-05
1538 -0.012109003771838848 5.497674396007974e-05
258 0.0003078910634699781 0.0003053360610310436
1282 -0.003438144068338394 1.560172302242893e-05
770 0.0005179891781486314 -2.3415705069411283e-06
130 -0.0006054979160903024 -0.0006005094064117322
642 0.0020065025222558504 -9.09372995061772e-06
386 -0.0009179202659902429 4.162221157622055e-06
66 0.009816145326954441 0.009734980292078482
322 -0.0033261756137010303 1.5090567109545972e-05
194 -0.003230274370115993 1.4657053997115785e-05
34 -0.013533979999198665 -0.013422047523472966
162 0.004909441309202976 -2.2284152330423295e-05
98 0.0013183521538087785 -6.024427576205622e-06
18 0.01149719393426167 0.011402118305286486
82 -0.007373367325390438 3.350943134625556e-05
50 0.009278887746719009 -4.214324847184919e-05
42 -0.001341427026779904 6.055781433426817e-06
26 -0.0029721432105946416 1.3535157058629043e-05
22 -0.02259539766700788 0.00010252814427885651
14 0.02575685538915428 -0.00011685881122088555
2051 0.007131234788996993 -3.2355044849217796e-05
1027 -0.012813920800556204 5.816316473466353e-05
515 -0.0034002166539434074 1.5421919728894173e-05
3075 0.008576226838168258 -0.008647724483501413
2563 0.006553735201592523 -0.006608359023314136
1539 -0.010479846058610161 0.0105672300505317
259 4.9774855283315736e-05 -2.32602001985588e-07
1283 -0.0020429813958777257 0.0020600144607122186
771 -8.784670147941612e-05 8.859084236137724e-05
131 -0.00016823779851751265 7.542907275163305e-07
643 0.001179301302292027 -0.0011891088883502908
387 -0.00030202664253716524 0.0003045416767238085
67 0.01163071882462268 -5.279810100375388e-05
323 -0.001901262544098133 0.0019171059812880774
195 0.0002895066947135914 -0.0002919399392058171
35 -0.017226355608399455 7.821739686794638e-05
163 -0.0004299143228542945 0.0004335174543407741
99 0.0034153940984085903 -0.0034439336749568757
19 0.014529674325377643 -6.596686979384413e-05
83 -0.0047362053398749444 0.004775744130811917
51 0.002749846629655469 -0.0027727814988450917
43 0.005154741496515697 -0.005197787583957449
27 -0.005477091946878795 0.005522817249871074
23 -0.012493321373514724 0.012597418299966636
15 0.01660444935557391 -0.01674279301953218
2052 -0.0015666639817233624 -0.0015537254392953622
1028 0.010476040297818932 0.010389432855086346
516 -0.005375021531472029 -0.005330559001800633
3076 -0.01220381640735738 5.538239001245889e-05
2564 0.000384802032749532 -1.7626109971081473e-06
1540 0.020395171733759602 -9.257315140312377e-05
260 0.006222888038117903 0.006171450379874099
1284 0.0029418803061813984 -1.3329790159791115e-05
772 -0.01178371114939358 5.347225072121847e-05
132 0.0041489952008222615 0.004114659359928755
644 -0.004876632751849735 2.2159915402401134e-05
388 -0.004067897495430103 1.845453492402888e-05
68 -0.010320313668367206 -0.010234960032422597
324 0.011709613955274811 -5.314079265660024e-05
196 -0.0012359853829326532 5.590619752173352e-06
36 0.009604489864769444 0.009525021247150604
164 0.0027276568665316925 -1.238573162279245e-05
100 -0.000992765243552612 4.552952993351485e-06
84 -0.0028749271155167023 1.2960085106616901e-05
52 0.005588697777151139 -2.5335187905968994e-05
44 -0.025224386150798923 0.00011450531402300424
28 0.01855346787040641 -8.427099930131615e-05
2053 0.003519040367620685 -1.5958546715771442e-05
1029 0.009560590790587783 -4.34076451489057e-05
517 -0.0008564171678770648 3.926215904576642e-06
3077 -0.0028266374305928495 0.0028502355896825667
2565 -0.007327606718506027 0.007388629525596505
1541 0.022338143711993746 -0.022524351700440787
261 0.007914916650981091 -3.592079617110143e-05
1285 -0.0036697264418048964 0.003700346696362108
773 -0.007845605844887475 0.00791098746444574
133 0.0035217829263247185 -1.6019044584722243e-05
645 -0.003256499252660077 0.0032836614757408207
389 -0.003474471171821421 0.003503423671342363
69 -0.00511693805635997 2.326191288458401e-05
325 0.002673294672874145 -0.0026955580094523658
197 -0.008397794765285226 0.008467824839466993
37 0.003238045218859204 -1.4750283092426223e-05
165 0.013367807534068401 -0.01347933537130984
101 -0.008173681784026925 0.008241888887257843
85 -0.0004190888849284129 0.0004225145878688574
53 0.010754830902194224 -0.01084454289110282
45 -0.02375628030955509 0.023954367896728456
29 0.015461869638251432 -0.01559080388078866
2054 -0.01568153511226 7.11212678491218e-05
1030 0.0127976980310124 -5.80389178720056e-05
518 -0.0195143908211111 8.851833104319533e-05
3078 -0.014264581002533803 0.01438339907151328
2566 0.02003238059847776 -0.020199276225863223
1542 -0.01813722832096757 0.01828833477104704
262 0.0019467702386241506 -8.820205634855613e-06
1286 0.013186784368796316 -0.01329670456516695
774 -0.0025047492104205253 0.0025256494044320846
134 0.006597605971472887 -2.9917049649817157e-05
646 -0.0008682125358344656 0.0008755061948478347
390 0.0012581488757754601 -0.00126862330949783
70 -0.025754832936079296 0.00011685497063790352
326 0.014399147153039015 -0.014519211831941794
198 0.019813152028680687 -0.019978429808932295
38 0.02734817581188146 -0.00012409980761032117
166 -0.029604856230045783 0.02985183379794595
102 0.017404606182001393 -0.017549689921403707
86 -0.0022406660925078452 0.0022592081541670753
54 -0.01878104307757206 0.018937835221024647
46 0.01840131556780221 -0.018554758787280027
30 -0.008045783334229069 0.008112735612175064
2055 -0.009658362587943925 0.009738816336460775
1031 0.004580515343830371 -0.004618640778734077
519 -0.012931259822397312 0.01303898645850351
3079 6.81256213771949e-05 0.015025084665216775
2567 -0.00014051261513723317 -0.030977007294658524
1543 0.00015975741554406087 0.03521453917770841
263 -0.00024662839616136476 0.0002486976971344208
1287 -8.147398686946569e-05 -0.017952169340897644
775 1.2282558186919058e-06 0.000266574191489405
135 0.003819201935552759 -0.0038510041345616265
647 2.5363882045931547e-07 4.797010896234678e-05
391 -1.3021486873640858e-05 -0.0028721500548195213
71 -0.014582853247891124 0.014704358578996225
327 -7.788304830783733e-05 -0.01715576680721252
199 -0.00013294742771374215 -0.029276360855611635
39 0.014680480706795887 -0.014802810124542414
167 0.00020092388711089653 0.04424176891819646
103 -0.00012643335090182356 -0.027854841620348528
87 1.881992654217145e-05 0.004161887141807163
55 0.00013018298460557162 0.028650277462767274
47 -0.00016155992627452922 -0.035587251878480615
31 8.095213868281162e-05 0.01784995312274058
2056 0.005918971001108255 0.005870057227316217
1032 -0.011942736421693242 -0.011844002536806243
520 0.00359980280405013 0.00357000959671438
3080 0.0159319425021103 -7.230074432097253e-05
2568 0.003268581600480614 -1.4811529178282764e-05
1544 -0.02180260980232276 9.896017024912024e-05
264 -0.0037997481421310603 -0.003768336132567328
1288 -0.0013930379830924952 6.309931528061398e-06
776 0.008783387258485913 -3.985294873004218e-05
136 -0.00017822656243540432 -0.0001767594843339192
648 0.001569315159605111 -7.124933801879726e-06
392 -0.001341431758245747 6.091341315522054e-06
72 0.008555134086585186 0.008484392706183213
328 -0.0030209785832427194 1.3716013776720123e-05
200 -0.0024377265644506367 1.1071044787836808e-05
168 0.0037087755243582435 -1.6852448408914533e-05
104 0.0007182163269829889 -3.2816401783746117e-06
88 -0.005341375601285141 2.4272037760455692e-05
56 0.006972599880536769 -3.168161846683726e-05
2057 0.003983814496652765 -1.807873749997083e-05
1033 -0.01695038520610011 7.694793019614913e-05
521 -0.0027636665739290142 1.2511218890334815e-05
3081 0.009299508130186573 -0.009377061059107872
2569 0.009989341852324527 -0.010072560280498192
1545 -0.02160359348438445 0.021783672880288336
265 -0.005246164826822133 2.3809102390393925e-05
1289 0.001775188487460698 -0.0017899975813054942
777 0.005250558073892745 -0.005294301674970108
137 -0.00035853932259477013 1.6237597407714927e-06
649 -0.0004715670206526628 0.0004755229179129203
393 0.0008491012326861585 -0.0008561747411077594
73 0.00983183673873599 -4.463171707475655e-05
329 -0.0007552389897770184 0.0007615390916276926
201 0.0013241082723457003 -0.0013351439025325901
169 -0.0021074989687730463 0.0021250723671342405
105 0.0014972712600557435 -0.0015097819537927373
89 -0.001348470525247298 0.001359742351749092
57 0.0004924713163689813 -0.0004965813400240219
2058 0.010640318609662486 -4.8274652253932416e-05
1034 0.007059936148499118 -3.20922990448717e-05
522 0.019273432882100025 -8.746675543447042e-05
3082 -0.0003955123436277897 0.00039889510773460555
2570 -0.016804919114458333 0.016944974276753122
1546 0.010505280416875535 -0.010592784632510092
266 0.0031705474557223814 -1.4387145903190953e-05
1290 -0.001480231104415115 0.00149256274612253
778 0.0032164499001222186 -0.0032432802540663472
138 0.0018649617012494394 -8.468343488899178e-06
650 0.0025975182708335527 -0.0026192175665073784
394 -0.0030959498512821864 0.0031217508464632926
74 0.000564012312493777 -2.569159659411442e-06
330 -0.0010437935190831043 0.0010524845407574902
202 -0.003916606569480612 0.003949247010330761
170 0.006535077677994509 -0.006589594180651795
106 0.004943291831642773 -0.004984526978189653
90 -0.010697391160823409 0.010786582119687632
58 0.010720819810984146 -0.010810267133168534
2059 0.0031805161549595326 -0.003207020217736151
1035 0.010013791419946998 -0.01009733919765024
523 0.01439429775355572 -0.014514284887292535
3083 3.8600012603378413e-05 0.008492946734426021
2571 0.0001258759519995601 0.027741058908751736
1547 -9.340432264302992e-05 -0.02059063146683932
267 0.0018521116426462479 -0.0018675434126698086
1291 -5.387754590070576e-07 -0.00011752862992043999
779 -2.0797125122296104e-05 -0.004578529758348978
139 -0.0007399001480538342 0.000746081634321899
651 -3.118592604171628e-05 -0.006862546332242637
395 1.3323207749607923e-05 0.002936378025853667
75 -0.0015603239948804306 0.0015733284694762525
331 2.7368015059390585e-06 0.0006037770107117598
203 1.89635746676189e-05 0.0041783213588157874
171 -2.972065359790845e-05 -0.006544856666996399
107 -2.4955763339300516e-05 -0.005496753178565097
91 5.140270069859953e-05 0.011324343308070374
59 -4.506223401321141e-05 -0.009921119903616321
2060 0.006544005895915909 -2.9642284889318267e-05
1036 -0.029002321684379172 0.0001316201558529895
524 0.006797286147019514 -3.079149047465516e-05
3084 0.0215589526877225 -0.021738630939281568
2572 -0.0101572776496938 0.010241856826799624
1548 0.013083975826395054 -0.013193004788600408
268 -0.013414073634182488 6.085964105807259e-05
1292 -0.01888947393322485 0.019046917647207708
780 5.676453708207126e-05 -5.7260986479205076e-05
140 -0.0050721305352205565 2.3015957795215846e-05
652 0.00530959470895311 -0.005353920624464297
396 -0.005477953697998397 0.005523633129414478
76 0.02157975939110901 -9.790009820917486e-05
332 -0.010198903531052135 0.010283968992505848
204 -0.013560217098773265 0.013673329389191715
172 0.019519116070056627 -0.019681959379234924
108 -0.020128387918260437 0.020296216353258224
92 0.011752244098228814 -0.011850169983013812
60 0.0021772183939058835 -0.0021954764847517683
2061 0.01264454003967165 -0.012749838913664161
1037 -0.02267448237774907 0.022863480744572017
525 0.00018316705899506705 -0.00018458674586126287
3085 -0.00017505543007370378 -0.03858263420018518
2573 4.978671238198791e-05 0.01098885906193322
1549 -0.00013560008470489467 -0.02988598223292428
269 -0.0038702219755667867 0.0039024429759307437
1293 0.00015452457908885964 0.03404718600782619
781 4.3515967163610456e-05 0.009590405196786916
141 0.0030900027159656627 -0.0031158143855254303
653 1.4190392309767884e-05 0.0031319627356351442
397 5.4586688198459614e-05 0.012026476969746281
77 0.013242471215640815 -0.013352823142807243
333 6.63434193021604e-05 0.014612877751980391
205 0.00010390415940951507 0.022886438584606376
173 -0.00016002681290661265 -0.03523347961617928
109 0.00011807503298641618 0.026012368844658493
93 -3.9520076244073806e-05 -0.008711625052698003
61 -6.947385768882147e-05 -0.01528265809525004
2062 -0.022953683215233087 0.02314495922255178
1038 0.008100841919809528 -0.008168325807158972
526 0.011338414179561824 -0.011432978593245583
3086 0.0001033263600800727 0.022778994027054893
2574 5.657276479883888e-05 0.01245827551900224
1550 8.445110288380599e-05 0.01861105915067668
270 -0.014405037602632932 0.014525156283389587
1294 -7.192737189876538e-05 -0.015836974681750344
782 -0.00010022266966653978 -0.02207853889271186
142 -0.017938227403473016 0.01808788427090158
654 -0.00013033049385401948 -0.028703456104565324
398 -4.7650600762174626e-05 -0.01050171047192366
78 0.0034500758637544034 -0.003478784231241556
334 -3.3775156481190986e-06 -0.0007484118232542718
206 -3.65849780233743e-05 -0.008069026589795232
174 7.763266647940893e-05 0.01708756519911621
110 6.183041342600842e-05 0.013619125409588232
94 -0.00011716092633829338 -0.025817685497814605
62 0.00014846575498363905 0.03268843170842672
2063 0.0001585645849570084 0.0349522152968031
1039 -0.00010253257014794604 -0.022598427933409968
527 -8.011455507947511e-05 -0.017640564060446742
3087 0.02402942466451518 0.023830844513956662
2575 0.008435476232398882 0.008365660104178087
1551 0.016534401750851784 0.016397730276511747
271 7.590409900552535e-05 0.01671764898149469
1295 -0.017736895519944833 -0.01759018752974853
783 -0.01687928410751274 -0.016739709890265523
143 0.00011362587524856842 0.02501605432834719
655 -0.019942271270827334 -0.01977733062577444
399 -0.009193830058578519 -0.009117830334215734
79 3.8897706758149965e-06 0.0008509626299821749
335 -0.003224320723434005 -0.0031976775432354
207 -0.009221479209541956 -0.009145273650769893
175 0.018077760320844467 0.01792814586778197
111 0.0034333467637127583 0.003404946981968331
95 -0.014103463307353143 -0.013986881726867125
63 0.022898317251685712 0.022708822395061626
2064 -0.0033378122030472013 -0.0033102444337215963
1040 0.010260105465485675 0.010175270666370142
528 0.0010665670198309778 0.0010577487375547192
3088 -0.013623075405907278 6.18298761315857e-05
2576 -0.005246787974000455 2.380525250011283e-05
1552 0.009904843306957439 -4.494042598107694e-05
272 0.004567946169845751 0.00453017555660328
1296 0.0033625830044490823 -1.5256271129237216e-05
784 -0.00412754949970223 1.8732320581082642e-05
144 -0.0034656597583132376 -0.003436978389563485
656 0.004623863979088827 -2.100861390884301e-05
400 0.003601935870421853 -1.635303850946747e-05
336 0.003894186892775726 -1.7687904253213786e-05
208 0.0012879581043182384 -5.843471264338343e-06
176 -0.001653565736635381 7.517833102816427e-06
112 8.471662091806166e-05 -3.7692422541627317e-07
2065 0.001120059748428704 -5.0951395147117395e-06
1041 0.011959947530471972 -5.429854665604343e-05
529 0.004620722986647561 -2.097849342341448e-05
3089 -0.006456484746302715 0.006510330235796831
2577 -0.005792172943885743 0.00584045793129352
1553 0.007526095845866214 -0.007588815445112366
273 0.006784706072562552 -3.0800649420273684e-05
1297 -0.0007837396011584071 0.0007902917748748329
785 -0.0037279382538401343 0.0037590050922653748
145 -0.0017134030127792617 7.79592897325422e-06
657 0.005580618309684534 -0.005627177084235628
401 -0.0004667448216106298 0.00047063233515352973
337 0.0017920999865500232 -0.0018070516138548017
209 0.002591658387035501 -0.0026132735083669455
177 -0.004145369027441971 0.004179955103338487
113 -0.0005799536068534013 0.0005847852392472479
2066 -0.016257780508974532 7.378246096770953e-05
1042 0.0018379359124667729 -8.30209761517768e-06
530 -0.011722106560345412 5.324723533442613e-05
3090 -0.004200391652786115 0.004235351945495089
2578 0.0040052581565119035 -0.004038706587551746
1554 0.008673763309840201 -0.008746093795117954
274 -0.0032219279102350036 1.462834313347726e-05
1298 0.0029000897706866775 -0.002924284709093327
786 -0.0027564419622108454 0.002779428075082325
146 -0.007414578717744561 3.364621784920606e-05
658 -0.004806628799027167 0.00484669167199559
402 0.003762693887563866 -0.003794066155311477
338 0.0022608231154714856 -0.0022796694931412715
210 -0.010205694904335 0.010290828726252383
178 0.012601180540724899 -0.012706288463854597
114 -0.001641035797889103 0.0016547725371540644
2067 -0.007684643130368637 0.007748710023095929
1043 -0.003941164163311264 0.003974082250813846
531 -0.012419423607235735 0.012523019009929078
3091 -6.877275755389299e-06 -0.0015057765026022752
2579 -6.7710591463115e-05 -0.01491195478363956
1555 -2.271785685942927e-05 -0.004999230020159811
275 -0.0020721518724251633 0.0020894288453787145
1299 -1.0211044004464326e-05 -0.0022478907773104072
787 2.221352227901209e-05 0.004891619741338576
147 -0.0007376957335873509 0.0007438195261129486
659 6.102152864801088e-05 0.013442806163253393
403 -1.6595669374011917e-05 -0.0036557537995876204
339 -1.3072252880439053e-05 -0.0028792910205909716
211 4.723813584897413e-05 0.010402259411351835
179 -6.752950625731464e-05 -0.014869800412083179
115 8.958706708647707e-08 1.5157702179008071e-05
"""

def load_state(raw_data, N=12):
    dim = 2**N
    psi = np.zeros(dim, dtype=np.complex128)
    lines = raw_data.strip().split('\n')
    for line in lines:
        parts = line.split()
        idx = int(parts[0])
        real = float(parts[1])
        imag = float(parts[2])
        psi[idx] = real + 1j * imag
    
    norm = np.linalg.norm(psi)
    if norm < 1e-15:
        # If norm is effectively zero (should not happen with given data), treat carefully
        # Here we assume provided data has non-zero norm.
        pass
    psi /= norm
    return psi

# ==========================================
# 2. Operator Construction Helper Functions
# ==========================================

def get_pauli_matrix(pauli_char):
    if pauli_char == 'I': return np.eye(2, dtype=np.complex128)
    if pauli_char == 'X': return np.array([[0, 1], [1, 0]], dtype=np.complex128)
    if pauli_char == 'Y': return np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
    if pauli_char == 'Z': return np.array([[1, 0], [0, -1]], dtype=np.complex128)
    raise ValueError(f"Unknown Pauli: {pauli_char}")

def pauli_string_to_matrix(paulis, N):
    # paulis: string like "XYZ" for first 3 qubits
    # We need to construct the 2^N x 2^N matrix
    # For N=12, explicit dense matrices are 4096x4096. 
    # Operations like H|psi> can be done via tensor products efficiently.
    # But we also need [H, O]. 
    # Given N=12, storing operators as dense complex128 matrices (4096^2 = 16M entries)
    # 16M * 16 bytes = 256 MB per operator. 
    # We have ~350 basis operators + 2 Symmetry operators. 
    # 352 * 256 MB ~= 90 GB. Too much memory.
    # Strategy: Use sparse matrices or calculate actions/commutators directly.
    # However, constructing constraints M sym c = 0 requires [P_alpha, O_k].
    # We can compute [P_alpha, O_k] matrix elements by summing over the sparse structure.
    # P_alpha and O_k are both Pauli strings.
    # Commutator of two Pauli strings P, Q is:
    # [P, Q] = PQ - QP = (c - c*) PQ if PQ = c QP ? 
    # Pauli strings either commute (PQ = QP) or anti-commute (PQ = -QP).
    # Then [P, Q] = PQ - QP = 2 PQ (if anti-commute) or 0 (if commute).
    # Since P, Q are Hermitian, PQ is Hermitian if they commute, anti-Hermitian if anti-commute.
    # [P, Q] is anti-Hermitian (i times a Hermitian Pauli).
    # So [P_alpha, O_k] is a linear combination of Pauli strings.
    # We just need to expand this commutator in the basis of our Hamiltonian space (Distance <= 2).
    
    # First, construct a map from Pauli string (index representation) to sparse matrix?
    # No, we just need to verify commutation.
    # The constraint is [H, O] = 0.
    # This means sum_j c_j [P_j, O] = 0.
    # Let R_{j} = [P_j, O].
    # We define an inner product trace(A^\dagger B).
    # if {R_j} basis is orthogonal, we just project.
    # Pauli basis is orthogonal: tr(P_a P_b) = dim * delta_ab.
    # tr([P_a, O] P_b) = 0 for all b is the condition.
    # Since [P_a, O] expansion coefficients are simple (2 * scalar factor),
    # we can treat this directly.
    
    # Wait, [P_a, O] might generate Pauli strings of length > 2 due to O having strings of length up to N.
    # However, since our H is restricted to Distance <= 2, 
    # does the projection of [P_a, O] onto the Distance <= 2 subspace need to be zero?
    # YES. H is restricted to that subspace. 
    # [H, O] will generally live in the full algebra.
    # But the condition is [H, O] = 0 as operators. 
    # This implies every component must be zero.
    # The component of [H, O] in the Distance <= 2 subspace must be zero.
    # (The other components are automatically zero because H has no support there).
    # Actually, [H, O] = sum c_a [P_a, O].
    # P_a is dist <= 2. O is sum of strings up to length N.
    # [X_i, O_j] can span large distances.
    # So yes, we must enforce Sum c_a (coeff of [P_a, O] on basis P_gamma) = 0
    # for all basis operators P_gamma that appear in the expansion of the commutators.
    
    # This is a linear system.
    pass

def get_pauli_pairs(N=12, max_dist=2):
    # Returns list of (indices, string) for operators.
    # Indices 0-35: Single qubits.
    # Indices 36+: Two qubits.
    paulis = ['X', 'Y', 'Z']
    ops = []
    
    # 1. Single site
    for i in range(N):
        for p in paulis:
            ops.append({(i, p),}) # Set of tuples (site, pauli)
            
    # 2. Two site
    # Order from prompt: 
    # X_0 X_1, X_0 Y_1... (fixed 0,1 pair)
    # X_0 X_2...
    # X_1 X_2...
    # This ordering is standard: iterate pairs (i,j), then paulis (p_i, p_j).
    
    # Based on prompt list:
    # X_0 X_1 (dist 1)
    # ...
    # Z_0 Z_1
    # X_0 X_2 (dist 2)
    # ...
    # Z_0 Z_2
    # X_1 X_2 (dist 1)
    # ...
    # Z_1 Z_2
    # X_1 X_3 (dist 2)
    
    # Let's identify the order of pairs (i,j).
    # (0,1), (0,2), (1,2), (1,3), (2,3), (2,4), (3,4), (3,5)...
    # Pattern:
    # k=0: (0,1)
    # k=1: (0,2), (1,2)
    # k=2: (1,3), (2,3)
    # k=3: (2,4), (3,4)
    # ...
    # Wait, checking prompt list for large indices:
    # ... Z_9 Z_11
    # X_10 X_11 ...
    # The prompt list ends with Z_10 Z_11.
    # Pairs seem to follow the connectivity of a chain for k=1, k=2.
    
    # Let's reconstruct the pair list exactly as ordered in the problem.
    # Problem text:
    # X_0 X_1 ... Z_0 Z_1
    # X_0 X_2 ... Z_0 Z_2
    # X_1 X_2 ... Z_1 Z_2
    # X_1 X_3 ... Z_1 Z_3
    
    # It seems like for each site i, it connects to i+1 and i+2.
    # But the list is sorted by the first index, then second?
    # Indices of qubits: 0 to 11.
    
    # Explicit list construction based on the order observed in the prompt text snippet:
    pairs = []
    # Reading from the prompt:
    # 0,1
    # 0,2
    # 1,2
    # 1,3
    # 2,3
    # 2,4
    # ...
    # 9,11
    # 10,11
    
    for i in range(N):
        if i+1 < N: pairs.append((i, i+1))
        if i+2 < N: pairs.append((i, i+2))
        
    # Let's verify this block matches prompt snippet
    # i=0: (0,1), (0,2) -> Matches (X_0 X_1, ... X_0 X_2)
    # i=1: (1,2), (1,3) -> Matches (X_1 X_2, ... X_1 X_3)
    # i=9: (9,10), (9,11) -> Matches. (ends with X_9 X_11 ... Z_9 Z_11 block?)
    # Prompt says:
    # Z_9 Z_11
    # X_10 X_11...
    # So yes, after i=9 comes the pair (10,11).
    # My logic generates (10,11) and (10,12-no). Yes.
    
    for p1, p2 in pairs:
        for char1 in paulis:
            for char2 in paulis:
                ops.append({(p1, char1), (p2, char2)})
                
    return ops

# ==========================================
# 3. Linear System Construction
# ==========================================

def pauli_multiply(p1, p2):
    # p1, p2 are dicts/site-sets {(q, 'X'), ...}
    # result is a complex coefficient times a Pauli string (set of (q, pauli))
    # P1 * P2 = coeff * P3
    
    # Phase tracking
    # X Y = iZ, Y X = -iZ
    # Order matters. Pauli multiplication is anti-commutative for diff basis.
    # P1 * P2 = (prod factors)
    
    # We want to compute P1 * P2.
    # Simplify using map: X->1, Y->2, Z->3 (mod 4 arithmetic for X,Y,Z + I is tricky)
    # Better: Just implement logic.
    # For each qubit:
    # I*A = A
    # A*A = I
    # X*Y = iZ, X*Z = -iY
    # Y*Z = iX, Y*X = -iZ
    # Z*X = iY, Z*Y = -iX
    
    # Sparse op intersection
    sites1 = {s for s,_ in p1}
    sites2 = {s for s,_ in p2}
    all_sites = sites1.union(sites2)
    
    coeff = 1.0 + 0.0j
    result_set = {}
    
    # Handle overlap
    common = sites1.intersection(sites2)
    for s in common:
        c1 = next(c for q,c in p1 if q==s)
        c2 = next(c for q,c in p2 if q==s)
        if c1 == c2:
            # Cancel out (A*A = I)
            # I is not stored in result_set
            coeff *= 1.0
        else:
            # Compute product
            # Map to integers: X=1, Y=2, Z=3
            # 1*2 = i3, 1*3 = -i2, 2*3 = i1
            # Anti-symmetry: swap changes sign
            lookup = {
                frozenset(('X','Y')): ('Z', 1j), # X*Y = iZ
                frozenset(('Y','X')): ('Z', -1j),# Y*X = -iZ
                frozenset(('X','Z')): ('Y', -1j),# X*Z = -iY
                frozenset(('Z','X')): ('Y', 1j), # Z*X = iY
                frozenset(('Y','Z')): ('X', 1j), # Y*Z = iX
                frozenset(('Z','Y')): ('X', -1j) # Z*Y = -iX
            }
            char, phase = lookup[frozenset((c1, c2))]
            coeff *= phase
            result_set[s] = char
            
    # Handle exclusive sites
    for s in sites1 - sites2:
        c = next(c for q,c in p1 if q==s)
        result_set[s] = c
    for s in sites2 - sites1:
        c = next(c for q,c in p2 if q==s)
        result_set[s] = c
        
    # Sort for consistent representation
    sorted_tuple = tuple(sorted(result_set.items()))
    return coeff, sorted_tuple

def construct_constraints(N, basis_ops, O1_parts, O2_parts):
    # We need to build matrix M such that M c = 0
    # Constraints:
    # 1. [H, O1] proj = 0
    # 2. [H, O2] proj = 0
    # 3. (I - psi psi^T) H psi = 0 (Eigenstate condition)
    
    # 1 & 2: Commutation
    # [P_a, O_k] = P_a O_k - O_k P_a
    # We compute this linear combination.
    # O_k is a sum of Paulis. O = sum w_j Q_j.
    # [P_a, O] = sum w_j [P_a, Q_j]
    
    # We only care if the result has support on the basis_ops (H-support).
    # Actually, prompt says H is linear combination of basis_ops.
    # [H, O] must be zero.
    # If [P_a, Q_j] has components only outside basis_ops, it doesn't constrain coeff for P_a 
    # because H cannot generate that component to cancel it?
    # NO. H is restricted. The equation is sum c_a [P_a, O] = 0.
    # If [P_a, O] has a component "r" that is NOT in the span of {[P_b, O]} for b!=a?
    # Effectively, we just look at the expansion of [P_a, O] in the full Pauli basis.
    # Since the result must be 0, and the Pauli basis is orthogonal, 
    # the coefficient for every Pauli string R in the expansion must be 0.
    # So for each R appearing in any [P_a, O], we have an equation.
    
    # Optimization: We only need the projection of the constraint onto the orthogonal complement
    # of the subspace spanned by [P_a, O] terms that can't be cancelled? 
    # No, we simply set the linear system Sum c_a [P_a, O] = 0.
    # This is a matrix equation.
    
    # Let's define a function to compute commutation contributions.
    # This is computationally heavy.
    # O1 has 2*N terms. A_r, B_r.
    # A_r is string of Z up to r-1 then X.
    # So length r.
    # O1 has terms up to length N.
    
    # Let's calculate constraints using a dictionary mapping PauliString -> EquationIndex
    
    equations = {} # key: pauli_string_tuple, val: list of (coeff, op_index)
    
    basis_map = {i: op for i, op in enumerate(basis_ops)}
    # basis_ops: list of sets. e.g. {(0, 'X')} or {(0, 'X'), (1, 'Y')}
    # We need a way to hash these. Sorted tuple is good.
    
    # Pre-compute O1 and O2 as dictionary of PauliString -> Weight
    def build_O(N):
        O1 = {}
        O2 = {}
        for r in range(N):
            # A_r
            # Z_0 ... Z_{r-1} X_r
            sA = {}
            for k in range(r): sA[k] = 'Z'
            sA[r] = 'X'
            kA = tuple(sorted(sA.items()))
            
            w1_A = np.exp(-r)
            w2_A = np.exp(-(N-1-r))
            
            if kA in O1: O1[kA] += w1_A
            else: O1[kA] = w1_A
            
            if kA in O2: O2[kA] += w2_A
            else: O2[kA] = w2_A
            
            # B_r
            sB = {}
            for k in range(r): sB[k] = 'Z'
            sB[r] = 'Y'
            kB = tuple(sorted(sB.items()))
            
            w1_B = -np.exp(-r)
            w2_B = np.exp(-(N-1-r))
            
            if kB in O1: O1[kB] += w1_B
            else: O1[kB] = w1_B
            
            if kB in O2: O2[kB] += w2_B
            else: O2[kB] = w2_B
            
        return O1, O2

    O1_mat, O2_mat = build_O(N)
    
    # Constraint generation function
    def add_comm_constraints(O_dict, eq_dict):
        # For each P_alpha in basis
        for alpha_idx, P_alpha_tuple in basis_map.items():
            P_alpha = dict(P_alpha_tuple)
            
            # For each Q_term in O
            for Q_tuple, w_Q in O_dict.items():
                Q_op = dict(Q_tuple)
                
                # Compute [P, Q] = PQ - QP
                # 1. P Q
                coeff1, res1 = pauli_multiply(dict(P_alpha), Q_op)
                coeff1 *= w_Q
                
                # 2. Q P
                coeff2, res2 = pauli_multiply(Q_op, dict(P_alpha))
                coeff2 *= w_Q
                
                # Combine
                # [P,Q] = P Q - Q P
                # Add to equation for 'res1'
                if res1 in eq_dict: eq_dict[res1].append((coeff1, alpha_idx))
                else: eq_dict[res1] = [(coeff1, alpha_idx)]
                
                # Subtract for 'res2'
                if res2 in eq_dict: eq_dict[res2].append((-coeff2, alpha_idx))
                else: eq_dict[res2] = [(-coeff2, alpha_idx)]

    print("Constructing Commutation Constraints...")
    add_comm_constraints(O1_mat, equations)
    add_comm_constraints(O2_mat, equations)
    
    # Convert equations dict to list of (matrix_row, RHS)
    # RHS is 0.
    # Filter: if an equation has no terms (shouldn't), skip.
    # Also, if the equation result string is empty (Identity), it implies trace zero.
    # Since Paulis are traceless except identity, and H is traceless? 
    # H is sum of Paulis, so tr(H)=0. [H,O] is traceless? Yes.
    # Identity term in commutator must be 0.
    # pauli_multiply returns empty tuple for identity.
    
    M_rows = []
    # We only keep equations that cannot be automatically satisfied.
    # Since H is span{basis_ops}, if a specific Pauli string R appears in the expansion
    # of some [P, O], and that R is NOT in the span of all other commutators,
    # we have a constraint.
    # Effectively, we treat every R found as a constraint equation.
    # Since the coefficients of H are the variables, and the constraint is linear:
    # Sum coeff_i * c_i = 0.
    
    # Note: [P, O] yields complex coeff?
    # Pauli multiply yields complex phases (i, -i).
    # H must be Hermitian. c_i real.
    # Equation: Sum (Real + i Img) c_i = 0.
    # This implies Sum Real(c_i) = 0 AND Sum Img(c_i) = 0.
    
    final_equations = []
    
    for p_string, terms in equations.items():
        # terms is list of (coeff, alpha_idx)
        # coeff is complex
        # Build real equation parts
        real_parts = [(t[0].real, t[1]) for t in terms if abs(t[0].real) > 1e-15]
        imag_parts = [(t[0].imag, t[1]) for t in terms if abs(t[0].imag) > 1e-15]
        
        if real_parts:
            final_equations.append(real_parts)
        if imag_parts:
            final_equations.append(imag_parts)
            
    print(f"Generated {len(final_equations)} commutation equations.")
    return final_equations

def construct_eigen_constraints(psi, basis_ops, basis_map):
    # (I - |psi><psi|) H |psi> = 0
    # Let v = H |psi>. v - psi (psi^* v) = 0
    # v - psi * E = 0 for some E.
    # Project v onto orthogonal complement of psi.
    # v . psi_perp = 0.
    
    dim = len(psi)
    # Gram-Schmidt orthonormal basis for subspace orthogonal to psi?
    # Too big.
    # We can use the fact that the solution space is low dimensional if we find nullspace of M_sym first?
    # Iterative approach:
    # 1. Construct M_sym.
    # 2. Find nullspace vectors V. dim(V) = d. c = V x.
    # 3. Project Eigenstate constraint onto this subspace.
    # (I - psi psidag) (sum V_k alpha_k) psi = 0.
    # Let W_k = P V_k psi. where P = I - psi psidag.
    # We need sum alpha_k W_k = 0.
    # This is a linear system for alpha_k.
    
    # So we need to apply each basis operator P_alpha to |psi>.
    # P_alpha |psi> = vector.
    
    # N=12, dim=4096. 
    # Sparse multiplication for Pauli strings is very fast.
    
    print("Computing P_alpha |psi> for basis operators...")
    
    # Precompute P_alpha acting on psi
    # basis_ops size ~ 350.
    # Storing 350 vectors of size 4096 is 
    # 350 * 4096 * 16 bytes ~= 22 MB. Manageable.
    
    results = []
    
    # Optimized Pauli action
    # Z|0>=|0>, Z|1>=-|1> -> flips sign of 1s in index.
    # X|0>=|1>, X|1>=|0> -> swaps index i with i ^ (1<<k).
    # Y|0>=i|1>, Y|1>=-i|0> -> X then Z phase.
    
    op_vectors = []
    
    for op in basis_ops:
        # op is a set of (site, pauli)
        # Initialize as copy of psi
        res = np.zeros(dim, dtype=np.complex128)
        
        # We handle X, Y, Z.
        # X and Y involve permutations. Z involves phases.
        # Do permutation first (X/Y basis), then apply Z phases.
        
        # Actually, for each op:
        # 1. Calculate phase map for Zs.
        # 2. Apply X/Y permutation.
        
        # Efficient loop:
        # Iterate over indices where psi is non-zero?
        # Psi is sparse? The table implies many zeros, but not extremely sparse.
        # Given structured data, likely Psi is dense-ish or has specific pattern.
        # For N=12, dense iteration is fast (4096 ops).
        
        # Let's perform the loop over all indices 0..2^N-1
        # To speed up, use numpy array operations if possible.
        # But Pauli strings are specific bitwise manipulations.
        
        # Decompose op into X, Y, Z sets on sites.
        X_sites = []
        Y_sites = []
        Z_sites = []
        for s, p in op:
            if p == 'X': X_sites.append(s)
            elif p == 'Y': Y_sites.append(s)
            elif p == 'Z': Z_sites.append(s)
            
        # Permutation indices
        # X and Y flip bits.
        mask = 0
        for s in X_sites: mask |= 1 << s
        for s in Y_sites: mask |= 1 << s
        
        # Target indices are i ^ mask
        # We construct the vector res.
        # res[i ^ mask] = psi[i] * phase
        
        # Phase:
        # Z on site s: factor +1 if bit_s(i)=0, -1 if bit_s(i)=1.
        # Y involves additional i factor.
        # Total factor = (prod over Ys i) * (prod over Zs (-1)^bit_s)
        # Note: bit_s(i) in source index i? 
        # Yes, Z acts on the basis state |i>.
        # When we map |i> to |j> where j = i ^ mask, the bits flipped are X/Y sites.
        # The Z phase is applied to the source |i>.
        # Check Y: Y|0> = i|1>. Y|1> = -i|0>.
        # bit 0 -> i. bit 1 -> -i.
        # This is i * (-1)^bit.
        # So Y contributes factor i * (-1)^bit_s(i).
        
        # Total phase for source vector index i:
        # coeff = (i)^{nY} * prod_{s in Z} (-1)^bit_s(i) * prod_{s in Y} (-1)^bit_s(i)
        # = (i)^{nY} * prod_{s in Zs+Ys} (-1)^bit_s(i)
        
        nY = len(Y_sites)
        z_iter_sites = Z_sites + Y_sites
        
        # Vectorized calculation
        all_indices = np.arange(dim)
        target_indices = all_indices ^ mask
        
        # Calculate Z phase factor
        # prod (-1)^bit = (-1)^{sum(bits)}
        # sum bits for z_iter_sites
        z_mask = 0
        for s in z_iter_sites:
            z_mask |= 1 << s
        
        # Count bits
        # We need bit count for z_mask & i.
        # bincount is slow?
        # popcount using bitwise ops is hard in numpy without ufunc.
        # parity is (-1)^{count of 1s}.
        # We can check this iteratively or use lookup table for small N?
        # N=12 is small.
        # Create an array of phases.
        
        # Precompute phase map for Z operations
        # Can be done by iterating 0..dim-1
        
        # Given N=12, explicit python loop over 4096 is fast enough (<0.1s)
        # Doing this 350 times is ~35s. A bit slow.
        # Let's optimize.
        # The loop over i:
        # idx = i ^ mask
        # phase = (1j)^nY
        # for s in z_sites: if (i>>s)&1: phase *= -1
        
        phases = np.ones(dim, dtype=np.complex128)
        if nY % 4 == 1: phases[:] *= 1j
        elif nY % 4 == 2: phases[:] *= -1
        elif nY % 4 == 3: phases[:] *= -1j
        
        for s in z_iter_sites:
            # Vectorized parity for bit s
            # Parity is 1 if bit is 1, else -1?
            # (-1)^bit. 0 -> 1, 1 -> -1.
            # bit 0 -> 1. bit 1 -> -1.
            # Vector: 1 - 2*( (indices>>s) & 1 )
            mask_s = 1 << s
            bits = (all_indices >> s) & 1
            phases *= (1.0 - 2.0 * bits)
            
        # Apply to psi
        # res[target_indices] = psi[source_indices] * phases
        res[target_indices] = psi * phases
        
        op_vectors.append(res)
        
    return op_vectors

# ==========================================
# 4. Solver
# ==========================================

def solve_hamiltonian(N, psi):
    # 1. Basis
    basis_ops = get_pauli_pairs(N, max_dist=2)
    basis_map = {i: tuple(sorted(op)) for i, op in enumerate(basis_ops)}
    num_coeffs = len(basis_ops)
    print(f"Basis size: {num_coeffs}")
    
    # Find index of Y_0 Y_1 for normalization
    target_op_tuple = tuple(sorted({(0, 'Y'), (1, 'Y')}))
    target_idx = -1
    for i, op in enumerate(basis_ops):
        if tuple(sorted(op)) == target_op_tuple:
            target_idx = i
            break
    if target_idx == -1:
        raise ValueError("Y_0 Y_1 not in basis??")
        
    # 2. Symmetry Constraints Matrix
    # M_sym is a list of sparse rows? Or dense?
    # M_sym c = 0
    # Construct dense M_sym using variable count
    # 350 variables. Equations maybe a few hundred.
    comm_eqs = construct_comm_constraints(N, basis_ops, None, None)
    
    # Convert comm_eqs to dense matrix
    M_sym = np.zeros((len(comm_eqs), num_coeffs), dtype=np.float64)
    for r, row_terms in enumerate(comm_eqs):
        for coeff, idx in row_terms:
            M_sym[r, idx] = coeff
            
    print(f"Symmetry constraint matrix shape: {M_sym.shape}")
    
    # SVD to find nullspace of M_sym
    # We want (A - S) c = 0, but here just M c = 0.
    # Compute SVD of M_sym
    # U, s, Vh = linalg.svd(M_sym)
    # Nullspace vectors are columns of V corresponding to s < epsilon.
    
    # Check tolerance for "zero" singular values
    Weights, singulars, Vt = scipy.linalg.svd(M_sym)
    rank = np.sum(singulars > 1e-10)
    null_dim = num_coeffs - rank
    print(f"Symmetry Rank: {rank}, Nullspace dim: {null_dim}")
    
    if null_dim == 0:
        print("Warning: No nullspace found. Relaxing tolerance.")
        # If strict, maybe no solution exists exactly.
        # For now, assume solution exists.
        # Let's look for smallest singular value
        min_s = singulars[-1]
        print(f"Min singular value: {min_s}")
        # Might need to solve least squares if no exact nullspace
        
    # Construct projector or basis for nullspace
    V_null = Vt.T[:, rank:] # Columns are basis for nullspace
    
    # 3. Eigenstate Constraint
    # Constrain c in Null(M_sym) such that (I - psi psi^T) H psi = 0
    # c = V_null * x
    
    # Compute W = P_op_vectors projected onto orthogonal complement
    op_vectors = construct_eigen_constraints(psi, basis_ops, basis_map)
    
    # Project vectors op_vectors onto Ortho(psi)
    # P = I - psi psi^\dagger
    psi_col = psi.reshape(-1, 1)
    P_ortho = np.eye(len(psi), dtype=np.complex128) - psi_col @ psi_col.conj().T
    
    # Stack op_vectors as columns
    A_dense = np.column_stack(op_vectors) # dim x num_coeffs
    
    # Projected action
    A_proj = P_ortho @ A_dense
    
    # Reduce A_proj to nullspace
    # We need (A_proj @ c) = 0
    # (A_proj @ V_null) x = 0
    A_reduced = A_proj @ V_null
    
    # We need nullspace of A_reduced
    # A_reduced dim is 4096 x null_dim.
    # We can solve via SVD again or LSQR.
    Ua, sa, Vha = scipy.linalg.svd(A_reduced)
    
    # The nullspace of A_reduced is the set of x s.t. variance is 0.
    # Ideally we expect a 1D solution.
    # Check singular values
    print(f"Singular values of A_reduced (Last 5): {sa[-5:]}")
    
    rank_A = np.sum(sa > 1e-8)
    null_dim_A = null_dim - rank_A
    print(f"Reduced Rank: {rank_A}, Nullspace dim: {null_dim_A}")
    
    if null_dim_A < 1:
        print("Error: No solution satisfying eigenstate condition in nullspace.")
        return None
        
    # Solution vector x is the nullspace of A_reduced
    x = Vha.T[:, rank_A]
    
    # If multiple solutions, we need to check Y_0 Y_1 scaling.
    # We expect a unique solution.
    # c = V_null @ x
    
    # 4. Normalization
    # We want c[target_idx] = 1
    # If null space is 1D, x is a vector.
    # c_raw = V_null @ x[:, 0]
    # scale = 1.0 / c_raw[target_idx]
    # c = c_raw * scale
    
    # If null space > 1D (unlikely), we minimize something or pick any? 
    # Problem implies unique.
    
    # Handle potential array vs scalar shape
    if x.ndim == 1:
        c_raw = V_null @ x
    else:
        # Take the first nullspace vector if multiple
        c_raw = V_null @ x[:, 0]
        
    scale = 1.0 / c_raw[target_idx]
    c = c_raw * scale
    
    return c, basis_ops

# ==========================================
# 5. Verification
# ==========================================

def verify_solution(c, basis_ops, N, psi):
    # 1. Reconstruct H (sparse?)
    # 2. Check Commutations
    # 3. Check Eigenstate
    # 4. Check Norm
    
    print("\n--- Verification ---")
    
    # 1. Y_0 Y_1 coeff
    target_op = tuple(sorted({(0, 'Y'), (1, 'Y')}))
    t_idx = -1
    for i, op in enumerate(basis_ops):
        if tuple(sorted(op)) == target_op:
            t_idx = i
            break
    print(f"Y_0 Y_1 Coeff: {c[t_idx]}")
    
    # 2. Eigenstate residual
    # Compute H|psi> efficiently using the precomputed vectors in previous step?
    # We can recompute. N=12 is small.
    
    op_vectors = []
    for op in basis_ops:
        # ... (same loop as construct_eigen_constraints) ...
        # To avoid code duplication, we assume `op_vectors` are available or recompute.
        # Let's just use the slow way for verification (cleaner code)
         X_sites = []
        Y_sites = []
        Z_sites = []
        for s, p in op:
            if p == 'X': X_sites.append(s)
            elif p == 'Y': Y_sites.append(s)
            elif p == 'Z': Z_sites.append(s)
        
        all_indices = np.arange(2**N)
        mask = 0
        for s in X_sites: mask |= 1 << s
        for s in Y_sites: mask |= 1 << s
        target_indices = all_indices ^ mask
        
        phases = np.ones(2**N, dtype=np.complex128)
        nY = len(Y_sites)
        if nY % 4 == 1: phases[:] *= 1j
        elif nY % 4 == 2: phases[:] *= -1
        elif nY % 4 == 3: phases[:] *= -1j
        
        z_iter_sites = Z_sites + Y_sites
        for s in z_iter_sites:
            bits = (all_indices >> s) & 1
            phases *= (1.0 - 2.0 * bits)
            
        res = np.zeros(2**N, dtype=np.complex128)
        res[target_indices] = psi * phases
        op_vectors.append(res)

    H_psi = np.zeros(2**N, dtype=np.complex128)
    for i, vec in enumerate(op_vectors):
        H_psi += c[i] * vec
        
    # Eigenvalue
    # Energy = <psi|H|psi>
    E = np.vdot(psi, H_psi)
    print(f"Energy E: {E}")
    
    # Norm of (H - E)|psi>
    # Should be close to 0
    residual = H_psi - E * psi
    r_norm = np.linalg.norm(residual)
    print(f"Eigenstate Residual Norm: {r_norm}")
    
    # 3. Commutator Norm
    # Compute [H, O1] and [H, O2] Frobenius norm squared / dim
    # Or just max element?
    # Prompt要求: ||[H,O]||_F^2/tr(I) < 1e-10.
    # tr(I) = 2^N.
    # ||A||_F^2 = sum |a_ij|^2.
    # This is hard for N=12 explicitly (4096x4096 matrix).
    # But Pauli basis expansion is easy.
    # [H, O] is a sum of Paulis.
    # Let [H, O] = sum_k d_k P_k.
    # Since P_k are orthogonal with trace = 2^N (if k!=Id) or 2^{N+1} (if Id)?
    # Trace(P_a P_b) = dim * delta_ab.
    # So || sum d_a P_a ||_F^2 = sum |d_a|^2 * ||P_a||_F^2.
    # ||P_a||_F^2 = Tr(P_a^2) = Tr(I) = 2^N.
    # So we just need the coefficients of the expansion of [H, O] in the Pauli basis.
    
    # We need to construct [H, O1] expansion coefficients.
    # H = sum c_a P_a.
    # [P_a, O] is what we calculated in `construct_comm_constraints`.
    # `comm_eqs` gave us lists of linear combinations summing to 0.
    # But here we want the vector IN the Pauli basis to check its weight.
    
    # Re-calculate [H, O] expansion efficiently.
    # O = sum w_j Q_j.
    # [H, O] = sum_a c_a [P_a, O].
    
    # Map PauliString -> Coefficient
    comm_coeff_map = {}
    
    def add_op_contrib(coeff, op_tuple):
        if op_tuple in comm_coeff_map:
            comm_coeff_map[op_tuple] += coeff
        else:
            comm_coeff_map[op_tuple] = coeff
            
    # O1, O2 defined previously
    O1_mat, O2_mat = construct_constraints.__wrapped__.O1_mat, construct_constraints.__wrapped__.O2_mat
    # Wait, O1_mat is local to that function. 
    # Let's just redefine the calculation or make it global?
    # Since it's a script, I'll redefine O1, O2 briefly or assume access.
    # For this script, I will put O construction inside main.
    pass 

# Main Execution
if __name__ == "__main__":
    N = 12
    psi = load_state(raw_data, N)
    
    # Solve
    coeffs, basis = solve_hamiltonian(N, psi)
    
    if coeffs is not None:
        print("\n--- Solution Found ---")
        # Output formatting
        # The prompt asks for the vector of coefficients.
        # We just print them clearly.
        
        # Verification requires O1, O2 access.
        # I will replicate O construction here.
        def build_O_local(N):
            O1 = {}
            O2 = {}
            for r in range(N):
                sA = {}
                for k in range(r): sA[k] = 'Z'
                sA[r] = 'X'
                kA = tuple(sorted(sA.items()))
                O1[kA] = O1.get(kA, 0) + np.exp(-r)
                O2[kA] = O2.get(kA, 0) + np.exp(-(N-1-r))
                
                sB = {}
                for k in range(r): sB[k] = 'Z'
                sB[r] = 'Y'
                kB = tuple(sorted(sB.items()))
                O1[kB] = O1.get(kB, 0) - np.exp(-r)
                O2[kB] = O2.get(kB, 0) + np.exp(-(N-1-r))
            return O1, O2
        
        O1, O2 = build_O_local(N)
        
        # Expand [H, O]
        def get_commutator_norm_sq(O_ops):
            # O_ops: dict {op_tuple: weight}
            # Iterate over non-zero coeffs in solution
            # sparse coeffs
            non_zero_indices = np.where(np.abs(coeffs) > 1e-12)[0]
            
            expansion = {}
            
            for a_idx in non_zero_indices:
                ca = coeffs[a_idx]
                P_a = dict(basis[a_idx])
                
                for Q_tuple, wQ in O_ops.items():
                    Q = dict(Q_tuple)
                    
                    # P_a Q
                    c1, r1 = pauli_multiply(P_a, Q)
                    add_op_contrib(ca * wQ * c1, r1)
                    
                    # Q P_a
                    c2, r2 = pauli_multiply(Q, P_a)
                    add_op_contrib(ca * wQ * (-c2), r2)
                    
            # Calculate norm
            norm_sq = 0
            for key, val in expansion.items():
                if abs(val) > 1e-14:
                    norm_sq += abs(val)**2 # since |P|=sqrt(dim)
            
            return norm_sq / (2**N)

        n1 = get_commutator_norm_sq(O1)
        n2 = get_commutator_norm_sq(O2)
        
        print(f"||[H, O1]||_F^2/tr(I): {n1}")
        print(f"||[H, O2]||_F^2/tr(I): {n2}")
        
        print("\n--- Hamiltonian Coefficients ---")
        # Print in the requested format/order
        # order is `basis` list order (X0, Y0, Z0, ...)
        # We can print white-space separated or tab separated.
        for val in coeffs:
            print(val)

```