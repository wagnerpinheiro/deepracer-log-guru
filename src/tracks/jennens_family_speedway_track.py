#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class JennensFamilySpeedwayTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Jennens Family Speedway"
        self._ui_description = "The Jennens Family Speedway (49.56 m) is named in honor of the first ever racing family and 2021 re:Invent finalists James ""JJ"" and Timothy ""Flatearth"" Jennens. This track features two blistering fast drag strips right into unforgiving 90 degree sweeping turns that can spin out even the most skilled developers."
        self._ui_length_in_m = 49.56  # metres
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "2022_october_open"
        self._track_sector_dividers = [46, 100]
        self._annotations = config.jennens_family_speedway_annotations
        self._track_width = 1.067

        self._track_waypoints = [(-7.755003452301025, 0.4451555125415325), (-7.505678415298459, 0.27408921718597234),
                                 (-7.244629383087158, 0.12151135504245758), (-6.972953081130978, -0.011228904128076037),
                                 (-6.694684982299805, -0.12963902950286865), (-6.41720986366272, -0.24994993954896927),
                                 (-6.139669418334961, -0.3701086901128292), (-5.862192869186401, -0.4904141963343136),
                                 (-5.5851404666900635, -0.6116961240768433), (-5.308419942855835, -0.7337275296449661),
                                 (-5.032577991485596, -0.8577362298965454), (-4.757369041442871, -0.9831396788358688),
                                 (-4.483355522155762, -1.1111348569393158), (-4.208613991737366, -1.2375427782535553),
                                 (-3.933869481086731, -1.3639634847640991), (-3.659485936164856, -1.4911675453186035),
                                 (-3.385401487350464, -1.619014024734497), (-3.1114695072174072, -1.7471864819526672),
                                 (-2.837660074234009, -1.87562096118927), (-2.5639175176620483, -2.0041980147361755),
                                 (-2.289720058441162, -2.131802499294281), (-2.0152634978294373, -2.258848547935486),
                                 (-1.7403600215911865, -2.3849234580993652), (-1.4650830030441284, -2.510182499885559),
                                 (-1.1890831291675568, -2.6338380575180054), (-0.9121726751327515, -2.7554404735565186),
                                 (-0.634554997086525, -2.875421404838562), (-0.3561219498515129, -2.993494987487793),
                                 (-0.07585849240422249, -3.106951951980591), (0.21357212215662003, -3.194725513458252),
                                 (0.5040899366140366, -3.278777003288269), (0.7953570783138275, -3.360203981399536),
                                 (1.087129384279251, -3.439800500869751), (1.3795784711837769, -3.5168734788894653),
                                 (1.6725150346755981, -3.5920709371566772), (1.9657999873161316, -3.6658999919891357),
                                 (2.259369969367981, -3.7385900020599365), (2.5531080961227417, -3.8105969429016113),
                                 (2.847051978111267, -3.881759524345398), (3.140995979309082, -3.9529190063476562),
                                 (3.4348909854888916, -4.0242840051651), (3.728566527366638, -4.096544623374939),
                                 (4.0220324993133545, -4.16965389251709), (4.3156349658966064, -4.242184996604919),
                                 (4.609933853149414, -4.311862587928772), (4.9044880867004395, -4.380454063415527),
                                 (5.199220657348633, -4.448277473449707), (5.494209051132202, -4.514976382255554),
                                 (5.789388418197632, -4.580825090408325), (6.084751605987549, -4.645842552185059),
                                 (6.380423545837402, -4.709444522857666), (6.676470041275024, -4.771275997161865),
                                 (6.97294282913208, -4.831032037734985), (7.26960563659668, -4.889832496643066),
                                 (7.566822052001953, -4.9457690715789795), (7.8641345500946045, -5.001286029815674),
                                 (8.159615516662598, -4.951810598373413), (8.406055450439453, -4.780893325805664),
                                 (8.562281608581543, -4.523993968963623), (8.63389539718628, -4.2309370040893555),
                                 (8.648118019104004, -3.9290995597839355), (8.625285148620605, -3.6276700496673584),
                                 (8.57523775100708, -3.3294734954833984), (8.506796836853027, -3.034928560256958),
                                 (8.506796836853027, -3.034928560256958), (8.476519346237183, -2.7347664833068848),
                                 (8.5135657787323, -2.434995412826538), (8.585251808166504, -2.1412404775619507),
                                 (8.664247512817383, -1.849313497543335), (8.740426063537598, -1.55663001537323),
                                 (8.817792892456055, -1.2642599940299988), (8.898229122161865, -0.9727175235748291),
                                 (8.980339527130127, -0.681643009185791), (9.066332340240479, -0.39169690012931824),
                                 (9.15629243850708, -0.10295629687607288), (9.203824520111084, 0.19454235583543822),
                                 (9.216181755065918, 0.496659100055695), (9.202358722686768, 0.7986833155155182),
                                 (9.159722328186035, 1.097980409860611), (9.08905839920044, 1.3919295072555542),
                                 (8.987367153167725, 1.6766055226325989), (8.854998111724854, 1.9483780264854431),
                                 (8.694060325622559, 2.204278588294983), (8.507275104522705, 2.4419875144958496),
                                 (8.298409700393677, 2.6605790853500366), (8.071115493774416, 2.8599555492401114),
                                 (7.82850980758667, 3.040425419807434), (7.573786020278931, 3.2033729553222656),
                                 (7.30945110321045, 3.3502370119094844), (7.0372235774993905, 3.4819134473800655),
                                 (6.758669614791869, 3.599635481834412), (6.475301504135132, 3.7052711248397827),
                                 (6.187966585159302, 3.799584150314331), (5.897493600845337, 3.8837616443634033),
                                 (5.604870557785034, 3.960146427154541), (5.311467170715332, 4.033480882644653),
                                 (5.0262510776519775, 4.132853984832764), (4.730224132537842, 4.192736029624939),
                                 (4.428300380706787, 4.1963454484939575), (4.132031559944153, 4.138618469238281),
                                 (3.853487491607666, 4.021769046783447), (3.6084929704666138, 3.8457579612731934),
                                 (3.411071538925171, 3.617482900619507), (3.2602025270462036, 3.355684518814087),
                                 (3.140528440475464, 3.0780140161514282), (3.0351579189300537, 2.7945384979248047),
                                 (2.929121971130371, 2.5113149881362915), (2.799983024597168, 2.238517999649048),
                                 (2.6032760143280043, 2.0098019838333148), (2.3587000370025617, 1.8329170346260064),
                                 (2.0838890075683576, 1.7077589631080623), (1.7914485335350037, 1.631926953792572),
                                 (1.490757465362551, 1.6019275188446047), (1.1888760328292847, 1.6152389645576477),
                                 (0.8928671777248383, 1.675501525402069), (0.6057200878858566, 1.7701780200004578),
                                 (0.3245176561176777, 1.8814440369606018), (0.04630109667778015, 2.000022053718567),
                                 (-0.23208790179342031, 2.1181859970092773), (-0.5125381946563721, 2.231346011161804),
                                 (-0.7919032573699951, 2.3471999764442444), (-1.071234107017517, 2.463137447834015),
                                 (-1.3506739735603333, 2.578809976577759), (-1.6303449869155884, 2.6939234733581543),
                                 (-1.910144031047821, 2.80872642993927), (-2.1901875138282776, 2.9229310750961304),
                                 (-2.4705530405044556, 3.036341428756714), (-2.7511759996414185, 3.149114966392517),
                                 (-3.0321154594421387, 3.2610939741134644), (-3.3134440183639526, 3.372096538543701),
                                 (-3.595812439918518, 3.4804195165634155), (-3.8793119192123413, 3.5857499837875366),
                                 (-4.163656949996948, 3.6887749433517456), (-4.448596000671387, 3.7901490926742554),
                                 (-4.733931541442871, 3.8904019594192505), (-5.019349098205566, 3.9904184341430664),
                                 (-5.304849624633789, 4.090198993682861), (-5.590124845504761, 4.19062352180481),
                                 (-5.875044584274292, 4.2920531034469604), (-6.159180402755737, 4.3956520557403564),
                                 (-6.44232439994812, 4.501933336257935), (-6.725490093231201, 4.608154058456421),
                                 (-7.008341550827026, 4.715210914611816), (-7.291232585906982, 4.822164058685303),
                                 (-7.574861288070679, 4.927034139633179), (-7.856085538864136, 5.038276672363281),
                                 (-8.14598560333252, 5.122975587844849), (-8.446453571319584, 5.123118400573729),
                                 (-8.70826148986816, 4.980955600738527), (-8.872729301452638, 4.7290720939636195),
                                 (-8.968108654022217, 4.4424121379852295), (-9.031425952911377, 4.146733522415158),
                                 (-9.090214252471924, 3.8500900268554688), (-9.146362781524658, 3.5529894828796387),
                                 (-9.200953483581543, 3.2555309534072876), (-9.238299369812012, 2.9554984569549596),
                                 (-9.239519596099854, 2.6533539295196533), (-9.18390703201294, 2.3566945791244507),
                                 (-9.067930221557617, 2.077654540538788), (-8.931593418121338, 1.8077549934387207),
                                 (-8.777645587921143, 1.5474955439567566), (-8.606619358062744, 1.2981362640857697),
                                 (-8.417943000793455, 1.0618529021739933), (-8.212388515472412, 0.8401062488555908),
                                 (-7.991051435470581, 0.6341079920530319), (-7.755003452301025, 0.4451555125415325)]
