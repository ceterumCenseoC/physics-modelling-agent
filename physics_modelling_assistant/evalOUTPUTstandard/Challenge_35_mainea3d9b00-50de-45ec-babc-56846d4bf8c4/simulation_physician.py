
```python
import numpy as np
from scipy import linalg

# --- 1. Define Constants and Grid ---
N = 12  # Number of qubits
DTYPES = np.complex128

# Included indices based on the user problem description (columns 1 and 2)
# Indices are 0-based.
included_indices = [0, 1]

# Dimensions
dim = 2**N
num_included = len(included_indices)

# --- 2. Define Pauli Matrices ---
sigma_x = np.array([[0, 1], [1, 0]], dtype=DTYPES)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=DTYPES)
sigma_z = np.array([[1, 0], [0, -1]], dtype=DTYPES)
identity = np.eye(2, dtype=DTYPES)

paulis = {'I': identity, 'X': sigma_x, 'Y': sigma_y, 'Z': sigma_z}

def get_pauli_string(indices, chars):
    """
    Constructs the Kronecker product of Pauli matrices.
    indices: list of site indices (0 to N-1) where the operator acts non-trivially
    chars: list of 'X', 'Y', or 'Z' corresponding to the indices
    """
    if len(indices) != len(chars):
        raise ValueError("Indices and chars must have same length")
    
    ops = [paulis['I']] * N
    for i, char in zip(indices, chars):
        if not (0 <= i < N):
             raise ValueError(f"Index {i} out of bounds for N={N}")
        ops[i] = paulis[char]
    
    mat = ops[0]
    for op in ops[1:]:
        mat = np.kron(mat, op)
    return mat

# --- 3. Define State |psi> ---
# Use the exact amplitudes provided in the table.
# Map integer (row) -> complex amplitude
psi_data_raw = """
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

psi_vec = np.zeros(dim, dtype=DTYPES)
lines = psi_data_raw.strip().split('\n')
for line in lines:
    parts = line.split()
    if len(parts) != 3: continue
    b = int(parts[0])
    re = float(parts[1])
    im = float(parts[2])
    psi_vec[b] = re + 1j * im

# Normalize the vector to match typical quantum states, though data points might not cover full space
# The provided data is highly precise, so we trust the values.
# However, for numerical stability in solving for H, we might need to be careful about the singular values.
# Let's assume psi_vec is as given.

# --- 4. Define Symmetry Operators O1 and O2 ---
# O1 = sum_r e^{-r} (A_r - B_r)
# O2 = sum_r e^{-(N-1-r)} (A_r + B_r)
# A_r = (prod Z) X_r, B_r = (prod Z) Y_r

# To compute commutators [P_k, O_j], we don't strictly need the full matrix forms of O1, O2
# if we know how P_k interacts with A_r, B_r.
# However, constructing O1, O2 is easier to verify and compute.
# Size N=12 is small enough for dense matrix manipulation (4096x4096).
# Memory: 4096*4096*16 bytes ~ 268 MB. Acceptable for modern RAM.

def get_A_r(r):
    # A_r
    indices = list(range(r))
    chars = ['Z'] * r + ['X']
    return get_pauli_string(indices, chars)

def get_B_r(r):
    # B_r
    indices = list(range(r))
    chars = ['Z'] * r + ['Y']
    return get_pauli_string(indices, chars)

O1_mat = np.zeros((dim, dim), dtype=DTYPES)
O2_mat = np.zeros((dim, dim), dtype=DTYPES)

# Precompute scalars
exp_decay = {r: np.exp(-r) for r in range(N)}
exp_decay_r2 = {r: np.exp(-(N-1-r)) for r in range(N)}

# Construct O1, O2
for r in range(N):
    A = get_A_r(r)
    B = get_B_r(r)
    O1_mat += exp_decay[r] * (A - B)
    O2_mat += exp_decay_r2[r] * (A + B)

# --- 5. Construct Basis Operators ---
# We need to generate the basis P_k.
# The list is explicitly given in the prompt. We will parse it.
# 1- site: X_i, Y_i, Z_i.
# 2- site (d=1): P_i P_{i+1}
# 2- site (d=2): P_i P_{i+2}

# Let's hardcode the generation logic to match the prompt's list order.
basis = []
# One-site ops
for i in range(N):
    basis.append(('X', [i]))
    basis.append(('Y', [i]))
    basis.append(('Z', [i]))

# Two-site ops dist 1
for i in range(N-1):
    for p1 in ['X', 'Y', 'Z']:
        for p2 in ['X', 'Y', 'Z']:
             # Prompt order: X_0 X_1, X_0 Y_1, X_0 Z_1, Y_0 X_1, Y_0 Y_1...
             # Outer loop p1, inner loop p2
             basis.append((p1+p2, [i, i+1]))

# Two-site ops dist 2
for i in range(N-2):
    for p1 in ['X', 'Y', 'Z']:
        for p2 in ['X', 'Y', 'Z']:
             basis.append((p1+p2, [i, i+2]))

# Convert basis list to matrix forms
basis_ops = [get_pauli_string(indices, list(label)) for label, indices in basis]
num_ops = len(basis_ops) # Should be 225
print(f"Number of basis operators: {num_ops}")

# --- 6. Linear System Setup ---
# Constraints:
# 1. [H, O1] = 0  -> sum_k c_k [P_k, O1] = 0
# 2. [H, O2] = 0  -> sum_k c_k [P_k, O2] = 0
# 3. H|psi> = E|psi> -> sum_k c_k P_k |psi> = E |psi>
# 4. c_Y0Y1 = 1 (Index 40 based on counting)

# We need to flatten these matrix equations into vector equations.
# Dimension of Hilbert space is dim = 4096.
# Each matrix eq [P_k, O_j] is a dim x dim matrix.
# We can vectorize it. vec([P, O]) = (I kron P - P^T kron I) vec(O).
# But here we are constructing the linear system for c_k.
# So we look at coefficient of c_k.
# sum_k c_k * Q_k = 0, where Q_k = [P_k, O_j].
# This implies each element of Q_k must sum to 0.
# That's dim^2 equations per operator. Too many to solve directly if we want to solve for 225 vars?
# Actually we can flatten Q_k to a vector of length dim^2.
# So we have 2 * dim^2 equations from symmetry.
# And dim equations from eigenstate.
# Total unknowns: 226 (225 c_k + E).

# Let's build the matrix A and vector b for A x = b
# Unknowns x = [c_0, ..., c_224, E]
# Note: c_40 is fixed to 1. We can substitute it or add a constraint row.
# Let's add a constraint row to be explicit. Or better, construct the system for all vars
# and the last row is c_40 = 1.

A_rows = []
b_rows = []

# --- Symmetry Constraints ---
# Helper to commutator and flatten
def get_commutator_vec(P, O):
    # returns vec(P @ O - O @ P)
    comm = P @ O - O @ P
    return comm.flatten()

# Optimize: Since P_k are sparse Pauli strings and O_j are dense sums,
# we can reduce the dimensionality effectively.
# The system is overdetermined. We can solve least squares.
# Dimension 4096^2 is 16 million. That's large but manageable for a sparse solver? 
# The matrices P_k are very sparse (16 ones/zeros out of 4096).
# The result [P_k, O] will be sparse?
# O is dense sum of many strings. [P, Q] for Paulis P, Q is number preserving if they commute, or i*Pauli if they anticommute.
# Actually, O is a sum of MANY Pauli terms.
# So [P_k, O_j] will be dense.
# This makes the 16M equations approach too heavy for simple matrix operations in memory (16M x 225 floats = 14GB).

# Alternative approach:
# We only need coefficients c_k such that sum c_k [P_k, O] = 0.
# This is a linear subspace constraint. We can find nullspace of the map c -> [H, O].
# We can sample the constraint? No, we need strict 10^-10 accuracy.
# We can recursively build the operators? No.

# Better approach:
# Instead of flatt to dim^2, we verify commutation using the basis of Pauli strings.
# Any 2^N x 2^N matrix can be written as sum of Pauli strings.
# We have 225 P_k.
# O1 and O2 are defined.
# [P_k, O_j] can be expressed in the full Pauli basis (size 4^N).
# We only work with the subspace spanned by [P_k, O_j].
# Let's compute the commutator and express it in the full Pauli basis.
# But 4^12 = 16 million terms.
# However, O1, O2 are sums of 12*2 = 24 terms each.
# P_k are single or double Pauli strings.
# Commutator of Pauli strings is proportional to a Pauli string.
# [Pa, Pb] is 0 or 2i * Pa*Pb (normalized).
# So [P_k, O_j] is a sum of at most (number of terms in O_j) Pauli strings.
# O_j has 24 terms.
# So [P_k, O_j] has max 24 * 4 = 96 non-zero terms in the 4^N expansion.
# This is sparse!
# The constraint sum c_k [P_k, O_j] = 0 means that for every Pauli string S in the support of {[P_k, O_j]},
# the sum of coefficients must be 0.
# This drastically reduces the number of equations from 16M to a few hundred.

def pauli_to_int(pauli_string_tuple):
    # Map a tuple of characters ('X','Y','Z','I') to an index for lookup
    # Actually, for commutator logic, we can just use the tuples as keys in a dictionary.
    pass

def multiply_paulis(p1, idxs1, p2, idxs2):
    # p1, p2 are lists of chars like ['X', 'Y']
    # idxs1, idxs2 are lists of positions
    # Result is a (coeff, PauliString)
    # Product of Paulis.
    
    # Merge maps
    res_map = {}
    for char, idx in zip(p1, idxs1):
        if idx in res_map:
            res_map[idx] = multiply_single(res_map[idx], char)
        else:
            res_map[idx] = char
            
    for char, idx in zip(p2, idxs2):
        if idx in res_map:
            res_map[idx] = multiply_single(res_map[idx], char)
        else:
            res_map[idx] = char
            
    # Filter out Identities and calc coeff
    final_str = []
    coeff = 1.0
    for k in sorted(res_map.keys()):
        c = res_map[k]
        if c == 'I':
            continue
        final_str.append((k, c))
        
    return coeff, final_str

def multiply_single(c1, c2):
    if c1 == 'I': return c2
    if c2 == 'I': return c1
    if c1 == c2: return 'I'
    # Check cyclic order X -> Y -> Z -> X
    if {c1, c2} == {'X', 'Y'}: return 'Z'
    if {c1, c2} == {'Y', 'Z'}: return 'X'
    if {c1, c2} == {'Z', 'X'}: return 'Y'
    return None # Should not happen

# Re-define basis in Pauli String format for sparse algebra
# basis is already a list of tuples (label_string, indices_list)
# Let's construct the commutator constraints using this algebra.

rules = {
    frozenset(['X','Y']): (1j, 'Z'), # X Y = i Z -> XY - YX = 2i Z -> [X,Y] = 2iZ. 
                         # Standard P_a P_b = delta_ab I + i e_abc P_c
                         # [X, Y] = 2i Z
    frozenset(['Y','Z']): (1j, 'X'),
    frozenset(['Z','X']): (1j, 'Y'),
}

def get_pauli_product_term(char1, char2):
    if char1 == char2: return 1.0, 'I' # X^2 = I
    if char1 == 'I': return 1.0, char2
    if char2 == 'I': return 1.0, char1
    # c1 != c2 and neither is I
    # XY = iZ
    # YX = -iZ
    # This function returns coeff * P such that char1 * char2 = coeff * result
    # result is char3
    s = frozenset([char1, char2])
    pref, res_char = rules[s]
    # Check determinant of permutation
    if (char1, char2) in [('X','Y'), ('Y','Z'), ('Z','X')]:
         return pref, res_char
    else:
         return -pref, res_char

def get_comm_support(P_idxs, P_chars, O_idx, O_char, coeff_O):
    # Returns list of (PauliString, coeff) representing [P, O_term]
    # P * O - O * P
    # P = P1 P2 ... Pk
    # O_term = coeff_O * Q1 Q2 ... Ql
    # Result is linear combination of Pauli strings
    
    # Compute P * O
    # Merge sites
    current_sites = {}
    for i, c in zip(P_idxs, P_chars): current_sites[i] = c
    for i, c in zip(O_idx, O_char): current_sites[i] = get_pauli_product_term(current_sites.get(i, 'I'), c)
    
    # Extract coeff and string for P*O
    p1_coeff = 1.0
    p1_str = []
    for i in sorted(current_sites.keys()):
        c_coeff, c_char = current_sites[i]
        p1_coeff *= c_coeff
        if c_char != 'I':
            p1_str.append((i, c_char))
            
    # Compute O * P
    current_sites_op = {}
    for i, c in zip(O_idx, O_char): current_sites_op[i] = c
    for i, c in zip(P_idxs, P_chars): current_sites_op[i] = get_pauli_product_term(current_sites_op.get(i, 'I'), c)
        
    p2_coeff = 1.0
    p2_str = []
    for i in sorted(current_sites_op.keys()):
        c_coeff, c_char = current_sites_op[i]
        p2_coeff *= c_coeff
        if c_char != 'I':
            p2_str.append((i, c_char))
            
    # [P, Q] = PQ - QP = coeff_O * ( (coeff1 * P1) - (coeff2 * P2) )
    # Note: standard commutator [P, Q]. No i in the definition!
    # Our get_pauli_product_term returns i when appropriate.
    # So P*O is already i * Z etc.
    
    res = []
    # Normalize Pauli strings to tuples for dict keys
    # coeff_O[i][j] includes the real scalar weight e^(-r) etc.
    
    s1_key = tuple(p1_str)
    s2_key = tuple(p2_str)
    
    val1 = coeff_O * p1_coeff
    val2 = coeff_O * p2_coeff
    
    # P1 and P2 might be the same string (if they commute)
    if s1_key == s2_key:
        if abs(val1 - val2) > 1e-15:
            res.append((s1_key, val1 - val2))
    else:
        if abs(val1) > 1e-15: res.append((s1_key, val1))
        if abs(val2) > 1e-15: res.append((s2_key, -val2)) # subtract
        
    return res

def build_symmetry_constraints():
    # Dictionary to store linear equations
    # Key: PauliString (tuple of (idx, char)), Value: List of (basis_idx, coeff_in_equation)
    rows = {} # PauliString -> {basis_idx: coeff}
    
    # Process O1
    for r in range(N):
        coeff = np.exp(-r)
        
        # A_r term
        A_idx = list(range(r)) + [r]
        A_char = ['Z']*r + ['X']
        
        # B_r term
        # O1 has A - B, so coeff_B is -coeff (for sum_k c_k [P, -B] = -coeff [P, B])
        # Get comm support for [P_k, A_r]
        # and [P_k, B_r]
        
        # Precompute [P_k, A_r] and [P_k, B_r] for all k
        # Symmetry basis indices are 0 to N-1
        
        basis_idxs_A = [list(range(r)) + [r], ['Z']*r + ['X']]
        basis_idxs_B = [list(range(r)) + [r], ['Z']*r + ['Y']]
        
        # Iterate over our Hamiltonian basis ops
        for k in range(num_ops):
            label, indices = basis[k]
            # P_k is label (e.g. 'XX') at indices (e.g. [5,6])
            chars = list(label)
            
            # [P, A]
            comm_PA = get_comm_support(indices, chars, basis_idxs_A[0], basis_idxs_A[1], coeff)
            # [P, -B] -> -coeff * [P, B]
            comm_PBn = get_comm_support(indices, chars, basis_idxs_B[0], basis_idxs_B[1], -coeff)
            
            # Merge into rows
            # rows[str] += c_k * coeff_from_comm
            all_terms = comm_PA + comm_PBn
            
            for p_str, c_coeff in all_terms:
                if p_str not in rows: rows[p_str] = {}
                if k not in rows[p_str]: rows[p_str][k] = 0.0
                rows[p_str][k] += c_coeff

    # Process O2
    # O2 = sum e^{-(N-1-r)} (A + B)
    for r in range(N):
        coeff = np.exp(-(N-1-r))
        
        # A_r term: coeff
        # B_r term: coeff
        
        basis_idxs_A = [list(range(r)) + [r], ['Z']*r + ['X']]
        basis_idxs_B = [list(range(r)) + [r], ['Z']*r + ['Y']]
        
        for k in range(num_ops):
            label, indices = basis[k]
            chars = list(label)
            
            # [P, coeff*A] = coeff * [P, A]
            comm_PA = get_comm_support(indices, chars, basis_idxs_A[0], basis_idxs_A[1], coeff)
            # [P, coeff*B]
            comm_PB = get_comm_support(indices, chars, basis_idxs_B[0], basis_idxs_B[1], coeff)
            
            all_terms = comm_PA + comm_PB
            for p_str, c_coeff in all_terms:
                if p_str not in rows: rows[p_str] = {}
                if k not in rows[p_str]: rows[p_str][k] = 0.0
                rows[p_str][k] += c_coeff
                
    # Now convert rows dict to matrix A_sym
    # We have equations: sum_k rows[p_str][k] * c_k = 0
    # This is A_sym c = 0
    equations = []
    for p_str, k_coeffs in rows.items():
        # Filter non-zero coeffs
        sparse_row = []
        for k, v in k_coeffs.items():
            if abs(v) > 1e-12:
                sparse_row.append((k, v))
        if sparse_row:
            equations.append(sparse_row)
            
    return equations

sym_equations = build_symmetry_constraints()
print(f"Number of symmetry equations: {len(sym_equations)}")

# --- 7. Eigenstate Constraints ---
# H |psi> = E |psi>
# sum_k c_k P_k |psi> - E |psi> = 0
# We only have amplitudes for specific bitstrings b in included_indices (0, 1)??
# Wait, the prompt says "partial information". The table has 0 to 115 and others.
# Ah, 'included_indices' was a guess from "Current Task" context: "Implement Python code to find a Hamiltonian ... (3) has the given state as an eigenstate".
# Correction: The prompt gives a table of specific amplitudes. We should use ALL of them.
# The table has many rows. Let's parse all bits in the table.
# The table is provided in the prompt. I will use the psi_vec constructed earlier which covers all provided bits.
# psi_vec has zeros for bits not in the table.
# The eigenstate equation must hold FOR ALL BASIS STATES.
# But we only know psi_b for some b.
# We can only enforce the equation for the known b.
# However, the constraints on H (symmetry) strongly restrict it.
# Let's construct the equations for all b in the table.
# H|psi> = sum_k c_k P_k |psi>.
# P_k |psi> is a vector. We only care about its projection onto |b> where psi_b is known (or maybe we care about overlaps with unknown states?).
# If psi_b is unknown, the equation <b|H|psi> = E <b|psi> involves unknown LHS and RHS.
# But H|psi> - E|psi> = 0. So projection on any |b> is 0.
# Even if <b|psi> is unknown, we could argue that if we have enough constraints on c_k, the solution works.
# But typically in these inverse problems, we use the known bits.
# Let's use all bits provided in the table.
# The table has bits like 0, 2048, 1024...

# Indices of known amplitudes
known_indices = [int(line.split()[0]) for line in lines if len(line.split())==3]
print(f"Using {len(known_indices)} eigenstate constraints from table.")

# We need <b| P_k |psi>.
# P_k acts on |psi>. P_k |psi> = P_k * psi_vec.
# Then <b| ... is just the b-th element of the resulting vector.
# The equation is: sum_k c_k (P_k @ psi_vec)[b] - E * psi_vec[b] = 0
# sum_k c_k M_{bk} - E v_b = 0
# Let's construct M matrix (sparse is better, but N=12 is small enough for dense if careful)
# M is size len(known_indices) x num_ops.
# For each row b and op k:
# M[b, k] = (P_k @ psi_vec)[b]
# P_k is a Pauli string.
# Action of Pauli string on state: flips signs and swaps amplitudes.
# (P_k @ psi_vec)[b] = coeff * <b| P_k |psi> = coeff * <inv(P_k) b | psi>
# Where inv(P_k) = P_k (since Paulis are Hermitian and Unitary).
# So M[b, k] = coeff * psi[indices_map(b)]
# coeff is +/-1 or +/-i? No, Paulis are real: X, Z have real coeffs. Y has imaginary coeffs?
# Y = [[0, -i], [i, 0]]. This is i*[[0,-1],[1,0]]?
# Standard Paulis: X=[[0,1],[1,0]], Y=[[0,-i],[i,0]], Z=[[1,0],[0,-1]].
# Since we have complex amplitudes in psi, we need to handle the phase correctly.
# <b| Y |psi> = sum_b' <b|Y|b'> psi_{b'}
# Y is Hermitian. 
# If b' = b (diagonal elements 0), 0.
# If b' corresponds to flipped bit, <b|Y|b'> is +/-i?
# Actually, define SigmaY = [[0,-i],[i,0]].
# Then the matrix element determines the phase.

def get_matrix_element(op_indices, op_chars, b_vec, psi_vec):
    # Compute (P @ psi)[b] = sum_c P_{b,c} psi_c
    # Since P is a Pauli string, it has only 1 non-zero per row/col.
    # P maps |c> to coeff * |b>, so P_{b,c} = coeff.
    # So (P @ psi)[b] = coeff * psi[c], where |c> is the state such that P|c> = coeff |b>.
    # Equivalent to |c> = coeff * P |b>.
    # So c is related to b by the bitwise inverses of X/Y.
    # Z does not change the state index, just sign.
    
    # b_int: integer 0..4095
    # We need to find the index c and the coefficient.
    
    # Initialize
    c_bits = b_vec.copy()
    coeff = 1.0
    
    for i, char in zip(op_indices, op_chars):
        if char == 'I': continue
        
        if char == 'Z':
            # Z|0> = |0>, Z|1> = -|1>
            # Check bit i state in c_bits (which is b)
            # If 1, multiply by -1
            if (c_bits[i] == 1):
                coeff *= -1.0
                
        elif char == 'X':
            # X|0> = |1>, X|1> = |0>
            # X|0> maps to |1>. So X|1> maps to |0>.
            # In terms of P|psi>, (Ppsi)_b. 
            # P_k |psi>. If P_k has X, it exchanges amplitudes.
            # (P psi)[b] takes psi from the state that maps to b.
            # If P acts on qubit i as X, it swaps bit i.
            # So we need to flip bit i in c_bits to get the source index.
            c_bits[i] = 1 - c_bits[i]
            
        elif char == 'Y':
            # Y|0> = i|1>, Y|1> = -i|0>
            # Bit flip + phase
            # Source bit must be flipped to contribute to b
            c_bits[i] = 1 - c_bits[i]
            # Phase: if source was 0 (now target is 1), coeff is +i
            # if source was 1 (now target is 0), coeff is -i
            # Wait, r = 1 - c_bits[i] is source.
            # Check r.
            # If r=0 (original 0), Y maps to i*1. Current target is 1. c bits is target.
            # So if c_bits[i] (target) is 1, source was 0 -> +i.
            # If c_bits[i] (target) is 0, source was 1 -> -i.
            if c_bits[i] == 1:
                coeff *= 1j
            else:
                coeff *= -1j

    # Convert c_bits to int
    c_int = 0
    for i in range(N):
        if c_bits[i] == 1:
            c_int += (1 << i)
            
    return coeff * psi_vec[c_int]

# Precompute M matrix
M = np.zeros((len(known_indices), num_ops), dtype=DTYPES)
target_b_vecs = []
for b_int in known_indices:
    # get bit vec
    b_vec = [(b_int >> i) & 1 for i in range(N)]
    target_b_vecs.append(b_vec)

for k in range(num_ops):
    label, indices = basis[k]
    chars = list(label)
    # Fill column k
    for row_idx, b_int in enumerate(known_indices):
        b_vec = target_b_vecs[row_idx]
        M[row_idx, k] = get_matrix_element(indices, chars, b_vec, psi_vec)

# Construct Eigenstate equations
# M c - E v = 0  ->  M c = E v
# v = psi_vec[known_indices]
v = psi_vec[known_indices]

# --- 8. Solve Linear System ---
# System:
# 1. Symmetry: S_sym * c = 0  (dim ~ few hundred)
# 2. Eigenstate: M * c - v * E = 0 (dim ~ few hundred)
# 3. Norm: c_40 = 1

# Total unknowns: 225 + 1 = 226.
# Total equations: > 226.
# We construct A and b for A x = b, where x = [c, E].
# Then we will add one row for c_40 = 1? Or set c_40 = 1 and remove 1 unknown.
# Since c_40 = 1 is a hard constraint, let's project it out.
# x will be 226 - 1 = 225 unknowns (c_0..c_39, c_41..c_224, E).
# New indices in x:
# c_k -> idx_k for k != 40. Map k -> k if k < 40 else k-1.
# E -> idx 224 (last one).

# Construct matrix A_rows (list of sparse rows dicts)
def get_idx_in_x(k):
    if k < 40: return k
    if k == 40: return None
    return k - 1

# 1. Symmetry Equations
# sum_k S[s, k] c_k = 0
# Substitute x, ignore c_40 term, move it to RHS?
# sum_{k!=40} S[s, k] x_{map(k)} = - S[s, 40] * 1
for eq in sym_equations:
    # eq is list of (k, val)
    row = {} # k -> val
    rhs = 0.0
    for k, val in eq:
        if k == 40:
            rhs -= val # Move to RHS: sum(c...) + c_40 term = 0 => sum(others) = -1 * term_40
        else:
            idx = get_idx_in_x(k)
            if idx is not None:
                row[idx] = val
    
    if row:
        A_rows.append(row)
        b_rows.append(rhs)

# 2. Eigenstate Equations
# sum_k M[b, k] c_k - E v[b] = 0
# sum_{k!=40} M[b, k] x_{map(k)} - v[b] * E = - M[b, 40]
idx_E = 224
for b_idx in range(len(known_indices)):
    row = {}
    right_hand_side = -M[b_idx, 40]
    
    for k in range(num_ops):
        val = M[b_idx, k]
        if k == 40: continue
        idx = get_idx_in_x(k)
        if idx is not None:
            row[idx] = val
            
    row[idx_E] = -v[b_idx]
    
    A_rows.append(row)
    b_rows.append(right_hand_side)

# 3. Constraint c_40 = 1 is handled by moving terms.
# Do we need an extra regularization? No.
# However, we have an overdetermined system.
# Solve A x = b.
# Use least squares.
# Convert to dense for simplicity? Size:
# Rows = len(A_rows).
# Cols = 225.
# len(A_rows) is SymEqs + Len(Known).
# SymEqs ~ 200. Known ~ 200-300.
# Total ~ 500.
# 500 x 225 is small.

n_rows = len(A_rows)
n_cols = 225
A_dense = np.zeros((n_rows, n_cols), dtype=DTYPES)
b_vec = np.zeros(n_rows, dtype=DTYPES)

for r in range(n_rows):
    row_dict = A_rows[r]
    for c, val in row_dict.items():
        A_dense[r, c] = val
    b_vec[r] = b_rows[r]

# Solve using Least Squares
# Note: A is complex. b is complex.
# scipy.linalg.lstsq handles complex.
x_sol, residuals, rank, s = linalg.lstsq(A_dense, b_vec)

print(f"Rank of A: {rank}")
print(f"Residual norm: {np.linalg.norm(A_dense @ x_sol - b_vec)}")

# --- 9. Reconstruct Solution ---
c_sol = np.zeros(num_ops, dtype=DTYPES)
cnt = 0
for k in range(num_ops):
    if k == 40:
        c_sol[k] = 1.0 + 0j
    else:
        c_sol[k] = x_sol[get_idx_in_x(k)]

E_sol = x_sol[idx_E]

print(f"Energy E: {E_sol.real} + {E_sol.imag}i")

# --- 10. Verification ---
# Verify Commutators
H_mat = np.zeros((dim, dim), dtype=DTYPES)
for k in range(num_ops):
    H_mat += c_sol[k] * basis_ops[k]

comm1 = H_mat @ O1_mat - O1_mat @ H_mat
comm2 = H_mat @ O2_mat - O2_mat @ H_mat

norm1 = np.linalg.norm(comm1, 'fro')
norm2 = np.linalg.norm(comm2, 'fro')
trace_I = dim
normalized_frobenius_sq1 = (norm1**2) / trace_I
normalized_frobenius_sq2 = (norm2**2) / trace_I

print(f"||[H, O1]||^2 / tr(I): {normalized_frobenius_sq1:.4e}")
print(f"||[O1, H]||^2 / tr(I): {normalized_frobenius_sq2:.4e}") # Typo in my thought, O1 is symmetric-ish?
# Wait, the condition is ||[H, O_1]||_F^2/tr(I) < 10^-10
# My comm1 is [H, O1].
# Let's check.

target_threshold = 1e-10
print(f"Condition satisfied? {normalized_frobenius_sq1 < target_threshold and normalized_frobenius_sq2 < target_threshold}")

# Verify Eigenstate
# H|psi> - E|psi>
res = H_mat @ psi_vec - E_sol * psi_vec
res_norm = np.linalg.norm(res)
print(f"|| H|psi> - E|psi> ||: {res_norm:.4e}")
# Also check only on known bits?
res_known = np.linalg.norm(res[known_indices])
print(f"|| on known bits: {res_known:.4e}")

# --- 11. Output Format ---
# The user wants the solution vector.
# Provided as a block of numbers.
# The list format matches the generation order.

output = []
for val in c_sol:
    # The values should be Real. Small imaginary parts might be numerical noise.
    # Check prompt: "numerical vector of coefficients". Usually implies real scalars for Hermitian H.
    # My derivation used Pauli matrices which are Hermitian. 
    # C_k should be real.
    # Let's take the real part if imag is small.
    if abs(val.imag) > 1e-8:
        print(f"Warning: Large imaginary part for coefficient {val}")
    output.append(f"{val.real:.18e}")

# Join with newlines or spaces?
# "Represent the solution as a numerical vector... output vector of coefficients"
# The prompt text has a list of numbers block.
# I will provide the Python code to generate it and the textual block.

# Recalculate strictly real to be safe
# c_sol_real = np.real_if_close(c_sol, tol=1e-10)
# output_str = "\n".join([f"{v:.18e}" for v in c_sol_real])

# Final check on normalization: c[40] (Y0Y1) should be 1.0.
print(f"Coefficient of Y0Y1 (idx 40): {c_sol[40]}")

# Print the output vector
text_output = "Solution coefficients vector:"
for val in c_sol:
    text_output += f"\n{val.real:.18e}"
    
print(text_output)

```