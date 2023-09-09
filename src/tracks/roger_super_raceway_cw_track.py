#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class RogerSuperRacewayClockwiseTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Roger Super Raceway (Clockwise)"
        self._ui_description = "Are you ready rip on the Roger Super Raceway? The Roger Super Raceway was inspired by a real-life track in the home town of AWS Community Member, Roger Logan. At 60.17m this track features no shortage of lightning fast drag strips and unforgiving technical sections that will put even the most skilled developer to the test."
        self._ui_length_in_m = 60.17  # metres
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "2022_september_pro_cw"
        self._track_sector_dividers = [45, 83, 118, 157]
        self._annotations = config.roger_super_raceway_cw_annotations
        self._track_width = 1.067

        self._track_waypoints = [(4.9345816647515655, -3.889916430988316), (4.857811450958252, -3.9948275089263916),
                                 (4.769832513461829, -4.090533864812512), (4.654093503952026, -4.21643853187561),
                                 (4.42922043800354, -4.416549921035767), (4.183729529380798, -4.590635061264038),
                                 (3.9293205738067627, -4.751775503158569), (3.672837972640991, -4.909595489501953),
                                 (3.4152320623397827, -5.065578460693359), (3.157427430152893, -5.221232891082764),
                                 (2.900146484375, -5.377748966217041), (2.641840100288391, -5.532570123672485),
                                 (2.383417010307312, -5.687195062637329), (2.1248000264167786, -5.84149694442749),
                                 (1.8660320043563843, -5.995543479919434), (1.6071659922599792, -6.149425983428955),
                                 (1.3482455015182495, -6.303216457366943), (1.0893166363239288, -6.456992864608765),
                                 (0.8304259777069092, -6.610833644866943), (0.5716194063425064, -6.764816045761108),
                                 (0.31294300965964794, -6.91901707649231), (0.054452747106552124, -7.073529005050659),
                                 (-0.20385359227657318, -7.228349924087524), (-0.4617278575897217, -7.383887529373169),
                                 (-0.720135435461998, -7.538519382476807), (-0.9959840178489685, -7.657934904098511),
                                 (-1.2923265099525452, -7.705623388290405), (-1.590729534626007, -7.671332120895386),
                                 (-1.8742290139198303, -7.571087837219238), (-2.1407440304756165, -7.430980443954468),
                                 (-2.4024789333343506, -7.282034635543823), (-2.664831519126892, -7.134187459945679),
                                 (-2.9275964498519897, -6.987061977386475), (-3.190437912940979, -6.840072393417358),
                                 (-3.453692078590393, -6.69382381439209), (-3.717109441757202, -6.547869443893433),
                                 (-3.980719566345215, -6.402263402938843), (-4.244485974311825, -6.25693988800049),
                                 (-4.508378505706787, -6.111847162246704), (-4.772372007369992, -5.9669370651245135),
                                 (-5.036435604095455, -5.822155475616457), (-5.300539970397949, -5.677448034286499),
                                 (-5.564656972885132, -5.532763481140137), (-5.828760385513306, -5.388055086135864),
                                 (-6.092822790145874, -5.2432708740234375), (-6.356793165206909, -5.098318099975586),
                                 (-6.6207275390625, -4.953300952911377), (-6.884440660476685, -4.807881593704224),
                                 (-7.139030933380127, -4.647738933563232), (-7.361320495605469, -4.445281028747559),
                                 (-7.517810583114624, -4.190410375595093), (-7.53454327583313, -3.893230438232422),
                                 (-7.4263975620269775, -3.6134579181671143), (-7.283920526504517, -3.348145008087158),
                                 (-7.1432785987854, -3.081853985786438), (-7.004126310348511, -2.8147809505462646),
                                 (-6.866101503372192, -2.5471240282058716), (-6.72887396812439, -2.279056429862976),
                                 (-6.59209942817688, -2.0107579827308655), (-6.45526647567749, -1.742489516735077),
                                 (-6.317865610122681, -1.4745109677314758), (-6.17940092086792, -1.207081139087677),
                                 (-6.041265487670898, -0.939488023519516), (-5.945026397705078, -0.6822457015514374),
                                 (-6.073970556259155, -0.3666770961135626), (-6.321714639663696, -0.22686946392059326),
                                 (-6.5843665599823, -0.07955485582351685), (-6.84908652305603, 0.06402149796485901),
                                 (-7.114335060119629, 0.20662204921245575), (-7.378912925720215, 0.3504594452679157),
                                 (-7.641710996627808, 0.49752071127295494), (-7.9015350341796875, 0.6497689485549927),
                                 (-8.157031774520874, 0.8091608583927155), (-8.402181625366211, 0.9839580655097961),
                                 (-8.627012252807617, 1.1841208040714264), (-8.820356369018555, 1.4146685004234314),
                                 (-8.966530323028564, 1.6774795055389404), (-9.049440383911133, 1.966453492641449),
                                 (-9.06244421005249, 2.2669119834899902), (-9.01448917388916, 2.5639795064926147),
                                 (-8.921839714050293, 2.8503040075302124), (-8.798450469970703, 3.1249234676361084),
                                 (-8.657577514648438, 3.391066074371338), (-8.511129379272461, 3.6542065143585205),
                                 (-8.360389471054077, 3.91491162776947), (-8.20578646659851, 4.173344969749451),
                                 (-8.048080682754517, 4.429898500442505), (-7.889273166656494, 4.685772180557251),
                                 (-7.7294275760650635, 4.9409990310668945), (-7.557718515396118, 5.188135623931885),
                                 (-7.330789089202881, 5.383260488510132), (-7.039602518081665, 5.442188024520874),
                                 (-6.749600648880005, 5.365515947341919), (-6.478294372558594, 5.2349793910980225),
                                 (-6.208916425704956, 5.100363492965698), (-5.941094636917114, 4.962661027908325),
                                 (-5.67430305480957, 4.822970390319824), (-5.408254146575928, 4.681870698928833),
                                 (-5.142674684524536, 4.53988790512085), (-4.877168893814087, 4.397769451141357),
                                 (-4.610759973526001, 4.257349967956543), (-4.343870639801025, 4.117846488952637),
                                 (-4.076905012130737, 3.9784878492355347), (-3.8102675676345825, 3.8385030031204224),
                                 (-3.5442285537719727, 3.6973835229873657), (-3.278586983680725, 3.5555174350738525),
                                 (-3.013143539428711, 3.413282036781311), (-2.7476974725723267, 3.2710505723953247),
                                 (-2.4820505380630493, 3.129194498062134), (-2.2160050868988037, 2.988088011741638),
                                 (-1.94936603307724, 2.8481059074401855), (-1.6819429993629456, 2.7096270322799683),
                                 (-1.4135540127754211, 2.573030471801758), (-1.1440139412879944, 2.438718557357788),
                                 (-0.8731957077980042, 2.3069995045661926), (-0.6007252633571633, 2.1787474751472478),
                                 (-0.3286186717450619, 2.0496524572372437), (-0.05976395308971405, 1.9140465259552002),
                                 (0.20540387369692326, 1.7712504863739014), (0.46969670057296753, 1.6268909573554993),
                                 (0.7365152537822723, 1.4872244596481323), (1.0107985734939575, 1.3628072440624237),
                                 (1.2980909943580627, 1.2726288437843323), (1.5978339910507202, 1.2487168312072754),
                                 (1.8895899653434753, 1.3206867575645447), (2.1462550163269043, 1.4782094955444336),
                                 (2.3640635013580322, 1.6865904927253723), (2.552157998085022, 1.9220744967460632),
                                 (2.719224452972412, 2.172672927379608), (2.8739525079727173, 2.431115984916687),
                                 (3.0169049501419067, 2.6961084604263306), (3.1180084943771362, 2.979097008705139),
                                 (3.1688950061798096, 3.2758580446243286), (3.218222975730896, 3.5729395151138306),
                                 (3.253376007080078, 3.8720110654830933), (3.281959056854248, 4.171799421310425),
                                 (3.304949998855591, 4.472067356109619), (3.321148991584778, 4.772777318954468),
                                 (3.328013062477112, 5.073847532272339), (3.319617509841919, 5.374855041503906),
                                 (3.277864933013916, 5.672797441482544), (3.1853665113449097, 5.959321022033691),
                                 (3.0864970684051514, 6.243775367736816), (3.0843929052352905, 6.528187990188599),
                                 (3.2875930070877075, 6.7501139640808105), (3.515863537788391, 6.946503400802612),
                                 (3.7539669275283813, 7.130877494812012), (3.998227119445801, 7.307013511657715),
                                 (4.247915506362915, 7.475368976593018), (4.510985374450684, 7.620661020278931),
                                 (4.80303692817688, 7.687553882598877), (5.1032915115356445, 7.673438310623169),
                                 (5.400804281234741, 7.626688241958618), (5.696415901184082, 7.569203853607178),
                                 (5.9895405769348145, 7.500141143798828), (6.279688358306885, 7.419488430023193),
                                 (6.566424608230591, 7.327440023422241), (6.849428415298462, 7.224488973617554),
                                 (7.128535032272339, 7.111395359039307), (7.4037535190582275, 6.989141464233398),
                                 (7.675267219543457, 6.858865976333618), (7.94340181350708, 6.721771001815796),
                                 (8.208663702011108, 6.579193115234375), (8.471426010131836, 6.4320619106292725),
                                 (8.733869075775146, 6.2843616008758545), (8.939800262451172, 6.076733350753784),
                                 (9.018955707550049, 5.786710500717163), (9.05711030960083, 5.4880805015563965),
                                 (9.070948123931885, 5.187314510345459), (9.020205020904541, 4.892150402069092),
                                 (8.89781141281128, 4.617202997207642), (8.764265060424805, 4.347283840179443),
                                 (8.629583835601807, 4.077928900718689), (8.495044708251953, 3.808501958847046),
                                 (8.361777782440186, 3.5384451150894165), (8.230854272842407, 3.267243981361389),
                                 (8.103418111801147, 2.994391083717346), (7.989548921585083, 2.7161624431610107),
                                 (7.968470096588135, 2.416504979133606), (7.965446472167969, 2.1155190467834473),
                                 (7.9670186042785645, 1.814433991909027), (7.950138092041016, 1.5142894983291626),
                                 (7.836574077606201, 1.2370719909667969), (7.69194221496582, 0.9729131162166595),
                                 (7.548372507095337, 0.7081894874572754), (7.404282093048096, 0.4437481388449669),
                                 (7.2597880363464355, 0.17952673509716988), (7.114906072616577, -0.08448194712400436),
                                 (6.969611167907715, -0.3482635170221329), (6.823899507522583, -0.6118152439594269),
                                 (6.677760362625122, -0.8751300275325775), (6.531185150146484, -1.1382023990154266),
                                 (6.384162902832031, -1.4010254740715027), (6.23668909072876, -1.6635950207710266),
                                 (6.088737964630127, -1.9258965253829956), (5.940360069274902, -2.1879565119743347),
                                 (5.7913994789123535, -2.449685573577881), (5.641528844833374, -2.710894465446472),
                                 (5.491264343261719, -2.9718769788742065), (5.340514898300171, -3.2325799465179443),
                                 (5.189194917678833, -3.492951512336731), (5.035552024841309, -3.7519344091415405),
                                 (4.9345816647515655, -3.889916430988316)]
